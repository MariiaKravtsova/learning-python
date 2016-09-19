""" Visualizing my Expenses """

import matplotlib.pyplot as plt

def draw_chart(labels, values):
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('expenses.png')
    plt.show()

if __name__ == '__main__':
    categories = int(input('Enter number of categories: '))
    labels = []
    values = []
    while categories > 0:
        label = input('Enter category: ')
        labels.append(label)
        value = float(input('Expenditure: '))
        values.append(value)
        categories = categories - 1
    draw_chart(labels, values)
