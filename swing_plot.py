import matplotlib.pyplot as plt
from numpy import pi

def swing_plot(sol):
    fig, axes = plt.subplots(2, 3, figsize=(9, 7))
    axes = axes.ravel()
    for i, ax in enumerate(axes):
        ax.plot(sol.t, sol.response[:, i])
        if i < 3:
            ax.plot([sol.t[0], sol.t[-1]], [ pi/2, pi/2], 'r--')
            ax.plot([sol.t[0], sol.t[-1]], [-pi/2,-pi/2], 'r--')
            ax.set_title('$q_{}$'.format(i+1))
        else:
            ax.set_title('$\dot{q}_' + '{}$'.format(i-2))
    return fig
