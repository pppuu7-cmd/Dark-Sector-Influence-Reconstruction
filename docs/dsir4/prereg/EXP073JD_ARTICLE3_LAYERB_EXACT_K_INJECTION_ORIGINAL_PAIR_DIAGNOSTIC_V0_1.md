# Exp073JD — Article 3 Layer-B exact-k injection original-pair diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JC AND BEFORE ANY EXP073JD NUMERICAL OUTPUT.

## Bound authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 107 retained rows, `f_B=0`, exact native production-vs-dense maximum `0.9998247463807295 > 1e-3`; covariance restriction unauthorized. Exp073JC is validated support-only `ORIGINAL_PAIR_REFERENCE_BRACKET_OBSERVED_PLUS_0_PLUS_0`, run/job `34468721378 / 102843338789`, artifact ZIP SHA256 `d6c89ed81e20feb952b4c2d6290e37f66e2a931929b4aa2d5b11fd32a128132d`, durable authority commit `ec39d96c9faebf8a9b2b09114af92c133292a0f3`.

Exp073JC reduced the original 10-vs-20 relative discrepancy only from `0.9998247463807295` to `0.9870472335808126` at the alpha-left probe and from `0.9996789502402558` to `0.7099380201271409` at the beta-symmetric probe. Thus common-bracket transport identifies model-dependent native-grid movement as a real contributor but does not cure the coarse-grid instability.

## Source-level mechanism fact being tested
The exact pinned CLASS-IV source accepts `k_output_values`, copies them into `ppt->k_output_values`, and during perturbation initialization explicitly adds those values into every internal perturbation k list. The transfer output routine evaluates and returns transfer/source functions on `ppt->k`. Therefore an exact requested physical k can in principle be represented as an actual internal perturbation mode and later read through the same patched public gauge-invariant `d_m` transfer column, avoiding post-hoc log-k interpolation between neighboring native modes.

This source-level fact is only an implementation opportunity. It is not scientific authority and does not by itself justify changing the frozen Layer-B estimator.

## Purpose
Determine whether the catastrophic original-pair `k_per_decade_for_pk=10` versus `20` response discrepancy persists when each historical target k is explicitly injected into the internal perturbation k grid and the same public `d_m` transfer value is read directly at that injected k, with no interpolation in k.

This is a mechanism diagnostic only. It distinguishes:
1. output/native-grid interpolation and model-dependent grid motion; from
2. residual finite-difference, time-interpolation, source-integration, or other numerical instability at the same physical k.

## Frozen execution
Use exact pinned CLASS-IV source `ac627d54e9ce196a08878d1ba33999819925d19c`, audited public gauge-invariant `d_m` exposure patch, exact baseline/precision inputs, `h=1e-4`, and the same four models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`.

Historical probes:
- alpha-left: `z=0.7000000000000001`, `k=0.002502504647141259 Mpc^-1`;
- beta-symmetric: `z=0.9351`, `k=0.01860440444314368 Mpc^-1`.

Diagnostic ladder: `k_per_decade_for_pk in {10,20}` only.

For every model and density:
1. Set `k_output_values` to the two exact physical target values above. In pinned CLASS-IV these values are internal `k` values in `Mpc^-1`; the public transfer table reports `k/h` in `h/Mpc`.
2. Compute the same `mTk` transfer/source stack with the exact pinned inputs and patches.
3. Retrieve the public class-format transfer table at each probe redshift.
4. Convert its reported k coordinate back to physical `Mpc^-1` with the model's own `h`.
5. Locate the injected target only by nearest-coordinate identity. Record absolute and relative coordinate mismatch. Infrastructure validity requires relative mismatch `<=1e-12`; this is solely a lookup/provenance criterion and MUST NOT be used as a scientific response tolerance or rescue.
6. Read the public patched `d_m` value at that actual injected grid row directly. No interpolation, smoothing, averaging, extrapolation, effective coordinate, bracket transport, or fiducial-P substitution is allowed.
7. Compute alpha-left one-sided and beta symmetric finite-difference responses with frozen `h=1e-4` exactly as in Exp073IR/JC.
8. Compute exact 10-vs-20 response discrepancy `abs(a-b)/max(abs(a),abs(b))` for finite positive response magnitudes.
9. Record injected index, table size, physical coordinate, coordinate mismatch, raw `d_m`, signed response, absolute response, and provenance.

## Frozen interpretation
Exp073JD MAY establish only whether exact internal-k evaluation materially suppresses the original 10-vs-20 discrepancy at the two historically worst probes.

- If both exact-k discrepancies fall below the historical `REL_TOL=1e-3`, classify this as strong mechanism evidence that native-grid interpolation/evaluation architecture, rather than the physical finite-difference response itself, caused the original Exp073IR failure. This still does NOT retroactively PASS Exp073IR. The next step must be a prospectively preregistered full-row exact-k architecture audit with unchanged physical operator and thresholds before any scientific rerun.
- If either discrepancy remains above `1e-3`, exact-k injection is insufficient and mechanism isolation must continue. No tolerance rescue is permitted.

Exp073JD MUST NOT redefine Exp073IR, authorize covariance restriction, create Wm_S3 authority, or create model/manuscript authority.

## Frozen classifications
- `EXACT_K_ORIGINAL_PAIR_OBSERVED_PLUS_0_PLUS_0`: complete finite exact-k records produced.
- `INVALID_INFRA_PLUS_0_PLUS_0`: source/hash/build/interface/input/exact-k lookup/execution prevents valid observation.

The raw diagnostic may report whether each observed discrepancy is numerically below the historical reference threshold, but classification remains support-only `+0/+0` in all scientifically valid outcomes.

Global frozen DSIR boundaries remain unchanged. In particular `REL_TOL=1e-3` and finite-difference `h=1e-4` are unchanged; exact-threshold ambiguity remains `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue is allowed.
