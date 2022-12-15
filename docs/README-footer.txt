[**Archive**][19] - Read-only repo with no further updates planned  
[**Clone**][18] - Full copy of a repo, but not linked to the original repo  
**Copy** - Similar to a clone, but only a portion of the original repo is copied. For example, a specific tag or folder  
[**Fork**][18] - Full copy of a repo which is linked to the original, upstream repo  
**Program** - Linux/Unix executable

## Markdown Code Auto-Generated

[Markdown][17] is intended to be easy-to-read and easy-to-write. Per its creators:

> The overriding design goal for Markdown’s formatting syntax is to make it as readable as possible. The idea is that a Markdown-formatted document should be publishable as-is, as plain text, without looking like it’s been marked up with tags or formatting instructions.

As a [text file][20], this Markdown-based [`README.md`][21] file is neither easy-to-read nor easy-to-write, and should not be considered a good example of using Markdown. In particular, the syntax for the tables and the badges is cumbersome to read and write.

With that in mind, **this [`README.md`][21] file is automatically generated from files in the [`docs`][7] directory**. Any time a source file is changed in that directory, the [`Generate README`][4] workflow is triggered. The workflow generates a new top-level README and automatically pushes the updated version to the repository.

Manually changing this [`README.md`][21] file directly will trigger the [`Generate README`][4] workflow, overwriting any manual changes and reverting the text back to whatever is defined by the `docs` directory files.

## Tools

See the [`README`][6] file in the [`tools`][5] directory for a description of the various tools used to maintain this repository.

## GitHub Features

This repo also demonstrates various GitHub features, including:

- [GitHub actions][9]
  - Several workflows are defined:
    - Validate links in the README files ([`Check Markdown Links`][10])
    - Validate a script ([`Verify codegen script`][11])
    - Auto-generate and push a file to the repo ([`Generate README`][12])
- [GitHub Environment Variables][14]
  - Used in action scripts
- [GitHub Job Summaries][15]
  - Used in action scripts
  - [Blog entry][16] introducing the feature
- [GitHub Flavored Markdown (GFM)][8]
  - Used to display the repo status tables
- [Badges/Shields][13]
  - GitHub-defined shields for workflow status
  - Shields.io-defined shields for other status
  
## License

The software and other files in this repository are released under what is commonly called the [MIT License][100]. See the file [`LICENSE.txt`][101] in this repository.

[4]: https://github.com/Andy4495/Repo-Status/actions/workflows/generate-readme.yml
[5]: ./tools
[6]: ./tools/README.md
[7]: ./docs
[8]: https://github.github.com/gfm/#tables-extension-
[9]: https://docs.github.com/en/actions
[10]: https://github.com/Andy4495/Repo-Status/actions/workflows/CheckMarkdownLinks.yml
[11]: https://github.com/Andy4495/Repo-Status/actions/workflows/verify-codegen.yml
[12]: https://github.com/Andy4495/Repo-Status/actions/workflows/generate-readme.yml
[13]: https://github.com/badges/shields
[14]: https://docs.github.com/en/actions/learn-github-actions/environment-variables
[15]: https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#adding-a-job-summary
[16]: https://github.blog/2022-05-09-supercharging-github-actions-with-job-summaries/
[17]: https://daringfireball.net/projects/markdown/
[18]: https://github.community/t/the-difference-between-forking-and-cloning-a-repository/10189
[19]: https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories
[20]: https://raw.githubusercontent.com/Andy4495/Repo-Status/main/README.md
[21]: ./README.md
[100]: https://choosealicense.com/licenses/mit/
[101]: ./LICENSE.txt
[//]: # ([200]: https://github.com/Andy4495/Repo-Status)
