# Exp069H — C5 q=3 unmodified-upstream physical-provider certification v0.1

**Date:** 2026-08-27  
**Status:** PROSPECTIVE PROVIDER-CERTIFICATION PREREGISTRATION — frozen before any Exp069H solver execution.

## Why this experiment is allowed

Exp069B remains permanently `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1` at its frozen ordinary-GR versus designer-zero target criterion `5e-6`.

Exp069F subsequently executed a separately preregistered paired general-accuracy ladder and classified

`GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`.

Its frozen target maxima were

`M_q = [5.302921926e-6, 2.904403569e-6, 1.701118686e-6, 1.310789027e-6]`

for `q=[1,2,3,4]`. The first preregistered target PASS is q=2.

However Exp069F also stored exact-equal solver-native GR/designer grids. Its same-node raw maxima were

`R_q = [9.938162077e-6, 5.400555775e-6, 2.842130238e-6, 1.517781618e-6]`.

Therefore q=3 is the **smallest already-tested unmodified-upstream accuracy point for which both target and direct same-node raw maxima are below the historical 5e-6 scale**. This provider experiment prospectively selects q=3 for that reason. q=4 is not substituted after output.

The selection uses completed Exp069F only as mechanism evidence and candidate-route design. Exp069H is a new independent certification experiment and must satisfy the previously frozen Exp069G C1–C8 minimum contract. Nothing here reclassifies Exp069B/F.

## Pinned upstream and cosmology

Use exactly

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Use the same matched cosmology as Exp069B–F:

- `H0=67 km/s/Mpc`;
- `ombh2=0.0224`;
- `omch2=0.1200`;
- no massive neutrinos;
- `massless_neutrinos=3.046`;
- `helium_fraction=0.2404`;
- `A_s=2.10e-9`;
- `n_s=0.965`;
- no reionization;
- linear power only.

Ordinary reference: `EFTflag=0`.

Designer branch:

- `EFTflag=3`;
- `DesignerEFTmodel=1`;
- `EFTwDE=0`;
- requested `EFTB0` as listed below;
- `model_background_num_points=6000`;
- `EFTCAMB_skip_RGR=False`;
- `EFTCAMB_GR_threshold=1e-8`;
- all established Exp069B–F stability settings unchanged.

## Frozen numerical provider setting

For every ordinary-GR and designer run set using the public API:

- `AccuracyBoost=3.0`;
- `lAccuracyBoost=3.0`;
- `lSampleBoost=1.0`;
- `DoLateRadTruncation=True`;
- `NonLinear_none`;
- `kmax=0.30 Mpc^-1`;
- `k_per_logint=320`.

No accuracy parameter may change after output inspection.

## Frozen B0 sequence

Run the designer sequence in this exact order:

`B0 = [0, 1e-12, 1e-10, 1e-8, 1e-6]`.

The first four points test the exact/near-zero boundary. `B0=1e-6` is the production-scale nontrivial-signal point inherited from the existing C5 program.

No point may be added, removed, replaced or reordered after output inspection.

## Frozen physical powers and sampling

Use direct public linear solver powers with

- matter variable: `delta_nonu`;
- Weyl variable: `Weyl`, i.e. the already validated CAMB convention corresponding to `k^2(phi+psi)/2`;
- `P_mm = P(delta_nonu,delta_nonu)`;
- signed `P_Wm = P(Weyl,delta_nonu)`;
- `P_WW = P(Weyl,Weyl)`.

No absolute value may be applied to `P_Wm`.

Target nodes remain exactly

- `z=[0.0,0.295,0.51,0.934,1.491,2.33,3.0]`;
- `k=[0.003,0.01,0.03,0.10,0.20] Mpc^-1`.

Store solver-native raw grids/powers and target-grid powers. Raw same-node residuals are interpreted only if GR and designer raw k/z grids are exactly equal.

## C1 — independent exact-zero closure: HARD

Run a fresh ordinary-GR reference and a fresh designer `B0=0` case under the q=3 provider setting.

Define target closure

`M0 = max_{z,k,blocks} abs(P_designer0/P_GR - 1)`.

Require

`M0 <= 5e-6`.

Also require exact equality of the solver-native GR/designer raw k/z grids and define

`R0 = max_{same raw nodes,blocks} abs(P_designer0/P_GR - 1)`

using only finite cells with nonzero GR denominator. Require

`R0 <= 5e-6`.

This additional same-node hard requirement is prospectively stronger than Exp069F's target-only primary classification and is included specifically so interpolation cannot hide a raw failure.

Any zero-denominator raw cell is recorded explicitly and excluded only from the relative quotient; it is not replaced by a finite invented value.

