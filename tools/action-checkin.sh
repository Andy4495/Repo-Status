#!/bin/sh

# https://github.com/Andy4495/Repo-Status

# Script to checkin file inside GitHub action if it changed
# Required first parameter is original file
# Required second parameter is updated file, and is the file that will be pushed to repo

diff $1 $2

result=$?

if [ $result -ne 0 ]
then
  echo "Pushing updated file $2"
  git config --global user.email "Andy4495@users.noreply.github.com"
  git config --global user.name "Andreas Taylor"
  git add $2
  git commit -m "Update $2 by generate-readme.yml action"
  git push origin main
  echo "$2 changed -> pushed new version to $GITHUB_REPOSITORY. " >> $GITHUB_STEP_SUMMARY
else
  echo "File did not change."
  echo "$2 unchanged. $GITHUB_REPOSITORY not updated." >> $GITHUB_STEP_SUMMARY
fi




