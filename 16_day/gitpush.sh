#!/bin/bash

git add .
git add -u
read -p "Commit message: " message
git commit -m "$message"
git push origin master

