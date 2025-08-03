# Initial Conditions

Waveframe 3.0 defines initial conditions not by tuning scalar fields or invoking inflation, but by anchoring cosmological time to entropy itself.

## Anchor Point

We set:
- `t₀ = 0`: The beginning of cosmological time
- `H(t₀) = H₀`: Normalized to 1 in natural units

This serves as the origin point for all entropic evolution.

## Normalization

We work in natural units:
- `k_B = ℓ_P = 1`
- `H(t₀) = 1`
- `a(t₀) = 1` (by convention)

All quantities evolve forward from this point using differential laws.

## Integration Driver

From the modified expansion law derived via entropy:

```math
\frac{dS}{dt} = \gamma \Rightarrow \dot{H} = -\frac{\gamma H^3}{2\pi}
```

We integrate forward in time using:
- A small timestep `dt`
- Dynamical update of `H(t)`
- Entropy evolution: `S(t) = \pi / H(t)^2`

## Justification

Traditional cosmology often treats initial conditions as arbitrary constants of integration or as outputs of high-energy inflationary physics. In contrast, Waveframe sets its anchor at the point of minimum entropy — a thermodynamic origin rather than a quantum fluctuation.

This makes the model cleaner, falsifiable, and directly tied to observable expansion rates.

## Summary

Initial conditions are:
- Anchored at `t = 0`, with `H₀ = 1`
- Driven forward by an entropy law rather than scalar potentials
- Designed for seamless integration into observable quantities like `H(z)` and `μ(z)`
