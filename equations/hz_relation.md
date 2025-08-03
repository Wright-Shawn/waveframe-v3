# Hubble Parameter as a Function of Redshift \( H(z) \)

To compare the Waveframe 3.0 model against observations, we need to express the Hubble parameter \( H \) as a function of redshift \( z \), not cosmic time \( t \).

---

## Step 1: Invert the Scale Factor

From the entropic scale factor:

\[
a(t) = a_0 \cdot \exp\left[ 2 \sqrt{rac{\pi}{\gamma}} \cdot \sqrt{t - t_0} ight]
\]

Take the natural logarithm:

\[
\ln \left( rac{a(t)}{a_0} ight) = 2 \sqrt{rac{\pi}{\gamma}} \cdot \sqrt{t - t_0}
\]

Solving for time:

\[
t(a) = t_0 + \left( rac{\gamma}{\pi} ight) \cdot rac{1}{4} \cdot \left[ \ln \left( rac{a(t)}{a_0} ight) ight]^2
\]

Since redshift is defined as:

\[
1 + z = rac{a_0}{a(t)}
\Rightarrow
a(t) = rac{a_0}{1 + z}
\]

Substitute and get:

\[
t(z) = t_0 + \left( rac{\gamma}{\pi} ight) \cdot rac{1}{4} \cdot \left[ \ln (1 + z) ight]^2
\]

---

## Step 2: Substitute into \( H(t) \)

From the expansion law:

\[
H(t) = \left( rac{\pi}{\gamma (t - t_0)} ight)^{1/2}
\]

Substitute \( t(z) \):

\[
H(z) = \left( rac{\pi}{\gamma \cdot \left( rac{\gamma}{\pi} \cdot rac{1}{4} \cdot [\ln(1 + z)]^2 ight)} ight)^{1/2}
\]

Simplify:

\[
H(z) = rac{2}{\ln(1 + z)}
\]

---

## Final Result

\[
H(z) = rac{2}{\ln(1 + z)}
\]

This is a direct, falsifiable prediction of the entropic expansion model. It behaves differently from ΛCDM, especially at low redshift where logarithmic terms dominate.

---

## Notes

- This result assumes \( a_0 = 1 \) and natural units
- Divergence at \( z = 0 \) is avoided by regularization or normalization to match \( H(z = 0) = 1 \)
- This relation will be tested directly against SN Ia, BAO, and RSD datasets
