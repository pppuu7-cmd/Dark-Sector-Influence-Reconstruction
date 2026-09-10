# Exp073JC — Article 3 Layer-B reference-bracket original-pair diagnostic v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JB AND BEFORE ANY EXP073JC NUMERICAL OUTPUT.

## Bound authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 107 retained rows, `f_B=0`, exact native production-vs-dense maximum `0.9998247463807295 > 1e-3`; covariance restriction unauthorized. Exp073JB is validated support-only `COMMON_BRACKET_TRANSPORT_OBSERVED_PLUS_0_PLUS_0`, run/job `34463544046 / 102826719366`, artifact ZIP SHA256 `974e08c04c82c052d216a0de95a19cc0345f8845735769dc725955629cc8f991`. At the historical beta probe, common-reference-bracket adjacent-density change fell to `0.0029800645293267063` for `320->640`, versus native `0.42559958697775674`.

## Purpose
Test whether the same reference-physical-bracket transport materially suppresses the discrepancy on the **original frozen Exp073IR production/dense pair** `k_per_decade_for_pk=10` versus `20`, before any attempt to justify a new numerical evaluation architecture. This remains a mechanism diagnostic only.

## Frozen execution
Use exact pinned CLASS-IV source `ac627d54e9ce196a08878d1ba33999819925d19c`, audited public gauge-invariant `d_m` exposure patch, exact baseline/precision inputs, `h=1e-4`, and the same historical probes:
- alpha-left: `z=0.7000000000000001`, `k=0.002502504647141259 Mpc^-1`;
- beta-symmetric: `z=0.9351`, `k=0.01860440444314368 Mpc^-1`.

Diagnostic ladder: `k_per_decade_for_pk in {10,20}` only.
For each density and probe compute the same four models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`.

For each probe/density:
1. Record ordinary model-native fixed-target interpolation exactly as Exp073JB.
2. Use the reference `(0,0)` model physical native bracket `[k_lo_ref,k_hi_ref]` and exact log-k target fraction.
3. Transport every perturbed model to those two physical coordinates by the same log-k interpolation on its own native table, then interpolate between transported endpoints using the exact reference fraction.
4. Compute the same alpha-left one-sided and beta symmetric finite-difference responses with `h=1e-4` for native and common-bracket values.
5. Compute exact 10-vs-20 relative discrepancy `abs(a-b)/max(abs(a),abs(b))` for finite positive response magnitudes for both native and common-bracket sequences.
6. Record all brackets, endpoint values, response signs, and transport provenance.

## Frozen interpretation
This experiment MAY establish only whether reference-bracket transport suppresses the original-pair numerical discrepancy at the two historically worst probes. It MUST NOT redefine Exp073IR, replace its estimator, authorize covariance restriction, or create scientific/model/manuscript authority.

No averaging, smoothing, extrapolation, tolerance adjustment, effective coordinate, fiducial-P substitution, or threshold rescue is allowed. `REL_TOL=1e-3` remains the historical scientific threshold and is recorded only as a reference; Exp073JC does not itself PASS the Layer-B scientific gate.

## Frozen classifications
- `ORIGINAL_PAIR_REFERENCE_BRACKET_OBSERVED_PLUS_0_PLUS_0`: complete finite records produced.
- `INVALID_INFRA_PLUS_0_PLUS_0`: source/hash/build/interface/input/execution prevents valid observation.

Exact next action after consumption: if common-bracket transport strongly suppresses the original 10-vs-20 discrepancy, prospectively design a full-row grid-invariant evaluation architecture audit before any scientific rerun. If not, continue mechanism isolation. Historical Exp073IR remains unchanged in either case.
