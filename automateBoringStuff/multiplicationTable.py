i = 0
j = 0
while i < 10:
    for j in range(10):
        result = i * j
        print('%d * %d = %d' % (j, i, result))
        j += 1
    print('\n')
    i += 1
