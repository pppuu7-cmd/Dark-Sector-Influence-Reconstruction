# Exp069I — Exp069H raw-k unit/provenance audit v0.1

**Date frozen:** 2026-08-27  
**Status:** PROSPECTIVE UNIT/PROVENANCE AUDIT — frozen before every Exp069I solver execution.

## Motivation

Exp069H has completed with scientific classification

`PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1`.

Its primary target-grid provider path explicitly used physical `k_hunit=False` and passed the frozen exact-zero closure. Its raw same-node checks also passed, but a post-run source audit found that the raw accessor call omitted the `k_hunit` keyword while the stored key was named `raw_k_Mpc^-1`.

Pinned upstream

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`

defines

`get_linear_matter_power_spectrum(..., hubble_units=True, k_hunit=True, ...)`

and in the underlying raw spectrum accessor uses

`kh = ks / (H0/100)`

when `k_hunit=True`, otherwise `kh=ks`.

Therefore Exp069I asks one narrow question before any C3+C5 physical support mask is built:

> Is the Exp069H raw-grid problem only a mislabeled k-axis convention, with powers and same-node provider residuals invariant under explicit physical-k output, or does it reveal a deeper scientific provider inconsistency?

This audit does not move any Exp069H threshold and does not silently modify its immutable artifact.

## Historical state frozen into the audit

- Exp069B remains permanent `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.
- Exp069F remains `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`.
- Exp069H remains historically classified `PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1` unless and until a new experiment changes downstream eligibility; this audit never rewrites its historical result.
- Exp070C C3 provider remains certified.
- no common C3+C5 physical support mask has yet been applied.
- G7/G8/G9 are OPEN.

## Frozen solver/cosmology

Use exactly the same pinned upstream and matched q=3 zero-limit pair as Exp069H:

- upstream: `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`;
- ordinary GR: `EFTflag=0`;
- designer zero: `EFTflag=3`, `DesignerEFTmodel=1`, `EFTwDE=0`, `EFTB0=0`;
- `H0=67 km/s/Mpc`, hence nominal `h=0.67`;
- same matter/radiation/primordial settings as Exp069H;
- `AccuracyBoost=3`, `lAccuracyBoost=3`, `lSampleBoost=1`, `DoLateRadTruncation=True`;
- linear power only;
- `kmax=0.30 Mpc^-1`, `k_per_logint=320`;
- target `z=[0,0.295,0.51,0.934,1.491,2.33,3]`;
- target physical `k=[0.003,0.01,0.03,0.10,0.20] Mpc^-1`;
- blocks `P_mm`, signed `P_Wm`, `P_WW` using `delta_nonu` and `Weyl` exactly as Exp069H.

No positive-B0 production run is required: Exp069I is a unit/provenance audit of the zero pair, not a repeat provider certification.

## Three frozen raw accessor calls

For each block and each fresh GR/designer-zero result object, call the raw linear power accessor three ways on the **same result object**:

1. **implicit/default**
   `get_linear_matter_power_spectrum(..., hubble_units=False, nonlinear=False)`;
2. **explicit h-scaled k**
   `get_linear_matter_power_spectrum(..., hubble_units=False, k_hunit=True, nonlinear=False)`;
3. **explicit physical k**
   `get_linear_matter_power_spectrum(..., hubble_units=False, k_hunit=False, nonlinear=False)`.

No interpolation is allowed in U1–U4.

## U1 — pinned-source/default binding: HARD

Before interpreting numerical arrays, verify from the checked-out pinned source that:

- `get_linear_matter_power_spectrum` has default `k_hunit=True`;
- the k conversion branch is `kh = ks / (H0/100)` for true and `kh=ks` for false;
- upstream HEAD before/after equals the pinned SHA.

Also require, in fresh numerical output, that implicit/default and explicit-true calls return exactly equal k arrays, z arrays and power arrays (`np.array_equal`) for every block and both GR/designer cases.

PASS iff all conditions hold.

## U2 — raw k-axis conversion: HARD

Let

- `k_def` be the implicit/default raw k array;
- `k_phys` be the explicit `k_hunit=False` raw k array;
- `h_read = result.Params.H0/100`.

Require exact z-array equality and define

`E_k = max abs(k_def*h_read/k_phys - 1)`

over finite positive k cells.

Frozen tolerance:

