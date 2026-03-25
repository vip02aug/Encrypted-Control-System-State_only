import numpy as np

def quantize_state(x, scale=1.0):
    return np.round(scale * x).astype(np.int64)

def sample_noise(shape, sigma=1.0):
    return np.round(np.random.normal(0, sigma, shape)).astype(np.int64)
