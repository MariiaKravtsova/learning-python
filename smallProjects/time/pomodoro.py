import time, webbrowser

print('How long are you styding for?')
study = int(input()) * 60
print('How long is your break?')
pause = int(input()) * 60

while study > 0:
    time.sleep(1)
    study = study - 1
    print(study)

webbrowser.open('https://www.youtube.com/watch?v=c6rP-YP4c5I')

while pause > 0:
    time.sleep(1)
    pause = pause - 1

webbrowser.open('https://trello.com/b/INnUpB2g/weekly')
