
import numpy as np
from scipy.integrate import quad

# Constants
c = 299792.458  # speed of light in km/s

def H_z(z, gamma=1.0, t0=0.0):
    # Entropic model: H(z) = sqrt(pi / gamma) * (1 / sqrt(t(z) - t0))
    # This requires a z -> t conversion; assume approximation or precomputed t(z)
    # For this implementation, we'll use an inverse mapping based on a(t)
    return np.sqrt(np.pi / gamma) * (1 / np.sqrt(t_of_z(z) - t0))

def t_of_z(z, gamma=1.0):
    # Approximate inverse of a(t) = exp[2 sqrt(pi/gamma) sqrt(t - t0)]
    # Solve for t(z): ln(a) = 2 sqrt(pi/gamma) sqrt(t) => t = (ln(1/(1+z)) / (2 sqrt(pi/gamma)))^2
    return (np.log(1 / (1 + z)) / (2 * np.sqrt(np.pi / gamma)))**2

def luminosity_distance(z, gamma=1.0):
    integrand = lambda z_prime: 1.0 / H_z(z_prime, gamma)
    integral, _ = quad(integrand, 0, z)
    dL = (1 + z) * c * integral  # in km/s * 1/H(z) units
    return dL  # returns distance in Mpc assuming H in km/s/Mpc

def distance_modulus(z, gamma=1.0):
    dL = luminosity_distance(z, gamma)
    mu = 5 * np.log10(dL) + 25
    return mu

# Example usage:
if __name__ == "__main__":
    zs = np.linspace(0.01, 2.0, 100)
    mus = [distance_modulus(z, gamma=0.1) for z in zs]

    for z, mu_val in zip(zs, mus):
        print(f"z = {z:.2f}, mu(z) = {mu_val:.2f}")
