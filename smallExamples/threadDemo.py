import time, threading

print('Run')
def pause():
    time.sleep(3)
    print('Resume')
threadObj = threading.Thread(target=pause)
threadObj.start()
print('Stop')
