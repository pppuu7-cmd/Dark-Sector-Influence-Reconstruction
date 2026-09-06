# DSIR research log — 2026-09-06 — Exp073EZ resume-binding audit

Scope: DSIR only.

- Live reconciliation found authoritative Exp073EY checkpoint-resume `34010599584 / 101425638857` still IN_PROGRESS; queued DSIR runs were zero. No partial numerical output was inspected.
- Identified a prospective governance defect: immutable Exp073EZ v0.1 prereg blob `346bdbedcb34bdd67a0df88e5444f08071e822b6` still bound admission to the original failed Exp073EY run `34006214398`, so it could not literally admit a valid resume candidate.
- Created provenance-only resume-binding erratum `experiments/073ez_ww_s0_s1_filebacked_checkpoint_provenance_admission_v0_2_resume_binding_erratum.md`, commit `d694c80fd488b60faaea68a37294ee85cff5fe77`, blob `c5125bb9a09f6c02a1d6b48a862902ead9127b61`, before the resume result was known.
- Scientific arithmetic, ordered `(S0,S1)`, NSIDE/ell/bands, public BPW route, exact A/B criterion, six-stage checkpoint semantics and authority token were unchanged.
- Hosted static audit run/job `34012838925 / 101431487475` SUCCESS emitted `PASS_EXP073EZ_RESUME_BINDING_STATIC_AUDIT_V0_1`; support/governance `+0/+0` only.
- Exp073EZ terminal artifact ID/digest and terminal candidate values remain deliberately unbound until Exp073EY is terminal and independently consumed.

Next: terminal-consume Exp073EY resume; on independently verified candidate PASS, instantiate Exp073EZ admission using v0.1 science contract plus v0.2 resume-binding erratum. Only EZ admission PASS creates `WW_S0_S1` authority.
