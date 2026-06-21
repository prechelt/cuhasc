#!/bin/bash
set -eo pipefail   # pipefail: a failing producer (e.g. `sbx run`) fails the pipe

# ----- call args:
iterations=$1

# ----- settings:
projectname=cuhasc
max_retries=3       # retries per round after an abnormal end (4 attempts total)
retry_wait=120      # seconds to wait between those retries
ratelimit_buffer=60 # extra seconds to wait past a rate-limit reset time
# use_sandbox=1 -> run the agent inside the `sbx` sandbox (default).
# use_sandbox=0 -> call `claude` directly in this working copy (no PTY, no
# sandbox lifecycle); more reliable but unsandboxed. Override via the env var.
use_sandbox=${use_sandbox:-0}  # env var of same name if set, else 0
agent_options="--permission-mode bypassPermissions --verbose --output-format stream-json -p"
last_agent_output=".last_agent_output.txt"  # file for debugging
last_assistant_text=".last_assistant_text.txt"  # file for debugging

# ----- prompt:
prompt=$(cat docs/agents/loop-prompt.md)
finish_msg="<promise>COMPLETE!</promise>"  # must match prompt text

# `sbx` may be a Windows console executable and always wraps its output in OSC
# set-window-title control sequences (ESC ] ... BEL/ST), at the start and end of
# the stream. Those bytes make jq choke ("Invalid numeric literal"), so strip them
# before any jq. Works for both the `sbx run` JSONL stream (one object per line)
# and the single multi-line `sbx ls --json` document, since it removes only the
# escape sequences and leaves the JSON intact.
strip_junk() { sed -u -E 's/\x1b\][^\x07\x1b]*(\x07|\x1b\\)//g'; }

# The sandbox is a container owned by the Docker Desktop daemon (Windows side);
# its lifecycle is independent of this pipeline. Killing the local `sbx run`
# client (Ctrl-C) does NOT stop the agent inside it -- only `sbx stop` does.
sandbox_status() {
  sbx ls --json 2>/dev/null | strip_junk | \
    jq -r --arg s "$projectname" '.sandboxes[]? | select(.name==$s) | .status'
}

stop_sandbox() {
  local status
  status=$(sandbox_status)
  if [ -n "$status" ] && [ "$status" != "stopped" ]; then
    echo "----- stopping sandbox '$projectname' (was: $status) -----" >&2
    sbx stop "$projectname" >&2 || true
  fi
}

# `sbx run` returning only means the output stream closed, not that the agent
# exited. The authoritative "agent done" signal is the sandbox returning to
# 'stopped'. Wait for that; if it isn't stopped shortly after the stream ends,
# report that the stream died for an unknown reason while work keeps going.
wait_until_stopped() {
  local status i
  # Grace: on a normal finish the daemon may flip to 'stopped' a beat after the
  # stream closes -- don't raise a false alarm for that.
  for i in 1 2 3; do
    status=$(sandbox_status)
    if [ -z "$status" ] || [ "$status" = "stopped" ]; then
      return
    fi
    sleep 1
  done
  echo "!!! output stream ended (reason unknown) but sandbox '$projectname' is still '$status' -- work is continuing; waiting for it to finish... !!!" >&2
  while [ -n "$status" ] && [ "$status" != "stopped" ]; do
    sleep 5
    status=$(sandbox_status)
  done
  echo "----- sandbox '$projectname' finished (it was still running after the stream ended) -----" >&2
}

on_interrupt() {
  echo "" >&2
  echo "***** interrupted; stopping sandbox before exit *****" >&2
  stop_sandbox
  exit 130
}
trap on_interrupt INT TERM

run_agent() {
  if [ "$use_sandbox" = "1" ]; then
    sbx run $projectname -- $agent_options "$prompt"
  else
    claude $agent_options "$prompt"
  fi
}

