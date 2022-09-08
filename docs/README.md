# About This Directory

The top-level repository [README.md][1] file is auto-generated based on files in the [`docs`][9] directory.

The repo status tables are generated from the files [`repo-list-libraries.txt`][2], [`repo-list-sketches.txt`][3], [`repo-list-informational.txt`][10] and [`repo-list-other.txt`][4].

The rest of the README is copied as-is from [`README-header.txt`][5] (for text before the status tables) and [`README-footer.txt`][6] (for text after the status tables).

Therefore, in order to edit the top-level README.md file, edit the files in this `docs` directory, and the [`Generate README`][8] workflow will auto-generate and checkin a new README.md file using the [`generate-README.sh`][7] script.

## License

The software and other files in this repository are released under what is commonly called the [MIT License][100]. See the file [`LICENSE.txt`][101] in this repository.

[1]: ../README.md
[2]: ./repo-list-libraries.txt
[3]: ./repo-list-sketches.txt
[4]: ./repo-list-other.txt
[5]: ./README-header.txt
[6]: ./README-footer.txt
[7]: ../tools/generate-README.sh
[8]: https://github.com/Andy4495/Repo-Status/actions/workflows/generate-readme.yml
[9]: ../docs
[10]: ./repo-list-informational.txt
[100]: https://choosealicense.com/licenses/mit/
[101]: ../LICENSE.txt
[//]: # ([200]: https://github.com/Andy4495/Repo-Status)
