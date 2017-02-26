#!/bin/python
arr = [1, 2, 3, 4, 5]
x = sum(arr)
print("{} {}".format(x-max(arr), x-min(arr)))
print(*arr, sep='\n')
arr1 = map(float, arr)
print(*arr1)
print(arr)
