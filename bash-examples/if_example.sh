#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
	echo "Looks good"
else
	echo "Error: 127.0.0.1 not found in /etc/hosts"
fi
