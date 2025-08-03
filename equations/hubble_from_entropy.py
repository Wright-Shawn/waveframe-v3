import numpy as np

def Hubble_entropy(t, gamma, t0=0, Omega_k=0, H0=70, c=299792.458):
    """
    Computes H(t) from the entropy-based expansion law:
        H(t) = sqrt(pi / (gamma * (t - t0)))

    Parameters:
    - t : array-like, time values
    - gamma : float, entropy growth rate
    - t0 : float, initial time (default = 0)
    - Omega_k : float, curvature parameter (default = 0, flat)
    - H0 : float, Hubble constant in km/s/Mpc (default = 70)
    - c : float, speed of light in km/s (default = 299792.458)

    Returns:
    - H : array, Hubble parameter values in 1/time units
    - H_scaled : array, Hubble parameter in km/s/Mpc for comparison
    """
    t = np.array(t)
    H = np.sqrt(np.pi / (gamma * (t - t0)))

    # Optional: convert to observable units using H0 scale
    unit_scale = c / H0  # Mpc per unit time
    H_scaled = H / unit_scale  # Now in km/s/Mpc

    if Omega_k != 0:
        print("Warning: Curvature handling not yet implemented in H(t).")

    return H, H_scaled
