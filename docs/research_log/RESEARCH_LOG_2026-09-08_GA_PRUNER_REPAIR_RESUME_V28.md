# DSIR research log — GA pruner repair/resume V28

Date: 2026-09-08. Scope: DSIR only.

- Read current recovery/research authority, GA/GB preregistrations, process ledger and recent commits; reconciled live Actions.
- Consumed terminal Exp073GA run `34189540992`: hosted `101944582891` SUCCESS, home `101944608861` FAILURE, final GB skipped.
- Downloaded artifact `10043979600`; independently verified ZIP SHA256 `b859e658e1046c4d9905d589003a1d26aaf3e2601c51d9db361b48176226906a` against GitHub digest.
- Verified preserved Replica A six-stage chain, correct namespace/source/contract, same-field `S3->S3/[3,3]`, exact 19,327,352,832-byte file-backed evidence, canonical selected `<f8 [39,12288] EE<-EE` SHA256 `e4aad74b8b733d280f4abfd6654778f0e037ab6060b12a908d30f8ec34c36c07`, and all-finite selected payload. Replica B had not started.
- Diagnosed first causal failure after A completion: false wrapper requirement for absent pinned-base token `WW_S1_S1`. Classified `implementation/infrastructure FAIL +0/+0`, not scientific FAIL.
- Reconciled a concurrent DSIR repair commit `f52fa856eb029c64f744926eecf55f506fcf1da5`, pruner blob `fc3e4d8444630e4b5a2dde0a052e1069b7887c01`, which removes only that false transform requirement.
- Rebound the GA workflow prospectively in commit `f6d8b429ac64643e7cb7766e0bfa2ab51abe751d`, adding a hosted static regression that verifies the real FM source-token set and explicitly proves `WW_S1_S1` is absent before any home compute.
- Recovery run `34197207582` launched automatically from the workflow binding. Hosted job `101967492875` SUCCESS with `PASS_EXP073GA_PRUNER_TRANSFORM_SOURCE_STATIC_REGRESSION_V0_1` and `PASS_EXP073GA_HOSTED_LAUNCH_AUDIT_V0_3`; home job `101967543808` is IN_PROGRESS on the frozen checkpoint-resumable GA gate.
- No competing home-heavy run launched. Partial numerical output of the active recovery run was not inspected.

Next action: terminal-consume `34197207582`; preserve/verify A checkpoint resume, require complete B and exact A/B candidate equality, then permit only frozen GB admission.
