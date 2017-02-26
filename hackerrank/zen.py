#!/bin/python3

import sys

n = int(input().strip())
octothorpe = '#'
space = ' '
result = ''
for i in range(n):
    result = (space * (n-1)) + (octothorpe * (i + 1))
    n -= 1
    print(result)
