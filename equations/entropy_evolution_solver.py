
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Natural units, but we track gamma explicitly
gamma = 1.0

def dH_dt(t, H):
    return - (gamma * H**3) / (2 * np.pi)

def solve_entropy_H(t_span, H0=1.0, num_points=1000):
    t_eval = np.linspace(t_span[0], t_span[1], num_points)
    sol = solve_ivp(dH_dt, t_span, [H0], t_eval=t_eval, method='RK45')
    return sol.t, sol.y[0]

def compute_scale_factor(t_array, H_array):
    dt = np.gradient(t_array)
    ln_a = np.cumsum(H_array * dt)
    return np.exp(ln_a - ln_a[0])  # Normalize a(t=0) = 1

if __name__ == "__main__":
    t0, t1 = 1e-5, 2.0  # Avoid t=0 singularity
    t_vals, H_vals = solve_entropy_H((t0, t1))
    a_vals = compute_scale_factor(t_vals, H_vals)

    plt.figure()
    plt.plot(t_vals, a_vals, label="a(t)")
    plt.xlabel("Time")
    plt.ylabel("Scale Factor a(t)")
    plt.title("Entropy-Driven Expansion: a(t)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("figures/entropy_scale_factor.png", dpi=300)
    plt.show()
