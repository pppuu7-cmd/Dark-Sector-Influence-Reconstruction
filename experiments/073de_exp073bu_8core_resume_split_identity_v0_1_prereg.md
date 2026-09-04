# Exp073DE — Exp073BU 8-core split-identity checkpoint-resume audit v0.1

Date: 2026-09-04
Scope: DSIR only. Support/infrastructure gate `+0/+0`; no Wm_S3 science authority can be created.

## Trigger
Exp073BU 8-core v0.4 run/job `33901458494 / 101116305364` ended `failure` while the science step remained reported `in_progress`; all `if: always()` evidence/classification steps remained pending and no Actions artifact exists. This is an infrastructure-incomplete terminal state, not a scientific comparator result.

## Frozen historical science identity
- `FROZEN_SCIENCE_HEAD = c02c018ede6a1fcf7aef1a848c0118a0669ed67f`
- original v0.4 science workflow blob = `f8c70a4206321b0dc10b57f63a2a06163da2249a`
- original contract fingerprint = `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`
- original checkpoint root = `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`
- A/B namespaces remain `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`.

Historical manifests must never be rewritten to substitute a newer implementation identity. Resume validation must continue passing the frozen science head and original contract fingerprint exactly.

## Prospective repair implementation
The only permitted implementation change is the already audited Exp073DD lineage repair from `ci/exp073bu_wm_s3_fresh_ab_production_v0_2.py`, combined with the exact-equivalence-certified 8-core adapter. A thin wrapper may patch the v0.2 module's imported v0.1 base with exactly the same 8-core constants/adapter used by `ci/exp073bu_wm_s3_fresh_ab_production_8core_v0_3.py`.

No scientific arithmetic, bands, masks, source data, TE selection, checkpoint boundaries, comparison rule, tolerance, rounding, smoothing or averaging may change.

## Hosted D1 gate
PASS only if a machine-checkable static audit proves all of the following:
1. frozen science head, original contract fingerprint, original workflow blob and original checkpoint root are literal immutable bindings;
2. the v0.2 lineage implementation blob is exactly repository-bound;
3. the 8-core adapter/source blobs are exactly those already certified by Exp073BU exact-equivalence authority;
4. the thin resume wrapper changes only module wiring/constants needed to combine v0.2 lineage with the frozen 8-core execution adapter;
5. restore remains fail-closed on replica, namespace, frozen science head, original contract fingerprint, payload SHA and provenance;
6. the wrapper retains exactly 8 outer/OpenMP workers and nested BLAS/MKL/NumExpr threads at 1;
7. no historical checkpoint manifest mutation/migration is introduced.

PASS token: `PASS_EXP073DE_SPLIT_IDENTITY_RESUME_BINDING_V0_1`.
FAIL/BLOCKED remain support/infrastructure `+0/+0` and cannot alter Wm_S3 authority.

## After PASS
Only after raw hosted PASS is independently consumed may a separate self-hosted resume workflow be prospectively activated. That workflow must first require the original checkpoint root to exist and validate complete-stage manifests against the frozen science identity. Missing or invalid checkpoints must BLOCK/fail closed rather than silently recompute verified expensive stages. It must never run concurrently with another DSIR self-hosted process.
