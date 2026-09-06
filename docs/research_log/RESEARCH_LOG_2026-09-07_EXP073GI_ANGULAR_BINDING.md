# DSIR research log — Exp073GI angular-authority binding support audit

Date: 2026-09-07. Scope: DSIR only.

Exp073FM `WW_S1_S1` remained the sole live self-hosted science job. No partial numerical result or checkpoint content from FM was inspected and no competing home job was started.

Prospectively frozen contract: `docs/dsir4/DSIR4_ANGULAR_AUTHORITY_BINDING_CONTRACT_V0_1.md`, blob `af2cdbfa03e0a68c24df8d1009c723d411d2d0a2`. Prereg: `experiments/073gi_dsir4_angular_authority_binding_static_audit_v0_1_prereg.md`, blob `709171bb9780a9ac50311643a12f2dc4656cbfaa`.

The frozen support boundary requires admitted `G_DOMAIN_MAPPING` before angular binding, repository-admitted WW authorities only, the complete symmetric S0..S3 pair inventory, canonical `EE<-EE` `<f8 [39,12288]`, NSIDE=4096, ell 0..12287, 39 bands, and fail-closed `NOT_YET_TESTABLE` for missing authority. Candidate-only evidence, workflow-success-only evidence, partial checkpoints and numerical-rescue substitutions are forbidden.

Hosted static audit run/job `34062621354 / 101565732456` and activation-marker duplicate run/job `34062632135 / 101565765437` both completed SUCCESS and raw-log verification yielded the same support-only token `PASS_EXP073GI_DSIR4_ANGULAR_AUTHORITY_BINDING_STATIC_AUDIT_V0_1`, with `classification=SUPPORT_PLUS_0_PLUS_0`, `g_angular_authority_created=false`, `scientific_model_authority_created=false`, `self_hosted_science_started=false`.

The second execution duplicated only a cheap hosted static audit because an activation-only commit was made before observing the first triggered run. No heavy computation, runner ownership, frozen science or authority was duplicated.

Scientific status: `G_ANGULAR_AUTHORITY` remains `NOT_YET_TESTABLE`; Exp073GI is infrastructure/support only. C0/C1 `G_DOMAIN_MAPPING` authority does not imply angular or model authority.

Next priority remains terminal consumption of Exp073FM and canonical Exp073FR only after an independently validated exact candidate PASS.
