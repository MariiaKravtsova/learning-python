#! python3

import time
print('Press Enter')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        laptTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, laptTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')
