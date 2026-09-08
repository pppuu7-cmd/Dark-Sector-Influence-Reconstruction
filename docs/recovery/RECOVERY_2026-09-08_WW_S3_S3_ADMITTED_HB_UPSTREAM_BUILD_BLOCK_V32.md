# DSIR authoritative recovery — V32 — 2026-09-08

Scope: DSIR only. Earlier recovery notes remain immutable history.

## Preserved scientific authority

WW admitted authority includes `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`, `S2_S2`, `S2_S3`, and `S3_S3`.

`WW_S3_S3 = SCIENTIFIC_AUTHORITY_ADMITTED` from hosted recovery/admission run `34218457380`, job `102035691774 SUCCESS`, head `4e5514b6077e1d70537586b43c9b5ca0e51abcf2`, consuming GA artifact `10051382493` with digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. Historical GA comparator failures remain implementation/provenance `+0/+0`, not scientific FAIL.

## Current gate: Exp073HB

Frozen prereg: `docs/dsir4/prereg/EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1.md`, blob `fc5f08889f84e628cb789070abd9179a74ef7e04`.

Implementation chain:

- `09908cdea139deee26f79ec2b6b56a093250dfe9` — deterministic HB producer patcher;
- `c2602fb42a289292cdc37394058a6fbcbc5c9042` — pin patcher to upstream Git-blob guards;
- `38e25e208ea730399f293b6c1930c34de6cc7aee` — hosted HB build/static workflow;
- `1df037bdb071f9b5c1cfa3e11f8978c88754b552` — install hosted GSL dependency.

Run `34223854538`, job `102053091684`, passed identity checks, deterministic patch application, static endpoint semantics (`PASS_EXP073HB_STATIC_SEMANTICS_V0_1`) and dependency install, then failed in full solver compilation inside unchanged pinned upstream `source/background.c` with structural C parse errors (`case label not within a switch statement`, etc.).

Classification: `BLOCKED/IMPLEMENTATION_PLUS_0_PLUS_0`; scientific FAIL contribution `0`.

No automatic repair of `background.c`, upstream commit, or HB build-success criterion is authorized: any such change would modify the pinned solver/provenance or weaken the frozen prereg. No cosmological run or runtime record payload was produced.

Research log: `docs/research_log/RESEARCH_LOG_2026-09-08_EXP073HB_PINNED_UPSTREAM_BUILD_BLOCK.md`, creation commit `5a2c22f5ef50b6d93f4336b0c8330102cfccf5df`.

## Current process status

No self-hosted heavy owner should be started for C2 while HB is not raw-log PASS. Real 28-packet / 1792-byte C2 extraction remains NOT YET AUTHORIZED. `prediction_ready=false`; C2 `scientific_model_authority_created=false`; `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Next permitted action is to resolve the pinned-upstream baseline/full-build blocker only through an explicit prospective authority that preserves solver scientific semantics and then rerun the hosted-only HB audit. Do not reinterpret the build blocker as scientific evidence.

## Frozen boundaries preserved

`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
