# DSIR recovery V21 — Exp073FY pruner repair and checkpoint-first resume

Authority date: 2026-09-07. This note supersedes V20 for the active process only; all previously admitted DSIR science remains preserved.

## Terminal run consumed

Exp073FY run `34147009217`, head `f04346a8e6909cb4342e536a0e7328f5ca5e54c9`, hosted job `101821110137` SUCCESS, home job `101821144414` FAILURE. FZ admission was skipped. Classification: **implementation/infrastructure FAIL +0/+0**, not a scientific FAIL.

The first causal failure occurred after expensive Replica A had reached `replica_receipt_complete`: `ci/exp073fy_verify_and_prune_replica_v0_1.py` required an uppercase lexical token `WW_S1_S2` that does not exist in its pinned frozen FS base. No tolerance, arithmetic, source-domain, source-order, field semantics, or acceptance criterion was changed.

Artifact `10031272604`, name `exp073fy-ww-s2-s3-filebacked-ab-v0-1`, GitHub digest and independently recomputed ZIP SHA256 `624a44f05b2762a58d1191b58df41c194b86bcc7ceb5622517c0a55f64405a6c`. It contains complete Replica A manifests through `replica_receipt_complete` and no Replica B result. Preserved selected EE is `<f8 [39,12288]`, 3,833,856 bytes, SHA256 `3a787a12152ec023b6747145ec96345bc805ab0c96b5a26d0b528a9d68672de2`; public BPW receipt records exact `19,327,352,832`-byte file-backed MCM, `[4,39,4,12288]`, `EE<-EE`, no tolerance rescue, ordered `[2,3]`, `S2->S3`, distinct-field handoff.

Important provenance audit finding: preserved A manifests contain checkpoint namespace `checkpoints/exp073fy-ww-s3-s3-a-v0-1` even though their scientific payload is correctly `[2,3] / S2->S3`. Static inspection traced this to a cascade in the FY wrapper: after the intended hyphenated namespace replacement, the later word-boundary `s2 -> s3` transform mutates the namespace a second time. This is a provenance/checkpoint-identity defect, not a numerical result. It must fail closed; do not admit or relabel A as scientific authority. Do not weaken the frozen namespace contract to accommodate it.

## Repair already committed

Commit `c28396aa4cba6206f737cfd683b9f27f9cbe5273` changes only the FY post-receipt pruner lexical guard by removing the requirement for the absent uppercase token; new pruner blob `8c0e7ae30a80c6d74e6a1fbc079c1d2bc4eef773`. All actual source/order/distinct-field/hash/no-rescue checks remain.

Commit `3217ea05f5ab8a45bc237f34a8fa894e8c49df38` binds that blob in the FY workflow and triggered exactly one checkpoint-first recovery run.

## Current process

Authoritative active run: Exp073FY `34157571794`, head `3217ea05f5ab8a45bc237f34a8fa894e8c49df38`. Hosted audit job `101852463413` is SUCCESS. Home job `101852500796` is IN_PROGRESS on the single self-hosted DSIR runner, checkpoint root `~/.cache/dsir/exp073fy-ww-s2-s3-filebacked-ab-v0-1`. No competing heavy run is permitted.

Because the namespace cascade was discovered independently while this run is active, do not modify the running workflow or inspect partial numerical output. Let it fail closed if it reaches the inconsistent checkpoint identity. On terminal state, consume its artifact/log first. If the expected namespace mismatch is the first causal failure, prospectively fix the FY wrapper transform itself (protect namespace tokens before the later `s1/s2` word replacements), add a static regression proving exact `exp073fy-ww-s2-s3-{a,b}-v0-1` namespaces and absence of `ww-s3-s3`, bind the repaired blob, and resume only from checkpoints that verify under the prospectively repaired identity. Do not recompute a scientifically valid expensive stage unnecessarily, but do not rewrite invalid checkpoint provenance in place.

## Science authority

`WW_S2_S3` remains **NOT ADMITTED**. Only successful exact FY A/B candidate validation followed by frozen Exp073FZ token `PASS_EXP073FZ_WW_S2_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create authority. GA/`WW_S3_S3` remains forbidden until FZ succeeds. All prior admitted WW authority through `WW_S2_S2` remains unchanged.

C2 Exp073GZ remains preregistered/support-only and does not alter this heavy authority chain.
