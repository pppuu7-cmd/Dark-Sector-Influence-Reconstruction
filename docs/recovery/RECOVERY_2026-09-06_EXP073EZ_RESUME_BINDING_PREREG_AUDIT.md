# DSIR recovery — 2026-09-06 — Exp073EZ resume-binding preregistration audit

Scope: DSIR only; RTK/RQIR excluded.

## Context

At live reconciliation, authoritative Exp073EY checkpoint-resume run `34010599584`, home job `101425638857`, remained `IN_PROGRESS`; queued DSIR runs were zero. No partial numerical output was inspected and no durable stage beyond the previously admitted replica-A `mcm_fits_verified` was inferred.

The existing immutable Exp073EZ v0.1 admission preregistration, blob `346bdbedcb34bdd67a0df88e5444f08071e822b6`, still named the original failed Exp073EY run `34006214398` and activation head `0476ce61a84a97392abb80afadad188a588bbe1f` as the candidate-producing execution. That original run is historical `INFRASTRUCTURE_SOFTWARE_PATCH_BINDING_FAIL +0/+0`, so a literal v0.1 execution binding would block admission of any valid candidate emitted by the prospectively audited checkpoint resume.

## Prospective governance repair

Before the resume result was known, created:
`experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_2_resume_binding_erratum.md`
commit `d694c80fd488b60faaea68a37294ee85cff5fe77`, blob `c5125bb9a09f6c02a1d6b48a862902ead9127b61`.

The erratum changes provenance/execution binding only. It preserves all v0.1 science, checkpoint, exactness and authority-writing semantics unchanged. It binds the candidate-producing process to:
- run `34010599584`;
- hosted repair audit `101425618749` SUCCESS;
- home candidate job `101425638857`;
- activation/head `4c570bf6b7f3f53547f43e2882149defa125da89`;
- resume workflow blob `7c0e8718357cfe4448b26c372a0567edf860f572`;
- repair erratum blob `a6fc7a1a3af86f8f02eba8c02294283192642784`;
- repair wrapper blob `a9cabeadc9b091424246adf00e9959dc62145e9b`;
- qualified FITS-read patch blob `d534b698f9131688d263eedcef27260386c58641`;
- unchanged science driver/source/contract/checkpoint identities.

The terminal artifact ID, artifact digest, independent ZIP SHA256, terminal selected-array hashes and terminal classification remain deliberately unknown and may only be bound after the home job is terminal.

## Hosted static audit

Workflow `.github/workflows/exp073ez-resume-binding-static-audit-v0-1.yml` was added and activated without using the home runner.

Run/job `34012838925 / 101431487475` = SUCCESS. Raw job log emitted exact token:
`PASS_EXP073EZ_RESUME_BINDING_STATIC_AUDIT_V0_1`.

The audit fail-closed verified base EZ blob, resume-binding erratum blob, resume workflow blob, repair erratum/wrapper/read-patch identities, exact resume run/job/head identity, hosted repair-audit SUCCESS, unchanged authority-writing token, and absence of a tolerance-style rescue in the erratum. This is governance/support evidence `+0/+0`; it creates no WW authority.

## Current authority and next action

`WW_S0_S0` remains admitted. Current science target remains `WW_S0_S1`. `DSIR-HOME-PC` remains reserved exclusively for Exp073EY resume `34010599584 / 101425638857` while active.

On terminal, consume the resume artifact against the frozen Exp073EY gate. Only an independently validated candidate PASS may be bound into the Exp073EZ admission implementation under v0.1 plus this v0.2 execution-binding erratum. Only token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1` may create `WW_S0_S1` authority.
