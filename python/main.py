import numpy as np
from system_model import system_dynamics
from controller import controller
from state_encrypt import state_encrypt
from state_recover import state_recover
from utils import quantize_state, sample_noise

def main():
    A = np.array([[0.5, 0.0, 0.0],
                  [0.1, 0.6, 0.0],
                  [0.0, 0.2, 0.7]])

    B = np.array([[1.0],
                  [0.0],
                  [1.0]])

    K = np.array([[0.2, 0.1, 0.3]])
    r = np.array([[500.0]])
    x = np.array([[5.0],
                  [2.0],
                  [1.0]])

    q = 2**31 - 1
    scale = 1.0
    sigma = 1.0
    n = x.shape[0]

    Sx = np.array([[2, 1, 0],
                   [0, 1, 1],
                   [1, 0, 2]], dtype=np.int64)

    Vx = np.zeros((n, 1), dtype=np.int64)

    N = 10

    print("Running state-encryption-only simulation...\n")

    for k in range(N):
        u = controller(K, x, r)
        x_next = system_dynamics(A, B, x, u)

        m_x = quantize_state(x, scale=scale)
        noise = sample_noise((n, 1), sigma=sigma)
        Vx = state_encrypt(Sx, Vx, m_x, noise, q)

        x_rec = state_recover(Vx, scale=scale, q=q)

        print(f"Step {k}")
        print("x      =\n", x)
        print("u      =\n", u)
        print("Vx     =\n", Vx)
        print("x_rec  =\n", x_rec)
        print("-" * 40)

        x = x_next

if __name__ == "__main__":
    main()
