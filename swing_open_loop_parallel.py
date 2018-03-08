import numpy as np
import scipy
import multiprocessing as mp
from swing_open_loop import open_loop_test
from datetime import datetime

def f(i, j, k, N, arr):
    pid = N * N * i + N * j + k
    amp = i / (N-1)
    ome = j / (N-1)
    phi = k / (N-1)
    sol = open_loop_test(amp, ome, phi)
    np.save('./data/d{}'.format(pid), sol)
    print('Pid:%d solved for amp:%.2f\tomg:%.2f\tphi:%.2f' % (pid, amp * 2 * np.pi, ome * 10, phi * 2 * np.pi))
    print(str(datetime.now())[:-7] + '\ttask ID:{} is done'.format(pid))
    arr[pid] = np.max(np.abs(sol.response[:, 0]))

if __name__ == '__main__':
    N = 20
    m = mp.Manager()
    p = mp.Pool(processes=mp.cpu_count())
    arr = m.Array('f', [0]*N*N*N)
    workers = []

    for i in range(N):
        for j in range(N):
            for k in range(N):
               workers.append(p.apply_async(func=f, args=(i, j, k, N, arr)))

    work = lambda workers: [w.get() for w in workers]

    work(workers)

    arr = np.array(arr).reshape(N, N, N)
    np.save('./data/stat', arr)
    print('open loop analysis done')



