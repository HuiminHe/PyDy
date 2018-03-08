from scipy.integrate import odeint
from swing_config import *

f = cloudpickle.load(open('./swing_open_loop_dynamic.dll', 'rb'))

def fv_gen(amp, ome, phi, q_max):
    return lambda t, y: amp * np.sin(ome * t + phi) / (1 + np.exp((np.abs(y[1:3])-q_max) / 0.01) * np.logical_or(np.abs(y[1:3]) < q_max, y[1:3] * y[4:] > 0))

def open_loop_test(amp, ome, phi):
    amp = np.ones(2) * amp_max *amp
    ome = np.ones(2) * ome_max * ome
    phi = np.ones(2) * phi_max * phi

    fv = fv_gen(amp, ome, phi, q_max)
    q0 = np.array([np.pi/6, 0, 0])
    a0 = np.array([0, 0])
    v0 = fv(t0, np.r_[q0, np.zeros(3)])
    y0 = np.r_[q0, 0, v0]
    sol = odeint(f, y0, t, args=(param0, con0, a_max, fv, dt))
    return Solution(t, sol, param0)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from swing_plot import swing_plot
    from swing_anim import swing_animation
    amp = 0
    ome = 0
    phi = 0
    sol = open_loop_test(amp, ome, phi)
    #fig = swing_plot(sol)
    #plt.show(fig)
    anim = swing_animation(sol)
    plt.show(anim)

