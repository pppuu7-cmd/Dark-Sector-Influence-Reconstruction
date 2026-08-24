# Experiment 031 — first block-aware cross-family model comparison

Date: 2026-08-24
Status: **COMPLETE — NO DISCOVERY CLAIM**
Prerequisite: Experiment 030 comparison-readiness PASS.

## Scope

This is the first actual DSIR comparison of different dark-sector mechanisms in a common response space. It is deliberately limited to the validated raw theory-response geometry on the frozen low-k linear-structure block.

It is **not** yet an observational likelihood ranking. It does not apply survey covariance/kernel whitening, and it makes no discovery claim.

## Objects compared

- C1 smooth non-phantom dark energy: one-sided `epsilon_w=1+w` response ray;
- C2 interacting vacuum: physical negative-alpha cone ray and two-sided beta tangent line;
- C3 generalized dark matter: local positive sound-speed and viscosity rays;
- C5 designer f(R): minimum resolved production ray at `B0=1e-6` after exact-zero subtraction.

C0 LambdaCDM is the common response origin. C4 thermal WDM remains in the separately validated small-scale transfer block and is not imputed into the low-k matrix.

## Comparison decomposition

For each response surface `R(z,k)` compute

\[
R=U\Sigma V^T.
\]

The leading separable approximation is

\[
R(z,k)\simeq\sigma_1A_1(z)S_1(k),
\]

with rank-1 variance fraction

\[
f_1=\frac{\sigma_1^2}{\sum_i\sigma_i^2}
\]

and relative residual

\[
\epsilon_{sep}=\sqrt{1-f_1}.
\]

This is a response-shape diagnostic, not a microscopic degree-of-freedom count.

## Hard computation result

GitHub Actions run `32772758097` completed successfully at commit `5a0893abef9f492677df01399a6339c10257c158`.

Machine status:

`FIRST_BLOCK_AWARE_MODEL_COMPARISON_COMPLETE_NO_DISCOVERY_CLAIM`.

### Individual separability

- C1 smooth wDE: `f1=0.999861`, residual `0.01180`;
- C2 IDE alpha: `f1=0.998156`, residual `0.04294`;
- C2 IDE beta: `f1=0.922353`, residual `0.27865`;
- C3 GDM cs2: `f1=0.9999999984`, residual `4.03e-5`;
- C3 GDM cv2: `f1=0.9999999980`, residual `4.43e-5`;
- C5 designer f(R): `f1=0.999999879`, residual `3.48e-4`.

IDE-beta is therefore the least separable `A(z)S(k)` response among the sampled directions.

### Full 35-cell response geometry

Important orientation-aware angles include:

- GDM cs2 vs cv2: `0.3226 deg` — strong internal degeneracy;
- IDE negative-alpha vs GDM cs2: `24.9345 deg`;
- IDE negative-alpha vs GDM cv2: `24.7864 deg`;
- smooth wDE vs GDM cs2: `59.8042 deg`;
- smooth wDE vs IDE beta: `80.5209 deg`;
- GDM cs2 vs designer f(R): oriented ray angle `154.8182 deg`;
- GDM cv2 vs designer f(R): oriented ray angle `154.5119 deg`.

The large oriented GDM/f(R) angle mainly reflects opposite physical sign: GDM pressure/viscosity suppresses clustering whereas designer f(R) enhances it in this control direction.

### Scale/time-mode decomposition

The most striking result is the leading scale-shape cluster:

\[
\theta_S(c_s^2,c_v^2)=0.02436^\circ,
\]

\[
\theta_S(c_s^2,f(R))=0.07813^\circ,
\]

\[
\theta_S(c_v^2,f(R))=0.10169^\circ.
\]

Thus GDM pressure, GDM viscosity and designer f(R) have nearly the same leading **scale mode** over the current five low-k nodes.

They differ much more in time/sign. For GDM cs2 vs f(R), the unoriented leading time-mode angle is `25.1817 deg`; for GDM cv2 vs f(R), `25.4879 deg`.

Smooth wDE is much flatter in scale:

\[
\theta_S(wDE,GDM\ cs2)=59.4167^\circ.
\]

## Main findings

1. **GDM internal degeneracy:** `cs2` and `cv2` are almost the same low-k matter-power direction and need another channel.
2. **Shared scale-shape cluster:** GDM cs2, GDM cv2 and designer f(R) have nearly identical leading scale shapes despite different dynamics and signs.
3. **Time leverage matters:** the GDM/f(R) similarity is largely broken by temporal evolution/sign rather than scale shape alone.
4. **Smooth wDE differs mainly by scale-shape:** it is much flatter in k.
5. **IDE beta is intrinsically less separable:** a single `A(z)S(k)` product is a poor approximation compared with the other controls.

## Interpretation rule

A small theory-space angle is **not** by itself observational degeneracy. Data-space distinguishability must later be evaluated after applying response kernels and covariance whitening.

Conversely, a large raw-theory angle is not a Bayes factor or exclusion significance.

Artifact digest: `sha256:aa8e7cf99e922107a42e4ab09be014a7fed57d95baf96a5b3f99652fc51b3a0c`.

The output of Experiment 031 feeds the discriminant graph and later data-whitened comparison; it is not a final ranking of cosmological models.
