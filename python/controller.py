import numpy as np

def controller(K, x, r):
    return r - K @ x
