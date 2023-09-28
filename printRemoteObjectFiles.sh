#!/bin/bash

set -ef -o  pipefail

# Get all object files from latest OneLifeData7 master branch remotely from Github

# Check for missing tools to perform the script reliably.
REQUIRED_TOOLS=("jq" "curl" "awk")
all_tools_exists=1
for i in "${REQUIRED_TOOLS[@]}"; do
    test ! "$(command -v "${i}")" && >&2 echo "You are missing the ${i} tool!" && all_tools_exists=0
done
test "${all_tools_exists}" -eq 0 && >&2 echo "All the tools above need to be installed to run this script. Aborted." \
    && exit 1

# TARGET can be either git branches, tags or commit hash.

TARGET="${1}"
if [[ -z "${TARGET}" ]]; then
    # default branch
    TARGET="master"
fi

curl -sSf -o - "https://api.github.com/repos/twohoursonelife/OneLifeData7/git/trees/${TARGET}?recursive=1" \
    | jq -rc '.tree
              | .[]
              | .path
              | split("/")
              | if .[0] == "objects" then .[1] else null end
              | select(. != null)' \
    | grep -E '^[0-9]+\.txt$'
