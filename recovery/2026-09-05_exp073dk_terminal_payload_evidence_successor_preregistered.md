# Exp073DK terminal canonical-payload evidence successor preregistered

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.
Classification: support/evidence preparation `+0/+0`; no Wm_S3 authority.

## Live scientific process preserved
Exp073DJ / Exp073BU checkpoint resume run/job `33910213781 / 101144660519` remains IN_PROGRESS. The active step is still the frozen checkpoint-preserving A-then-B resume. No partial numerical values were inspected and no competing heavy/self-hosted process was launched.

## Independent evidence audit
The frozen launcher `ci/exp073bu_wm_s3_science_launcher_8core_v0_3.py` performs the scientific terminal comparison directly on A/B `selected_te.bin` using both whole-file SHA equality and `numpy.array_equal` on `<f8 [39,12288]`. The Exp073DJ Actions evidence step, however, copies terminal/replica/adapter receipts and manifests but not the two canonical payload byte files. Therefore its ordinary artifact alone is insufficient for an independent post-terminal re-execution of `numpy.array_equal` from raw canonical bytes.

This is an evidence/reproducibility gap only. It does not alter, weaken, rescue, or invalidate the frozen science gate and it does not justify inspecting partial outputs.

## Prospective deterministic repair
Preregistered Exp073DK v0.1 at `experiments/073dk_exp073bu_terminal_payload_evidence_export_v0_1_prereg.md`, prereg blob `1e8f29f8552475748680439924c13590d352549a`, prereg commit `286b6dace47cd2c2dc631be544a998401557cef2`.

Added workflow `.github/workflows/exp073dk-exp073bu-terminal-payload-evidence-export-v0-1.yml`, commit `75c0d7d8197bc29d7a06037a355aaf34b17f8d59`.

The successor is `workflow_run`-triggered only after completion of `Exp073DJ checkpoint-preserving Exp073BU resume v0.1` and additionally hard-binds upstream run ID `33910213781`. It performs no NaMaster, mask, workspace, MCM, PCL, or production-driver calculation. It only validates frozen identities/hashes, copies the already-final A/B canonical `selected_te.bin`, verifies byte-for-byte SHA against manifests and receipts, and independently recomputes exact SHA equality and `numpy.array_equal` on the copied payloads. Missing terminal receipt/payload/provenance is fail-closed BLOCKED/infrastructure `+0/+0`.

The successor also acquires the existing DSIR home lock and checks for any other queued/in-progress self-hosted DSIR job before touching the historical checkpoint root. It is not a competing scientific control plane and cannot create scientific authority by itself.

## Exact next action
Continue tracking `33910213781 / 101144660519` without duplication. On terminal state, consume Exp073DJ raw receipt/artifact under the frozen contract. Exp073DK should then deterministically export the canonical A/B payload evidence; independently verify its artifact before admitting or rejecting any Wm_S3 authority. If Exp073DJ has no terminal receipt, Exp073DK must fail closed and the result remains infrastructure/BLOCKED `+0/+0`.
