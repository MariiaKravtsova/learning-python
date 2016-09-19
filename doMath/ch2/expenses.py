""" Visualizing my Expenses """

import matplotlib.pyplot as plt
import csv

def process_csv():
    with open('expenses.csv', newline='') as csvfile:
        streamreader = csv.reader(csvfile, delimiter=',')
        labels = []
        values = []
        for row in streamreader:
            labels.append(row[0])
            values.append(row[1])
    draw_chart(labels, values)

def draw_chart(labels, values):
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('expenses.png')
    plt.show()

if __name__ == '__main__':
    process_csv()
