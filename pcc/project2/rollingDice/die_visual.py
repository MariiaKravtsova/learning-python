import pygal
from die import Die

# Creating two D8
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list
results = []

for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyzing results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D8 50000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'
    '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequncy of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual.svg')
