# DSIR-4 C2 IDE runtime sampling and provenance contract v0.1

Date: 2026-09-07

Scope: `C2_IDE_LOCAL_TANGENT_CONE` only.

Status: **PROSPECTIVELY FROZEN / SUPPORT-ONLY / +0/+0**.

This contract is frozen before any C2 cosmological extraction using the admitted diagnostic hook/recorder path. It does not set `prediction_ready=true`, does not admit C2 through `G_DOMAIN_MAPPING`, and cannot create a scientific PASS/FAIL by itself.

## Authority chain

The following upstream identities remain immutable for this contract:

- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- C2 common-coordinate interface: `docs/dsir4/mappings/C2_IDE_DELTAM_EXTRACTION_CONTRACT_V0_1.md`;
- reference point: `(alpha,beta)=(0,0)`;
- alpha tangent: one-sided `alpha=-h`, `h={1e-4,1e-3,1e-2}`, derivative base step `1e-4`;
- beta tangent: symmetric `beta=+/-h`, `h={1e-4,1e-3,1e-2}`, central derivative base step `1e-4`;
- physical branch: `rho_idm>0` and `rho_iv>=0` over the required history;
- precision preset: recovered `dsir_ide_p8.pre`, unchanged;
- Exp073GP recorder ABI audit: run `34114027439`, job `101716542107`, support PASS;
- Exp073GQ hook-to-recorder adapter audit: run `34114126843`, job `101716863503`, support PASS.

No downstream gate result may be used to alter these identities.

## Frozen sampling domain

Use the already-frozen DSIR-4 domain and inherited admissible grid only:

- redshift nodes, ascending order: `[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`;
- physical `k` nodes in `Mpc^-1`, ascending order: `[0.00067, 0.00201, 0.0067, 0.0201]`;
- common bound: `0 < k <= 0.06664762008318016 Mpc^-1`;
- linear regime only;
- no quasi-static or sub-horizon shortcut.

The recovered `0.067 Mpc^-1` node is outside the frozen upper bound and remains excluded. It must not be rounded down, tolerance-admitted, substituted, or replaced after observing results.

## Deterministic coordinate ordering

Canonical coordinate order is:

1. model-point block in the prospectively frozen tangent order below;
2. within each model point, redshift ascending in the exact node order above;
3. within each redshift, physical `k` ascending in the exact node order above.

Frozen model-point order:

1. C0/reference `(alpha,beta)=(0,0)`;
2. alpha `h=1e-4`: `(alpha,beta)=(-1e-4,0)`;
3. alpha `h=1e-3`: `(alpha,beta)=(-1e-3,0)`;
4. alpha `h=1e-2`: `(alpha,beta)=(-1e-2,0)`;
5. beta minus `h=1e-4`: `(0,-1e-4)`;
6. beta plus `h=1e-4`: `(0,+1e-4)`;
7. beta minus `h=1e-3`: `(0,-1e-3)`;
8. beta plus `h=1e-3`: `(0,+1e-3)`;
9. beta minus `h=1e-2`: `(0,-1e-2)`;
10. beta plus `h=1e-2`: `(0,+1e-2)`.

This ordering is serialization authority only; it does not modify the already-frozen tangent definitions.

## Runtime extraction rule

The admitted observation-only diagnostic path may only copy already-computed source quantities needed by the frozen `Delta_m` interface. It must not:

- alter solver state;
- alter the integration path, step size, precision, tolerances, source equations, species sums, gauge evolution, or branching;
- write values back into CLASS perturbation/background structures;
- add a second cosmological integration to obtain a missing field;
- interpolate, smooth, average, extrapolate, clamp, rescue, or replace non-finite/missing values;
- derive C2 source values from historical `mPk` payloads.

A coordinate that cannot be emitted exactly under the frozen source path is recorded as unavailable/invalid-for-artifact and is not silently repaired.

## Required record and provenance

For each admitted record, the canonical payload must bind at minimum:

- schema name/version;
- exact solver repository and commit;
- DSIR repository head SHA used to build the extractor;
- exact source-file SHA256 for the pinned perturbation source;
- exact diagnostic-hook/adapter implementation identity;
- exact recorder ABI/schema identity;
- exact baseline input and `dsir_ide_p8.pre` identities/hashes;
- model point `(alpha,beta)` and tangent label;
- `z`, physical `k [Mpc^-1]`, and deterministic coordinate index;
- raw source fields required by the frozen `Delta_m` construction, with explicit sign/unit declarations;
- reconstructed `Delta_m` and matched C0/reference linkage;
- `rho_idm>0` and `rho_iv>=0` branch diagnostics;
- finite/non-finite status without coercion;
- canonical record hash and final payload SHA256.

If any mandatory provenance field is absent or cannot be reproduced from immutable inputs, the artifact is **INVALID_FOR_SCIENCE** or remains **NOT_YET_TESTABLE** according to the admission layer; it is not a scientific model FAIL.

## No interpolation / no post-hoc coordinate recovery

Only exact requested frozen `(z,k)` coordinates are admissible under this version. No interpolation, nearest-node substitution, smoothing, averaging, extrapolation, or post-hoc grid densification is permitted.

If the pinned solver/extractor cannot provide an exact requested node under the frozen interface, that node is unavailable. A future interpolation or alternate-grid method would require a new prospectively frozen contract version before seeing the corresponding scientific outcome.

## Canonical payload requirements

Serialization must be deterministic and machine-readable with:

- stable field order or canonical-key serialization;
- stable record ordering defined above;
- finite numeric representation policy fixed before execution;
- explicit excluded/unavailable status records where required;
- no NaN-to-zero, missing-to-zero, or sign repair;
- one SHA256 over the complete canonical payload;
- human-readable summary generated from that payload, not edited independently.

Repeated serialization of byte-identical logical input must reproduce the same payload SHA256.

## Admission sequence

The next C2 steps are strictly ordered:

1. hosted/static audit of this runtime sampling/provenance implementation;
2. only after that PASS, one authorized runtime extraction using the pinned solver and frozen model/grid order;
3. deterministic payload/hash verification;
4. provenance/branch/domain admission;
5. only then may `prediction_ready` be reconsidered and Gate-1 scientific interpretation occur.

A support/static PASS is `+0/+0`. A runtime/infrastructure failure before admitted terminal prediction is also `+0/+0`. `INVALID_FOR_SCIENCE`, `NOT_YET_TESTABLE`, and `OUTSIDE_DOMAIN` are not scientific FAIL.

## Heavy-run concurrency guard

At freeze time, heavy authority remains Exp073FU run `34103803637` (`WW_S1_S3`), with a self-hosted science job still active. No C2 cosmological extraction heavy-run is authorized while that heavy-run remains active. Hosted/static implementation audits may proceed only if they do not start another self-hosted heavy computation.

## Current scientific status

- C2 residual/source mapping: `mapping_ready=true`;
- diagnostic source site: validated support-only;
- recorder ABI and hook-to-recorder transfer: validated support-only;
- runtime sampling/provenance contract: frozen here;
- cosmological deterministic prediction payload: absent;
- `prediction_ready=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`;
- scientific contribution of this contract: `+0/+0`.
