# Exp073DJ — checkpoint-preserving Exp073BU 8-core resume orchestration v0.1

Date: 2026-09-04
Scope: DSIR only. This is an infrastructure/resume orchestration for the already frozen Exp073BU Wm_S3 A/B science gate; it is not a new or altered scientific hypothesis.

## Historical science identity (immutable)
- frozen science head: `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`;
- original science workflow blob: `f8c70a4206321b0dc10b57f63a2a06163da2249a`;
- original contract fingerprint: `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`;
- checkpoint root: `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`;
- namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`;
- terminal science PASS token remains exactly `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`.

The terminal run `33901458494 / 101116305364` is historical `INFRASTRUCTURE_INCOMPLETE +0/+0`, not scientific FAIL. Any existing historical terminal receipt is read-only evidence and must not be overwritten; resume writes a separate terminal receipt.

## Validated repair implementation
Activation requires repository-bound raw support authority through Exp073DI and exact blobs:
- resume lineage driver `a0b3f399cb26457c03b57dd16e79245aec4fbca0`;
- 8-core resume wrapper `d0fd545ef7b1245f21a5d7cba2f3b2eed459d87b`;
- resume-only launcher validator `0026c9607c935b4b2ad90a396cecee735b893738`;
- frozen launcher `8a725ba135e3e120ce6e8d0db3dd14d95d4ffd6e`;
- exact OMP8 adapter `63ee393791bba43d3eabbea654efdb9d439d477e`;
- exact parametric downstream source `be4f381de4c5c043a9c0fcd107e63ef3f2079578`.

## Activation and noncompetition
A hosted preflight must exact-bind the historical science identity, repair implementation and immutable recovery authority, then fail closed if another queued/in-progress DSIR self-hosted job exists. The self-hosted job must acquire the existing DSIR home lock before any resume computation and repeat the live self-hosted noncompetition check.

## Checkpoint inventory before work
The self-hosted process must require the **existing** historical checkpoint root; it may not create a replacement root if missing. For each replica, the six complete-stage manifests must form an ordered prefix. Every existing manifest must exactly match replica, namespace, frozen science head, original contract fingerprint, no historical Wm_S3 import and no other-replica read. Where a stage payload exists, its stored SHA/shape identity must be verified against the actual payload before it is accepted as durable.

No later complete stage may exist after a missing earlier stage. Any malformed/gapped/identity-mismatched checkpoint is `BLOCKED/INFRASTRUCTURE_INCOMPLETE`; do not delete it and do not start fresh silently.

## Resume semantics
- preserve all valid complete stages read-only;
- if no durable stage exists, computing the missing work is allowed because nothing expensive was verified;
- if masks are complete, restore exact mask payloads and preserve cumulative lineage `{lens:1,source:1}`;
- if workspace/full/selected stages are complete, never recompute them;
- full-window -> selected-TE resume is exact `wins[0,:,0,:] = TE<-TE`, canonical `<f8 [39,12288]`, with exact `numpy.array_equal` verification;
- valid legacy complete replica receipts are read-only;
- persisted adapter runtime proof is accepted only under the exact Exp073DI fallback contract;
- execute A to completion, release replica-local live state, then B, then the unchanged exact A/B comparator.

## Compute contract
Exactly 8 OpenMP/outer workers. `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`, `BLIS_NUM_THREADS=1`, `VECLIB_MAXIMUM_THREADS=1`. Hardware affinity must expose exactly 8 CPUs and runtime probe must show `DSIR_OMP_TEAM=8`.

## Frozen science
39 frozen bands; DES NSIDE=4096; ell `0..12287`; Wm `TE<-TE`; canonical `<f8 [39,12288]`; exact whole-payload SHA256 equality **and** `numpy.array_equal`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.

## Terminal classification
- valid raw PASS token plus exact SHA and `numpy.array_equal` => scientific PASS and Wm_S3 authority may be admitted only after independent artifact consumption;
- exact A/B inequality => `SCIENTIFIC_REPEATABILITY_FAIL` under the frozen gate;
- missing/malformed provenance, runner loss, checkpoint defect, transport/dependency failure => `INFRASTRUCTURE_INCOMPLETE` or `BLOCKED`, `+0/+0`;
- workflow success by itself is never scientific PASS.
