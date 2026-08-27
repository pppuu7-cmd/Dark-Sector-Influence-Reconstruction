# Exp069I — C5 raw-k unit provenance audit v0.1

**Date frozen:** 2026-08-27  
**Status:** PROSPECTIVE UNIT/PROVENANCE AUDIT — no Exp069I runtime output exists before this file.

## Purpose

Exp069H has already passed its frozen provider-certification criteria. This audit does **not** retest or weaken that certification.

A provenance issue was identified after Exp069H classification and before any common C3+C5 physical support mask was frozen: the Exp069F/H raw accessor calls

`get_linear_matter_power_spectrum(..., hubble_units=False, nonlinear=False)`

without an explicit `k_hunit` argument, while the pinned upstream source defines

`k_hunit=True`

by default and documents that this returns `k/h`. The historical DSIR JSON field was named `raw_k_Mpc^-1`, which is therefore potentially a unit-label error.

The target-grid interpolator in Exp069F/H explicitly used `k_hunit=False`, so target-grid physical k values and target-grid acceptance metrics are not implicated.

Exp069I prospectively determines the exact runtime semantics and freezes the correction boundary before any support-mask construction.

## Pinned upstream

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`

Pinned source fact to verify at runtime/source checkout:

- function: `camb/results.py::CAMBdata.get_linear_matter_power_spectrum`;
- default: `k_hunit=True`;
- source relation when true: returned coordinate is internal physical `ks / (H0/100)`;
- when false: returned coordinate is internal physical `ks`.

## Frozen cosmology/provider point

Use the same ordinary-GR cosmology and numerical settings as Exp069H:

- `H0=67 km/s/Mpc`, hence `h=0.67`;
- `ombh2=0.0224`;
- `omch2=0.1200`;
- massless neutrinos `3.046`, no massive neutrinos;
- `A_s=2.10e-9`, `n_s=0.965`;
- no reionization;
- linear only;
- q=3 accuracy;
- `kmax=0.30`;
- `k_per_logint=320`.

The audit uses ordinary GR only. No dark-sector response amplitude is needed to establish accessor units.

## Frozen accessor calls

For each block `mm`, signed `Wm`, `WW`, call exactly:

### A — historical/default raw accessor

`get_linear_matter_power_spectrum(v1,v2,hubble_units=False,nonlinear=False)`

with `k_hunit` omitted.

### B — explicit k/h raw accessor

`get_linear_matter_power_spectrum(v1,v2,hubble_units=False,k_hunit=True,nonlinear=False)`.

### C — explicit physical-k raw accessor

`get_linear_matter_power_spectrum(v1,v2,hubble_units=False,k_hunit=False,nonlinear=False)`.

No interpolation is used in A/B/C.

## Frozen criteria

### U1 — default semantics closure

Require for all three blocks:

- A and B returned k arrays are exactly `np.array_equal`;
- A and B redshift arrays are exactly equal;
- A and B power arrays are exactly equal.

PASS iff all hold.

This establishes that the historical omitted argument is operationally identical to explicit `k_hunit=True` in the pinned version.

### U2 — physical conversion closure

Let `h=H0/100=0.67`.

For every raw node require

`k_default * h == k_physical`

within the frozen representation-level relative tolerance

`64 * eps(float64)`

with zero absolute tolerance except the unavoidable floating multiplication represented by the relative guard.

Also require A/C redshift arrays exactly equal and A/C power arrays exactly equal.

PASS iff all three blocks satisfy these conditions.

This is a unit/provenance check, not a scientific model tolerance.

### U3 — target-grid immunity

Construct the same Exp069H interpolator with explicit

`k_hunit=False`

and evaluate the frozen physical target k values

`[0.003,0.01,0.03,0.10,0.20] Mpc^-1`

at the frozen redshifts

`[0,0.295,0.51,0.934,1.491,2.33,3.0]`.

Require the interpolator configuration to report/use explicit physical k semantics and verify that every target k lies within the explicit physical raw-C support.

No comparison to a retuned target grid is allowed.

PASS iff all target nodes remain inside the physical raw support for every block.

### U4 — historical-label classification

If U1 and U2 pass with the expected pinned semantics, classify the old field name

`raw_k_Mpc^-1`

in Exp069F/H artifacts as

`HISTORICAL_LABEL_INCORRECT_VALUES_ARE_K_OVER_H`.

This classification changes metadata semantics only. It does not rewrite immutable artifacts.

If U1/U2 do not establish that relation, classify

`RAW_K_SEMANTICS_UNRESOLVED`

and block the common physical support mask.

### U5 — science-result preservation

The audit must explicitly preserve:

- Exp069B: permanent FAIL;
- Exp069F: `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`;
- Exp069H: `PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`.

No Exp069H threshold or residual may be recomputed using a different target grid.

Reason: its raw criteria compare powers at identical native nodes and are invariant to a common coordinate rescaling; its target criteria already used explicit `k_hunit=False`.

## Frozen overall outcomes

If U1–U3 all pass and the historical label is resolved as expected:

`PASS_C5_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1`.

If the runtime semantics are internally consistent but differ from the pinned-source expectation:

`FAIL_C5_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1`.

If execution/source checkout fails before the criteria can be evaluated:

`INCOMPLETE_EXP069I`.

## Allowed correction after PASS

A PASS authorizes only these prospective metadata/provider actions:

1. future physical-provider products must call `k_hunit=False` explicitly whenever a coordinate is labelled `Mpc^-1`;
2. historical Exp069F/H artifact fields remain immutable but are documented as `k/h` where applicable;
3. any common C3+C5 support mask must use explicit physical `k [Mpc^-1]` coordinates on both providers and must not ingest the mislabeled historical raw coordinate verbatim.

No spectral amplitude correction, interpolation repair, normalization fit or threshold change is authorized.

## Gate boundary

- C3 provider: certified;
- C5 provider: certified by Exp069H;
- common support-validity mask: **BLOCKED pending Exp069I**;
- G7/G8/G9 remain `OPEN`.
