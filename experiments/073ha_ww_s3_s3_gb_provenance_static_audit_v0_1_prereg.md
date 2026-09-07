# Exp073HA — WW_S3_S3 GB provenance static audit v0.1 preregistration

Date: 2026-09-08
Classification: SUPPORT_PLUS_0_PLUS_0
Execution class: GitHub-hosted only; no self-hosted runner use; no numerical WW payload inspection.

## Purpose

Prospectively audit the already-frozen Exp073GB provenance-admission verifier and its binding inside the already-frozen Exp073GA WW_S3_S3 workflow before the expensive GA run is allowed to start. This audit must not change GA science, thresholds, ordering, source maps, numerical code, or admission criteria.

## Frozen objects

The audit MUST bind and inspect without modification:
- `ci/exp073gb_verify_ga_candidate_v0_1.py` blob `ee065b7d844090ae16386cc6944db23846d663ec`;
- its exact FX verifier base blob `eb907944eac68b9fd13c405399cf238a8cb5bc96`;
- `.github/workflows/exp073ga-ww-s3-s3-home-science-v0-1.yml` blob `e7505c0264b0f66aa2682a326486567784a54135`;
- GA home wrapper blob `f28bf114e6da502e2a3a0a97f0828c27849814c9`;
- GA pruner blob `24ee2408b4b66a17001fb734e9e46d008179c310`;
- GA terminal comparator blob `263c69075f8a9c5ad3644224485f20fbb3961406`.

## Required static invariants

The hosted audit must verify:
1. GB transforms only the frozen FW/FX same-field admission semantics to GA/GB S3_S3 semantics.
2. Required tokens include `PASS_EXP073GA_WW_S3_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, `PASS_EXP073GB_WW_S3_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `S3->S3`, `[3,3]`, `{'s3':1}`, and `ww_s3_s3_authority_created=true`.
3. Stale FW/FX S2_S2 scientific tokens are forbidden after transformation.
4. The GA workflow invokes this exact GB verifier only after `home-science` success and verifies the downloaded artifact digest before admission.
5. GB still requires both pre-prune full-chain proof tokens, exact terminal PASS, live-exclusivity proof, exact A/B byte equality, finite values, exact adapter route, complete prune manifest hashes, and no tolerance rescue through its frozen base verifier.
6. No `np.allclose`, `np.isclose`, rounding, smoothing, averaging or tolerance-rescue path is introduced.
7. This audit creates no WW authority and must never dispatch GA or use a self-hosted runner.

## PASS token

Only a successful hosted static audit may emit:
`PASS_EXP073HA_WW_S3_S3_GB_PROVENANCE_STATIC_AUDIT_V0_1`

This token is support-only `+0/+0`; only a later successful Exp073GB execution on a real admitted GA artifact may create `WW_S3_S3` scientific authority.
