# Scale Factor Derivation

From the entropy-driven expansion law, we derived the Hubble parameter as a function of time:

\[
H(t) = \left( \frac{\pi}{\gamma(t - t_0)} \right)^{1/2}
\]

Since:

\[
H(t) = \frac{\dot{a}}{a}
\]

we can separate variables:

\[
\frac{da}{a} = \left( \frac{\pi}{\gamma} \right)^{1/2} \cdot \frac{dt}{\sqrt{t - t_0}}
\]

---

## Integration

Integrate both sides:

\[
\int \frac{da}{a} = \left( \frac{\pi}{\gamma} \right)^{1/2} \int \frac{dt}{\sqrt{t - t_0}}
\]

This gives:

\[
\ln a(t) = 2 \left( \frac{\pi}{\gamma} \right)^{1/2} \cdot \sqrt{t - t_0} + C'
\]

Exponentiating both sides:

\[
a(t) = a_0 \cdot \exp\left[ 2 \left( \frac{\pi}{\gamma} \right)^{1/2} \cdot \sqrt{t - t_0} \right]
\]

---

## Result

The scale factor grows with a square-root exponential form:

\[
a(t) = a_0 \cdot \exp\left[ 2 \sqrt{\frac{\pi}{\gamma}} \cdot \sqrt{t - t_0} \right]
\]

Unlike power-law or de Sitter expansion, this represents a **thermodynamically driven growth**—neither purely inflationary nor purely matter-like. It’s a new class of cosmological evolution.

---

## Summary

- Driven by constant entropy flow: \( dS/dt = \gamma \)
- Scale factor grows sub-exponentially: \( a(t) \sim \exp[\sqrt{t}] \)
- No scalar field, no cosmological constant—just information flow

This becomes the backbone for deriving redshift and observational comparisons like \( H(z) \), \( \mu(z) \), and structure growth metrics.
