# Exp073C — nonlinear independent matter/Weyl provider candidate landscape result v0.1

**Date:** 2026-08-27  
**Landscape classification:** `NO_COMPLETE_PUBLIC_CANDIDATE_ROUTE_EXP073C`

## Scope

This prospective landscape search was frozen before candidate ranking in `experiments/073c_nonlinear_provider_candidate_landscape_prereg_v0_1.md`.

The required DSIR nonlinear interface is not merely a nonlinear matter spectrum. It requires a reproducible physical route to

- `P_mm(k,z)`;
- signed `P_Wm(k,z)`;
- `P_WW(k,z)`;

for both C3/GDM and C5/designer-f(R), with model-specific Weyl semantics and support plausibly approaching the Exp072C planning frontier (`z_min≈0.0087346`, `k_max≈4.81826 Mpc^-1`).

Search used primary papers, official documentation and public code repositories available through 2026-08-27. No covariance, nuisance, G7 relation/null or G8 result was used.

## C5 / f(R) landscape

### e-MANTIS — strong matter-only candidate

Primary paper: Sáez-Casares, Rasera & Li, *The e-MANTIS emulator: fast predictions of the non-linear matter power spectrum in f(R)CDM cosmology*, MNRAS 527 (2024), DOI `10.1093/mnras/stad3343`, arXiv `2303.08899`.

Official documentation: `https://e-mantis.pages.obspm.fr/e-mantis/`.

The public emulator predicts the nonlinear **matter-power boost** `B(k)=P_f(R)/P_LCDM`. Its stated conservative range is approximately `k<7 h/Mpc`, `z<2`, with maximum error around 3% over the emulated parameter domain. This is highly relevant to the Exp072C k scale but supplies `P_mm`, not an independently calibrated signed `P_Wm` or `P_WW` API.

Frozen classification: `P_mm=NATIVE`, `P_Wm=UNSUPPORTED`, `P_WW=UNSUPPORTED` for the DSIR three-block requirement.

### FORGE — strong matter-only candidate

Primary paper: Arnold et al., *FORGE — the f(R)-gravity cosmic emulator project I: Introduction and matter power spectrum emulator*, MNRAS 515 (2022), DOI `10.1093/mnras/stac1091`, arXiv `2109.04984`.

FORGE emulates the fully nonlinear f(R) matter power spectrum and reports useful accuracy to `k≈10 h/Mpc` over its simulation parameter domain. The simulation suite was designed to support later lensing observables, but the published/public provider in this work is a matter-power emulator rather than an independent three-block Weyl/matter provider.

Frozen classification: `P_mm=NATIVE`, `P_Wm=UNSUPPORTED`, `P_WW=UNSUPPORTED` at provider level.

### ReACT / ACTio-ReACTio — broad matter-only framework

Primary code: `https://github.com/nebblu/ACTio-ReACTio`.

Primary paper: Taylor et al., *Fast and accurate predictions of the non-linear matter power spectrum for general models of Dark Energy and Modified Gravity*, MNRAS 519 (2023), DOI `10.1093/mnras/stac3783`.

ReACT provides a public halo-model-reaction route for the nonlinear **matter** power spectrum in f(R) and other beyond-LCDM models. The current public code documents nonlinear Poisson-equation modelling and matter two-point statistics, but not a certified independent nonlinear `P_Wm/P_WW` provider satisfying the DSIR block contract.

Frozen classification: `P_mm=NATIVE/FRAMEWORK`, `P_Wm=UNSUPPORTED`, `P_WW=UNSUPPORTED` as a complete DSIR provider.

### Important f(R) nuance

Hu-Sawicki f(R) has model-specific quasi-static relations between the metric potentials and matter, and current Euclid modelling writes a lensing modification `Sigma` rather than treating lensing as arbitrary. This makes a future **model-specific derivation** of Weyl blocks scientifically plausible, but the current landscape search did not find a public calibrated provider exposing nonlinear signed `P_Wm` and `P_WW` over the required domain with the validation needed by DSIR.

This distinction is deliberate: a physically justified model-specific derivation could pass a future provider contract, but silently applying a GR matter-to-Weyl closure to an f(R) matter emulator does not pass Exp073C.

## C3 / GDM landscape

### Classical GDM halo-model work — nonlinear matter only and approximate

Thomas, Kopp & Marković, *Using large-scale structure data and a halo model to constrain generalized dark matter*, MNRAS 490 (2019), DOI `10.1093/mnras/stz2634`, arXiv `1905.02739`, explicitly notes that GDM was defined perturbatively and develops an approximate halo model to explore nonlinear **matter** clustering.

Kopp, Skordis & Thomas, *An extensive investigation of the Generalised Dark Matter model*, Phys. Rev. D 94 (2016), DOI `10.1103/PhysRevD.94.043512`, arXiv `1605.00649`, identifies nonlinear extension as a required future development and discusses possible EFT/fluid routes rather than supplying a calibrated nonlinear three-block provider.

### 2026 dedicated GDM simulations — important new partial candidate

Sakr & López-Sánchez, *Forecast on the generalised dark matter properties from a Euclid-like survey*, arXiv `2601.16943` (2026), reports dedicated simulations and a nonlinear GDM matter power spectrum for photometric probes.

This is genuine progress relative to the older landscape, but it is still not a complete DSIR provider. The paper states that the simulations generate GDM initial conditions from the linear GDM matter spectrum and then evolve collisionless N-body particles, neglecting GDM thermal velocities; it reports nonlinear `P_delta-delta`. For lensing it sets the Weyl modification to the standard relation (`Sigma=1`) for the studied Lambda-GDM framework rather than publishing an independent nonlinear signed `P_Wm/P_WW` provider. The setup also samples specific scenarios rather than exposing a validated public emulator/API across the DSIR C3 training family.

Frozen classification for the current DSIR need: `P_mm=PARTIAL/NATIVE_SIMULATION`, `P_Wm=DERIVATION_ASSUMED_BUT_NOT_PROVIDER-CERTIFIED`, `P_WW=DERIVATION_ASSUMED_BUT_NOT_PROVIDER-CERTIFIED`.

## Cross-family result

No discovered public/reproducible candidate or composable candidate set satisfies all of the following simultaneously:

1. nonlinear `P_mm`, signed `P_Wm`, and `P_WW`;
2. model-specific nonlinear Weyl semantics rather than an unvalidated GR closure;
3. applicability to both the C3/GDM and C5/designer-f(R) training families;
4. a versionable provider/API or calibrated data product;
5. support plausibly covering the low-z/high-k region demanded by Exp072C.

Therefore the frozen Exp073C outcome is

`NO_COMPLETE_PUBLIC_CANDIDATE_ROUTE_EXP073C`.

This is not equivalent to “nonlinear modelling is impossible.” It means that the missing DSIR provider cannot currently be obtained by simply importing one established public package under the frozen requirements.

## Highest-value partial ingredients

The most useful ingredients found are:

- C5 nonlinear matter: e-MANTIS / FORGE, with ReACT as a complementary semi-analytic framework;
- C3 nonlinear matter: the new dedicated GDM simulation strategy in arXiv:2601.16943 plus the older GDM halo/spherical-collapse literature;
- projection layer: already solved by DSIR/ACT as shown by Exp073B.

The remaining technical problem is to construct and certify nonlinear Weyl auto/cross information consistently with each model family, especially C3's nonlinear fluid closure and C5's screened scalar/metric fields.

## Gate state

No covariance restriction, whitening, nuisance SVD/rank, G7 relation/null or G8 selection is authorized.

G7 OPEN. G8 OPEN. G9 OPEN.
