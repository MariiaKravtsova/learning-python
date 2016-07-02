import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, low and high temperatures from a csv file
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, lows, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        low = int(row[3])
        lows.append(low)

        high = int(row[1])
        highs.append(high)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format Plot
plt.title('Daily high and low temperatures 2014', fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperatures', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()