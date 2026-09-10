# Exp073JO — full-traversal topology amendment v0.1

Date frozen: 2026-09-10. Scope: DSIR Article III / Exp073JO process recovery only.

Status: PROSPECTIVELY FROZEN BEFORE ANY VALID EXP073JL NUMERICAL RESULT AND BEFORE EXP073JO HEAVY RECOVERY IS ACTIVATED.

This amendment adds a fail-closed completion guard to the already frozen Exp073JO response-call checkpoint architecture. It does not change any scientific arithmetic, target geometry, atom inclusion, response, interpolation, finite-difference step, tolerance, row rule, physical domain, or result classification.

## Authority basis
The independently verified Exp073JK artifact from run/job `34495159732 / 102931623100`, artifact `10160083225`, ZIP SHA256 `a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99`, executed the exact same Exp073IR traversal/support structure used by JL. Only the common k-grid density differs; response-call topology is determined by the frozen DES/BOSS traversal and masks, not by the number of injected common k nodes.

Its raw `response_engine_audit` establishes the complete traversal counts:
- inherited suite slot 10: exactly `441` complete `response(z,targets)` calls, `83666` target evaluations, zero unsupported target evaluations;
- inherited suite slot 20: exactly `569` complete calls, `121682` target evaluations, zero unsupported target evaluations.

The difference in call count is expected from the frozen Exp073IR lifecycle: slot 10 executes DES plus BOSS GL64, while slot 20 executes DES plus BOSS GL64 plus the additional BOSS GL128 dense-z control.

## Added process completion guard
A recovered Exp073JL result is process-admissible through Exp073JO only if the JO wrapper reports exactly:
- slot 10 completed call count = `441`;
- slot 20 completed call count = `569`.

Any other terminal call count is `INVALID_INFRA_PLUS_0_PLUS_0` regardless of whether an output JSON exists. It cannot create a JL authority and activates neither JN nor JM.

The target-evaluation totals `83666` and `121682` are retained as independent topology expectations and SHOULD be checked against the final ordinary JL `response_engine_audit`. Because JL changes only the guarded common k lattices and preserves the target traversal, these totals must remain identical. Unsupported target evaluations must remain zero under the already-frozen JL gate.

## Checkpoint prefix implication
Durable checkpoint storage may contain only prefixes of these full per-slot call sequences. Therefore valid indices are:
- slot 10: `0..440`;
- slot 20: `0..568`.

A checkpoint entry beyond those limits, a gap, or any final prefix shorter/longer than the complete topology is infrastructure-invalid. No scientific inference may be made from a partial prefix.

All original Exp073JO and Exp073JL anti-rescue rules remain unchanged, including `REL_TOL=1e-3`, `h=1e-4`, exact masks/support, no denominator floor, no atom/row removal, and no covariance/Wm_S3 authorization from support-only work.
