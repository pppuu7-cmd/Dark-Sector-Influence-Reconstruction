# DSIR recovery — Exp073DJ Wm_S3 exact PASS and terminal-evidence recovery

Date: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Scientific authority newly admitted
Exp073DJ checkpoint-preserving Exp073BU resume, workflow `.github/workflows/exp073dj-exp073bu-checkpoint-resume-v0-1.yml`, run `33910213781`, hosted job `101144603730`, self-hosted job `101144660519`, activation head `c0f5959b3edb0957cfb14a1d06f7715242d57f48`, completed SUCCESS at `2026-09-05T00:19:55Z`.

The Actions artifact is `9959064322`, name `exp073dj-exp073bu-checkpoint-resume-33910213781-c0f5959b3edb0957cfb14a1d06f7715242d57f48`, GitHub digest `sha256:4c9cbebdf4be2e901943a738ebb7df9c1040a6d9524bdd359feb3d3331a647c9`. An independent download produced the identical ZIP SHA256.

The raw `terminal_science_receipt_resume_v0_1.json` was inspected, not inferred from workflow success. It records:
- `classification = PASS`;
- exact raw token `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`;
- `science_gate_scored = true`, `wm_s3_authority_created = true`;
- frozen science head `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`;
- contract fingerprint `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`;
- A/B namespaces `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`;
- canonical comparison dtype `<f8`, shape `[39,12288]`;
- `whole_canonical_sha256_equal = true`;
- `numpy_array_equal = true`;
- `no_tolerance_rescue = true`;
- A and B selected-TE SHA256 both `d282ebdf98dc04e41a8c85f487e209634a8324ce7677107112b8abfd1660f749`;
- A and B fresh-PCL SHA256 both `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`;
- A and B workspace FITS SHA256 both `7f563fb42487261165dc574beb395e552565a634a86f6a46798f0ef33300f0e6`;
- `historical_wm_s3_numerical_import = false`;
- 8 execution workers and PyMaster 2.7.

The A/B replica receipts and selected-TE manifests were also inspected. They preserve exact source/fingerprint/namespace identities, `TE<-TE`, `<f8 [39,12288]`, no other-replica output read, no historical Wm_S3 numerical import, exact 8-core execution semantics and no tolerance rescue. Therefore **Wm_S3 scientific angular authority is now admitted as exact PASS**. Historical Exp073CM resource FAIL and original Exp073BU v0.4 runner-loss remain unchanged historical `+0/+0` outcomes.

## Exp073DK support failure — not a science failure
The automatically triggered Exp073DK terminal-payload support run `33932618320` failed in hosted job `101214169930`; self-hosted export job `101214196702` was skipped. First causal failure from logs was `ValueError: substring not found` inside the static regression harness while locating expected workflow text, before any historical checkpoint-root access. Classification: infrastructure/evidence support failure `+0/+0`. It does not invalidate or rescue the frozen Exp073DJ scientific PASS.

## Exp073DL prospective evidence recovery
Exp073DL was preregistered as support/evidence `+0/+0` only in `experiments/073dl_exp073bu_terminal_payload_evidence_recovery_v0_1_prereg.md`, prereg commit `d22a4cddd4675ca3174eb0ba38d8b5cd16ba7296`, blob `1422fc524ed1a391fa6a0b3a464a2c754fcca01a`.

Two hosted-only activation attempts (`33934660163`, `33934706167`) failed fail-closed in their own self-referential static-audit harnesses before self-hosted checkpoint access; both export jobs were skipped. The static regression was then externalized to `ci/exp073dl_evidence_guard_static_test_v0_1.py`, commit `a1dd414f5f4f27f1eed3a4e3020be8e901448e7d`, eliminating the self-reference ambiguity. Workflow repair/activation commit `c604862f7fe859ae2271b38a0c8148f395317f95` launched run `33934784345`.

At this recovery note, Exp073DL hosted job `101220470223` is SUCCESS and self-hosted evidence-only job `101220495111` is IN_PROGRESS. It performs no NaMaster/mask/workspace/MCM/PCL recomputation: after fail-closed lock and live noncompetition it only reads/copies already-terminal A/B selected-TE payloads, exact-validates identities/hashes, and independently recomputes SHA equality and `numpy.array_equal` for durable reproducibility evidence. Exp073DL cannot create or alter Wm_S3 scientific authority.

## Current ownership / next action
DSIR-HOME-PC is reserved only by Exp073DL evidence-only job `101220495111` while it runs. No competing heavy scientific run may start. When terminal, consume its raw artifact and independently verify artifact SHA, A/B payload SHA, dtype/shape, and `numpy.array_equal`; classify strictly as support evidence PASS or infrastructure/BLOCKED `+0/+0`. Then choose the next scientific gate from the now-admitted Wm_S3 frontier, without modifying any frozen historical result.
