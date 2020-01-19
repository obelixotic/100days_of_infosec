#!/bin/bash

git add ~/girgit/100days_of_infosec/
read -p "Commit message: " message
git commit -m "$message"
git push origin master

