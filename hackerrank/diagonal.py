#!/bin/python3

import sys


n = int(input().strip())
a = []
count = 0
primary = 0
secondary = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for i in a:
    primary += i[count]
    count += 1
    secondary += i[n-1]
    n -= 1
print(abs(primary - secondary))
