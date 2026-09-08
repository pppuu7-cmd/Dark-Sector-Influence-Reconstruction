# DSIR recovery V27 — GA ledger synchronization

Date: 2026-09-08. Scope: **DSIR only**. Earlier recovery notes remain immutable.

## Scientific authority

No scientific authority changed in this governance-only iteration. `WW_S2_S3 = SCIENTIFIC_AUTHORITY_ADMITTED` remains preserved from V26. `WW_S3_S3` remains `NOT_YET_ADMITTED` while the frozen final heavy gate runs.

## Live authoritative process

Live GitHub reconciliation confirms exactly one in-progress workflow and zero queued workflows: Exp073GA `WW_S3_S3`, run `34189540992`, head `10e6fb67af7d6485fca3d1ecf2362e4622883417`. Hosted launch audit job `101944582891` is SUCCESS. Self-hosted home-science job `101944608861` is IN_PROGRESS at `Run frozen WW_S3_S3 A/B gate with durable checkpoints`.

Checkpoint root is `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`; artifact name is `exp073ga-ww-s3-s3-filebacked-ab-v0-1`. Exact candidate token remains `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Only frozen GB verifier output `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` together with `classification=SCIENTIFIC_AUTHORITY_ADMITTED` and `ww_s3_s3_authority_created=true` may create final authority.

## Governance repair

`docs/CURRENT_PROCESS.md` had remained stale at V25/HD despite V26 repository authority and active GA. It was synchronized in commit `8e168bd9bb1f2a3177d493197e610aaaaaae1b52`. This repair changes no scientific code, arithmetic, source order, domain, thresholds, tolerances, checkpoint semantics, or acceptance criteria.

No partial GA numerical output was inspected. No competing home-heavy workflow was launched.

## Next allowed transition

Consume GA only after terminal evidence exists. Verify raw home log, artifact digest, provenance/contract/checkpoint identity, full A+B chains, exact same-field `S3->S3/[3,3]`, exact file-backed proof, finiteness and exact byte/array equality. If candidate succeeds, permit only frozen hosted GB provenance admission. Infrastructure/implementation/provenance failure remains `+0/+0`; a valid frozen numerical failure is scientific FAIL.
