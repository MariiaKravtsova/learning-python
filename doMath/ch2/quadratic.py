""" Quadratic function calculator and plotter """
import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x coordinates')
    plt.ylabel('y coordinates')
    plt.title('Quadratic Function')
    plt.show()
    plt.savefig('quadratic.png')

if __name__ == '__main__':
    x_values = range(-5, 5)
    y_values = []
    for x in x_values:
        y = x**2 + 2*x + 1
        y_values.append(y)
    draw_graph(x_values, y_values)
