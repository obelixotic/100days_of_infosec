#!/bin/bash

alias gtw='cd $working_dir'

wd(){
	working_dir=$(pwd)
	echo "You're working dir is $working_dir"
}