## C2 — positive-B0 continuity: HARD

For each tiny-positive point `B0 in {1e-12,1e-10,1e-8}`, compare directly to the fresh q=3 designer `B0=0` provider output.

Define

`C_target(B0) = max abs(P_B0/P_0 - 1)`

on the frozen target nodes and

`C_raw(B0)`

analogously on exact-equal raw nodes.

Require for every tiny-positive point:

- `C_target(B0) <= 5e-6`;
- `C_raw(B0) <= 5e-6`;
- all stored powers finite on the frozen target support.

This does not require a nonzero response at arbitrarily tiny B0. It only requires continuity of the positive branch into the validated numerical zero boundary.

## C3 — nontrivial production signal: HARD

At `B0=1e-6` define

`S_prod = max_{z,k,blocks} abs(P_prod/P_GR - 1)`

on the frozen target grid.

Require

`S_prod >= 1e-3`.

Rationale frozen before Exp069H output: `1e-3` is two hundred times the historical `5e-6` zero-closure scale and remains well below the previously observed percent-level production response, so passing cannot be achieved by collapsing the positive branch onto numerical GR.

Also require all production target powers finite.

## C4 — signed cross-power semantics: HARD

For every case:

- store `P_Wm` exactly as returned by the signed cross-power accessor;
- do not take `abs(P_Wm)` or reconstruct it from auto-powers;
- record units/k convention/redshift ordering;
- require two repeated accessor traversals to return identical signed arrays under the repeatability criterion below.

No pre-assigned sign is required; the physical returned sign is the evidence.

## C5 — repeatability and state integrity: HARD

### Repeated-accessor control

For every completed solver result object:

1. extract blocks in order `[mm,Wm,WW]`;
2. extract again in reverse order `[WW,Wm,mm]`;
3. compare the resulting raw grids, raw powers and target powers for the same named block.

Require exact `np.array_equal` for finite arrays and exact equality of grid arrays. Any NaN/Inf is a failure because target support is required finite.

### Independent zero rerun

After the main sequence, execute one additional independent designer `B0=0` run with identical frozen parameters.

Compare its target and exact-equal raw powers to the primary `B0=0` run and require

`D_repeat_target <= 1e-12`

and

`D_repeat_raw <= 1e-12`

where each is the maximum absolute relative difference over finite nonzero-denominator cells.

This tolerance is far below the 5e-6 physical closure criterion and is a reproducibility control, not a relaxed physics threshold.

Also require the ordinary GR provider object to remain unchanged after all block extraction by repeated forward/reverse access.

## C6 — no retrospective correction: HARD

Forbidden:

- floor subtraction;
- fitted renormalization;
- spectrum rescaling;
- smoothing;
- jitter;
- pseudoinverse;
- changing target cells or support after seeing residuals;
- changing q or B0 points;
- changing the 5e-6 closure/continuity scale;
- changing the 1e-3 production-signal threshold.

No upstream source patch is used. This is an **unmodified-upstream numerical provider route**.

## C7 — theory boundary versus provider: HARD interpretation boundary

The analytic `A=0` exact-GR theorem may be reported as mechanism context but is not used to manufacture the B0=0 spectrum. Exp069H must use the literal public `EFTB0=0` branch at q=3 and satisfy C1–C6 numerically.

## C8 — failure semantics: HARD

Execution/case failure is `INCOMPLETE_EXP069H` and is not converted into a scientific FAIL without completed hard metrics.

If execution completes, scientific PASS requires **all** C1–C7 hard checks. Any completed hard-check violation gives

`FAIL_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`.

If all hard checks pass, classify

`PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`.

No partial provider certification is allowed.

## Integrity controls

Require in the final artifact:

- preregistration commit predates every Exp069H solver run;
- upstream SHA before/after equals the pinned commit;
- exact requested/readback accuracy and designer settings;
- exact B0, z, k and block order;
- exact raw-grid equality before raw quotient use;
- signed `P_Wm` preservation;
- repeated-accessor controls;
- independent zero rerun;
- no upstream source modification;
- no post-hoc criterion changes.

## Gate authorization if PASS

A PASS would make the q=3 unmodified-upstream C5 provider **eligible** for the next G7 prerequisite step under Exp069G.

It would then authorize only the next prospective action:

`validated C3 + certified C5 -> preregister common physical support-validity mask`.

It would **not** by itself:

- close G7;
- authorize a law fit before support/covariance/nuisance steps;
- close G8 or G9;
- establish new physics.

If FAIL, preserve it and return to a newly preregistered provider/mechanism route without changing these criteria.
