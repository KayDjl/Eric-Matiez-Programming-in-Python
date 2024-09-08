import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()
    points_number = range(rw.num_points)
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=10)
 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    
    keep_run = input("y/n: ")
    if keep_run == 'n':
        break