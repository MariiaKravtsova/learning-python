def even_odd(arr):
    odd = ''
    even = ''
    for i in arr:
        if arr.index(i) % 2 == 0:
            even += i
        else:
            odd += i
    print(even, odd)

t = int(input())
arr = list()
for i in range(t):
    s = input().strip()
    arr.append(s)

for i in range(len(arr)):
    even_odd(list(arr[i]))
