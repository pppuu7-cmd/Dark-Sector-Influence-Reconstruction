# DSIR recovery — 2026-09-08 WW_S3_S3 admitted; C2 heavy exclusivity released V31

Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved authority

All authority from V30 is preserved unless explicitly advanced below. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW authorities through `WW_S2_S3` remain preserved.

## Exp073GA terminal consumption

Exp073GA recovery run `34197207582`, head `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`, is terminal `failure`. This workflow status is **not** a scientific failure.

Raw home job `101967543808` proves both expensive frozen replicas completed full-chain verification before prune:

- `PASS_EXP073GA_REPLICA_A_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`;
- `PASS_EXP073GA_REPLICA_B_FULL_CHAIN_VERIFIED_BEFORE_PRUNE_V0_1`;
- live exclusivity token `PASS_EXP073GA_LIVE_EXCLUSIVITY`.

The first causal failure occurred only afterward in the terminal comparator:

`RuntimeError: fail-closed receipt identity mismatch A:checkpoint_namespace`

The source artifact is `10051382493`, name `exp073ga-ww-s3-s3-filebacked-ab-v0-1`, exact GitHub ZIP digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

Materialized A/B receipts carry the intended exact namespaces `checkpoints/exp073ga-ww-s3-s3-{a,b}-v0-1`, frozen contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, canonical `EE<-EE` `<f8 [39,12288]`, and identical selected-EE SHA256 `e4aad74b8b733d280f4abfd6654778f0e037ab6060b12a908d30f8ec34c36c07`. Each selected payload is exactly `3,833,856` bytes and finite. The logged file-backed MCM proof remains exact `19,327,352,832` bytes.

Therefore run `34197207582` is classified **implementation/provenance failure `+0/+0`**, not scientific FAIL. No verified expensive stage is invalidated.

## Minimal prospective comparator repair

The first causal implementation defect was the GA wrapper's failure to transform the hyphenated FM namespace segment `ww-s1-s1` even though semantic underscore tokens were transformed. The repository-authoritative minimal repair is commit `becbbb58dc59a9f548ddb2c2628cbc5cb1404616`, comparator blob `6e7b45578c647a70233fec7db7d0a1d3c88d1774`. It adds exact `ww-s1-s1 -> ww-s3-s3` transformation plus positive/negative namespace guards. Frozen science arithmetic, domain, source order, tolerances and checkpoint payloads are unchanged.

## Exp073GD recovery admission — scientific authority created

The repository-native hosted recovery workflow `.github/workflows/exp073gd-ww-s3-s3-terminal-receipt-recovery-admission-v0-1.yml` consumed the already completed immutable GA evidence without home recomputation.

Authoritative recovery run: `34218457380`, head `4e5514b6077e1d70537586b43c9b5ca0e51abcf2`, job `102035691774 SUCCESS`.

The workflow fail-closed bound source run/job/artifact/digest, required both A/B full-chain tokens and the exact historical namespace failure, verified the materialized A/B namespaces, re-ran only the repaired terminal comparator, and then executed the unchanged frozen GB verifier blob `cc815737e658a850452d9b0f9488e703f8de84ea`.

Raw job log emits all required authority tokens:

- `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`;
- `ww_s3_s3_authority_created=true`;
- `heavy_recompute_performed=false`.

Accordingly **`WW_S3_S3` is now SCIENTIFIC_AUTHORITY_ADMITTED**. Historical GA implementation failures remain historical `+0/+0`; they are not rewritten.

A concurrently created hosted Exp073HE materialized recompare route is redundant reconciliation evidence only and must not become a competing authority/control plane. No further HE dispatch is permitted now that GD has admitted the same frozen target.

## Heavy ownership / C2 frontier

Live Actions reconciliation after admission shows **0 in-progress and 0 queued workflows**. The self-hosted heavy runner is free; no DSIR heavy owner is active.

Therefore the former C2 state `BLOCKED_BY_HEAVY_RUN_EXCLUSIVITY` is released. However real C2 28-packet / 1792-byte runtime is **not yet authorized**, because prospectively frozen Exp073HB build/static audit must pass first.

Exp073HB preregistration remains exactly `docs/dsir4/prereg/EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1.md`, blob `fc5f08889f84e628cb789070abd9179a74ef7e04`, expected token `PASS_EXP073HB_C2_DIAGNOSTIC_EXACT_ENDPOINT_PRODUCER_BUILD_AUDIT_V0_1`, classification ceiling `SUPPORT_PLUS_0_PLUS_0`.

Exact next permitted gate: implement the deterministic diagnostic-only exact-endpoint producer patch and run the **hosted-only** Exp073HB build/static audit. It must execute no cosmological run and create zero runtime payload records. Only a raw-log validated HB PASS may authorize the subsequent real diagnostic extraction under the already frozen GZ receipt-admission contract.

## Frozen science boundaries

Unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
