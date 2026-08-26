# Exp069B — C5 explicit-EFT Python physical power bridge v0.1

**Date:** 2026-08-26  
**Status:** prospective corrective contract frozen before the first Exp069B numerical output.

## 1. Motivation and immutable relation to Exp069A

Exp069A is permanently recorded as

`FAIL_C5_DESIGNER_FR_PHYSICAL_POWER_BRIDGE_V0_1`.

The evaluable Exp069A run showed that all nonzero designer `B0` points were bitwise identical to the exact-zero control while the same pinned C5 `.ini` physics had previously produced nonzero responses through the native H-EFTCAMB executable. Source audit then identified the missing integration step: the pinned H-EFTCAMB Python API exposes and upstream examples use

`pars.EFTCAMB.initialize_parameters(pars, eftcamb_params, ...)`

to initialize the additional EFT model state. Exp069A used ordinary `camb.read_ini()` only.

Exp069B tests this one corrective hypothesis. Exp069A remains FAIL regardless of Exp069B outcome.

## 2. Allowed change

The **only scientific-interface change** relative to Exp069A is the ingestion of designer EFT parameters:

1. read the same ordinary CAMB baseline with the pinned Python wrapper;
2. set the same frozen transfer grid and `NonLinear_none` state;
3. for designer cases call the upstream explicit
   `CAMBparams.EFTCAMB.initialize_parameters(CAMBparams, EFTCAMB_params, print_header=True)`;
4. audit the resulting active EFT state before requesting powers;
5. calculate the same direct physical power blocks.

No cosmological parameter, designer parameter, `B0` point, evaluation cell, variable pair, unit convention, tolerance or PASS/FAIL threshold may be changed from Exp069A.

## 3. Immutable solver and cosmology

Pinned solver:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Ordinary CAMB baseline is identical to Exp069A:

- `H0 = 67 km/s/Mpc`;
- `ombh2 = 0.0224`;
- `omch2 = 0.1200`;
- `omnuh2 = 0`;
- `massless_neutrinos = 3.046`;
- no massive neutrino eigenstates;
- `helium_fraction = 0.2404`;
- `As = 2.10e-9`;
- `ns = 0.965`;
- reionization disabled;
- scalar/tensor CMB spectra and lensing not required for this bridge;
- `NonLinear_none` / `do_nonlinear = 0`.

The common baseline file must contain no designer EFT selection keys. Those keys enter only through the explicit Python EFT dictionary below.

## 4. Frozen explicit EFT dictionary

For every designer run initialize the pinned EFTCAMB Python state with exactly:

- `EFTflag = 3`;
- `DesignerEFTmodel = 1`;
- `EFTwDE = 0`;
- `EFTB0 = B0`;
- `EFT_ghost_math_stability = F`;
- `EFT_mass_math_stability = F`;
- `EFT_ghost_stability = T`;
- `EFT_gradient_stability = T`;
- `EFT_mass_stability = F`;
- `EFT_mass_stability_rate = 10.0`;
- `EFT_additional_priors = T`;
- `EFTCAMB_turn_on_time = 0.01`;
- `EFTCAMB_stability_time = 1e-10`;
- `EFTCAMB_stability_threshold = 0.0`.

Frozen controls and production points remain:

- GR reference: standard pinned CAMB state with no designer initialization;
- exact designer GR-limit: `B0=0` through the explicit EFT initializer;
- production: `B0={1e-6,1e-5,1e-4,1e-3}`.

No production point may be removed after output.

## 5. Frozen physical grid and direct powers

Identical to Exp069A:

\[
z=\{0,0.295,0.51,0.934,1.491,2.33,3.0\},
\]

\[
k=\{0.003,0.01,0.03,0.10,0.20\}\ {\rm Mpc}^{-1},
\]

with internal `kmax=0.30 Mpc^-1`.

Request with `nonlinear=False`, `hubble_units=False`, `k_hunit=False`:

\[
P_{mm}=P(\texttt{delta_nonu},\texttt{delta_nonu}),
\]

\[
P_{Wm}=P(\texttt{Weyl},\texttt{delta_nonu}),
\]

\[
P_{WW}=P(\texttt{Weyl},\texttt{Weyl}).
\]

No Poisson reconstruction, transfer-table substitution, absolute-value replacement of signed `P_Wm`, nonlinear correction or CLEFT term is allowed.

## 6. Hard tests

