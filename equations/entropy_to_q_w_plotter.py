import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Load H(z) data from entropic model
z = np.linspace(0, 3, 300)
H = 1 / np.log(1 + z + 1e-8)  # Avoid division by zero at z=0

# Numerical derivative dH/dz
dH_dz = np.gradient(H, z)

# Compute deceleration parameter q(z)
q = -1 - (1 + z) * dH_dz / H

# Compute effective equation of state w_eff(z)
w_eff = -1 + (2 / 3) * (1 + z) * dH_dz / H

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

ax1.plot(z, q, label="q(z)", color="tab:blue")
ax1.axhline(0, color='gray', linestyle='--', lw=0.5)
ax1.set_ylabel("Deceleration q(z)")
ax1.set_title("Entropy-Driven Cosmology: q(z) and w_eff(z)")
ax1.legend()
ax1.grid(True)

ax2.plot(z, w_eff, label="w_eff(z)", color="tab:red")
ax2.axhline(-1, color='gray', linestyle='--', lw=0.5)
ax2.set_ylabel("w_eff(z)")
ax2.set_xlabel("Redshift z")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig("entropy_to_q_w_plotter.png", dpi=300)
plt.show()
