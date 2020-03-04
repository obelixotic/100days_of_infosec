#!/bin/bash

for ((i=1000; i>1; i--));
do
tar -xvf "${i}.tar"
rm ${i}.tar
done
