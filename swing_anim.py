import cloudpickle
import matplotlib.pyplot as plt
from matplotlib import animation, rc


kinematics = cloudpickle.load(open('./swing_kinematic.dll', 'rb'))

def swing_animation(sol):
    res = sol.response
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.axis('equal')
    plt.axis([-3, 3, -3, 3])
    ax.set_title('Swing animation')
    line1, = ax.plot([], [], lw=1, color='k', linestyle='-', marker='o', ms=5)
    line2, = ax.plot([], [], lw=2, color='b', linestyle='-', marker='o', ms=3)
    time_template = 'time = %.2fs'
    time_text = ax.text(-2.5, 2.5, '')
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        time_text.set_text('')
        return (line1, line2, time_text)

    def animate(i):
        p1, p2, p3, p21, p31 = kinematics(sol.response[i, :], sol.parameters)
        line1.set_data([0, p1[0]], [0, p1[1]])
        line2.set_data([p21[0], p2[0], p3[0], p31[0]], [p21[1], p2[1], p3[1], p31[1]])
        time_text.set_text('time = %.2fs'%sol.t[i])
        return (line1,line2, time_text)
    # call the animator. blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=1000, interval=10, blit=True)
    return anim

if __name__ =='__main__':
    import sys
    if len(sys.argv) > 1:
        sol_file = sys.argv[1]
    else:
        sol_file = './sol_eg.pkl'
    sol = cloudpickle.load(open(sol_file, 'rb'))
    ani = swing_animation(sol)
    plt.show(ani)