# Exp073DL — Exp073BU terminal payload evidence recovery v0.1 preregistration

Date: 2026-09-05
Scope: DSIR only. Support/evidence `+0/+0`; no scientific arithmetic and no authority creation.

## Motivation
Exp073DJ run `33910213781` completed SUCCESS and produced its frozen terminal science artifact. The automatically triggered Exp073DK run `33932618320` failed in the hosted static-audit harness before any checkpoint-root access: Python raised `ValueError: substring not found` while locating one of the guard strings. The self-hosted export job was skipped. This is an infrastructure/evidence failure only and does not alter the frozen Exp073BU comparator or its result.

## Frozen upstream binding
- Exp073DJ upstream run: `33910213781`.
- Frozen science head: `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`.
- Contract fingerprint: `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`.
- Historical checkpoint root: `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`.
- A/B namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`.
- Canonical selected payload: `<f8 [39,12288]`, semantics `wins[0,:,0,:] = TE<-TE`.

## Prospective recovery gate
Exp073DL may only perform evidence recovery after a hosted prereg/static check and a live fail-closed home noncompetition check. It must acquire the DSIR home lock before any historical checkpoint-root filesystem access and keep the lock open across all root reads and copies. It may not run NaMaster, reconstruct masks, recompute workspaces/MCM/PCL, modify checkpoints, or alter any acceptance criterion.

It will read the already-terminal Exp073DJ resume receipt and A/B terminal manifests/receipts, exact-check source head, contract fingerprint, namespaces, dtype/shape/semantics and payload SHA256, copy the existing A/B `selected_te.bin` payloads into an immutable Actions artifact, then independently evaluate whole-file SHA equality and `numpy.array_equal` without tolerance.

Missing/malformed evidence, a busy lock, source/contract mismatch, payload SHA mismatch, wrong shape/dtype/semantics, non-finite values or any competing self-hosted DSIR run is fail-closed `BLOCKED`/`INFRASTRUCTURE_INCOMPLETE +0/+0`.

## Scientific authority boundary
Exp073DL cannot create or rescue Wm_S3 authority. It only independently corroborates the already-frozen Exp073DJ terminal comparator. Scientific classification remains governed by the prospectively frozen Exp073BU gate and raw token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`; exact A/B inequality would remain a scientific repeatability FAIL and no tolerance/rounding/smoothing/averaging rescue is permitted.
