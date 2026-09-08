# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HS_PASS_HT_RAW_RUNTIME_FRONT_V39.md` (creation commit `4b6742b7b9d42fa3965c9bff77d58ca64c34a99d`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

All prior scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW authority through scientifically admitted `S3_S3` remains preserved; `WW_S3_S3` authority is run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

C2 remains `raw_record_set_admitted=false`, `decoded=false`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Newly validated support result — Exp073HS

Exp073HS `34230896860 / 102076459069` is terminal `SUCCESS`. The raw job log was inspected and contains exact frozen token `PASS_EXP073HS_C2_FINAL_APPROXIMATION_INTERVAL_ENDPOINT_GUARD_BUILD_AUDIT_V0_1`. Classification is strictly `SUPPORT_PLUS_0_PLUS_0`. HS is a build/static implementation gate only and creates no runtime payload or scientific/model authority.

The earlier HR/HO failures remain historical implementation/runtime `+0/+0` results and are not rewritten.

## Current C2 frontier — Exp073HT raw reference runtime v0.3

A reconciled parallel DSIR process prospectively froze `docs/dsir4/prereg/EXP073HT_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_3.md` in commit `7c745691c6a6370f120fe7c65ccdf30c072d8b9d`. This frozen gate was materialized without creating a competing DSIR control plane:

- workflow implementation commit `b75d7aa497beae88eaef3e8a353dc66c2249129e`;
- workflow blob `9d99107f0dc309e5c05810085d92c5149531e0c0`;
- runtime binding/head commit `bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`;
- run `34235038323`;
- job `102090438079`;
- branch/head `main / bc51e53188ee4fd8f0c507e2be9e5b4fc47640ba`;
- GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner **none**;
- state at pointer update: **IN_PROGRESS**, runtime execution step;
- frozen binding verification and exact post-HS solver/serializer build already passed.

The HT gate keeps pinned solver `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, reference `(alpha,beta)=(0,0)`, unchanged 28 z/k nodes in frozen z-major/k-minor order, exact native endpoint observation, one 64-byte packet per request and exact aggregate size 1792 bytes. Interpolation/tolerance/nearest-coordinate/effective-coordinate rescue is forbidden.

Frozen post-HS source/config identities: `perturbations.c sha256=483b481b48e50a6afb396b15b85258ac6c5a7a39b38fb1c6192e7e4a95c139ae`; `evolver_ndf15.c sha256=3f12121ce2de319453e1ff5fadae9391fd96747731c0df3fa05fae1cd2608aa9`; baseline `sha256=0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`; precision `sha256=463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`.

## Exact next transition

Workflow SUCCESS alone is insufficient. On terminal HT, consume raw job log and artifact in the same iteration; verify GitHub digest, provenance/receipt run-job-head binding, source/config fingerprints, exactly 28 distinct ordered packets, exact 64-byte packet size, exact 1792-byte aggregate and aggregate SHA256. Only after all frozen checks may `PASS_EXP073HT_C2_REFERENCE_RAW_RUNTIME_PRODUCER_V0_3` be classified as `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`.

Even a validated HT candidate remains non-admitted and may not be decoded/mapped/interpreted. It can only authorize a separately prospectively frozen admission/receipt gate. On HT failure, diagnose only the first causal implementation/runtime/provenance defect and repair prospectively without altering scientific equations, arithmetic, model, grid, tolerances, ABI or provenance.

Global frozen DSIR science boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
