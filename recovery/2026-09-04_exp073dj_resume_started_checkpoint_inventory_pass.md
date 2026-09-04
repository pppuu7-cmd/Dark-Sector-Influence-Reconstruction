# Exp073DJ checkpoint-preserving Exp073BU resume — live start reconciliation

Date: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.
Classification: process-state / recovery note only; no scientific authority.

## Live Actions authority
Workflow `.github/workflows/exp073dj-exp073bu-checkpoint-resume-v0-1.yml`, run `33910213781`, activation/head `c0f5959b3edb0957cfb14a1d06f7715242d57f48`.

Hosted preflight job `101144603730` is terminal SUCCESS. Self-hosted science-resume job `101144660519` has been claimed by the home runner and is IN_PROGRESS.

Completed self-hosted steps at this reconciliation:
1. setup and checkout;
2. exact 8-core hardware plus existing historical checkpoint-root binding;
3. exact NaMaster 2.7 environment install/reuse;
4. fail-closed durable checkpoint inventory;
5. exact frozen Exp073R1 S3 authority staging;
6. exact DES lens mask staging plus hash verification;
7. deterministic OpenMP-8 full-window downstream compilation;
8. runtime certification of the actual 8-thread downstream.

The active step is `Live exclusivity and checkpoint-preserving Exp073BU A-then-B resume`. Evidence preparation, artifact upload and frozen terminal classification have not begun.

The GitHub decoded job-log endpoint returned BlobNotFound while the job is active, so this note records only step-level state exposed by the live Actions job object. It does not infer or inspect partial numerical values.

## Preserved frozen identity
Historical checkpoint root: `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`.
Historical frozen science/source head: `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`.
Original contract fingerprint: `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`.
A/B namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`.
Expected science PASS token remains exactly `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`.

## Governance
DSIR-HOME-PC remains RESERVED BY this single Exp073DJ/Exp073BU resume job. No competing self-hosted DSIR workload may be launched. Passing the checkpoint-inventory and runtime-certification steps is support/process evidence only and does not create Wm_S3 authority. Partial numerical output must not be used to change the frozen gate.

## Exact next action
Track run/job `33910213781 / 101144660519` without duplication. When terminal, independently consume the raw evidence artifact, verify artifact digest, frozen science/repair provenance, A/B checkpoint identities, canonical `<f8 [39,12288]` dtype/shape, whole-payload SHA equality and `numpy.array_equal`, and classify strictly under the frozen contract. Exact inequality is a scientific repeatability FAIL; checkpoint/runner/provenance/dependency failures remain infrastructure/BLOCKED `+0/+0` with valid checkpoints preserved.
