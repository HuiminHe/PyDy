import numpy as np
import cloudpickle
from collections import namedtuple

Solution = namedtuple('Solution', ['t', 'response', 'parameters'])


param0 = np.array([1, 1, 1,
                   1/12, 1/12, 1/12,
                   1.5, 1, 1, 1,
                   0.5, 0.5, 0.5,
                   0.5, 0.5,
                   9.8])

con0 = np.array([1000, 100, 0.01, np.deg2rad(75)])
a_max = np.array([10, 10]) * 10
q_max = np.array([1, 1]) * con0[-1]

t0 = 0
t1 = 10
dt = 0.01
t = np.arange(t0, t1, dt)
