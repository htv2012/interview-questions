#!/usr/bin/env bash

banner() {
    echo "# ======================================================================"
    echo "# $1"
    echo "# ======================================================================"
}

top=$(PWD)

# Find all files named Makefile and loop over each line safely
find . -type f -name Makefile | \
while IFS= read -r makefile; do
    # Extract the containing directory
    projectDir=$(dirname "$makefile")
    banner "$projectDir"
    set -x
    cd "$projectDir"
    set +x
    make
    if [ $? -ne 0 ]; then
        echo "$projectDir" >> "$top/failed.txt"
    fi
    cd "$top"
done
