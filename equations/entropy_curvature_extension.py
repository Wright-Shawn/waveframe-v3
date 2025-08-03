
"""
entropy_curvature_extension.py

Extension of the entropic cosmology framework to include spatial curvature.
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants (can be adjusted for different unit systems)
H0 = 70  # Hubble constant in km/s/Mpc
gamma = 1.0  # Entropic growth rate
pi = np.pi
c = 299792.458  # Speed of light in km/s

# Spatial curvature parameter: -1 (open), 0 (flat), 1 (closed)
Omega_k = 0.1

# Define redshift array
z_vals = np.linspace(0.01, 5, 500)

def H_entropy(z, gamma=1.0):
    return np.sqrt(pi / (gamma * np.log(1 + z)))

def H_total(z, gamma=1.0, Omega_k=0.0):
    H_ent = H_entropy(z, gamma)
    return np.sqrt(H_ent**2 + Omega_k * (1 + z)**2)

# Compute H(z) including curvature
H_vals = H_total(z_vals, gamma=gamma, Omega_k=Omega_k)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(z_vals, H_vals, label=f"Entropy+Curvature Model ($\Omega_k$ = {Omega_k})")
plt.xlabel("Redshift z")
plt.ylabel("H(z) [normalized units]")
plt.title("Entropy-Driven Cosmology with Spatial Curvature")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("/mnt/data/entropy_curvature_extension.png")
plt.show()
