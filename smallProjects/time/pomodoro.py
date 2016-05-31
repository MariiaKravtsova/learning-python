import datetime

print('How long are you styding for?')
study = int(input())
now = datetime.datetime.now()
print('How long is your break?')
pause = input()

while study > 0:
    studyTime = datetime.datetime.now().time.minute(study) - datetime.datetime.now()

print(studyTime)
