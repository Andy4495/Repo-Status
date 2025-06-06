# https://github.com/Andy4495/Repo-Status
#
# Usage: 
#   python3 markdown_table_codegen.py
#
#   Reads from stdin, two parameters per line: <repo-type> and repo-name
#     <repo-type> is one of: 
#       library | library-nocompile | sketch | sketch-nocompile | informational | <other>
#     <other> is one of: 
#       copy | copy-no-actions | fork | clone | archive
# 
# This script automates the creation of the Markdown text needed to create a table entry
# for a repo.
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
build = "[Build]"
release = "[GitHub release (latest SemVer)]"
reldate = "[GitHub Release Date]"
lastcommit = "[GitHub last commit]"
flat = "?style=flat"
compilesvg = "/actions/workflows/arduino-compile-sketches.yml/badge.svg"
compileyml = "/actions/workflows/arduino-compile-sketches.yml"
mdsvg = "/actions/workflows/check-links.yml/badge.svg"
mdyml = "/actions/workflows/check-links.yml"
buildsvg = "/actions/workflows/Build.yml/badge.svg"
buildyml = "/actions/workflows/Build.yml"

if len(sys.argv) != 1:
  print("Usage: " + sys.argv[0])
  quit()


for line in stdin:
  items = line.strip().split()
  repotype = items[0]
  repo = items[1]
  if repotype == 'library':
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| [!" + stars + "(" + shields + "stars/" + username + repo + flat + ")](" + github + repo + "/stargazers) [!" + 
    forks + "(" + shields + "forks/" + username + repo + flat + ")](" + github + repo + "/network/members) ", end = '')
    print("| [!" + compile + "(" + github + repo + compilesvg + ")](" + github + repo + compileyml + ") [!" + 
    markdown + "(" + github + repo + mdsvg + ")](" + github + repo + mdyml +  ") ", end = '')
    print("| [!" + release + "(" + shields + "v/release/" + username + repo + ")](" + github + repo + "/releases) [!" + reldate + "(" +
    shields + "release-date/" + username + repo + ")](" + github + repo + "/releases) ", end = '')
    print("[!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == 'library-nocompile':
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| [!" + stars + "(" + shields + "stars/" + username + repo + flat + ")](" + github + repo + "/stargazers) [!" + 
    forks + "(" + shields + "forks/" + username + repo + flat + ")](" + github + repo + "/network/members) ", end = '')
    print("| [!" + markdown + "(" + github + repo + mdsvg + ")](" + github + repo + mdyml +  ") ", end = '')
    print("| [!" + release + "(" + shields + "v/release/" + username + repo + ")](" + github + repo + "/releases) [!" + reldate + "(" +
    shields + "release-date/" + username + repo + ")](" + github + repo + "/releases) ", end = '')
    print("[!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == "sketch":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| [!" + stars + "(" + shields + "stars/" + username + repo + flat + ")](" + github + repo + "/stargazers) [!" + 
    forks + "(" + shields + "forks/" + username + repo + flat + ")](" + github + repo + "/network/members) ", end = '')
    print("| [!" + compile + "(" + github + repo + compilesvg + ")](" + github + repo + compileyml + ") [!" + 
    markdown + "(" + github + repo + mdsvg + ")](" + github + repo + mdyml + ") ", end = '')
    print("| [!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == "sketch-nocompile":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| [!" + stars + "(" + shields + "stars/" + username + repo + flat + ")](" + github + repo + "/stargazers) [!" + 
    forks + "(" + shields + "forks/" + username + repo + flat + ")](" + github + repo + "/network/members) ", end = '')
    print("| [!" + markdown + "(" + github + repo + mdsvg + ")](" + github + repo + mdyml + ") ", end = '')
    print("| [!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == "copy":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| Copy " , end = '')
    print("| [!" + compile + "(" + github + repo + compilesvg + ")](" + github + repo + compileyml + ") [!" + 
    markdown + "(" + github + repo + mdsvg + ")](" + github + repo + mdyml + ") ", end = '')
    print("| [!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == "copy-no-actions":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| Copy " , end = '')
    print("| *No Actions* ", end = '')
    print("| [!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == "fork":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| Fork " , end = '')
    print("| *No Actions* ", end = '')
    print("| [!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == "clone":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| Clone " , end = '')
    print("| *No Actions* ", end = '')
    print("| [!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == "archive":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| Archive " , end = '')
    print("| *No Actions* ", end = '')
    print("| [!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == "informational":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| [!" + stars + "(" + shields + "stars/" + username + repo + flat + ")](" + github + repo + "/stargazers) [!" + 
    forks + "(" + shields + "forks/" + username + repo + flat + ")](" + github + repo + "/network/members) ", end = '')
    print("| [!"  + markdown + "(" + github + repo + mdsvg +  ")](" + github + repo + mdyml + ") ", end = '')
    print("| [!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")
  if repotype == "program":
    print("| [" + repo +"](" + github + repo + ") ", end = '')
    print("| [!" + stars + "(" + shields + "stars/" + username + repo + flat + ")](" + github + repo + "/stargazers) [!" + 
    forks + "(" + shields + "forks/" + username + repo + flat + ")](" + github + repo + "/network/members) ", end = '')
    print("| [!" + build + "(" + github + repo + buildsvg + ")](" + github + repo + buildyml + ") [!" + 
    markdown + "(" + github + repo + mdsvg + ")](" + github + repo + mdyml + ") ", end = '')
    print("| [!" + lastcommit + "(" + shields + "last-commit/" + username + repo + ")](" + github + repo + "/commits) |")

