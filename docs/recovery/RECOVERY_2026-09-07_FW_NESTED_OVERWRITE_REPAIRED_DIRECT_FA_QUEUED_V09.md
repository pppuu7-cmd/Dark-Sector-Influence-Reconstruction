# DSIR immutable recovery — Exp073FW nested-overwrite diagnosis and direct-FA recovery V09

Date: 2026-09-07. Scope: DSIR only; RTK/RQIR excluded.

All previously admitted authority is preserved. `WW_S2_S2` remains NOT ADMITTED.

## Terminal run `34125530921`: implementation failure +0/+0

Hosted audit job `101753205410` passed raw token `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_4`, classification `SUPPORT_PLUS_0_PLUS_0`. Home job `101753245014` then failed before numerical science with:

- `continue: only meaningful in a for, while, or until loop`
- `syntax error near unexpected token '('`

The failure occurred about 60 ms after wrapper start. No checkpoint/evidence files existed; upload reported no files and Exp073FX admission was skipped. This is pre-science implementation `+0/+0`, not a scientific arithmetic FAIL.

First causal defect: the FW wrapper transformed and executed the FM wrapper, and that inherited wrapper generated a second transformed script using the same `$RUNNER_TEMP/exp073fw_home_filebacked_fullres_v0_1.transformed.sh` path as the outer transform. The executing shell therefore read a file that had been overwritten by its nested generator. This is a wrapper staging/self-overwrite defect only.

## Prospective repair

Repository commit `820b0f8c082e45b2f51c3ff9d076a197ee3848f2` replaces the nested FM-wrapper execution with the already-proven direct frozen-FA transform architecture used by the admitted FU path. It pins FA blob `309c464bbfbe4896bd560165985ee7f643d9ee22`, preserves the frozen FW S2->S2 driver identities, exact-equality contract, source ordering, checkpoint namespace and acceptance criteria, binds the existing storage-audit helper identities, emits a single generated shell, and runs `bash -n` before execution. Home-wrapper blob: `c4ef9587d5f4b54179304a44741eece2cec0a7a5`.

Binding commit `1c635f5192d26e76e0ec82a308363b666e5a248b` launched replacement run `34125785882`.

## Authoritative process at note creation

- run: `34125785882`
- head: `1c635f5192d26e76e0ec82a308363b666e5a248b`
- hosted audit job: `101754018941` SUCCESS
- raw hosted token: `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_5`
- hosted classification: `SUPPORT_PLUS_0_PLUS_0`
- home job: `101754061309` QUEUED
- checkpoint namespace: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`
- intended runner owner: `DSIR-HOME-PC-2`
- competing heavy run: none observed

No science/domain/arithmetic/tolerance/acceptance criterion was changed by the repair. Do not inspect partial numerical output to tune criteria and do not launch a competing home run.

Exact next action: when `34125785882` becomes terminal, consume raw logs/artifact and verify digest, complete checkpoint/provenance chain, S2->S2 same-field semantics, exact file-backed MCM proof, canonical finite `<f8 [39,12288] EE<-EE`, and exact A/B equality. Workflow success alone is not scientific PASS; only frozen Exp073FX can create `WW_S2_S2` authority.
