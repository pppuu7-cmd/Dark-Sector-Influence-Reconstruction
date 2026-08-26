# Experiment 054C — prospective C7 IDM–DR common source-response slope v0.1

Date: 2026-08-26
Status: **PREREGISTERED BEFORE FIRST C7 RESPONSE OUTPUT**
Gate relevance: prospective quantitative G7/G8 test

## Scientific question

Does a genuinely new transition-scale mechanism, C7 interacting dark matter–dark radiation (IDM–DR / ETHOS), obey the already calibrated C3+C5 relation

\[
\mathcal C_i=\frac{\Delta\ln k_R^{geo}}{\Delta\ln k_*}>0
\]

within the acceptance band frozen by Exp054A **before any C7 matter-power response existed**?

This experiment is the first allowed C7 response calculation. Exp054A fixed the common operator and band from C3 GDM dynamic shear and C5 designer f(R). Exp054B then selected the C7 coupling grid from CLASS source equations only and explicitly generated no C7 response products.

No part of the definition below may be changed after the first C7 `P(k,z)` output is generated. A FAIL is a scientific result and must not trigger recalibration.

## Frozen upstream and mechanism

Pinned solver:

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`

Frozen common cosmology and primordial settings:

- `h = 0.67`;
- `T_cmb = 2.7255 K`;
- `omega_b = 0.0224`;
- `omega_idm = 0.1200`, `omega_cdm = 0`;
- flat background (`Omega_k=0`, Lambda inferred by CLASS);
- `N_ur = 3.046`;
- `N_idr = 0.2`;
- `stat_f_idr = 0.875`;
- `A_s = 2.10e-9`, `n_s = 0.965`, `alpha_s = 0`;
- scalar adiabatic initial conditions, synchronous gauge;
- linear `mPk` only.

Frozen IDM–DR perturbation implementation:

- ETHOS `a_idm_dr` parametrization;
- `nindex_idm_dr = 4`;
- `idr_nature = free_streaming` (the pinned CLASS ETHOS default, made explicit here before response generation);
- `b_idr = 0`;
- `alpha_idm_dr = 1.5` and `beta_idr = 1.5` (pinned CLASS defaults, made explicit here before response generation).

The matched reference has the **identical IDM+IDR background and all identical numerical/primordial settings**, but `a_idm_dr = 0`.

## Frozen source definition and C7 grid

Pinned CLASS defines the IDM drag magnitude

\[
\Gamma_{idm\leftarrow idr}(z)
=\frac43\,\omega_{idr}\,a_{idm-dr}(1+z)
\left(\frac{1+z}{10^7}\right)^4.
\]

The source-native epoch and scale remain those frozen in Exp054B,

\[
\Gamma_{idm\leftarrow idr}(z_*)=\mathcal H(z_*),
\qquad
k_* = \mathcal H(z_*)/h.
\]

The five source targets, in the frozen response-run order, are

\[
k_* = [
0.08484582985947185,
0.07347864406347489,
0.05999506164903260,
0.04647197492427811,
0.03927598733289058
]\;h/{\rm Mpc}.
\]

Exp054B source-only inversion fixed the corresponding `a_idm_dr` values (1/Mpc):

\[
[
4.3913804613585236\times10^{10},
8.200519300792964\times10^{10},
2.0036633134204977\times10^{11},
6.341353932327471\times10^{11},
1.3815586723671924\times10^{12}
].
\]

The recovered source-target relative error was `<1.5e-15`. These values cannot be replaced by a response-selected grid.

## Frozen response domain

Use the standard DSIR low-k comparison grid, with no extra C7-selected nodes:

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\;h/{\rm Mpc}.
\]

For each CLASS output, interpolate `ln P` linearly in `ln k` onto these five k nodes. Reference and model are same-solver outputs from the same run contract.

Define the full response

\[
R(z,k)=\ln\frac{P_{C7}(k,z)}{P_{ref}(k,z)}.
\]

No additive `G+T+tau+I` decomposition is used in this gate.

## Frozen common response-scale operator

For each coupling point,

\[
q_k^R(k)=\frac{\sum_zR(z,k)^2}{\sum_{z,k}R(z,k)^2},
\qquad
k_R^{geo}=\exp\left(\sum_k q_k^R(k)\ln k\right).
\]

The response power must be finite and strictly non-zero. The five `k_R^{geo}` values are then ordered exactly as the frozen five source nodes above.

For every adjacent pair,

\[
\boxed{\mathcal C_i=
\frac{\ln(k_{R,i+1}^{geo}/k_{R,i}^{geo})}
{\ln(k_{*,i+1}/k_{*,i})}}.
\]

## Pre-frozen quantitative gate

Exp054A mechanically froze, from C3+C5 only,

\[
\boxed{
0.0022992620786061375
\le \mathcal C_i \le
0.09951219222831723
}
\]

for **every** adjacent C7 slope.

`PASS_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1` requires all of the following:

1. exactly the pinned solver commit and the five frozen coupling/source-scale pairs are used;
2. exactly seven frozen redshifts and five frozen low-k nodes are analyzed;
3. all response values and all `k_R^{geo}` are finite and response power is non-zero;
4. all four adjacent `C_i` are finite;
5. every `C_i` lies inside the already frozen Exp054A band, inclusive.

Any violation gives `FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1`. No band widening, coupling reselection, node deletion, sign flip, alternative centroid, or post-output recalibration is permitted for v0.1.

## Interpretation boundary fixed before output

A PASS would be the first prospective validation of the same quantitative source-response relation on a new C7 mechanism that contributed no response information to calibration or parameter selection. It would materially upgrade G7 and provide the fresh withheld-mechanism test required for G8, subject to the repository's gate wording and provenance checks.

A FAIL would falsify this proposed common quantitative law at C7 v0.1 while leaving the broader DSIR characteristic-scale/epoch organizing idea and earlier mechanism-specific findings intact.

Neither outcome by itself implies a fundamental action, intrinsic field count, no-hair theorem, observational detectability, or a universal dark-sector model.
