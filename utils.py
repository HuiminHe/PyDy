import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import cloudpickle

kinematic = cloudpickle.load(open('./swing_kinematic.dll', 'rb'))

def swing_animation(sol, param0):
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.axis('equal')
    plt.axis([-3, 3, -3, 3])

    line1, = ax.plot([], [], lw=1, color='k', linestyle='-', marker='o', ms=5)
    line2, = ax.plot([], [], lw=2, color='b', linestyle='-', marker='o', ms=3)

    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return (line1, line2)

    def animate(i):
        y = sol[i, :]
        p1, p2, p3, p21, p31 = kinematic(sol[i, :], param0)
        line1.set_data([0, p1[0]], [0, p1[1]])
        line2.set_data([p21[0], p2[0], p3[0], p31[0]], [p21[1], p2[1], p3[1], p31[1]])
        return (line1,line2)
    # call the animator. blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=1000, interval=10, blit=True)
    return anim


