#!/bin/sh

python3 ./markdown_table_codegen.py <./testdata/testfile-input.txt >./testfile-output.txt

diff ./testfile-output.txt ./testdata/output-check.txt

result=$?

echo "result = $result"

exit $result