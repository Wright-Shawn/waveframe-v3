"""
structure_growth_solver.py

Computes fσ₈(z) for an entropy-driven cosmology model.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, cumtrapz
from scipy.interpolate import interp1d

# ---- CONFIG ----
z_max = 3
z_samples = 300
z_vals = np.linspace(0, z_max, z_samples)

# Load or define H(z) here
# For demonstration: H(z) ∼ 1 / ln(1 + z)
def H_z(z, H0=70, alpha=1.0):
    return H0 / np.log(1 + alpha * (1 + z))

Hz_vals = H_z(z_vals)
Hz_interp = interp1d(z_vals, Hz_vals, kind='cubic')

# ---- GROWTH EQUATION ----
# Linear growth equation: D'' + [ (dlnH/dz) - (1+z)^{-1} ] D' - 3/2 * Ω_m(z) D / (1+z)^2 = 0
# Assume effective Ω_m(z) from entropy dynamics, not ΛCDM

def growth_rhs(D, z, H_func, H0, gamma_eff=0.3):
    D1, D2 = D
    H = H_func(z)
    dH_dz = (H_func(z + 1e-3) - H_func(z - 1e-3)) / 2e-3
    term1 = - (1 + z)**-1
    term2 = dH_dz / H
    source = 1.5 * gamma_eff * D1 / (1 + z)**2
    D1_prime = D2
    D2_prime = - (term1 + term2) * D2 + source
    return [D1_prime, D2_prime]

# Initial conditions: Early universe growth starts linear
D_init = [1e-5, 1e-5]
D_sols = odeint(growth_rhs, D_init, z_vals[::-1], args=(Hz_interp, 70))
D_sols = D_sols[::-1]  # Flip back to increasing z

# Normalize D(z)
D_vals = D_sols[:, 0]
D_vals /= D_vals[0]

# Compute f(z) = dlnD/dln a = -(1+z) dlnD/dz
f_vals = - (1 + z_vals) * np.gradient(np.log(D_vals), z_vals)

# Assume σ₈(z=0) = 0.8
fs8_vals = f_vals * D_vals * 0.8

# ---- PLOT ----
plt.figure(figsize=(8,5))
plt.plot(z_vals, fs8_vals, label=r'f$\sigma_8$(z)', color='darkred')
plt.xlabel('Redshift z')
plt.ylabel(r'f$\sigma_8$(z)')
plt.title('Structure Growth in Entropic Cosmology')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("fsigma8_entropic_model.png", dpi=300)
plt.close()
