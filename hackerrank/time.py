time = '02:45:54PM'
if time.endswith('PM'):
    status = time.split('PM')
    hours = status[0].split(':')
    if (hours[0] != '12'):
        hours[0] = str(int(hours[0]) + 12)
    if (int(hours[0]) >= 24):
        hours[0] = '00'
else:
    status = time.split('AM')
    hours = status[0].split(':')
    if (int(hours[0]) == 12):
        hours[0] = '00'
print(hours[0]+ ':' + hours[1] + ':' + hours[2])
