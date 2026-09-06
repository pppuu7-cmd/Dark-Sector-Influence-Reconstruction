# DSIR recovery — Exp073FN admitted WW_S0_S3; Exp073FO queued

Date: 2026-09-06. Scope: DSIR only.

## Exp073FG terminal consumption

Authoritative candidate run/job: `34034377795 / 101489679508`, head `4a02952ee3bcb368a088d87608f61243cd9f7056`.
Artifact: `9993520467`, name `exp073fg-ww-s0-s3-filebacked-ab-v0-1`, GitHub digest `sha256:8ddd1e1b81e5fa9c3a4de16c6d72b35353cb42bba04bb77c736aa4998340bde0`.
Independent ZIP SHA256 re-download matched exactly: `8ddd1e1b81e5fa9c3a4de16c6d72b35353cb42bba04bb77c736aa4998340bde0`.

Raw artifact verification established:
- terminal token `PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- classification `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`;
- source pair `S0->S3`, ordered indices `[0,3]`, distinct fields;
- exact canonical selected A/B SHA `db58af980e2997ebbe327ce91dfafb682c38fda1ba841c3d5acba78e429007d3`;
- selected arrays `<f8 [39,12288]`, finite, byte-equal and exact `numpy.array_equal`;
- full public BPW SHA `6a9fe87ab5ae44db5d475686cbc6024174b8c8384433c9d98f48e182557fc942`;
- workspace FITS SHA `af870ad38f5d74796519f18ab135bf1c0129d888206079606081e3bb7653fc5d`;
- both six-stage manifest SHA chains exactly match post-prune receipts;
- both receipts show public `get_bandpower_windows()` after `read_unbinned_MCM=True`, regular-file-backed MCM `19327352832` bytes, `/proc/self/maps` proof, no historical/manual numerical reconstruction, no tolerance rescue, no cross-replica output read.

## Governance collision and repair

`Exp073FL` was already occupied by the earlier `WW_S1_S1` driver-generation static audit. A later S0S3 admission prereg/workflow accidentally reused the label. Historical collided run `34047839320 / 101525992295` failed before admission because `gh api .../logs` refused terminal escape sequences. Classification: `INFRASTRUCTURE_LOG_TRANSPORT_FAIL_PLUS_0_PLUS_0`; no authority created.

The collision is not rewritten. A new unused label `Exp073FN` prospectively superseded that S0S3 admission implementation while freezing the same candidate evidence and scientific criteria. Prereg blob: `3294965fbbccc5e08eb6de7d0ed1556a263a2b6a`, creation commit `aa5230aba107557609e645b8b5a28006f5d275a5`.

Exp073FN run/job `34050154578 / 101532191756`, head `84c7505e0b84c00317e73e2045d973ae325a6b9a`, completed SUCCESS. Raw log contains exact token `PASS_EXP073FN_WW_S0_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `ww_s0_s3_authority_created=true`. The log-transport defect was repaired only with `gh api --allow-escape-sequences`; candidate evidence and frozen science were unchanged.

Therefore `WW_S0_S3` is now admitted scientific authority.

## Next frontier — WW_S1_S1 / Exp073FM

Heavy science prereg already exists at commit `391af1d14ca61f20ef42cccde348453ca84a1aaa`. Frozen semantics: authoritative S1 index `[1,1]`, reconstruct S1 exactly once per replica, construct exactly one spin-2 field, pass the same Python field object on both sides, canonical `EE<-EE` `<f8 [39,12288]`, exact A/B SHA and `numpy.array_equal`, no tolerance/rescue, hardened durable checkpoint/prune semantics.

Before home science, Exp073FO hosted-only transformation-readiness gate was preregistered at commit `90c3648d625a64c94e01fd3046fc0e683cfb5f69`, blob `8bbe6e45b10295c245f588a4bc65713acb1a1d2e`, and dispatched as run `34050224161`, job `101532385479`, head `0f9d5d6039b129390e780c805ae6043884135459`. At this recovery write it is QUEUED. It creates no authority and starts no self-hosted science.

DSIR-HOME-PC is currently free. Do not launch Exp073FM home science until production driver and fail-closed home envelope are committed and separately audited under FM/FH/FJ/FK/FL/FO boundaries.
