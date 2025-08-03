"""
redshift_entropy_link.py

Links redshift z to entropy S(z), Hubble parameter H(z), and cosmic time t(z)
in the Waveframe entropic cosmology model.
"""

import numpy as np
from scipy.integrate import quad

# Constants
H0_km_s_Mpc = 70.0                # Hubble constant in km/s/Mpc
c_km_s = 299792.458               # Speed of light in km/s
unit_scale = c_km_s / H0_km_s_Mpc # Mpc conversion factor

# Model parameter (can be tuned)
gamma = 1.0                       # Entropy production rate

# Hubble function under entropy law
def H_of_t(t, gamma=gamma):
    return np.sqrt(np.pi / (gamma * t))

# Inverse of redshift-time relation for entropy-driven model
def t_of_z(z, gamma=gamma):
    # a(t) ~ exp(A * sqrt(t)) implies ln(1+z) ~ sqrt(t)
    A = np.sqrt(np.pi / gamma)
    return (np.log(1 + z) / (2 * A))**2

# H(z) directly from t(z)
def H_of_z(z, gamma=gamma):
    t = t_of_z(z, gamma)
    return H_of_t(t, gamma)

# S(z) from H(z)
def entropy_of_z(z, gamma=gamma):
    H = H_of_z(z, gamma)
    return np.pi / H**2

# Comoving distance integrand
def integrand_dz(zp, gamma=gamma):
    return 1.0 / H_of_z(zp, gamma)

# Compute luminosity distance (optional for cross-checking)
def luminosity_distance(z, gamma=gamma):
    integral, _ = quad(integrand_dz, 0, z, args=(gamma,))
    return (1 + z) * integral * unit_scale

# Test output
if __name__ == "__main__":
    zs = np.linspace(0.01, 2.0, 50)
    for z in zs:
        t = t_of_z(z)
        H = H_of_z(z)
        S = entropy_of_z(z)
        dL = luminosity_distance(z)
        print(f"z = {z:.2f}, t = {t:.3f}, H = {H:.3f}, S = {S:.3f}, dL = {dL:.2f} Mpc")
