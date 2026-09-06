# DSIR recovery — staged WW successors while Exp073FM runs

Date: 2026-09-06. Scope: **DSIR only**; never mix RTK/RQIR.

## Authoritative running science

Exp073FM `WW_S1_S1` remains the sole live heavy process:
- workflow/run `34050657030`;
- home job `101533574294`;
- head `f0caca0c3e812710e5958ee13348a150d045a7d8`;
- state at reconciliation: `IN_PROGRESS`, step `Run frozen WW_S1_S1 A/B gate with durable checkpoints`;
- checkpoint namespaces `checkpoints/exp073fm-ww-s1-s1-a-v0-1` and `checkpoints/exp073fm-ww-s1-s1-b-v0-1`;
- partial numerical output was not inspected;
- `DSIR-HOME-PC` remains exclusively owned by job `101533574294`;
- live Actions reconciliation: one in-progress DSIR run, zero queued runs.

Canonical Exp073FR prereg remains `experiments/073fr_ww_s1_s1_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`, blob `aa08636426dd48142c3a3da7c032f1075a1be1f9`. It may run only after Exp073FM is terminal and independently consumed. The pre-terminal duplicate/automatic Exp073FR workflow was removed from active `main`; the active workflow path is intentionally absent while FM runs.

## Newly reconciled independent successor staging

Another DSIR process prospectively staged future ordered WW work on `main`. These commits are preparation/support only and do not change current authority or launch another home computation.

### Exp073FS — future WW_S1_S2 queue preparation

Hosted queue/static audit run/job `34054103704 / 101542730121` was inspected from raw logs and classified:
- token `PASS_EXP073FS_AUTONOMOUS_QUEUE_STATIC_AUDIT_V0_1`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `self_hosted_science_started=false`.

The staged `exp073fs-ww-s1-s2-home-science-v0-1.yml` is workflow-dispatch only and requires a successful Exp073FR admission run as explicit predecessor input. Its hosted launch audit verifies `PASS_EXP073FR_WW_S1_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1` and `ww_s1_s1_authority_created=true` before any home job can run. Therefore it does not compete with the currently running Exp073FM.

### Exp073FU — future WW_S1_S3 transformation audit

Historical v0.1 hosted static audit `34054723711 / 101544419091` failed before science. First causal failure from raw log: transform-audit implementation asserted the optional literal `Exp073FS` was necessarily present and raised `AssertionError: Exp073FS`. Classify as implementation/static infrastructure/support FAIL `+0/+0`; no self-hosted science and no authority.

A minimal prospective transform-only repair was committed (`5c0d75a57c909b0a0b699bbe79a5b5ab15c0f852`, followed by repaired bindings/workflow commits). Repaired v0.2 audit `34054859313 / 101544834479` was inspected from raw logs and passed exactly:
- token `PASS_EXP073FU_WW_S1_S3_TRANSFORMATION_STATIC_AUDIT_V0_2`;
- `classification=SUPPORT_PLUS_0_PLUS_0`;
- `self_hosted_science_started=false`.

No frozen scientific acceptance criterion, arithmetic, source domain, tolerance, or current Exp073FM computation was changed by this repair.

## Additional staged future transforms

Main now also contains prospectively staged transforms/preregs for later pairs (`Exp073FW/FX` S2S2, `Exp073FY/FZ` S2S3, `Exp073GA/GB` S3S3). These are not current scientific authority and are not running. They must still satisfy predecessor-admission, static-audit, live nonduplication, artifact-consumption and exact provenance requirements when their turn is reached. Their mere presence on `main` is not a PASS.

## Next permitted action

Do not launch any competing home job. When Exp073FM becomes terminal, first consume and classify its compact artifact under the frozen Exp073FM/Exp073FR contract. Only a valid independently consumed exact candidate PASS permits one hosted Exp073FR admission. After Exp073FR authority is actually admitted, future successor dispatch may proceed only through the prospectively frozen fail-closed predecessor checks.