do_it_once() {
  if [ "$use_sandbox" = "1" ]; then
    # Clean slate: a leftover agent from a previous (e.g. interrupted) round can
    # still be running in the persistent sandbox and would commit behind our back.
    stop_sandbox
  fi
  # Raw stream -> $last_agent_output (authoritative log, inspected afterwards).
  # Extracted assistant text -> terminal (live) and $last_assistant_text
  # (so the finish-promise check reads a file rather than capturing stdout, which
  # keeps the live display and avoids set -e/pipefail surprises in $()).
  run_agent | \
  tee "$last_agent_output" | \
  strip_junk | \
  jq --unbuffered -Rrj 'fromjson? |
           if .type=="assistant" then (.message.content[]? |
             if .type=="thinking" then (.thinking[0:100] + "\n")
             elif .type=="text" then ((.text | rtrimstr("\n")) + "\n")
             else empty end)
           elif .type=="result" then (if .is_error then ((.result // "") + "\n") else empty end)
           else empty end' | \
  # ^ -R + fromjson? parses each line tolerantly: a malformed/partial line is
  # skipped instead of aborting jq. Crucial -- an aborting jq sends SIGPIPE up
  # the pipe and kills `sbx run` mid-stream (the original "stream breaks off" bug).
  # --unbuffered + sed -u (in strip_junk) flush each event live instead of
  # block-buffering the pipe. Each assistant message ends in "\n" so messages land
  # on their own lines; `result` is shown only on error (on success it just repeats
  # the final assistant message).
  tee "$last_assistant_text"
}

# Item 1: the authoritative "this turn completed normally" signal is a final
# stream-json result event with is_error=false. Inspect the captured raw stream.
turn_succeeded() {
  local r
  r=$(strip_junk < "$last_agent_output" | \
      jq -Rr 'fromjson? | select(.type=="result") | (.is_error | not)' \
      2>/dev/null | tail -n1) || true
  [ "$r" = "true" ]
}

# Item 3: if the stream carries a *blocking* rate-limit event (status != allowed),
# echo its reset time (epoch seconds); empty otherwise.
ratelimit_reset() {
  strip_junk < "$last_agent_output" | \
    jq -Rr 'fromjson? | select(.type=="rate_limit_event")
            | .rate_limit_info | select(.status != "allowed") | .resetsAt' \
    2>/dev/null | tail -n1 || true
}

# Items 1-3: run one round, retrying on abnormal end / honoring rate-limit blocks.
run_round() {
  local attempt pstat reset now wait
  for (( attempt=0; attempt<=max_retries; attempt++ )); do
    pstat=0
    do_it_once || pstat=$?   # item 4: producer failure surfaces via pipefail
    [ "$use_sandbox" = "1" ] && wait_until_stopped

    # Honor a genuine rate-limit block first: wait until reset (+buffer), retry.
    reset=$(ratelimit_reset)
    if [ -n "$reset" ]; then
      now=$(date +%s); wait=$(( reset - now + ratelimit_buffer ))
      [ "$wait" -lt 0 ] && wait=0
      echo "----- rate-limited; waiting ${wait}s (until reset + ${ratelimit_buffer}s) -----" >&2
      sleep "$wait"
      continue
    fi

    if [ "$pstat" -eq 0 ] && turn_succeeded; then
      return 0
    fi

    echo "!!! round $iteration attempt $((attempt+1))/$((max_retries+1)) ended abnormally (producer status=$pstat, no successful result event) !!!" >&2
    if [ "$attempt" -lt "$max_retries" ]; then
      echo "----- retrying in ${retry_wait}s -----" >&2
      sleep "$retry_wait"
    fi
  done
  return 1
}

if [ -z "$iterations" ]; then
  echo "Usage: $0 <max-num-iterations>"
  exit 1
fi

for ((iteration=1; iteration<=$iterations; iteration++)); do
  printf '\n==================== ralph loop round %s ====================\n' "$iteration"
  if ! run_round; then
    echo "***** round $iteration failed after $((max_retries+1)) attempts; giving up. *****" >&2
    stop_sandbox
    exit 1
  fi
  if grep -qF "$finish_msg" "$last_assistant_text"; then
    echo "***** No more work found (as per the prompt) after $iteration iterations. *****"
    stop_sandbox
    exit 0
  fi
  sleep 5  # relax
done
stop_sandbox
