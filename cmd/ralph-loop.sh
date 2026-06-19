#!/bin/bash
set -e

projectname=cuhasc
finish_msg="<promise>COMPLETE!</promise>"  # must match prompt text
iterations=$1
prompt=$(cat docs/agents/loop-prompt.md)
if [ -z "$iterations" ]; then
  echo "Usage: $0 <max-num-iterations>"
  exit 1
fi

for ((iteration=1; iteration<=$iterations; iteration++)); do
  echo "==================== ralph loop round $iteration ===================="
  result=$(sbx run $projectname -- -p "$prompt" | tee /dev/stderr)  # show output and capture it

  if [[ "$result" == *"$finish_msg"* ]]; then
    echo "***** No more work found (as per the prompt) after $iteration iterations. *****"
    exit 0
  fi
  sleep 10  # relax
done