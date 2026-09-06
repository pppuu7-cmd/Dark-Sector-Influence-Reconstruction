# DSIR-4 analytic residual mappings — C0 LambdaCDM and C1 smooth-w v0.1

Frozen: 2026-09-07 under `DSIR4_COMMON_RESIDUAL_CONVENTION_V0_1`.

## C0 — LambdaCDM/GR reference

With the shared ordinary sector in `T_known`, the residual source is

\[
X^{C0}_{\mu\nu}=T^{cdm}_{\mu\nu}+T^{\Lambda}_{\mu\nu}.
\]

For pressureless CDM and a cosmological constant:

\[
\rho_X=\rho_c+\rho_\Lambda,\qquad p_X=-\rho_\Lambda,
\]
\[
\delta\rho_X=\delta\rho_c,\qquad q_X=q_c,
\]
\[
\delta p_X=0,\qquad \pi_X=0.
\]

The cosmological constant has no scalar perturbations. CDM has zero isotropic pressure perturbation and zero intrinsic scalar anisotropic stress. The velocity/momentum variable must be transformed to the frozen DSIR comoving response convention when producing observable predictions.

This mapping is valid throughout the frozen DSIR-4 v0.1 linear domain. It is the model mapping, not a claim that the LambdaCDM hypothesis passes the later observational gates.

## C1 — smooth non-phantom constant-w control

The frozen legacy pilot object is the local ray with

\[
\epsilon_w=1+w=10^{-4},\qquad w=-0.9999.
\]

The control is explicitly the **smooth-w** branch used by the legacy comparison: dark-energy perturbations are absent by control definition. The residual source is

\[
X^{C1}_{\mu\nu}=T^{cdm}_{\mu\nu}+T^{w,\,smooth}_{\mu\nu}.
\]

The background obeys

\[
\rho_w(a)=\rho_{w0}a^{-3(1+w)},\qquad p_w=w\rho_w.
\]

Therefore

\[
\rho_X=\rho_c+\rho_w,\qquad p_X=w\rho_w,
\]
\[
\delta\rho_X=\delta\rho_c,\qquad q_X=q_c,
\]
\[
\delta p_X=0,\qquad \pi_X=0
\]

for this deliberately smooth control branch. These zero perturbations are `STRUCTURAL_ZERO` **for the frozen smooth-control hypothesis**, not a statement about general physical quintessence or arbitrary wCDM perturbations.

The mapping is valid on the frozen DSIR-4 v0.1 linear comparison domain for this phenomenological control definition. A physical clustered dark-energy realization is a different hypothesis and requires its own mapping artifact.

## Non-equivalence warning

C0 and C1 coincide only in the limit `epsilon_w -> 0`. The finite C1 point `epsilon_w=1e-4` remains a distinct frozen hypothesis even if current observables have weak sensitivity to it.
