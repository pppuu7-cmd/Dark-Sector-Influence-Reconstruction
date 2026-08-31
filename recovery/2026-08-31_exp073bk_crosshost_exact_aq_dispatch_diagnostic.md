# DSIR recovery checkpoint — Exp073BK cross-host exact finalizer QA and AQ dispatch diagnostic

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Classification:** nonclassifying numerical/root-cause QA, `+0/+0`.

## Terminal Exp073BK

Run `33383770182` completed successfully.

Replica jobs:
- A `99461686927` — AMD EPYC 9V74;
- B `99461686872` — AMD EPYC 9V74;
- C `99461686803` — AMD EPYC 7763;
- D `99461686678` — AMD EPYC 7763.

Comparator job `99461909878` completed successfully.
Comparator artifact `9754784036`, digest `sha256:8ac37cbcb504f57ce19dd88274a5b04d8076d3a29580b532aa208d6d6cef7f98`.

All policies `default_t1`, `haswell_t1`, `default_t2`, `haswell_t2` were `EXACT_CROSSHOST_EQUAL`. Every W SHA was:

`ae2b070b84e5f763d77216fe35aab2921074469a881845c015302918018d03aa`.

Exp073BK is nonclassifying and gives no readiness credit.

## AQ root-cause narrowing

Historical AQ A/B used same nominal software versions and one-thread controls but did not expose identical runtime SIMD feature sets: AQ A was effectively X86_V3 while AQ B exposed X86_V4/AVX-512. A local causal test on the immutable real Exp073BD compact A showed that changing only OpenBLAS microkernel dispatch can change 82.17% of final W entries, with max abs difference `2.7755575615628914e-17`, comparable to AQ's `2.0816681711721685e-17` scale.

However AQ used stock NaMaster `NmtWorkspace.compute_coupling_matrix()` and `get_bandpower_windows()`, not the later Python low-memory solve. Therefore the dispatch result is a causal demonstration for the finalizer class of operations, not proof of the specific AQ internal causal path.

The BK EPYC 9V74 runner inspected after completion exposed only X86_V3, unlike historical AQ B on the same model name. Hypervisor-exposed SIMD/runtime feature set, not CPU model string alone, must therefore be considered part of exact numerical provenance.

## Deterministic-LU candidate

A local fixed-operation partial-pivot LU solve on the same real compact A produced canonical W SHA

`f3a22c35dff1f3b27f5f22e7966c1c926fbbc3a965293f88a9bf0b84fa97cf79`

unchanged under local Haswell/SkylakeX/Zen2 dispatch settings, with `max(abs(WQ-I))=1.2212453270876722e-15` and ordinary float64-level high-precision agreement. This authorizes consideration of a separately frozen hosted cross-host QA only; it is not authority.

Full audit: `docs/ARTICLE3_AQ_NUMERICAL_DISPATCH_AND_EXP073BK_AUDIT_2026-08-31.md`.

## Active classifying gate

Exp073BJ run `33379013167` remains the sole heavy Track-A Wm_S1 control plane unless terminal status has changed since this checkpoint. Do not duplicate it. Preserve its frozen exact comparator before all supplementary diagnostics.

## Accounting

`Verified: 52.0% | Draft/data: 53.7%`

Exp073AQ permanent FAIL preserved. Layer A/B, covariance/whitening, G7/G8/G9 remain unauthorized. No G8 jump.
