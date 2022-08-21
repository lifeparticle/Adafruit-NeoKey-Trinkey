#!/bin/sh

mkdir test

if [ $? -eq 0 ]; then
   echo "Folder created: " test
else
	num=0
	while ! mkdir test$num
	do
		num=$((num+1))
	done
	echo "Folder created: " test$num
fi