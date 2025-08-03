"""
unit_normalization_config.py

Centralized config for physical constants and unit scaling.
Used to ensure consistent conversions between natural and SI units.
"""

# Physical constants
c_km_s = 299792.458  # speed of light in km/s
H0_default = 70.0    # Hubble constant in km/s/Mpc
Mpc_to_km = 3.085677581e19  # 1 Mpc in km

# Derived unit scale
# This defines the unit conversion scale used to convert natural units to Mpc
unit_scale_Mpc = c_km_s / H0_default  # Used to rescale dimensionless distances into Mpc

# Usage:
# d_L_Mpc = d_L_code_units * unit_scale_Mpc
