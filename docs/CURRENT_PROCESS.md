# DSIR current-process ledger

Updated: 2026-09-05
Scope: DSIR only; RTK/RQIR excluded.

## Scientific authority
**Wm_S3 scientific angular authority is exact PASS.** Authoritative process: Exp073DJ checkpoint-preserving Exp073BU resume, run/job `33910213781 / 101144660519`, activation head `c0f5959b3edb0957cfb14a1d06f7715242d57f48`, frozen science head `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`, contract fingerprint `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`, checkpoint root `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`, namespaces `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`.

Artifact `9959064322` has GitHub and independently downloaded ZIP SHA256 `4c9cbebdf4be2e901943a738ebb7df9c1040a6d9524bdd359feb3d3331a647c9`. Raw receipt is `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3` with canonical `<f8 [39,12288]`, whole SHA equality=true, `numpy.array_equal=true`, no tolerance rescue; A/B selected-TE SHA256 both `d282ebdf98dc04e41a8c85f487e209634a8324ce7677107112b8abfd1660f749`.

Historical Exp073CM resource FAIL and original Exp073BU v0.4 runner-loss remain immutable `+0/+0` outcomes.

## Current process — Exp073DL evidence recovery support `+0/+0`
Prereg: `experiments/073dl_exp073bu_terminal_payload_evidence_recovery_v0_1_prereg.md`, commit/blob `d22a4cddd4675ca3174eb0ba38d8b5cd16ba7296 / 1422fc524ed1a391fa6a0b3a464a2c754fcca01a`.

Support failure history:
- Exp073DK `33932618320`: hosted static harness `ValueError: substring not found`, export skipped.
- Exp073DL `33934660163`, `33934706167`: self-referential hosted audit false positives, export skipped.
- Exp073DL `33934784345 / 101220495111`: hosted audit PASS and home lock/live noncompetition PASS; first causal failure before payload reading was `ModuleNotFoundError: No module named 'numpy'` from system `python3`; no artifact files were produced. Classification infrastructure/dependency `+0/+0`.

Prospective repair:
- external static regression: `ci/exp073dl_evidence_guard_static_test_v0_1.py`;
- frozen-Python binding regression commit `96475ac95061bbaf28f0b55437db8583dd6d22a1`;
- evidence workflow activation commit `726d629236da0e807093840de80915718805ca5d`;
- evidence payload checker now binds read-only to the already validated `$HOME/.cache/dsir-nmt27/bin/python`; it never installs dependencies or recomputes NaMaster/masks/workspaces/MCM/PCL.

Current live run: `33934918432`.
- hosted static-audit job `101220844879`: SUCCESS;
- self-hosted evidence-only job `101220868663`: QUEUED at latest reconciliation;
- expected support token `PASS_EXP073DL_TERMINAL_PAYLOAD_EVIDENCE_RECOVERY_V0_1`;
- DSIR-HOME-PC is RESERVED for this single queued evidence-only job; no competing self-hosted/heavy process may start;
- on SUCCESS consume and independently validate Actions artifact digest, exact A/B payload SHA, `<f8 [39,12288]`, finiteness and `numpy.array_equal`;
- on FAIL/BLOCKED diagnose first support/infrastructure cause without altering Wm_S3 PASS or historical checkpoints.

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next action
Consume run/job `33934918432 / 101220868663`. Only after its support evidence is terminal and classified may a next self-hosted process be launched. Once evidence recovery is closed, advance from the admitted Wm_S3 PASS to the next prospectively permitted DSIR scientific gate from repository frontier authority.
