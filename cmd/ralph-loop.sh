#!/bin/bash
set -e

projectname=cuhasc
finish_msg="<promise>COMPLETE!</promise>"  # must match prompt text
iterations=$1
agent_options="--permission-mode bypassPermissions --verbose --output-format stream-json -p"
prompt=$(cat docs/agents/loop-prompt.md)

do_it_once() {
  sbx run $projectname -- $agent_options "$prompt" | \
  tee .last_sbx_output.txt | \
  jq -rj 'select(.type=="assistant") | .message.content[]? | 
          if .type=="thinking" then (.thinking[0:100] + "\n") 
          elif .type=="text" then .text else empty end' | \
  tee /dev/stderr  # show output yet allow capturing it
}

if [ -z "$iterations" ]; then
  echo "Usage: $0 <max-num-iterations>"
  exit 1
fi

for ((iteration=1; iteration<=$iterations; iteration++)); do
  echo "==================== ralph loop round $iteration ===================="
  result=$(do_it_once) 
  if [[ "$result" == *"$finish_msg"* ]]; then
    echo "***** No more work found (as per the prompt) after $iteration iterations. *****"
    exit 0
  fi
  sleep 5  # relax
done