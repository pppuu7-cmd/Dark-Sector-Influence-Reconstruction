# Exp073JS — Article III fine-4097 cross-model lifecycle isolation v0.1

Date frozen: 2026-09-11. Scope: DSIR Article III process/support only. Effect `+0/+0`.

Status: PROSPECTIVELY FROZEN AFTER JR v0.2 terminal infrastructure-invalid classification, AFTER the pinned source audit, and BEFORE any Exp073JS numerical output.

## Purpose

JR v0.1 proved exact four-live-vs-sequential response equivalence on the 2049-node lattice. JR v0.2 attempted a corresponding 4097-node four-live proof, but every fine model job was externally terminated during the numerical step before a numerical receipt. Repeating the same four-live hosted architecture is therefore not justified.

Pinned-source audit shows the intended CLASS solver state is owned by each `Class` object. It also identifies a file-scope Romberg workspace in the fork, but proves that branch inactive on the frozen DSIR C2 path because the configuration retains default `fluid_equation_of_state=CLP`. Source inspection alone cannot exclude every possible residual cross-model lifecycle effect.

Exp073JS is therefore a dynamic isolation control on the exact fine lattice. It asks whether running the other three frozen finite-difference models sequentially between two fresh executions of a selected model changes the selected model's target vectors by even one bit. It never holds more than one CLASS instance live.

## Frozen identities

- CLASS-IV commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- baseline `configs/dsir4/c2/ide0_reference_v0_1.ini`;
- precision `configs/dsir4/c2/dsir_ide_p8_v0_1.pre`;
- fine guarded lattice: base N=4096, guard `(0,1)`, 4097 requested nodes;
- native `k_per_decade_for_pk=20`;
- capacity `_MAX_NUMBER_OF_K_FILES_=4608`, parser `_ARGUMENT_LENGTH_MAX_=131072` as infrastructure only;
- `h=1e-4`; `REL_TOL=1e-3` lineage metadata only;
- centered-cubic interpolation in `ln(k)` and requested-node lookup ceiling `1e-12` unchanged;
- model order exactly `reference`, `alpha_minus`, `beta_plus`, `beta_minus` with parameters `(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`;
- requests exactly JR A then B:
  - A: `z=float.fromhex('0x1.3851eb851eb85p-1')`, targets `[0.0013,0.0047,0.013,0.041]`;
  - B: `z=float.fromhex('0x1.1c28f5c28f5c3p+0')`, targets `[0.0019,0.0073,0.021,0.057]`;
- OMP/OpenBLAS/MKL/NUMEXPR threads exactly 1.

## One-live per-role protocol

Run four independent hosted jobs, one for each selected model role. In each job:

1. construct selected model as a fresh CLASS instance; evaluate A then B; serialize both target vectors as contiguous `<f8`; destroy/cleanup the instance;
2. in the original global model order with the selected role omitted, construct each of the other three models one at a time, evaluate A then B to exercise the same solver modules and target path, then destroy/cleanup it before constructing the next;
3. construct the selected model again as a completely fresh CLASS instance; evaluate A then B identically; destroy it;
4. compare selected-before vs selected-after exactly.

At no time may more than one CLASS instance be live. The three intervening model outputs are not scientific operands and must not be used in any relation/convergence calculation.

## Per-role PASS

`FINE4097_CROSS_MODEL_LIFECYCLE_ISOLATION_PASS_PLUS_0_PLUS_0` requires for A and B:

- exact lattice identity/count/guard and pinned provenance;
- zero unsupported targets;
- requested-node coordinate mismatch <= `1e-12` for all five instances;
- selected-before and selected-after finite masks exactly equal;
- positive masks exactly equal;
- `np.array_equal(selected_before, selected_after)` true;
- contiguous `<f8` SHA256 equal.

A valid bitwise inequality is `FINE4097_CROSS_MODEL_LIFECYCLE_ISOLATION_FAIL_PLUS_0_PLUS_0`. Any build/runtime/provenance/missing-result failure is `INVALID_INFRA_PLUS_0_PLUS_0`. No tolerance, ULP allowance, averaging, rounding or majority vote is allowed.

## Aggregate and interpretation ceiling

All four roles must produce valid PASS receipts to aggregate `FINE4097_ALL_MODEL_LIFECYCLE_ISOLATION_PASS_PLUS_0_PLUS_0`.

Aggregate PASS does **not** itself declare the sequential response engine equivalent to the unobserved 4097 four-live architecture and does not create Layer-B science authority. It permits only a separate, prospectively frozen **sequential-execution authorization audit** to consider the complete evidence bundle:

1. JR coarse-2049 direct four-live-vs-sequential exact PASS;
2. JQ fine-4097 same-run fresh/history/fresh exact PASS for all roles;
3. pinned source instance-ownership audit with the identified global Romberg branch shown inactive on frozen C2;
4. JS fine-4097 cross-model lifecycle-isolation exact PASS for all roles.

Only that later audit may authorize preregistration of a one-live recovered JL architecture. JS FAIL forbids such authorization pending a different execution architecture. INVALID_INFRA permits only minimal infrastructure repair.

Article III readiness remains 68% and funnel-freeze readiness remains 67% regardless of JS outcome. Covariance restriction remains unauthorized and Wm_S3 unopened.