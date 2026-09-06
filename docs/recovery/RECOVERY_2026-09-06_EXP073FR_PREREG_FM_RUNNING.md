# DSIR immutable recovery — Exp073FR prereg while Exp073FM running

Date: 2026-09-06. Scope: DSIR only.

## Preserved authority

Preserve all authority and historical outcomes from `docs/RECOVERY_LATEST.md`. In particular, admitted WW authorities remain `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`; no `WW_S1_S1` authority exists yet.

## Live authoritative process at this recovery point

- Exp073FM run `34050657030`;
- home-science job `101533574294`;
- head `f0caca0c3e812710e5958ee13348a150d045a7d8`;
- state: `IN_PROGRESS` in `Run frozen WW_S1_S1 A/B gate with durable checkpoints`;
- `DSIR-HOME-PC` owned exclusively by job `101533574294`;
- checkpoint namespaces `checkpoints/exp073fm-ww-s1-s1-a-v0-1` and `checkpoints/exp073fm-ww-s1-s1-b-v0-1`;
- partial numerical output not inspected; current durable stage remains `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`.

No competing home/self-hosted computation was launched.

## Newly frozen prospective gate

Exp073FR `WW_S1_S1` file-backed checkpoint provenance admission v0.1 was prospectively preregistered while Exp073FM was still running, before any terminal numerical result was consumed.

- prereg path: `experiments/073fr_ww_s1_s1_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`;
- creation commit: `55fa8c56ec8bb7e7cb0d278870a05619c5a59f67`;
- prereg blob: `aa08636426dd48142c3a3da7c032f1075a1be1f9`;
- frozen PASS token: `PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`;
- authority can be created only after terminal Exp073FM is independently consumed and every frozen provenance/checkpoint/source/same-object/file-backed/exact-equality check passes;
- Exp073FR performs no self-hosted heavy science and must not acquire the home runner.

The prereg preserves the Exp073FM science unchanged: `[1,1]`, one S1 reconstruction, one spin-2 field reused on both coupling sides, NSIDE=4096, ell `0..12287`, 39 bands, public file-backed BPW, exact MCM backing `19,327,352,832` bytes, canonical `<f8 [39,12288] EE<-EE`, exact SHA plus `numpy.array_equal`, finite values, and no tolerance/rescue path.

## Next action

If Exp073FM remains running, do not inspect partial numerical output and do not duplicate it. On terminal state, consume the compact evidence immediately. Only a fully verified Exp073FM candidate PASS permits generation/dispatch of the single hosted Exp073FR admission workflow. Exact numerical mismatch is a scientific FAIL; infrastructure/resource defects are diagnosed and repaired prospectively without weakening science.
