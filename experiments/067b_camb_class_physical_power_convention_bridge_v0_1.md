# Exp067B — CAMB ↔ CLASS physical power-convention bridge v0.1

Date: 2026-08-26
Status: preregistered before the first Exp067B numerical comparison.

## Purpose

Before any covariance-whitened G7 law is fit and before any fresh G8 withheld family is selected, validate the physical solver convention required by the ACT×unWISE solver-neutral projector.

Exp066A proved the algebraic independence of the projector inputs on analytic mock spectra. Exp067B asks a different question: on one fixed linear LambdaCDM reference, do pinned CAMB and pinned CLASS represent the three projector inputs with the same physical `k`, power units, Weyl scaling and sign convention?

This is a convention/reference gate only. It contains no dark-sector family response, no ACT data residual, no law fit and no null-statistic optimisation.

## Immutable solver provenance

- CAMB: `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- CLASS: `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.

Source contracts to audit before evaluation:

1. CAMB `docs/source/transfer_variables.rst` must state that power variable `Weyl` is `k^2*(phi+psi)/2` and that `get_matter_transfer_data` divides transfer variables by `k^2`;
2. CAMB `delta_nonu` must be the CDM+baryon weighted density excluding neutrinos;
3. CLASS `classy.pyx::get_Weyl_pk_and_k_and_z` must construct Weyl power using `k^4*((phi+psi)/(2*d_m))^2` times matter power;
4. CLASS `get_transfer_and_k_and_z(output_format='class')` must state curvature-`R=1` normalisation and expose `phi`, `psi` and density transfers.

A source-contract failure is an Exp067B FAIL, not permission to change the mapping after inspecting spectra.

## Frozen reference cosmology

Use a flat, massless-neutrino LambdaCDM reference so that CAMB `delta_nonu` and CLASS total nonrelativistic matter are exactly the same CDM+baryon species set:

- `H0 = 67 km/s/Mpc`, `h=0.67`;
- `omega_b = 0.0224`;
- `omega_cdm = 0.1200`;
- `Omega_k = 0`;
- `T_cmb = 2.7255 K`;
- massless effective neutrino number `N_eff/N_ur = 3.046`;
- no massive neutrino species and `mnu=0`;
- `YHe = 0.24`;
- `A_s = 2.10e-9` at `k_pivot=0.05 Mpc^-1`;
- `n_s = 0.965`;
- cosmological constant (`w=-1`);
- adiabatic scalar initial conditions only;
- **linear spectra only**; no HALOFIT/HMcode/CLEFT/nonlinear correction.

Reionization/optical-depth settings are not part of the tested low-redshift matter/Weyl power convention and must not be used as fit parameters.

## Frozen physical support

Physical wavenumber, never `h/Mpc`:

`k = {0.005, 0.02, 0.05, 0.10, 0.20} Mpc^-1`.

Redshift:

`z = {0.0, 0.5, 1.0, 2.0}`.

Twenty `(z,k)` cells are required for each spectrum. Missing/non-finite cells fail; no zero filling is allowed.

## CAMB side

Request linear matter-power interpolators with

- `hubble_units=False`;
- `k_hunit=False`;
- `var1,var2` equal to:
  - `('delta_nonu','delta_nonu')` → `P_mm^B`;
  - `('Weyl','delta_nonu')` → `P_Wm^B`;
  - `('Weyl','Weyl')` → `P_WW^B`.

The operational CAMB Weyl variable is therefore

`W = k^2*(phi+psi)/2`,

not the unscaled potential and not the `get_matter_transfer_data` Weyl column interpreted without its documented `1/k^2` transfer-table normalisation.

## CLASS side

Use CLASS-format transfer functions in the default synchronous calculation. With no massive neutrinos, `d_m` is the same CDM+baryon matter set as CAMB `delta_nonu`.

At each physical `(k,z)` define

`q_W(k,z) = k^2 * (phi+psi)/(2*d_m)`.

