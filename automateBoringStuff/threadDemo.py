import time, threading, datetime

startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)

print('Program now starting on Halloween 2029')
#
# print('Run')
# def pause():
#     time.sleep(3)
#     print('Resume')
# threadObj = threading.Thread(target=pause)
# threadObj.start()
# print('Stop')
