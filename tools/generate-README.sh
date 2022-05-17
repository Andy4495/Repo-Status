#!/bin/sh

# https://github.com/Andy4495/Repo-Status

# Script to auto-generate top-level README.md file
# Run this script from the top-level repository directory

if [ $1 ]
then
  FILENAME=$1
else 
  FILENAME=./README.md
fi

echo "Using output filename: $FILENAME"

echo "[//]: # ( THIS FILE IS AUTO-GENERATED! DO NOT EDIT THIS FILE DIRECTLY )" >$FILENAME
echo "[//]: # ( To make changes to this README, edit files in the docs directory instead. )" >>$FILENAME
echo "" >>$FILENAME

cat ./docs/README-header.txt >>$FILENAME

cat <<EOF >>$FILENAME

## Libraries

|   |   |   |  |
|-|-|-|-|
EOF

python3 ./tools/markdown_table_codegen.py <./docs/repo-list-libraries.txt >>$FILENAME

cat <<EOF >>$FILENAME

## Sketches

|  |  |  |  |
|-|-|-|-|
EOF

python3 ./tools/markdown_table_codegen.py <./docs/repo-list-sketches.txt >>$FILENAME

cat <<EOF >>$FILENAME

## Other

|  |  |  |  |
|-|-|-|-|
EOF

python3 ./tools/markdown_table_codegen.py <./docs/repo-list-other.txt >>$FILENAME

echo >>$FILENAME

cat ./docs/README-footer.txt >>$FILENAME
