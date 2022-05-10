# https://github.com/Andy4495/Repo-Status
#
# Usage: 
#   python3 markdown_table_codegen.py library|sketch|other
# 
# This script automates the creation of the Markdown text needed to create a table entry
# for a repo. There are three types of repos represented in the status table: libraries, 
# sketches and other. This script takes exactly one command line argument indicating the
# type of repo, reads stdin for repo names, and outputs the generated Markdown text to stdout.
#

from sys import stdin
import sys

username = "Andy4495/"
github = "https://github.com/" + username
shields = "https://img.shields.io/github/"
stars = "[GitHub Repo stars]"
forks = "[GitHub forks]"
compile = "[Arduino Compile Sketches]"
markdown = "[Check Markdown Links]"
release = "[GitHub release (latest SemVer)]"
reldate = "[GitHub Release Date]"
flat = "?style=flat"

if len(sys.argv) != 2:
  print("Usage: " + sys.argv[0] + " library | sketch | other")
  quit()

repotype = sys.argv[1]

for line in stdin:
  repo = line.strip()
  if repotype == 'library':
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| [!" + stars + "(" + shields + "stars/" + username + repo + flat + ")](" + github + repo + "/stargazers) [!" + 
    forks + "(" + shields + "forks/" + username + repo + flat + ")](" + github + repo + "/network/members) ", end = '')
    print("| [!" + compile + "(" + github + repo + "/actions/workflows/arduino-compile-sketches.yml/badge.svg)](" + 
    github + repo + "/actions/workflows/arduino-compile-sketches.yml) [!" + markdown + "(" + github + repo +
    "/actions/workflows/CheckMarkdownLinks.yml/badge.svg)](" + github + repo + "/actions/workflows/CheckMarkdownLinks.yml) | ", end = '')
    print("[!" + release + "(" + shields + "v/release/" + username + repo + ")](" + github + repo + "/releases) [!" + reldate + "(" +
    shields + "release-date/" + username + repo + ")](" + github + repo + "/releases) |")
  if repotype == "sketch":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| [!" + stars + "(" + shields + "stars/" + username + repo + flat + ")](" + github + repo + "/stargazers) [!" + 
    forks + "(" + shields + "forks/" + username + repo + flat + ")](" + github + repo + "/network/members) ", end = '')
    print("| [!" + compile + "(" + github + repo + "/actions/workflows/arduino-compile-sketches.yml/badge.svg)](" + 
    github + repo + "/actions/workflows/arduino-compile-sketches.yml) [!" + markdown + "(" + github + repo +
    "/actions/workflows/CheckMarkdownLinks.yml/badge.svg)](" + github + repo + "/actions/workflows/CheckMarkdownLinks.yml) |")
  if repotype == "other":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| [!" + stars + "(" + shields + "stars/" + username + repo + flat + ")](" + github + repo + "/stargazers) [!" + 
    forks + "(" + shields + "forks/" + username + repo + flat + ")](" + github + repo + "/network/members) ", end = '')
    print("| [!"  + markdown + "(" + github + repo +
    "/actions/workflows/CheckMarkdownLinks.yml/badge.svg)](" + github + repo + "/actions/workflows/CheckMarkdownLinks.yml) |")

