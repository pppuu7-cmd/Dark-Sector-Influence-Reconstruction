# Exp073FP — WW_S1_S1 exact production driver static audit v0.1

Date: 2026-09-06. Scope: **DSIR only**.

Purpose: freeze and hosted-audit the exact committed Exp073FM S1S1 production implementation before any home science. This gate is support `+0/+0` only.

Frozen implementation requirements:

1. Source pair is exactly `S1->S1`, ordered indices `[1,1]`.
2. Each replica calls authoritative `source_count_map(...,1)` exactly once when source reconstruction is fresh and stores exactly one canonical S1 source map checkpoint.
3. Each fresh workspace constructs exactly one spin-2 `NmtField` and passes the exact same Python object to both arguments of `compute_coupling_matrix`.
4. Equal-but-distinct second field is structurally absent; stale S0/S2/S3 source construction and cross-pair semantics fail closed.
5. Complete checkpoint order remains `fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`, with dedicated Exp073FM A/B namespaces and exact source-head/contract identities.
6. Completed-restore verification rechecks all six manifests and all still-present payload hashes before accepting a replica.
7. Public serialized BPW route remains `read_from(...,read_unbinned_MCM=True)` followed by `get_bandpower_windows()`, full `[4,39,4,12288]`, selected `wins[0,:,0,:] = EE<-EE`, canonical `<f8 [39,12288]`.
8. v0.2 file-backed adapter requires exactly one newly created MCM backing file, exact size `19,327,352,832` bytes and `/proc/self/maps` proof.
9. A/B candidate classification uses exact SHA equality + exact `numpy.array_equal` + finiteness. No `allclose`, `isclose`, tolerance, rounding, smoothing, averaging, manual reconstruction, effective-coordinate or fiducial rescue.
10. Candidate token is exactly `PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate creates no authority.

PASS token for this hosted static audit:

`PASS_EXP073FP_WW_S1_S1_EXACT_PRODUCTION_DRIVER_STATIC_AUDIT_V0_1`

Classification `SUPPORT_PLUS_0_PLUS_0`; `ww_s1_s1_authority_created=false`; `self_hosted_science_started=false`.

On PASS the next permitted step is a separately preregistered fail-closed home-envelope audit. On FAIL diagnose the first implementation/static defect and repair prospectively without weakening Exp073FM science.