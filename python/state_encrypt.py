import numpy as np

def state_encrypt(Sx, V_prev, m_x, noise, q):
    V = Sx @ V_prev + m_x + noise
    return np.mod(V, q)
