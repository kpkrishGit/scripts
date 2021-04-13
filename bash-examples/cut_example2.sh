#!/bin/bash

for logfile in /var/log/*log; do
	echo "File; $logfile"
	cut -f' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
