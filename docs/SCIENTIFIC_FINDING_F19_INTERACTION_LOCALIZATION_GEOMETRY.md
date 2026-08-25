# F19 — interaction-energy localization separates mechanisms along different axes

**Status:** HARD ESTABLISHED descriptive localization geometry on the frozen local C1/C2/C3/C5 low-k response directions (Exp048A); broader mechanism interpretation SUPPORTED only.

## Definitions

For the orthogonal interaction residual

\[
R(z,k)=\mu+T(k)+\tau(z)+I(z,k),
\]

define normalized squared-energy marginals

\[
\boxed{q_k(k)=\frac{\sum_z I(z,k)^2}{\|I\|^2}},
\qquad
\boxed{q_z(z)=\frac{\sum_k I(z,k)^2}{\|I\|^2}}.
\]

They satisfy

\[
\sum_kq_k=\sum_zq_z=1.
\]

Also define

\[
k_I^{geo}=\exp\left(\sum_kq_k\ln k\right),
\qquad
z_I=\sum_zq_zz.
\]

`q_k` and `q_z` locate the **energy of scale-time nonseparability**. They intentionally discard the sign of `I` and therefore complement rather than replace the signed interaction morphology of Exp046.

## Provenance

- run `32900967558`;
- source science head `879148df48087fe72ef4a360c9bca3b5e2766458`;
- artifact `9583033485`;
- artifact SHA256 `32455f976daa3c3821d80e4db595ab333cdb7d5cb74d92ab28865cbd81fe41f8`.

Operator controls pass:

- reconstruction error `0`;
- max normalized core/I orthogonality `2.5664e-15`;
- max scaled zero-mean residual `4.2198e-21`;
- max `q_k/q_z` normalization residual `1.0842e-19`;
- required ceiling `1e-12`.

No scientific similarity/separation threshold was frozen because the central GDM/f(R) localization pattern was inspected before the formal protocol. The numbers below are therefore **hard descriptive geometry**, not a preregistered classification PASS.

## Hard localization coordinates

| direction | `chi_I` | `k_I^geo [h/Mpc]` | `z_I` | peak interaction-energy cell `(z,k)` |
|---|---:|---:|---:|---|
| smooth-w | `0.0010805` | `0.0021645` | `0.97608` | `(0.295,0.001)` |
| GDM cs2 | `0.0453054` | `0.0509960` | `1.21890` | `(2.33,0.1)` |
| GDM cv2 | `0.0436337` | `0.0509697` | `1.23468` | `(2.33,0.1)` |
| designer f(R) | `0.299856` | `0.0510862` | `0.98436` | `(0.295,0.1)` |

IDE alpha/beta remain below the pre-existing `chi_I=1e-6` morphology floor and therefore have no normalized localization profile; they are missing/invalid for this operator, not zero.

## GDM versus designer f(R): scale-localization degeneracy, time-localization separation

For GDM cs2 versus f(R):

- `q_k` angle: **`0.040233 deg`**;
- `q_k` Hellinger: **`0.001111`**;
- `q_z` angle: **`20.14885 deg`**;
- `q_z` Hellinger: **`0.13355`**.

For GDM cv2 versus f(R):

- `q_k` angle: **`0.051465 deg`**;
- `q_k` Hellinger: **`0.001419`**;
- `q_z` angle: **`21.52113 deg`**;
- `q_z` Hellinger: **`0.14064`**.

Their geometric k centroids differ by only about `0.2%`, while redshift centroids differ by `0.235-0.250`.

**Hard descriptive interpretation:** the GDM and f(R) interaction residuals place almost the same fraction of their nonseparable power at each sampled scale, yet distribute that power very differently over cosmic time. This sharpens the older DSIR result that GDM and f(R) are scale-only lookalikes but temporally/full-structure separated.

The peak cell makes the contrast especially clear:

- GDM cs2/cv2 peak at **high redshift** `z=2.33`, `k=0.1`;
- designer f(R) peaks at **low redshift** `z=0.295`, `k=0.1`.

## Smooth-w versus designer f(R): complementary localization degeneracy

A second, nearly orthogonal pattern appears:

smooth-w versus f(R):

- `q_k` angle: **`79.3665 deg`**;
- `q_k` Hellinger: **`0.64069`**;
- `q_z` angle: **`1.92674 deg`**;
- `q_z` Hellinger: **`0.02432`**;
- redshift centroids differ by only `0.00828`.

Thus smooth-w and f(R) localize their interaction energy at nearly the same epochs but at radically different scales:

- smooth-w is dominated by `k=0.001` (`q_k~0.775`);
- f(R) is dominated by `k=0.1` (`q_k~0.794`).

This is complementary to the GDM/f(R) case.

## GDM pressure versus viscosity

GDM cs2/cv2 localization is almost identical:

- `q_k` angle `0.01128 deg`;
- `q_z` angle `1.38206 deg`;
- `k_I^geo` differs by only `~5e-4` fractionally;
- both peak at `(z=2.33,k=0.1)`.

This is consistent with their density and interaction-morphology degeneracy. Localization geometry does **not** replace metric slip as the demonstrated cs2/cv2 microphysical discriminator.

## New structural interpretation

The current four valid directions approximately occupy different corners in a two-axis localization picture:

- **smooth-w:** low-k / low-z interaction localization;
- **designer f(R):** high-k / low-z;
- **GDM:** high-k / higher-z;
- **IDE:** interaction near-null on this block.

This is more informative than one scalar `chi_I`: mechanisms can share one localization marginal while differ strongly in the other.

A useful response fingerprint therefore needs at least both **where in scale** and **where in time** nonseparability is localized, plus signed morphology and independent channels such as slip.

## Boundary

- This is response-energy localization, not a causal theorem about the microscopic mechanism.
- Squaring `I` removes sign/orientation information.
- The current low-k nodes and equal theory-space weighting are not a survey window.
- Smooth-w is known from Exp047B to be sensitive to the lowest-k node, so its scale-localization result requires domain stress testing before being called a family invariant.
- C4 WDM is absent, not zero.
- No universal mechanism law, intrinsic rank, survey detectability, G7 law or G8 discovery follows.

## Next tests

1. Exp048B: finite-amplitude flow of `q_k`, `q_z`, `k_I^geo`, `z_I` for GDM cv2 and designer f(R), using immutable manifold artifacts.
2. Leave-one-node localization stress test, especially smooth-w's `k=0.001` dependence.
3. Test whether decreasing `chi_I` at large GDM-cv2/f(R) amplitude correlates with movement of `k_I^geo` through the finite window.
4. Extend C4 WDM to a high-k time-dependent atlas before family-complete localization claims.
