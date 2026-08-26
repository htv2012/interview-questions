#!/usr/bin/env bash
# Fix a broken project

projectDir="$1"
echo ""
echo ">>>> FIXING $projectDir"
echo ""

cd "$projectDir"
rm Makefile pyproject.toml
copier copy $HOME/my/copier-templates/uv-leetcode .
py_replace_logger.py *.py
make
