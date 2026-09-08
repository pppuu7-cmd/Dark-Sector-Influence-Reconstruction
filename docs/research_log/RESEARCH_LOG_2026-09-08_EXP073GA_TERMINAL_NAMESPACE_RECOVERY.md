# DSIR research log — Exp073GA terminal namespace recovery

Date: 2026-09-08. Scope: DSIR only.

## Observed terminal state

Exp073GA recovery run `34197207582`, head `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`, is terminal `failure`. Hosted audit job `101967492875` was `SUCCESS`; home job `101967543808` was `FAILURE`; final hosted admission job `102024645907` was `SKIPPED`.

The home job completed both expensive replicas before the failure. Raw log contains `PASS_EXP073GA_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1` and `PASS_EXP073GA_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`. The failure occurred only in `exp073ga_compare_terminal_receipts_v0_1.py` with `RuntimeError: fail-closed receipt identity mismatch A:checkpoint_namespace`.

Preserved artifact: `10051382493`, name `exp073ga-ww-s3-s3-filebacked-ab-v0-1`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

## Root cause and classification

The GA comparator inherited FM namespaces containing the hyphenated token `ww-s1-s1`, but its transformation only replaced underscore-form `ww_s1_s1`. Therefore the transformed comparator expected stale `checkpoints/exp073ga-ww-s1-s1-{a,b}-v0-1` while the actual frozen GA receipts correctly contain `checkpoints/exp073ga-ww-s3-s3-{a,b}-v0-1`.

Classification: `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`. This is not a scientific FAIL and does not alter any hypothesis ID, numerical contract, threshold, source ordering, selected semantics, or acceptance criterion.

## Safe repair

Comparator-only prospective repair commit: `becbbb58dc59a9f548ddb2c2628cbc5cb1404616`; repaired comparator blob: `6e7b45578c647a70233fec7db7d0a1d3c88d1774`. The repair adds the missing exact lexical mapping `ww-s1-s1 -> ww-s3-s3` and explicit fail-closed assertions for the two GA checkpoint namespaces.

No heavy recomputation was launched. A hosted-only recovery/admission workflow was created at `.github/workflows/exp073gd-ww-s3-s3-terminal-receipt-recovery-admission-v0-1.yml`, creation commit `e34943633309509008b1c5bb90b8bca00b37e9a3`. It reuses only artifact `10051382493` and source job log `101967543808`, verifies the exact artifact digest, regenerates only `terminal_receipt.json` with the repaired comparator, then runs the already-frozen GB provenance verifier.

Recovery run: `34218365250`. At log creation time it is hosted-only and queued; no self-hosted/heavy job exists in this workflow.

## Scientific status

Preserved admitted authority through `WW_S2_S3` remains unchanged. `WW_S3_S3` remains `NOT_YET_ADMITTED` until the hosted recovery emits all three frozen authority markers:

- `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`
- `ww_s3_s3_authority_created=true`

Until then, do not start downstream 14-window join or any competing heavy work.
