# Exp069A — C5 designer-f(R) physical power-input bridge v0.1

Date: 2026-08-26
Status: PREREGISTERED — NO EXP069A PHYSICAL OUTPUT EVALUATED AT THIS COMMIT

## Purpose

Validate that the already-characterized C5 designer-f(R) family can supply the three independent physical spectra required by the validated ACT×unWISE linear/no-CLEFT forward interface:

\[
P_{WW}(k,z),\qquad P_{Wm}(k,z),\qquad P_{mm}(k,z),
\]

using the pinned modified-gravity solver directly, without reconstructing Weyl from matter through a GR Poisson relation.

This experiment is a power-input bridge only. It does not apply the survey-kernel validity mask, does not whiten covariance, does not fit a G7 relation, and does not select a G8 withheld family.

Exp068B is treated as the validated forward-interface prerequisite. Exp068A remains a permanent scientific FAIL and is not overwritten.

## Frozen provenance

Use the same H-EFTCAMB line already used by the C5 branch:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`

Any execution commit must record:

1. exact H-EFTCAMB git SHA;
2. compiler/runtime versions;
3. full cosmological and precision parameter files;
4. exact DSIR accessor/extraction code hash;
5. raw output hashes for the sampled spectra used by the gate.

No solver-version substitution is allowed inside Exp069A.

## Frozen physical variables and units

The solver-side variables are:

- matter: `delta_nonu`;
- metric/Weyl: `Weyl`, with the pinned CAMB convention
  \[
  W=k^2(\phi+\psi)/2.
  \]

Request direct auto/cross physical power spectra with

- `hubble_units=False`;
- `k_hunit=False`;
- `nonlinear=False`.

Therefore the frozen DSIR inputs are

\[
P_{mm}=P(\delta_{nonu},\delta_{nonu}),
\]

\[
P_{Wm}=P(Weyl,\delta_{nonu}),
\]

\[
P_{WW}=P(Weyl,Weyl).
\]

The bridge must not reconstruct `Weyl` from `delta_nonu` using a Poisson equation.

## Frozen cosmological controls

The first execution contains two solver cases under matched background/primordial/precision settings:

1. **GR control:** designer-f(R) parameter `B0 = 0`;
2. **C5 modified control:** `B0 = 1e-6`.

`B0=1e-6` is frozen because the canonical high-precision C5 manifold already treats `B0 >= 1e-6` as the production region, while `B0=1e-7` is explicitly a solver-threshold transition control. No parameter optimization or substitution of another nonzero B0 is permitted in Exp069A v0.1.

## Frozen support grid

This bridge is an input-convention validation, not the final survey validity mask. Use a deterministic rectangular diagnostic grid sufficient to cover the later ACT kernel audit while remaining linear/no-CLEFT:

- redshift nodes: `z = [0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`;
- physical wavenumber nodes in `Mpc^-1`: convert the existing DSIR C5 core nodes `[0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc` using the exact model H0/h recorded by the run, and additionally include physical `k = 0.2 Mpc^-1` if it lies inside the solver interpolation range without extrapolation.

No extrapolation is allowed. A node outside native solver support is recorded as unavailable, never zero.

## Frozen acceptance checks

### A1 — provenance and configuration

PASS iff all pinned provenance, cosmology, precision, linear/nonlinear flags, units and variable names match the preregistered contract exactly.

### A2 — finite signed physical triplet

At every available `(k,z)` cell for both GR and nonzero C5 cases:

- `P_mm` finite and strictly positive;
- `P_WW` finite and nonnegative, and strictly positive above numerical underflow;
- `P_Wm` finite and nonzero whenever both autos are nonzero;
- the sign of `P_Wm` is preserved and reported, never replaced by an absolute value.

### A3 — Cauchy/coherence bound

For each available cell define

\[
r^2(k,z)=\frac{P_{Wm}^2}{P_{WW}P_{mm}}.
\]

Require numerical consistency with a same-initial-condition transfer construction:

\[
|1-r^2| \le 5\times10^{-10}
\]

for cells whose denominator is above the floating-point numerical floor. Cells below the floor must be explicitly flagged rather than coerced to PASS.

### A4 — GR-limit physical convention bridge

At `B0=0`, compare the direct H-EFTCAMB triplet against the already validated pinned CAMB physical convention used by Exp067E/Exp068B at identical cosmology and matched `(k,z)` cells.

For each of `P_mm`, `P_WW`, and signed `P_Wm`, require

\[
\max |\Delta P|/\max(|P_{ref}|,P_{floor}) \le 3\times10^{-3}.
\]

The `3e-3` threshold is frozen here before Exp069A physical evaluation. `P_floor` must be defined deterministically from machine precision and the reference-array scale and recorded in the output.

### A5 — deliberately wrong missing-k^2 negative control

Construct a negative control by treating the CAMB transfer-table Weyl quantity as though the documented transfer-table `1/k^2` convention did not need correction. This deliberately wrong route must fail the physical-convention comparison by a large margin:

\[
\max_{cells,channels} D_{wrong} > 0.05.
\]

If the wrong control does not fail, Exp069A is FAIL because the convention test is not discriminating.

### A6 — nontrivial modified-gravity control

The `B0=1e-6` C5 point must differ from the GR control in at least one of the three physical spectra by

\[
\max |P_{C5}/P_{GR}-1| > 10^{-6}
\]

on at least one available cell. This only proves that the test exercises a nontrivial modified solution; it is not a phenomenological significance claim.

### A7 — no hidden repair

Hard FAIL if execution uses or silently introduces any of:

- nonlinear/Halofit/CLEFT correction;
- GR Poisson reconstruction of Weyl;
- absolute-valued cross power;
- interpolation extrapolation;
- replacement of unavailable cells by zero;
- post-hoc tolerance relaxation;
- solver commit substitution.

## Classification

Scientific PASS requires A1–A7 all pass.

Infrastructure/build/download failures are classified separately and do not become scientific FAIL unless the physical gate actually executes and fails a frozen criterion.

## Consequence of PASS

A PASS certifies C5 as a physically valid direct provider of `P_WW/P_Wm/P_mm` for later survey-support auditing. It does **not** certify linear theory over the entire ACT projector domain and does not close G7.

After Exp069A, the next power-input prerequisite is the C3/GDM direct `D_m` accessor/transfer-product bridge. Only after the training-family power bridges are certified may the common physical support/leakage mask be frozen and evaluated.

Gate state remains: G7 OPEN, G8 OPEN, G9 OPEN.
