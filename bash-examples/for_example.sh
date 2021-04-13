#!/bin/bash

for file in *.HTM; do
	name=$(basename "$file" .HTM)
	#echo mv "$file" "$name.html"
	# try with echo first to verify the script
	mv "$file" "$name.html"
done


# basename file.HTM .HTM => file
