#!/bin/bash

declare -A fields
i=0
for boi in $(cat testcourse); do
	echo $boi
	fields[$i]=$boi
done