Using CLASS linear matter power in `Mpc^3`, define

- `P_mm^C = P_m`;
- `P_Wm^C = q_W * P_m`;
- `P_WW^C = q_W^2 * P_m`.

This is a transfer-product identity for a single adiabatic primordial mode. It is **not** a Poisson reconstruction and does not infer Weyl from matter dynamics. The future solver-neutral interface continues to accept `P_WW`, `P_Wm`, `P_mm` as independent inputs.

As an internal source-level positive control, the constructed CLASS `P_WW^C` must agree with CLASS's own `get_Weyl_pk_and_k_and_z(nonlinear=False,h_units=False)` construction to relative/logarithmic tolerance `1e-10` on the common internal grid or its exact algebraic equivalent.

## Hard cross-solver statistics

For each spectrum define

`D_mm = max |ln(P_mm^C/P_mm^B)|`,

`D_WW = max |ln(P_WW^C/P_WW^B)|`,

and, using absolute cross-power amplitude after separately checking its sign,

`D_Wm = max |ln(|P_Wm^C|/|P_Wm^B|)|`.

Frozen acceptance:

- all auto powers finite and strictly positive;
- all cross powers finite and nonzero;
- CLASS and CAMB cross-power signs agree at every one of the 20 cells;
- `D_mm <= 0.03`;
- `D_WW <= 0.03`;
- `D_Wm <= 0.03`.

The 3% logarithmic tolerance is intentionally much wider than prior DSIR same-response cross-solver numerical closures, but many orders of magnitude tighter than a missing-`k^2` convention error. It is frozen before the first Exp067B comparison and is not to be recalibrated from the output.

## Rank-one adiabatic coherence controls

For each solver compute

`rho^2 = P_Wm^2/(P_WW*P_mm)`.

Because the frozen reference contains one adiabatic scalar initial mode and uses linear transfer products, require

`max |rho^2-1| <= 5e-8`

for both CAMB and CLASS over the 20 cells.

This is a convention/coherence control, not a universal dark-sector law; future multi-IC/stochastic models need not satisfy it.

## Missing-k^2 negative control

Construct the deliberately wrong CLASS auto-power obtained by interpreting the unscaled Weyl potential as the CAMB power variable:

`P_WW_wrong = P_WW^C / k^4`.

Against the correct CAMB `P_WW^B`, require

`median |ln(P_WW_wrong/P_WW^B)| >= 5`.

This control must fail badly in the expected direction, demonstrating that the regression would detect the exact convention error corrected by the 2026-08-26 erratum. It is a fixed negative control and cannot be used to tune the positive threshold.

## Hard outcome

PASS iff source provenance/contracts, CLASS internal Weyl construction, all finite/sign checks, all three `D<=0.03` cross-solver checks, both adiabatic coherence checks and the missing-`k^2` negative control pass.

PASS status:

`PASS_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1`

FAIL status:

`FAIL_CAMB_CLASS_PHYSICAL_POWER_CONVENTION_BRIDGE_V0_1`.

## Anti-retuning

After the first numerical comparison no change is permitted to solver commits, cosmology, gauge declaration, k/z nodes, `k^2` factor, power units, sign convention, interpolation rule, 3% thresholds, coherence threshold or negative-control threshold. Infrastructure failures before any comparison may be repaired without altering the frozen scientific contract.

## Gate semantics

A PASS validates the LambdaCDM physical convention needed to feed CLASS-family spectra into the solver-neutral ACT projector on the frozen linear support. It does **not** validate nonlinear prescriptions for arbitrary dark-sector/MG models, does not itself establish observational distinguishability, and does not close G7/G8/G9.

After PASS, a G7 candidate may be preregistered using only training families with an explicit validity mask, frozen Exp067A whitening operator, nuisance/identity quotient, one mathematical cross-channel relation and one null/permutation control. A fresh withheld family may be selected only after that G7 relation is frozen.
