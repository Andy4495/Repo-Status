#!/bin/sh

chmod +x ./tools/markdown_table_codegen.py

python3 ./tools/markdown_table_codegen.py <./tools/testdata/testfile-input.txt >./testfile-output.txt

diff ./testfile-output.txt ./tools/testdata/output-check.txt

result=$?

echo "result = $result"

exit $result
