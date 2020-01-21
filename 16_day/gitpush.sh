#!/bin/bash

cd ~/girgit/100days_of_infosec/
git add .
read -p "Commit message: " message
git commit -m "$message"
git push origin master

