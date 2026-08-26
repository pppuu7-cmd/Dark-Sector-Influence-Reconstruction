# Experiment 056B — prospective C8 IDM–photon endpoint half-transition v0.1

Date: 2026-08-26
Status: **PREREGISTERED BEFORE FIRST C8 RESPONSE OUTPUT**
Gate relevance: prospective F28 / G7 / G8 test

## Scientific question

Does a genuinely fresh response mechanism, C8 interacting dark matter–photon scattering, obey the endpoint-normalized half-transition relation qualified retrospectively by Exp055A/F28,

\[
\mathcal C_{50,i}=\frac{\Delta\ln k_{50}^{geo}}{\Delta\ln k_{source}}>0,
\]

when the complete operator, parameter grid, response domain, robustness test and acceptance rule are frozen before the first C8 matter-power response is generated?

Exp055A used already-seen C3, C5 and C7 responses and therefore could only qualify this relation for future preregistration. Exp056A then selected the C8 coupling grid from pinned CLASS source equations only and explicitly generated no matter-power or perturbation response. No part of this v0.1 contract may be changed after the first C8 `P(k,z)` output. A FAIL is a scientific result and must not trigger recalibration.

## Frozen solver, cosmology and C8 mechanism

Pinned solver:

`lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`

Frozen settings:

- `h = 0.67`, `T_cmb = 2.7255 K`;
- `omega_b = 0.0224`, `omega_idm = 0.1200`, `omega_cdm = 0`;
- `m_idm = 1e9 eV`;
- flat background, `N_ur = 3.046`;
- `YHe = 0.2404`, `recombination = RECFAST`, `reio_parametrization = reio_none`;
- scalar adiabatic initial conditions, synchronous gauge;
- `A_s = 2.10e-9`, `n_s = 0.965`, `alpha_s = 0`;
- linear `mPk` only;
- IDM–photon index `n_index_idm_g = 0`.

The matched reference has all identical background, primordial, thermodynamic and numerical settings but `u_idm_g = 0`.

## Frozen source definition and source-only selected grid

For the pinned implementation, Exp056A froze

\[
\Gamma_{idm\leftarrow\gamma}=\frac{4}{3}\frac{\rho_\gamma}{\rho_{idm}}\,d\mu_{idm\gamma},
\qquad
\Gamma(z_*)=\mathcal H(z_*),
\qquad
k_{source}=\mathcal H(z_*)/h.
\]

The five target source scales are, in immutable response-run order,

\[
k_{source}=[0.08484582985947185,0.07347864406347489,0.05999506164903260,0.04647197492427811,0.03927598733289058]\ h/{\rm Mpc}.
\]

The corresponding source-only selected couplings are

\[
u_{idm\gamma}=[1.9784961959913951\times10^{-13},2.7180740724473660\times10^{-13},4.2866377403625277\times10^{-13},7.7340788471244140\times10^{-13},1.1546648138593298\times10^{-12}].
\]

Exp056A clean run `32922159744` passed the no-response contamination guard; its maximum reconstructed source-rate and source-scale relative errors were approximately `2.22e-16` and `1.78e-15`. The above grid cannot be retuned from C8 response output.

## Frozen response domain

Use exactly the standard DSIR low-k grid:

\[
z=\{0.295,0.51,0.706,0.934,1.317,1.491,2.33\},
\]

\[
k=\{0.001,0.003,0.01,0.03,0.1\}\ h/{\rm Mpc}.
\]

At each redshift interpolate `ln P` linearly in `ln k` onto these five nodes and define

\[
R(z,k)=\ln\frac{P_{C8}(k,z)}{P_{ref}(k,z)}.
\]

No response-selected nodes, smoothing, sign flip, additive decomposition or post-output parameter adjustment is allowed.

## Frozen F28 half-transition operator

For every model and redshift row, define the endpoint-affine normalized response

\[
u(z,k)=\frac{R(z,k)-R(z,k_{min})}{R(z,k_{max})-R(z,k_{min})}.
\]

The endpoint contrast must be finite and non-zero. The row must have **exactly one** crossing of `u=0.5` on the frozen five-node interval. The crossing is interpolated piecewise linearly in `ln k`, exactly as in Exp055A. Global row monotonicity is not required; uniqueness of the half-transition crossing is the validity condition.

For each coupling,

\[
k_{50}^{geo}=\exp\left[\frac{1}{7}\sum_z\ln k_{50}(z)\right].
\]

For each adjacent source-grid pair in the frozen order,

\[
\boxed{\mathcal C_{50,i}=\frac{\ln(k_{50,i+1}^{geo}/k_{50,i}^{geo})}{\ln(k_{source,i+1}/k_{source,i})}}.
\]

## Pre-frozen prospective gate

`PASS_IDM_PHOTON_ENDPOINT_HALF_TRANSITION_PROSPECTIVE_V0_1` requires all of the following:

1. the pinned CLASS commit and exactly the five Exp056A source-selected couplings/source scales are used in the frozen order;
2. exactly seven frozen redshifts and five frozen low-k nodes are analyzed against the matched zero-coupling reference;
3. all response values and endpoint contrasts are finite, every endpoint contrast is non-zero, and all 35 model-redshift rows possess exactly one `u=0.5` crossing;
4. all four adjacent full-seven-redshift `C50` values are finite and **strictly positive**;
5. leave-one-redshift robustness passes: after deleting each of the seven redshifts in turn and recomputing all five `k50_geo`, every one of the resulting 28 adjacent `C50` values is finite and **strictly positive**.

Any violation gives `FAIL_IDM_PHOTON_ENDPOINT_HALF_TRANSITION_PROSPECTIVE_V0_1`. There is deliberately **no common slope-magnitude band**: Exp055A/F28 supported sign/order preservation but rejected a shared numerical coefficient. No coupling reselection, node deletion, alternative crossing, magnitude-band fitting or post-output recalibration is permitted for v0.1.

## Interpretation boundary frozen before output

A PASS would be the first prospective validation of the exact F28 half-transition/sign relation on C8, a mechanism whose response was not used to construct the operator or choose its couplings. It would materially strengthen G7 and provide the fresh withheld-prediction evidence required by the current G8 program; the final gate state must still be assigned conservatively from the repository's frozen gate definitions and provenance audit.

A FAIL would prospectively falsify the F28 candidate at C8 v0.1 while preserving Exp055A as a positive retrospective result and leaving earlier mechanism-specific DSIR findings intact. Failure reasons and outputs must be retained without tuning the contract.

Neither outcome is evidence for a fundamental dark-sector action, intrinsic field count, observational detectability, or a universal numerical slope coefficient.
