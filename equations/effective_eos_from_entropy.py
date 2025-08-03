
"""
Compute the effective equation of state w_eff(z) and deceleration parameter q(z)
from an entropy-driven cosmology model.

Assumes H(z) is defined from the entropy growth law:
    H(z) = H0 * (1 + z)^{-β}, where β = 0.5 for entropic model with H(t) ∝ 1/√(t − t0)
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
H0 = 70.0  # km/s/Mpc
z_vals = np.linspace(0.01, 4, 500)  # Avoid z=0 for derivative

# Define model H(z) from entropy-driven cosmology
beta = 0.5
H = H0 * (1 + z_vals)**(-beta)

# Compute dlnH/dln(1+z)
lnH = np.log(H)
ln1pz = np.log(1 + z_vals)
dlnH_dln1pz = np.gradient(lnH, ln1pz)

# Effective equation of state:
w_eff = -1 + (2/3) * dlnH_dln1pz

# Deceleration parameter:
q = -1 + dlnH_dln1pz

# Plot w_eff(z)
plt.figure()
plt.plot(z_vals, w_eff, label=r'$w_{\mathrm{eff}}(z)$', color='darkred')
plt.axhline(-1, ls='--', color='gray', lw=0.8)
plt.xlabel('Redshift z')
plt.ylabel(r'Effective $w(z)$')
plt.title('Effective Equation of State from Entropic Expansion')
plt.grid(True)
plt.legend()
plt.savefig("figures/effective_w_z.png", dpi=300)

# Plot q(z)
plt.figure()
plt.plot(z_vals, q, label=r'$q(z)$', color='darkblue')
plt.axhline(0, ls='--', color='gray', lw=0.8)
plt.xlabel('Redshift z')
plt.ylabel(r'Deceleration Parameter $q(z)$')
plt.title('Deceleration Parameter from Entropic Expansion')
plt.grid(True)
plt.legend()
plt.savefig("figures/deceleration_param.png", dpi=300)

print("Saved: effective_w_z.png and deceleration_param.png")