### B1 — provenance/source contract

Require the exact pinned H-EFTCAMB SHA and the same direct-power source contract certified in Exp069A:

- `delta_nonu` available as the CDM+baryon matter variable;
- `Weyl = k^2(phi+psi)/2`;
- arbitrary auto/cross power variable pairs supported;
- transfer-table `1/k^2` rescaling is not silently imported into physical power functions.

### B2 — explicit EFT active-state audit

For every designer case, before accepting its power output, require all of:

1. `initialize_parameters(...)` returns without exception;
2. `pars.EFTCAMB.EFTflag == 3`;
3. `pars.EFTCAMB.DesignerEFTmodel == 1`;
4. `pars.EFTCAMB.EFTCAMB_model_is_designer` is true;
5. `pars.EFTCAMB.read_parameters()` contains the explicitly supplied model/stability keys and records `EFTB0` equal to the requested value to floating-point roundoff;
6. `pars.EFTCAMB.model_name()` is non-empty;
7. the full solver calculation returns without `ERROR STOP` or Python exception;
8. the designer calculation satisfies the pinned EFTCAMB stability machinery rather than being accepted merely because a standard CAMB result exists.

Record the selected active flags, model name, requested dictionary, read-back values and model parameter values in the immutable output.

A no-op EFT layer is a hard FAIL even if finite powers are returned.

### B3 — physical-unit direct powers

At every frozen `(B0,z,k)` cell require finite direct `P_mm`, `P_Wm`, `P_WW`, with

- `P_mm>0`;
- `P_WW>0`;
- `P_Wm!=0`;
- `NonLinear_none` active.

### B4 — unit roundtrip

Unchanged from Exp069A. For GR and exact designer `B0=0`, convert a separately requested `(k/h,(Mpc/h)^3)` `P_mm` back to physical units and require

\[
\max r_{unit}\le2\times10^{-8}.
\]

### B5 — exact designer GR limit

Unchanged from Exp069A. For each of `mm`, `Wm`, `WW`, compare explicit designer `B0=0` to the standard GR reference and require

\[
\max r_X\le5\times10^{-6}.
\]

### B6 — signed single-mode coherence

Unchanged from Exp069A:

\[
\rho^2=\frac{P_{Wm}^2}{P_{WW}P_{mm}},
\qquad |\rho^2-1|\le2\times10^{-5}
\]

at every frozen cell. Record the sign of `P_Wm` and never replace it by `|P_Wm|`.

### B7 — missing-`k^2` negative control

Unchanged from Exp069A. The deliberately wrong diagnostic

\[
P_{WW}^{wrong}=P_{WW}/k^4,\qquad P_{Wm}^{wrong}=P_{Wm}/k^2
\]

must show the expected nonconstant scaling and maximum relative discrepancy greater than `1e2` for both blocks.

### B8 — production nondegeneracy

Unchanged from Exp069A. For every production `B0`, the complete set of `P_mm/P_Wm/P_WW` arrays may not be bitwise identical to exact designer `B0=0`. Record

\[
R_X=\ln|P_X(B0)/P_X(0)|
\]

without imposing a new magnitude/slope law.

## 7. PASS/FAIL

PASS iff B1-B8 all pass:

`PASS_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.

Otherwise:

`FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.

Any post-output scientific failure is preserved. Infrastructure failures before evaluable output may be repaired only without changing this contract.

## 8. Anti-retuning

After the first Exp069B output do not change:

- solver SHA;
- ordinary cosmology;
- explicit EFT dictionary keys/settings;
- `B0` grid;
- physical `(z,k)` grid or internal `kmax`;
- power-variable pairs;
- unit flags;
- thresholds `2e-8`, `5e-6`, `2e-5`, `1e2`;
- production nondegeneracy definition;
- top-level PASS/FAIL logic.

## 9. Gate semantics

Exp069B can certify only the C5 physical power-input bridge. It cannot close G7, cannot select the common ACT physical-support mask, cannot measure the final nuisance quotient and cannot choose a G8 withheld family.

If Exp069B passes, the next independent prerequisite remains the C3/GDM read-only gauge-invariant `D_m` physical power bridge. After both C5 and C3 are bridge-certified, freeze and evaluate the common ACT kernel/bandwindow validity mask before covariance restriction and nuisance SVD.

Entering state: **G7 OPEN, G8 OPEN, G9 OPEN**.
