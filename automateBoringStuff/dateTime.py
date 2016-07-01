import datetime
countTo = datetime.datetime(2017, 12, 17, 00, 00, 00)
graduationIn = countTo - datetime.datetime.now()
print('Days till graduation: ' + str(graduationIn))
