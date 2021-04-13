#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())


# run like this: cat test.txt | ./capitalize.py
# or
# ./capitalize.py < test.txt
