import numpy as np

def centered_mod(v, q):
    v = np.mod(v, q)
    half_q = q // 2
    return np.where(v > half_q, v - q, v)

def state_recover(Vx, scale=1.0, q=None):
    if q is not None:
        Vx = centered_mod(Vx, q)
    return Vx / scale
