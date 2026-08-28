# DSIR recovery/checkpoint — 2026-08-28

## Scope

This checkpoint records two independent facts without changing any frozen acceptance criterion and without advancing G7 out of order.

## Exp071L — authoritative negative scientific result

Authoritative summary commit: `0629182befec8671ee0d9261aa860c77908986bd`.
Preregistration commit: `9927f46caefbcd991b2c2e7691f4923c6f7552f6`.
Run: `33184079909`.
Artifact SHA256: `6ec9cc4dfa7a94ecec8e4540cbecf034b19bfdc7b0c85b30ac92331b205f71d4`.

Fresh-reference integrity passed exactly (`max_abs_relative_P_difference = 0`, `max_abs_relative_ttot_difference = 0`, threshold `1e-10`). Therefore the outcome is not an infrastructure failure.

Frozen separator: 45 deg.

Primary angles:
- K2+ vs GDM cs2: 166.43869440595827 deg
- K2+ vs GDM cv2: 164.92709673022526 deg
- K2- vs GDM cs2: 13.550260274305414 deg
- K2- vs GDM cv2: 15.070884431347679 deg

Minimum primary angle: 13.550260274305414 deg < 45 deg, hence `primary_pass = false`.

Scientific interpretation boundary: the strong oriented positive-K2 separation established by Exp071I/J/K does **not** establish specificity against a physically two-sided K2 nuisance line. The negative K2 displacement overlaps both positive GDM axes well below the preregistered separator. This negative result is preserved as an authoritative scientific falsification of the stronger interpretation; it must not be relabelled as infrastructure failure or removed by retrospective criterion changes.

## Exp073R1 v0.5 — live canonical G7 prerequisite

Canonical run: `33175886694` (`Exp073R1 DESY1 sequential whole-stream reconstruction v0.5`).
Head SHA: `2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c`.

Current checked state:
- `source-index`: completed / success.
- Stage-A authoritative source-object stream and exact row-aligned zbin index: PASS.
- Stage-A frozen no-Range identity contract: PASS.
- `metacal-map`: in progress.
- Active step: sequentially stream authoritative metacal object and execute frozen mapper.
- True Exp073R1 reproduction PASS assertion: not yet reached.

No duplicate heavy run is admissible while this canonical run is live.

## Gate discipline

G7 remains blocked until a genuine canonical Exp073R1 reproduction PASS exists. Required order remains:

1. validated physical forward/power-input bridges;
2. preregistered physical support-validity mask (Exp073P);
3. covariance restriction / whitening;
4. nuisance tangent rank / SVD;
5. quotient / relation / null control;
6. only then a fresh G8 withheld family.

Exp071L is an independent theory-space nuisance falsification and does not authorize skipping any G7 prerequisite.
