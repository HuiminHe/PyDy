from scipy.integrate import odeint

from swing_config import *

f = cloudpickle.load(open('./swing_open_loop_dynamic.dll', 'rb'))

def fv_gen(amp, omega, phi, q_max):
    return lambda t, y: amp * np.sin(omega * t + phi) / (1 + np.exp((np.abs(y[1:3])-q_max) / 0.01) * np.logical_or(np.abs(y[1:3]) < q_max, y[1:3] * y[4:] > 0))

def open_loop_test(amp, omega, phi):
    amp = np.array([1, 1]) * 2 * np.pi *amp
    omega = np.array([1, 1]) * 10 * omega
    phi = np.array([np.pi*2, np.pi*2]) * phi
    fv = fv_gen(amp, omega, phi, q_max)
    q0 = np.array([np.pi/6, 0, 0])
    a0 = np.array([0, 0])
    v0 = fv(t0, np.r_[q0, np.zeros(3)])
    y0 = np.r_[q0, 0, v0]
    sol = odeint(f, y0, t, args=(param0, con0, a_max, dt))
    return Solution(t, sol, param0)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from swing_plot import swing_plot
    amp = 0.9
    omega = 0.1
    phi = 0
    sol = open_loop_test(amp, omega, phi)
    fig = swing_plot(sol)
    plt.show(fig)


