"""
chi_squared_fitter.py

Fits model parameters (e.g., gamma, H0, alpha) to observational data using chi-squared minimization.
Recommended for use with Pantheon+ or similar SN Ia datasets.
"""

import numpy as np
from scipy.optimize import minimize
from luminosity_distance_solver import compute_mu_model  # Assumes existing function for mu(z)

def chi_squared(params, z_data, mu_obs, mu_err):
    gamma, H0, alpha = params
    mu_model = compute_mu_model(z_data, gamma=gamma, H0=H0, alpha=alpha)
    chi2 = np.sum(((mu_obs - mu_model) / mu_err) ** 2)
    return chi2

def fit_parameters(z_data, mu_obs, mu_err, initial_guess=(1e-5, 70, 1.0)):
    result = minimize(chi_squared, initial_guess, args=(z_data, mu_obs, mu_err))
    return result.x, result.fun
