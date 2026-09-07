# DSIR-4 C2 IDE common `Delta_m` extraction contract v0.1

Date: 2026-09-07

Scope: `C2_IDE_LOCAL_TANGENT_CONE` only.

Status: **FROZEN INTERFACE / IMPLEMENTATION NOT YET VALIDATED / +0/+0**.

This contract is a prospective, fail-closed interface definition. It does not create `prediction_ready=true`, does not admit C2 through `G_DOMAIN_MAPPING`, and does not create a scientific PASS/FAIL.

## Purpose

The recovered legacy IDE artifact is authoritative for the frozen tangent-cone parameterization, baseline cosmology, solver lineage, precision preset and physical branch, but its stored perturbation response is based on CLASS `mPk`. It must not be relabelled as the current common gauge-aware DSIR response.

The required common matter coordinate is

`Delta_m = delta_m + 3 (1+w_m) Hconf theta_m/k^2`,

with `Hconf=aH`, using the already-frozen DSIR G1/G2 convention. C2 must therefore generate the quantities required to reconstruct this coordinate from the same pinned `class_iv` solver lineage.

## Frozen solver and tangent provenance

No element below may be changed to improve downstream agreement:

- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- validated legacy source artifact: workflow run `32760042765`, job `97536488223`, artifact id `9532491954`;
- artifact digest: `sha256:408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`;
- reference point: `(alpha,beta)=(0,0)`;
- alpha tangent: one-sided `alpha=-h`, `h={1e-4,1e-3,1e-2}`, derivative base step `1e-4`;
- beta tangent: symmetric `beta=+/-h`, `h={1e-4,1e-3,1e-2}`, central derivative base step `1e-4`;
- physical branch mask: `rho_idm>0` and `rho_iv>=0` over the required history;
- precision preset: recovered `dsir_ide_p8.pre`, unchanged.

## Gauge/frame rule

The pinned IDE implementation is consumed in its supported synchronous-gauge perturbation frame. No unsupported Newtonian-gauge IDE execution may be introduced as a convenience bridge.

Gauge dependence is removed at the common-coordinate construction level by forming the already-frozen total-matter comoving response `Delta_m`; raw synchronous `delta`, raw velocity variables, or raw `mPk` are not interchangeable with that coordinate.

If the pinned implementation cannot expose a complete, auditable set of source variables sufficient to construct the frozen `Delta_m` coordinate with the G1/G2 sign and normalization conventions, the result is **NOT_YET_TESTABLE**, not a scientific FAIL and not grounds for a proxy substitution.

## Required per-coordinate raw payload

For every admitted `(model point, z, k)` coordinate, the immutable prediction payload must contain enough same-solver information to reconstruct and audit:

1. `z` and physical `k` in `Mpc^-1`;
2. the total-matter density perturbation entering the frozen DSIR `delta_m` definition;
3. the total-matter velocity-divergence/momentum quantity entering the frozen DSIR `theta_m` definition, including an explicit sign and normalization declaration;
4. `w_m=p_m/rho_m` for the same total-matter partition, or the source quantities from which it is deterministically reconstructed;
5. `Hconf=aH` in units consistent with `k`;
6. reconstructed `Delta_m`;
7. the matched C0/reference `Delta_m` generated with the same solver lineage and numerical settings;
8. the final same-solver response derived from the matched model/reference prediction;
9. physical-branch diagnostics proving `rho_idm>0` and `rho_iv>=0` over the required history;
10. solver commit, exact input files/settings, generator commit, serialization schema/version and payload SHA256.

No item may be silently inferred from a downstream observable or copied from the historical `mPk` response.

## Matter partition rule

The `delta_m`, `theta_m`, `rho_m` and `p_m` entering `Delta_m` must use one explicitly documented total-matter partition consistently for C2 and its C0 matched reference. The interacting dark pair must not be selectively omitted merely because its internal transfer cancels in total conservation.

Any change of matter partition is a new interface version and cannot be introduced after observing downstream gate outcomes.

## Output domain

Frozen DSIR-4 common domain:

- `0.295 <= z <= 2.33`;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- linear regime;
- no quasi-static/sub-horizon shortcut.

Recovered redshift nodes remain:

`[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`.

Recovered legacy k nodes convert at `h=0.67` to

`[0.00067, 0.00201, 0.0067, 0.0201, 0.067] Mpc^-1`.

The final `0.067 Mpc^-1` node is outside the frozen DSIR-4 upper bound and is excluded. It must not be rounded down, tolerance-admitted, or replaced post hoc. This contract freezes the admissible inherited extraction grid to the first four recovered physical-k nodes only:

`[0.00067, 0.00201, 0.0067, 0.0201] Mpc^-1`.

Introducing any additional k coordinate requires a prospectively versioned grid contract before its prediction is generated; it cannot be chosen after viewing scientific gate results.

## Matched-reference rule

Each C2 prediction must be paired with a C0 zero-interaction prediction generated from the same pinned solver checkout, baseline cosmology, precision file and extraction code. The only intended theory differences are the prospectively frozen C2 interaction parameter point and quantities causally implied by it.

A legacy reference spectrum or a cross-solver reference cannot silently replace this matched reference.

## Deterministic serialization

The prediction generator must emit a canonical machine-readable payload with:

- stable coordinate ordering;
- finite numeric values only for admitted coordinates;
- explicit masks/statuses for excluded coordinates;
- no NaN-to-zero or missing-to-zero coercion;
- exact provenance fields listed above;
- SHA256 over the canonical serialized payload;
- a compact human-readable audit summary derived from, not independently edited from, the same payload.

## Fail-closed implementation gate

Before `prediction_ready=true`, a hosted/static audit must verify all of the following:

- exact pinned solver identity;
- exact frozen alpha/beta tangent definitions;
- exact baseline and precision settings;
- supported synchronous source extraction only;
- explicit source-to-`Delta_m` variable mapping with units/signs;
- matched C0/C2 extraction path;
- physical branch mask;
- exact admitted z/k grid;
- deterministic serialization and reproducible payload SHA256;
- no use of historical `mPk` arrays as a substitute for the common `Delta_m` response.

Failure to supply required source variables or provenance leaves `prediction_ready=false` and `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`. A malformed artifact is invalid for science. Neither case is a scientific C2 rejection.

## Current state

- `mapping_ready = true`;
- tangent/baseline/precision provenance = recovered;
- common `Delta_m` extraction interface = frozen here;
- extraction implementation = not yet source-validated;
- deterministic prediction artifact = absent;
- `prediction_ready = false`;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- scientific contribution = `+0/+0`.

No downstream WW result or observational gate was used to choose this interface.