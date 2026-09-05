# DSIR recovery — Exp073DK lock-scope TOCTOU repair

Date: 2026-09-05
Scope: DSIR only; support/evidence infrastructure `+0/+0`.

## First causal defect
The prospectively preregistered Exp073DK terminal-payload evidence successor originally acquired the DSIR home-heavy `flock` in a dedicated shell step and then released that file descriptor when the step exited. Historical checkpoint-root access occurred in a later shell step. This violated the preregistered requirement to hold the existing DSIR home-heavy lock before touching the historical Exp073BU checkpoint root and created a time-of-check/time-of-use window between live noncompetition and immutable evidence export.

This defect is not a scientific/numerical result and does not alter the frozen Exp073BU comparator, arithmetic, boundaries, payload semantics, tolerance policy or currently running Exp073DJ process.

## Prospective repair
The Exp073DK successor now performs only upstream/prereg binding before the lock, acquires `~/.cache/dsir/DSIR-HOME-PC.exp073bu-8core-resume.lock` on FD 9, and retains FD 9 for the whole shell step that performs live self-hosted noncompetition plus every historical checkpoint-root filesystem read. It touches the historical root only after the lock is held and remains read-only with respect to that root, copying terminal evidence only into `$RUNNER_TEMP`.

Exact A/B namespace, source-head, contract-fingerprint, stage, payload SHA, shape `<f8 [39,12288]`, `TE<-TE`, finiteness, whole-file SHA equality and `numpy.array_equal` validation remain unchanged. The receipt remains support-only `+0/+0` with `science_gate_scored_here=false` and `wm_s3_authority_created_here=false`.

A hosted `static-audit` predecessor job was added to fail closed unless workflow source proves lock acquisition precedes checkpoint-root access and the pre-lock binding step contains no checkpoint payload/receipt access. The self-hosted export job now depends on that audit. The audit is ARMED prospectively; it is not a PASS until Exp073DJ terminates, triggers Exp073DK, and the raw hosted job result is validated.

## Frozen identities preserved
- Exp073DK prereg blob: `1e8f29f8552475748680439924c13590d352549a`.
- Frozen Exp073BU science head: `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`.
- Original contract fingerprint: `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`.
- Historical checkpoint root: `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`.
- A namespace: `checkpoints/exp073bu-wm-s3-a-v0-1`.
- B namespace: `checkpoints/exp073bu-wm-s3-b-v0-1`.
- Only admissible Wm_S3 PASS token remains `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`.

## Live process at reconciliation
Exp073DJ run/job `33910213781 / 101144660519` remains the single in-progress self-hosted DSIR scientific process. Hosted preflight `101144603730` is SUCCESS. The science-resume job remains IN_PROGRESS in `Live exclusivity and checkpoint-preserving Exp073BU A-then-B resume`; evidence/upload/classification are pending. Live Actions reconciliation remains `1 in_progress / 0 queued`. No competing heavy job was launched and no partial numerical output was inspected.

## Classification and next action
Classification of this repair: **prospective support/evidence infrastructure repair `+0/+0`**. It creates no Wm_S3 authority and cannot rescue a scientific inequality.

Exact next action remains terminal consumption of `33910213781 / 101144660519`. On terminal state, inspect the raw Exp073DJ science receipt/artifact and provenance first; then validate the automatically triggered Exp073DK static audit and canonical-payload evidence artifact. Scientific PASS requires the unchanged frozen exact comparator plus independent terminal evidence verification; infrastructure/evidence defects remain fail-closed `+0/+0`.
