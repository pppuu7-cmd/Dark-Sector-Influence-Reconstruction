# DSIR research log — GA ledger sync V27

Date: 2026-09-08. Scope: DSIR only.

- Read `docs/RECOVERY_LATEST.md` and immutable V26 recovery authority.
- Reconciled live GitHub Actions: exactly one in-progress workflow, Exp073GA run `34189540992`; zero queued workflows.
- Confirmed hosted job `101944582891` SUCCESS and home job `101944608861` IN_PROGRESS on the frozen `WW_S3_S3` A/B gate.
- Read the active GA workflow and exact comparator token. Frozen checkpoint root: `$HOME/.cache/dsir/exp073ga-ww-s3-s3-filebacked-ab-v0-1`; exact candidate token: `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; final admission token: `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` plus `ww_s3_s3_authority_created=true`.
- Detected stale `docs/CURRENT_PROCESS.md` still describing V25/HD and `WW_S2_S3` as not admitted.
- Repaired only the process ledger in commit `8e168bd9bb1f2a3177d493197e610aaaaaae1b52`; scientific code/contracts/thresholds were untouched.
- No partial numerical output was inspected and no competing heavy run was launched.

Next action: terminal-consume GA when it finishes; if candidate succeeds, allow only frozen GB admission.
