# DSIR authoritative recovery V91 — JQ exact PASS, JR active

Updated: 2026-09-11. Scope: DSIR only.

## Preserved scientific state

Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`. Exp073JI support feasibility and Exp073JJ/JK support-only NOT_CONVERGED authorities remain preserved. Frozen Article-III science remains unchanged: `REL_TOL=1e-3`, `h=1e-4`, 107 retained rows, certified domain/support/masks/traversal, covariance restriction unauthorized and Wm_S3 unopened.

## Exp073JQ terminal authority

Exp073JQ run `34531670122`, head `8058c212372862c9dc59fa6fceb8defb17e22d93`, completed all four model jobs and aggregate successfully. Aggregate job `103055501260` classified `SAME_RUN_HISTORY_INDEPENDENCE_PASS_PLUS_0_PLUS_0`.

Independently verified artifacts:
- reference job/artifact `103053605850 / 10173947598`, ZIP SHA256 `73869241f165682d20a8ee628ee7525088ecba08bf551707b2c1df682463ba5d`;
- alpha-minus `103053605627 / 10173933797`, ZIP SHA256 `54dc9719079aee45c36bfc8d4c4607c54b6d0566f3ee98f50a715e0611da38bc`;
- beta-plus `103053606048 / 10173948139`, ZIP SHA256 `0a93171c2344588ea86f12aaf7daf4b8e1f1d43f6745e5cddadfa1726fc13032`;
- beta-minus `103053605929 / 10173913061`, ZIP SHA256 `4ba2d130b79d3ebabc644efb405a34e942ce987f21a368eec48c914e84fb9d8c`;
- aggregate artifact `10173953963`, ZIP SHA256 `fcc2b4e5f08761ebca8f6ba1d44e460b3d024843f166fc5bddff6f1c2d7d516b`.

For every model, exact `<f8` bytes satisfy `fresh_A == after_history == fresh_B`; max same-run absolute and relative diagnostic difference are both exactly `0.0`. JQ durable authority commit `3bdba4626ab12994c9d27a16a4446fd2bf79512b`.

Interpretation ceiling: JO v0.5 cross-execution exact mismatch is not caused by query history under the frozen same-run control. Cross-run/process last-bit variability remains the identified confounder. Checkpointed JL replay remains forbidden. Future scientific comparison operands must stay within one runner/process boundary.

## Exp073JR active

Prospectively frozen JR prereg:
`docs/dsir4/prereg/EXP073JR_ARTICLE3_LAYERB_SAME_RUN_ATOMIC_ARCHITECTURE_PREFLIGHT_V0_1.md`, creation commit `937045e58a658930bfcf9397d4e920db97d93516`, blob `edc511f140640291f7ff7b7860b1c2064a64b758`.

Implementation:
`ci/exp073jr_article3_layerb_same_run_atomic_architecture_preflight_v0_1.py`, creation commit `909084e43ccfb436688855bd157e59e2ac512a11`, blob `31b59c134b2a51749f6b9c1b14a8bcc8fa9d204d`.

Workflow/head commit `7613953cff71fd26cb9b73e7148a4d6c7aa87895`.
Active run `34533562950`:
- coarse job `103059792169`;
- fine job `103059792478`.

JR compares original four-live-instance response arithmetic against a memory-safe one-live-instance-at-a-time implementation on the same runner/process for two prospectively frozen sample requests, separately on guarded 2049-node and 4097-node JL lattices. Exact `np.array_equal` and response-byte SHA equality are mandatory; no approximate rescue.

JR is process/support-only `+0/+0`. It cannot change science or readiness. Exact PASS permits only preregistration of a full recovered JL where every coarse/fine comparison is completed locally inside a fixed response-blind chunk job and aggregate receives summaries only. Valid NOT_EXACT forbids sequential architecture. Infra failure permits only minimal infrastructure repair.

## Stable readiness telemetry

- Article III repository readiness: **68%**.
- Overall funnel readiness for methodology freeze: **67%**.

## Exact next action

Terminal-consume run `34533562950`. Inspect both job logs and artifacts; independently verify ZIP/JSON hashes and exact response equivalence. On aggregate exact PASS create durable JR authority, then and only then prospectively freeze the full same-run chunked recovery of the unchanged Exp073JL scientific gate. Do not launch checkpointed JL replay or cross-run raw-operand comparison. On fine/reference resource failure, classify `INVALID_INFRA_PLUS_0_PLUS_0` and design a new prospective validation route without changing JL science.