`E_k <= 5e-14`.

Rationale frozen before Exp069I execution: the upstream relation is a single float64 multiply/divide by the same finite `h`; `5e-14` is a representation-level guard more than two orders of magnitude above machine epsilon and many orders below every physical provider threshold. It is not a cosmological fit tolerance.

Also require the readback `H0` to equal the requested `67` within the existing exact-readback machinery; no fitted h is permitted.

PASS iff all conditions hold.

## U3 — power-array invariance under k-unit output convention: HARD

For each GR/designer case and each block, require the raw power array returned by

- implicit/default,
- explicit `k_hunit=True`, and
- explicit `k_hunit=False`

to be exactly equal under `np.array_equal`.

No resampling, sorting or interpolation is allowed.

PASS iff every raw power array is exactly invariant.

## U4 — Exp069H raw residual invariance: HARD

On the exact native raw indices, construct signed GR/designer relative residual arrays

`R = (P_designer0-P_GR)/P_GR`

for finite nonzero-GR cells separately from:

- the implicit/default accessor outputs; and
- the explicit-physical-k accessor outputs.

Require:

1. valid-cell masks exactly equal;
2. residual arrays on valid cells exactly equal under `np.array_equal`;
3. maximum absolute raw residual from explicit physical-k output remains
   `<=5e-6`, the unchanged Exp069H hard scale.

Record the explicit-physical raw maximum `R0_phys`.

PASS iff all three conditions hold.

This criterion is what separates a label-only defect from a scientific raw-provider defect.

## U5 — physical target path regression: HARD

Using the same fresh q=3 GR/designer-zero results, evaluate the target powers only through

`get_matter_power_interpolator(..., hubble_units=False, k_hunit=False, nonlinear=False)`

on the unchanged physical target nodes.

Require:

- all target arrays finite;
- signed `P_Wm` retained;
- target exact-zero maximum
  `M0_phys <= 5e-6`, the unchanged Exp069H C1 target threshold.

No comparison support cell may be removed after seeing output.

PASS iff all conditions hold.

## U6 — corrected schema contract: HARD

If U1–U5 pass, the machine-readable audit must explicitly state:

- the old Exp069H key `raw_k_Mpc^-1` was semantically mislabeled because it came from the default `k_hunit=True` accessor;
- the old artifact remains immutable;
- future code must label default/true k output as `raw_k_h_Mpc^-1` (or an equally explicit `h/Mpc` semantic name);
- future **physical support-mask** construction must use an accessor with explicit `k_hunit=False` and label it `raw_k_Mpc^-1`;
- no power correction, floor subtraction or re-normalization is implied by this schema correction.

PASS iff the output carries all of these bindings.

## Forbidden operations

Exp069I may not:

- change q, cosmology, B0, z or target k nodes;
- fit h from the returned grids;
- use nearest-neighbour matching or interpolation in the raw unit tests;
- multiply the powers by any fitted unit correction;
- alter Exp069H historical residuals or thresholds;
- use the corrected unit label to hide a failing U3/U4/U5 result;
- apply the common support mask in this experiment.

## Overall immutable outcomes

If execution is incomplete before all hard metrics exist:

`INCOMPLETE_EXP069I_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1`.

If execution completes and U1–U6 all pass:

`PASS_EXP069H_RAW_K_UNIT_PROVENANCE_BUG_LOCALIZED_V0_1`.

Scientific meaning of PASS:

- the Exp069H raw-grid defect is localized to the k-axis schema/unit label;
- the Exp069H provider PASS remains eligible for downstream use;
- only the **corrected explicit-physical-k schema** becomes eligible for the next prospectively frozen C3+C5 support mask.

If execution completes and any U1–U6 hard condition fails:

`FAIL_EXP069H_RAW_K_UNIT_PROVENANCE_AUDIT_V0_1`.

Scientific meaning of FAIL:

- Exp069H remains a historical PASS under its original frozen checks, but C5 downstream provider eligibility is **suspended**;
- no support mask may be preregistered/applied from C5 until a new corrective provider/provenance experiment is frozen and passed.

## Gate boundary

Even a PASS does not apply or classify the common support mask. It authorizes only the next prospective step:

`certified C3 + certified C5 with corrected physical-k provenance -> preregister common support-validity mask`.

G7/G8/G9 remain OPEN under every Exp069I outcome.
