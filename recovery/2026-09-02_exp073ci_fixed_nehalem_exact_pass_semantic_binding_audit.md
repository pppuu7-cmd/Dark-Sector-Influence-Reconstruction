# Exp073CI deterministic fixed-dispatch finalizer v0.2 — terminal exact PASS and semantic/criteria-binding audit

Date: 2026-09-02

## Coordination state before write

Repository Actions inspection immediately before this write found 0 queued and 0 in-progress DSIR runs. DSIR-HOME-PC was free. No self-hosted work was triggered.

## Immutable execution authority

Exp073CI run `33646799130` is terminal. Hosted authorize job `100303472992` PASS. Worker jobs `100303530655` (R1), `100303530639` (R2), `100303530782` (R3), and `100303530588` (R4) all completed successfully. Frozen exact comparator job `100304043991` completed successfully.

Comparator authority:
- token: `PASS_EXP073CI_WM_S2_DETERMINISTIC_FIXED_NEHALEM_FINALIZER_EXACT_V0_2`
- classification: `EXACT_REPEATABILITY_PASS_NEW_VERSION`
- exact cross-worker/lane/repeat equality: true
- compact SHA: `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`
- K SHA: `c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795`
- W SHA: `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087`
- fixed core: `Nehalem`
- no tolerance used: true
- scientific authority for Exp073CI v0.2: true
- readiness delta from execution: `[0,0]`

Authority artifact: `9853165664`, digest `sha256:fcfccb6768948ffe34d28e9ed32da64d3b1d071704028fe6f312c1ab8b440f57`.

Worker artifact digests consumed by the comparator were:
- R1 artifact `9853144347`, digest `sha256:626986f40ee3bba084f88ae7b2442b30a48b091f40b5844af44e38846969c9c2`
- R2 artifact `9853146827`, digest `sha256:4c5881d00bb678d4bf7a9b0ae2af40aeaf867ef85033b455870c38f830b97932`
- R3 artifact `9853153894`, digest `sha256:6a72cb25696bb431e6733b1e6d77b87f08ea0f34e7cb3f7e8723c79dd95e1801`
- R4 artifact `9853138402`, digest `sha256:1d33ef88df62cbd45d1e1636c19588893444e8a6ba2b7090ffb47dae97df8fc9`

Frozen provenance remains prereg `1cf4ef96a44f26e7170d1ce6bd87c38dcc85cc7f`, helper `9f2f7870d912314e03f2f5725b07df12ace7fa92`, workflow `ca1af9bf17496e0f2bcb388356ea6a954844e2ef`, binding `835a916d5708d394cacc08c028cae1341e195868`, trigger/head `f8396c8e5e6b4a83340acf6ea0aaa262c9c71007`.

## Historical boundary preserved

Exp073CF finalizer v0.1 remains permanently classified `SCIENTIFIC_REPEATABILITY_FAIL_EXP073CF_WM_S2_FINALIZER_EXACT_V0_1`. Exp073CI is a new version and does not rescue, replace, average, prefer, or reclassify either historical Exp073CF replica.

## Static downstream semantic/criteria-binding audit

Result: `PASS_EXP073CI_V0_2_STATIC_SEMANTIC_CRITERIA_BINDING_AUDIT`, non-scoring `+0/+0`.

The audit compared the prospectively frozen Exp073CI contract against the original production finalizer source at path-history commit `d77b7ba88801f6788f3d386e72b445c7859c7153`.

Confirmed invariant semantics:
1. Exp073CI consumes the exact compact canonical `<f8 [39,12288]` authority already established by the Exp073CF compact comparator; both independent artifact lanes are hash-checked against the same canonical compact SHA.
2. K construction is not redefined: Exp073CI imports `k_from_a` from the original production finalizer implementation and requires the exact frozen K SHA.
3. Finalizer algebra is unchanged: Wm remains exactly `np.linalg.solve(K, A)` followed by canonical contiguous `<f8`; only the OpenBLAS kernel-dispatch environment is prospectively fixed.
4. Band count, ell extent, array shape, Wm TE<-TE interpretation, compact ordering, and no-tolerance exact-comparison rule are unchanged.
5. No Layer-A/Layer-B validity threshold, support boundary, covariance/whitening rule, nuisance-SVD criterion, quotient/null criterion, G7 criterion, or G8 rule is modified by Exp073CI.
6. The v0.2 output SHA is deliberately distinct from both historical v0.1 A and B outputs, preventing preferred-replica rescue semantics.

This static PASS establishes that the numerical determinism repair is semantically confined to the linear-solve backend dispatch. It does NOT by itself establish downstream physical validity, readiness increment, actual G7 authorization, or permission to jump to G8.

## Readiness and next gate

Article-3 readiness remains `Verified 52.0% | Draft/data 53.7%`. No frozen readiness ledger has yet prospectively accepted Exp073CI v0.2 for a readiness increment.

Exact next permitted gate: inspect the frozen Article-3 readiness ledger and downstream dependency records to determine whether a prospective ledger amendment can accept the new v0.2 deterministic finalizer as the repeatable Wm_S2 numerical primitive without bypassing the preserved gate order. Any ledger change must explicitly preserve Exp073CF historical FAIL and must not claim G7/G8 readiness that has not separately satisfied the physical support-validity, Layer A/B, covariance/whitening, nuisance-rank/SVD, and quotient/relation/null prerequisites.

Home runner remains FREE.
