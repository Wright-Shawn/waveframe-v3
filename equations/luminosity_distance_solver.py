import numpy as np
from scipy.integrate import quad

# Constants
c = 299792.458  # Speed of light in km/s
H0 = 70.0       # Hubble constant in km/s/Mpc

# Optional curvature parameter (currently unused, for future extensions)
Omega_k = 0

# Hubble parameter H(z) for entropy-driven cosmology
def H_entropy(z, gamma=1.0, t0=0.0):
    """Entropy-based H(z) model. Valid only for the derived Hubble function."""
    # This model: H(z) = H0 * (1 + z) / ln(1 + z)
    ln_term = np.log(1 + z)
    return H0 * (1 + z) / ln_term if ln_term != 0 else H0

# Comoving distance integrand
def integrand(z, gamma):
    return 1.0 / H_entropy(z, gamma)

# Compute luminosity distance in Mpc
def luminosity_distance(z, gamma=1.0):
    integral, _ = quad(integrand, 0, z, args=(gamma,))
    dL = (1 + z) * c * integral / H0  # Convert to Mpc using H0
    return dL

# Compute distance modulus μ(z)
def distance_modulus(z, gamma=1.0):
    dL = luminosity_distance(z, gamma)
    return 5 * np.log10(dL) + 25

# Example usage:
if __name__ == "__main__":
    z_vals = np.linspace(0.01, 2.0, 50)
    mu_vals = [distance_modulus(z, gamma=1.25) for z in z_vals]

    for z, mu in zip(z_vals, mu_vals):
        print(f"z = {z:.2f}, μ(z) = {mu:.2f}")
