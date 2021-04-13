#!/bin/bash

n=0
cmd=$1
while ! $cmd && [ $n -le 5 ]; do
	sleep $n
	((n+=1))
	echo "Retry #$n"
done;


#$ ./while_example2.sh p1
#./while_example2.sh: line 5: p1: command not found
#Retry #1
#./while_example2.sh: line 5: p1: command not found
#Retry #2
#./while_example2.sh: line 5: p1: command not found
#Retry #3
#./while_example2.sh: line 5: p1: command not found
#Retry #4
#./while_example2.sh: line 5: p1: command not found
#Retry #5
#./while_example2.sh: line 5: p1: command not found
#Retry #6
#./while_example2.sh: line 5: p1: command not found
#
