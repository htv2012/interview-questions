#!/usr/bin/env bash

banner() {
    echo "# ======================================================================"
    echo "# $1"
    echo "# ======================================================================"
}

set -e

top=$(PWD)

# Find all files named Makefile and loop over each line safely
find . -type f -name Makefile | while IFS= read -r makefile; do
    # Extract the containing directory
    projectDir=$(dirname "$makefile")
    banner "$projectDir"
    set -x
    cd "$projectDir"
    set +x
    make
    cd "$top"
done
