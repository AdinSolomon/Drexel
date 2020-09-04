#!/bin/bash

# default to getting UG CS courses but take optional argument
if [ -z $1 ]; then
	courses_url='http://catalog.drexel.edu/coursedescriptions/quarter/undergrad/cs/'
else
	courses_url=$1
fi

# get the courses' department code thing from the url
regex="[/]([a-z]{0,4})[/]?$"
if [[ $courses_url =~ $regex ]]; then 
	department_code=${BASH_REMATCH[1]}
	[ -z $department_code ] && echo "didn't work" && exit
fi

# do the thing!
dlen=$(( ${#department_code} + 1 ))
curl "$courses_url" 2>/dev/null |
html2text |
uniq |
sed -n '/\*\*\*\* Courses \*\*\*\*/,$p' |
tail -n +2 |
sed -n '/\[P                   \] \[Search\]/q;p' |
head -n -1 |
awk -v RS= -v len=$dlen '{ sub(substr( $1, len, 1), "-", $1); print > ( "courses/" $1 ".course.unformatted") }'
