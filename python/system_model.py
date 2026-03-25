import numpy as np

def system_dynamics(A, B, x, u):
    return A @ x + B @ u
