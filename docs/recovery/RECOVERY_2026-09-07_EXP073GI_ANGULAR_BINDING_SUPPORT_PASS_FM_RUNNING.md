# DSIR recovery — Exp073GI angular-authority binding support PASS while Exp073FM runs

Date: 2026-09-07. Scope: **DSIR only**. RTK/RQIR excluded.

## Authoritative heavy process unchanged

Exp073FM `WW_S1_S1` remains the sole live self-hosted science process:
- workflow/run `34050657030`;
- home job `101533574294`;
- head `f0caca0c3e812710e5958ee13348a150d045a7d8`;
- state at final reconciliation: `IN_PROGRESS`;
- runner owner: `DSIR-HOME-PC` exclusively by job `101533574294`;
- checkpoint namespaces `checkpoints/exp073fm-ww-s1-s1-a-v0-1` and `checkpoints/exp073fm-ww-s1-s1-b-v0-1`;
- partial numerical output and checkpoint contents were not inspected.

Live Actions at final reconciliation: exactly one in-progress DSIR run (Exp073FM) and zero queued runs. No competing home/self-hosted task was launched.

## Exp073GI prospectively frozen support boundary

Created before audit execution:
- contract `docs/dsir4/DSIR4_ANGULAR_AUTHORITY_BINDING_CONTRACT_V0_1.md`, creation commit `dee5c0c3ccba69db34f7aee5b8d46badfd1e6cb9`, blob `af2cdbfa03e0a68c24df8d1009c723d411d2d0a2`;
- prereg `experiments/073gi_dsir4_angular_authority_binding_static_audit_v0_1_prereg.md`, creation commit `dccac1ff8003cfbe22d805fe88e41e6e8c113923`, blob `709171bb9780a9ac50311643a12f2dc4656cbfaa`.

The contract defines only the boundary between already admitted `G_DOMAIN_MAPPING` and future `G_ANGULAR_AUTHORITY`. It requires repository-admitted angular authorities, never candidate-only/workflow-success/partial-checkpoint evidence; preserves exact `EE<-EE`, canonical `<f8 [39,12288]`, NSIDE=4096, ell `0..12287`, 39 bands; missing authority is `NOT_YET_TESTABLE`; infrastructure/resource failures remain distinct from scientific FAIL; no tolerance/effective-coordinate/fiducial-P/interpolation/smoothing/averaging/source-pair substitution rescue is allowed.

The complete symmetric WW inventory frozen for the four-source basis is:
`S0_S0, S0_S1, S0_S2, S0_S3, S1_S1, S1_S2, S1_S3, S2_S2, S2_S3, S3_S3`.

## Hosted static audit

Workflow install commit `ceecfa0909935089c21cb5504a1d2d6fcc1390a5`; a subsequent activation-marker-only commit `b190709ae9a9e53b1d0c00c78b36afc5cc4be4af` caused a second hosted support execution after the first push had already triggered. This duplicated only a cheap hosted static support audit, not heavy/home science, did not create a competing control plane, and changed no frozen scientific content.

Both runs were independently consumed from raw logs:
- run/job `34062621354 / 101565732456`, head `ceecfa0909935089c21cb5504a1d2d6fcc1390a5`: SUCCESS;
- run/job `34062632135 / 101565765437`, head `b190709ae9a9e53b1d0c00c78b36afc5cc4be4af`: SUCCESS.

Both raw logs emitted exactly:
- `PASS_EXP073GI_DSIR4_ANGULAR_AUTHORITY_BINDING_STATIC_AUDIT_V0_1`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `g_angular_authority_created=false`;
- `scientific_model_authority_created=false`;
- `self_hosted_science_started=false`.

Classification: **SUPPORT_PLUS_0_PLUS_0** only. Exp073GI creates no `G_ANGULAR_AUTHORITY`, no model authority and no scientific PASS/FAIL.

## DSIR-4 status after Exp073GI

C0 and C1 retain the previously admitted `G_DOMAIN_MAPPING` authority from repaired Exp073GH v0.2, but `G_ANGULAR_AUTHORITY` remains `NOT_YET_TESTABLE`. At present the admitted WW authority inventory includes S0S0 through S0S3; Exp073FM S1S1 is still an in-progress candidate and cannot be treated as admitted authority. The remaining WW queue is prospectively frozen but staged workflows/preregs are not authority.

Therefore no angular gate admission is scientifically permitted yet.

## Exact next actions

1. If Exp073FM becomes terminal, immediately consume and independently verify its frozen artifact/checkpoint/source/same-object/file-backed/exact-equality contract. A valid candidate PASS permits canonical hosted Exp073FR; exact mismatch is scientific FAIL; infrastructure/resource failure is repair/resume from verified checkpoints.
2. While FM remains running, do not inspect partial numerical output and do not start another home task.
3. DSIR-4 may continue only with independent support/preregistration that cannot manufacture missing angular authority or infer model PASS from mapping authority.
