# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Historical negative/resource/infrastructure outcomes remain immutable.

WW admitted authorities now include:
- `WW_S0_S0` — Exp073EO v0.2 `34005373819 / 101411448176`;
- `WW_S0_S1` — Exp073EZ `34017921734 / 101444964371`;
- `WW_S0_S2` — Exp073FF `34032384956 / 101484177968`;
- **`WW_S0_S3` — Exp073FN `34050154578 / 101532191756`, token `PASS_EXP073FN_WW_S0_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.**

## Exp073FG terminal candidate and admission

Exp073FG science run/job: `34034377795 / 101489679508`, head `4a02952ee3bcb368a088d87608f61243cd9f7056`, artifact `9993520467` (`exp073fg-ww-s0-s3-filebacked-ab-v0-1`). GitHub digest and independently re-downloaded ZIP SHA256 match exactly: `8ddd1e1b81e5fa9c3a4de16c6d72b35353cb42bba04bb77c736aa4998340bde0`.

Raw artifact validation established candidate token `PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate classification `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`; ordered `(S0,S3)` / `[0,3]`; distinct-field semantics; exact A/B selected SHA `db58af980e2997ebbe327ce91dfafb682c38fda1ba841c3d5acba78e429007d3`; canonical `<f8 [39,12288]`, `EE<-EE`, finite, byte-identical and exact-array-equal. Full public BPW SHA is `6a9fe87ab5ae44db5d475686cbc6024174b8c8384433c9d98f48e182557fc942`; workspace FITS SHA `af870ad38f5d74796519f18ab135bf1c0129d888206079606081e3bb7653fc5d`. Both six-stage manifest chains match their post-prune receipts exactly. Both receipts preserve public `get_bandpower_windows()` after `read_unbinned_MCM=True`, regular-file-backed unbinned MCM exactly `19,327,352,832` bytes with `/proc/self/maps` proof, no manual/historical numerical reconstruction, no tolerance rescue, and no cross-replica output read.

Governance correction: `Exp073FL` was already occupied by the earlier `WW_S1_S1` driver-generation static audit. A later S0S3 admission implementation accidentally reused that label. Historical collided run/job `34047839320 / 101525992295` is immutable `INFRASTRUCTURE_LOG_TRANSPORT_FAIL_PLUS_0_PLUS_0`; first causal failure was `gh api .../logs` rejecting terminal escape sequences. It created no authority. The collision is not rewritten.

Prospectively unused label **Exp073FN** superseded only the S0S3 admission implementation while freezing the same candidate evidence and criteria. Prereg blob `3294965fbbccc5e08eb6de7d0ed1556a263a2b6a`, creation commit `aa5230aba107557609e645b8b5a28006f5d275a5`. Exp073FN run/job `34050154578 / 101532191756`, head `84c7505e0b84c00317e73e2045d973ae325a6b9a`, passed raw hosted verification and emitted `PASS_EXP073FN_WW_S0_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s0_s3_authority_created=true`. The only transport repair was `gh api --allow-escape-sequences`; frozen science and candidate evidence were unchanged.

Immutable recovery note: `docs/recovery/RECOVERY_2026-09-06_EXP073FN_ADMITTED_S0S3_FO_QUEUED.md`.

## Current science frontier — WW_S1_S1 / Exp073FM

Exp073FM science prereg creation commit: `391af1d14ca61f20ef42cccde348453ca84a1aaa`.

Frozen target: `[1,1]`, authoritative S1 reconstructed exactly once per replica; exactly one spin-2 `NmtField`; exact same Python field object passed on both sides (`fb=fa` semantics); equal-but-distinct second field forbidden; DES NSIDE=4096; ell `0..12287`; 39 bands; public file-backed NaMaster/PyMaster route; full BPW `[4,39,4,12288]`; selected `EE<-EE`, canonical `<f8 [39,12288]`; exact A/B SHA plus `numpy.array_equal`; all finite; no tolerance/allclose/rounding/smoothing/averaging/manual reconstruction/effective-coordinate/fiducial rescue. Candidate token: `PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate alone creates no authority.

Existing hosted support remains preserved: Exp073FH same-field architecture, Exp073FJ semantic matrix, Exp073FK same-field transformation contract, and Exp073FL S1S1 driver-generation static audit. These are support `+0/+0` only.

### Current authoritative process — Exp073FO

Exp073FO hosted-only production-transformation readiness prereg: blob `8bbe6e45b10295c245f588a4bc65713acb1a1d2e`, creation commit `90c3648d625a64c94e01fd3046fc0e683cfb5f69`.

Live process at latest reconciliation:
- workflow/run **`34050224161`**;
- job **`101532385479`**;
- head **`0f9d5d6039b129390e780c805ae6043884135459`**;
- state **QUEUED**;
- expected token `PASS_EXP073FO_WW_S1_S1_PRODUCTION_TRANSFORMATION_READINESS_V0_1`;
- classification on PASS `SUPPORT_PLUS_0_PLUS_0`;
- `ww_s1_s1_authority_created=false`;
- `self_hosted_science_started=false`.

`DSIR-HOME-PC` is currently free. Do not launch Exp073FM home science until an exact S1S1 production driver, hardened terminal comparator/prune path and dedicated fail-closed home envelope are committed and separately hosted-audited. On Exp073FO PASS, that implementation/audit is the exact next permitted work. On Exp073FO FAIL, diagnose the first causal static/infrastructure defect and make the smallest prospective repair without changing frozen S1S1 science.

## Frozen global boundaries

Unless prospectively superseded: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
