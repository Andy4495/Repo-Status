# Repository Tools

This directory contains tools used by the [repository workflows][8].

[`action-checkin.sh`][9]

- Takes two arguments (pathnames to the old and new files) and pushes the new file to the repository if they differ
- Used by the [`Generate README`][3] workflow

[`generate-README.sh`][10]

- Generates the top-level [`README.md`][5] file
- Used by the [`Generate README`][3] workflow
- Uses the [`README-header.txt`][6] file to start the file, calls `markdown_table_codegen.py` to generate the Markdown code for the tables, and then uses the [`README-footer.txt`][7] file to complete the README.md file
- Can also be called manually at the command line. The first parameter is the output filename. If no output filename is specified, then the file `./README.md` is written.

[`markdown_table_codegen.py`][1]

- Generates the Markdown code for the repo status table. This code can be tedious and error-prone to write manually.
- Used by [`generate-README.sh`][10] as part of the [`Generate README`][3] workflow
- Can also be called manually at the command line (run from the top-level directory of the repository, not from the `tools` directory)
- Reads the repo type and repo name from `stdin`, and outputs Markdown code for the table row to `stdout`

[`testscript.sh`][2]

- Tests the [`markdow_table_codegen.py`][1] script by using [input data][12] from the [`testdata`][11] directory and comparing it against the [output file][13] in [`testdata`][11]
- Used by the [`Verify codegen script`][4] workflow
- Can also be called manually at the command line (run from the top-level directory of the repository, not from the `tools` directory)

## License

The software and other files in this repository are released under what is commonly called the [MIT License][100]. See the file [`LICENSE.txt`][101] in this repository.

[1]: ./markdown_table_codegen.py
[2]: ./testscript.sh
[3]: https://github.com/Andy4495/Repo-Status/actions/workflows/generate-readme.yml
[4]: https://github.com/Andy4495/Repo-Status/actions/workflows/verify-codegen.yml
[5]: ../README.md
[6]: https://github.com/Andy4495/Repo-Status/blob/main/docs/README-header.txt
[7]: https://github.com/Andy4495/Repo-Status/blob/main/docs/README-footer.txt
[8]: https://github.com/Andy4495/Repo-Status/actions
[9]: ./action-checkin.sh
[10]: ./generate-README.sh
[11]: ../tools/testdata
[12]: ../tools/testdata/testfile-input.txt
[13]: ../tools/testdata/output-check.txt
[100]: https://choosealicense.com/licenses/mit/
[101]: ../LICENSE.txt
[200]: https://github.com/Andy4495/Repo-Status
