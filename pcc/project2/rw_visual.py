import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep walking randomly
while True:
    # Make a random walk, and plot the points
    rw = RandomWalk(5000)
    rw.fill_walk()
    # Set size for the plotting window
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    #plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
    #    cmap=plt.cm.OrRd, edgecolor='none', s=1)

    # Highlight first one
    plt.scatter(0, 0, c='green', edgecolor='none', s=5)
    # Highlight last one
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolor='none', s=5)

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (Y/N): ')
    if keep_running == 'N':
        break
