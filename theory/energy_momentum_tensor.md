
# Energy-Momentum Tensor Derivation

## Starting Point: Lagrangian Density

We begin from the entropic field Lagrangian:

\[
\mathcal{L}(S, \partial_\mu S) = -rac{1}{2} \partial_\mu S \partial^\mu S - V(S)
\]

Here:
- \( S \) is the entropy field
- \( V(S) \) is a potential function that may encode saturation, phase transitions, or other nonlinearities

---

## Step 1: Define the Energy-Momentum Tensor

The energy-momentum tensor is defined as:

\[
T_{\mu
u} = rac{\partial \mathcal{L}}{\partial (\partial^\mu S)} \partial_
u S - g_{\mu
u} \mathcal{L}
\]

---

## Step 2: Compute Each Term

First term:

\[
rac{\partial \mathcal{L}}{\partial (\partial^\mu S)} = -\partial_\mu S
\]

So:

\[
T_{\mu
u} = -\partial_\mu S \partial_
u S + g_{\mu
u} \left( rac{1}{2} \partial_lpha S \partial^lpha S + V(S) ight)
\]

---

## Step 3: Interpretation

In a Friedmann–Lemaître–Robertson–Walker (FLRW) metric, this tensor yields an effective fluid with:

- Energy density:
\[
ho_S = rac{1}{2} \dot{S}^2 + V(S)
\]

- Pressure:
\[
p_S = rac{1}{2} \dot{S}^2 - V(S)
\]

This means entropy dynamics behave like a scalar field with kinetic and potential terms, contributing to cosmic acceleration or deceleration.

---

## Optional Generalization

In the presence of spatial gradients:

\[
ho_S = rac{1}{2} (\partial_t S)^2 + rac{1}{2} (
abla S)^2 + V(S)
\]
\[
p_S = rac{1}{2} (\partial_t S)^2 - rac{1}{6} (
abla S)^2 - V(S)
\]

These forms allow the entropy field to contribute anisotropic pressure or spatially varying energy density.

