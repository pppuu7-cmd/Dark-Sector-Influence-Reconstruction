# Experiment 054C — prospective C7 IDM–DR common source-response slope test v0.1

Date: 2026-08-26
Status: PREREGISTERED BEFORE FIRST C7 P(k,z) OUTPUT
Gate relevance: prospective G7 evidence; G8 remains separate

## Purpose

Test one **common quantitative relation** on a mechanism that did not contribute any response output to its calibration.

Calibration was frozen in Exp054A using only C3 GDM dynamic shear and C5 designer f(R). Exp054B then selected the C7 coupling grid using only the pinned CLASS IDM–DR source equations; its workflow explicitly generated no C7 response products.

No C7 result may be used to alter the relation, coupling grid, source-scale definition, response domain or acceptance interval below.

## Pinned upstream and family

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`

C7 uses ETHOS interacting dark matter + dark radiation:

- `h=0.67`, `omega_b=0.0224`;
- `omega_idm=0.1200`, `omega_cdm=0`;
- `N_ur=3.046`, `N_idr=0.2`;
- `nindex_idm_dr=4`;
- `idr_nature=free_streaming`;
- scalar adiabatic synchronous-gauge linear perturbations;
- matched reference: **identical IDM+IDR background** with `a_idm_dr=0`.

Thus the response isolates the effect of IDM–DR coupling within this family instead of comparing different radiation backgrounds.

## Frozen C7 coupling grid

Copied exactly from the clean Exp054B source-only selector:

\[
a_{idm-dr}=\{
4.3913804613585236\times10^{10},
8.200519300792964\times10^{10},
2.0036633134204977\times10^{11},
6.341353932327471\times10^{11},
1.3815586723671924\times10^{12}
\}\ {\rm Mpc}^{-1}.
\]

The associated mechanism-native source scales are frozen as

\[
k_*=\{
0.08484582985947185,
0.07347864406347489,
0.05999506164903260,
0.04647197492427811,
0.03927598733289058
\}\ h/{\rm Mpc}.
\]

## Frozen response domain

Use the standard DSIR low-k nodes

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\ h/{\rm Mpc}
\]

at

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\}.
\]

For each coupling,

\[
R(z,k)=\ln\frac{P_{IDM-DR}(k,z)}{P_{matched\ uncoupled}(k,z)}.
\]

Define full response-power localization

\[
q_k^R(k)=\frac{\sum_zR(z,k)^2}{\sum_{z,k}R(z,k)^2},
\qquad
k_R^{geo}=\exp\left[\sum_kq_k^R(k)\ln k\right].
\]

This is deliberately the same full-response operator used in Exp054A. It does not rely on the interaction residual `I`.

## Frozen quantitative prediction

For every adjacent coupling pair in the order above,

\[
\mathcal C_i=
\frac{\Delta\ln k_R^{geo}}
{\Delta\ln k_*}.
\]

Exp054A mechanically froze the prospective interval before C7 existed:

\[
\boxed{
0.0022992620786061375
\le \mathcal C_i \le
0.09951219222831723
}
\]

for **all four** adjacent C7 slopes.

### Hard science verdict

- `PASS_PROSPECTIVE_C7_COMMON_SLOPE_V0_1` iff every eligible adjacent `C_i` lies inside the frozen interval and all source/operator controls pass.
- `FAIL_PROSPECTIVE_C7_COMMON_SLOPE_V0_1` if at least one finite eligible `C_i` lies outside it.
- No widening, recentring, reordering or dropping of C7 points is allowed after outputs.

## Frozen source controls

The science workflow must independently reconstruct the IDM drag crossing from CLASS's own background and thermodynamics output:

\[
\Gamma_{idm\leftarrow idr}=
\dot\mu_{idm-dr}\frac43\frac{\rho_{idr}}{\rho_{idm}},
\qquad
\Gamma_{idm\leftarrow idr}(z_*)=\mathcal H(z_*),
\]

with

\[
k_*^{solver}=\mathcal H(z_*)/h.
\]

For every C7 point require

\[
\left|k_*^{solver}/k_*^{frozen}-1\right|\le2\times10^{-3}.
\]

The `2e-3` tolerance is frozen now, before any C7 spectrum, to cover output-grid interpolation while remaining much tighter than the spacing of adjacent source nodes.

## Frozen numerical/operator controls

- exactly seven explicit P(k,z) files for reference and every model;
- every frozen k lies inside the common interpolation domain;
- all response values finite;
- response L2 norm `>1e-4` for every C7 point, inherited from the existing C6 withheld-family control so that centroid ratios are not defined on a numerical null;
- `q_k` normalization residual `<=1e-12`;
- no failed CLASS model;
- source reconstruction must find exactly one relevant drag/H crossing for each selected model.

## Interpretation boundary

A PASS would be the first genuinely prospective new-family survival of a single common quantitative source→response localization relation calibrated before the family response existed. It would justify promoting G7 evidence materially, but it would **not by itself establish a universal dark-sector law**, fundamental field count, survey detectability, no-hair theorem or G8 discovery. A FAIL must be retained as a negative test of the candidate relation with no recalibration.
