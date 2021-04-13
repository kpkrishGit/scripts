#!/bin/bash
cut -d' ' -f5- test1.txt | sort | uniq -c | sort -nr | head

# -f5- field 5 and everything after
