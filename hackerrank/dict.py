import sys

phonebook = {}
n = int(input())
for i in range(n):
    entry = input().split(' ')
    phonebook[entry[0]] = int(entry[1])

for i in range(n):
    name = input()
    if name in phonebook:
        print("{}={}".format(name, phonebook[name]))
    else:
        print("Not found")
