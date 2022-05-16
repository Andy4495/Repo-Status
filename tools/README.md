# Repository Tools

This repository uses various tools to automate the creation of the README file and verify the links in the README.

`action-checkin.sh`

- Takes two arguments (pathnames to the old and new files) and pushes the new file to the repository if they differ
- Used by the [`Generate README`][3] workflow

`generate-README.sh`

- Generates the top-level [README.md][5] file
- Uses the [`README-header.txt`][6] file to start the file, calls `markdown_table_codegen.py` to generate the Markdown code for the tables, and then uses the [`README-footer.txt`][7] file to complete the README.md file
- Used by the [`Generate README`][3] workflow
- Can also be called manually at the command line. The first parameter is the output filename. If now output filename is specified, then the file `./README.md` is written.

`markdown_table_codegen.py`

- Generates the Markdown code for the repo status table. This code can be tedious and error-prone to write manually, so I created a Python script to generate the code based on the repository name and type.
- Used by `generate-README.sh`
- Can also be called manually at the command line
- Reads the repo type and repo name from stdin, and outputs Markdown code for the table row to stdout

`testscript.sh`

- Tests the `markdow_table_codegen.py` script by using input date from the `testdata` directory and comparing it against the output file in `testdata`
- Used by [`Verify codegen script`][4] workflow
- Can also be called manually at the command line

## License

The software and other files in this repository are released under what is commonly called the [MIT License][100]. See the file [`LICENSE.txt`][101] in this repository.

[1]: ./tools/markdown_table_codegen.py
[2]: ./tools/testscript.sh
[3]: https://github.com/Andy4495/Repo-Status/actions/workflows/generate-readme.yml
[4]: https://github.com/Andy4495/Repo-Status/actions/workflows/verify-codegen.yml
[5]: ../README.md
[6]: https://github.com/Andy4495/Repo-Status/blob/main/docs/README-header.txt
[7]: https://github.com/Andy4495/Repo-Status/blob/main/docs/README-footer.txt
[100]: https://choosealicense.com/licenses/mit/
[101]: ../LICENSE.txt
[200]: https://github.com/Andy4495/Repo-Status
