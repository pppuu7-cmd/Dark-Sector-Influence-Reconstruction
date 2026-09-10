# Exp073JL — corrected two hosted-runner shutdowns retrospective v0.2

Date: 2026-09-11. Scope: DSIR Article III execution history only. Effect `+0/+0`. This supersedes only the historical construction-count statement in v0.1.

Both historical Exp073JL v0.1 hosted attempts remain pure infrastructure failures: attempt 1 job `102938434376` and attempt 2 job `102944693569` both passed deterministic setup/build/input gates, entered the frozen numerical step, then received GitHub-hosted runner shutdown signals and emitted no scientific result artifact. Neither attempt is CONVERGED or NOT_CONVERGED.

Full source audit corrects the execution-shape count: the inherited Exp073IR traversal constructs four separate `ResolutionSuite` instances—coarse DES, coarse BOSS GL64, fine DES+BOSS GL64, and fine BOSS GL128. Each common-grid `ResolutionSuite` constructs four CLASS models simultaneously. Therefore the historical full-JL architecture performed **16 CLASS constructions total with up to four live at once**, not 12 as stated in retrospective v0.1.

This correction strengthens only the execution rationale for the already-authorized recovered route. It does not establish OOM as the causal mechanism of either runner shutdown and does not alter any scientific condition. Exp073JW has since independently verified the prospectively frozen eight-build/max-one-live lifecycle, and the response-blind request-plan audit has independently fixed the exact 441 coarse + 569 fine calls per role needed to preserve the inherited traversal.

No threshold, grid, domain, mask, interpolation, estimator, row accounting, covariance status or Wm_S3 status changes here. Readiness remains 68% / funnel-freeze 67% pending terminal recovered Exp073JL science.
