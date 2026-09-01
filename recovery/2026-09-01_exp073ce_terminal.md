# Exp073CE terminal — memory-stable Wm PCL hosted exact-equivalence QA

**Date:** 2026-09-01  
**Classification:** infrastructure/methodology hosted QA only; `+0/+0`; no Article-3 readiness credit.

## Coordination and authority

Before this write, GitHub Actions reported zero `in_progress` DSIR runs and exactly one queued run: Exp073CA attempt3 `33448843621`. The queued Exp073CA self-hosted frontier remains untouched. Home runner remains **OFFLINE/LOCKED**; no self-hosted trigger, rerun, WSL configuration, or alternative self-hosted workflow was used.

Preserved authority: Exp073BJ exact Track-A Wm_S1 PASS; Exp073AQ permanent historical exact-repeatability scientific FAIL; Exp073BD provisional/incomplete and forbidden downstream; Exp073BV source-lineage PASS; Exp073BW exact streaming-equivalence PASS; Exp073BZ checkpoint/failover PASS; Exp073CA attempt3 remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`; Exp073CC Q1 and Exp073CD Q1 remain synthetic/nonclassifying exact-equivalence PASS.

## Immutable execution provenance

- Experiment: `Exp073CE`
- Hosted run: `33523714876`
- Hosted job: `99909080713`
- Run conclusion: `success`
- Head/trigger commit: `3f07c0d0450d49641dcad3319184d89562d3d72f`
- Immutable artifact id: `9806792097`
- Artifact name: `exp073ce-hosted-memory-stable-exact-selftest-3f07c0d0450d49641dcad3319184d89562d3d72f`
- Artifact digest: `sha256:b8403d7997b2f1705f1163c9882be04558fd7272904de00f5a29e6d4cdefc857`
- Artifact created: `2026-09-01T15:07:49Z`
- Frozen preregistration commit: `54c46425349bedfce0ecf4bdca33ea214766d27c`
- Frozen helper commit: `07ed390e08a68b7ae17f8a58ad4fa882bb082f09`
- Frozen hosted workflow commit: `219b0db48113ef00f872ff753ed42cf5cf51b54f`
- Frozen binding commit: `9b6d1470e669405dd85e41583f38df89a8eabf30`

## Frozen receipt result

The immutable `exp073ce_receipt.json` reports `status = CE_Q1_MEMORY_STABLE_EXACT_EQUIVALENCE_PASS`, `science_gate_scored = false`, `verified_delta = 0.0`, `draft_data_delta = 0.0`.

All frozen synthetic cases `NSIDE={64,128,256}` completed and satisfied every preregistered exact condition:

- runtime `ainfo_mask.lmax` oracle and spill values agree and equal `3*nside-1`: `191`, `383`, `767`;
- first-mask ALM canonical dtype is `<c16>`;
- saved and reloaded ALM SHA-256 are exactly identical in every case;
- reloaded mapping is non-writeable in every case;
- oracle and spill PCL are finite with identical shapes;
- `np.array_equal(oracle_pcl, spill_pcl) == true` in every case;
- canonical `<f8>` final-PCL SHA-256 is exactly identical in every case;
- no tolerance, ULP, rounding, smoothing, averaging, preferred-replica, or alternate acceptance rule was used.

Case receipts:

- NSIDE 64: ALM SHA `748415ef73a18be294e58abfcfc3797953dfe7f69ca5925768d389a17f0aed06`; PCL SHA `57df5d50be6d1a3342a92aab9f5901000e158da58da1458df1381cd2d519be8f`.
- NSIDE 128: ALM SHA `ff26f94cdcb108e7a1b66517d73d184d79f4e433f1c4647f0f02bb61fd51d5d2`; PCL SHA `e6fab6d8a40d213dedf30f7cebd4df866845d9880b82e80090d48407b236aa7f`.
- NSIDE 256: ALM SHA `bfe3cd973aef552ae39ea107823430643dd0087f69c56a7f3f79e80973c338f0`; PCL SHA `1a61b60b947aee236236fd5777b98f71e5f55f626f77097288560e99f3656e6f`.

`/usr/bin/time -v` for the hosted selftest reported maximum RSS `172380 KiB`, no swaps, and exit status 0. This RSS is infrastructure diagnostic only and is not extrapolated into a claim that full `NSIDE=4096` is safe under the current 6 GiB WSL cap.

## Terminal classification

The preregistered branch applies exactly:

`CE_Q1_MEMORY_STABLE_EXACT_EQUIVALENCE_PASS`

This establishes hosted synthetic exact equivalence of the prospectively frozen production-semantic sequential/spill/reload PCL implementation package at the tested geometries. It does **not** close Wm_S2, does not classify Exp073CA scientifically, and does not authorize any real-survey/full-scale self-hosted execution while the overnight lock remains active.

**Readiness:** Verified **52.0%** | Draft/data **53.7%**, unchanged.  
**Delta:** `+0/+0`.  
**Home runner:** **OFFLINE/LOCKED**.

## Exact next scientifically permitted gate

While the home runner remains locked, no full-scale Wm_S2 successor may be triggered. The next permitted work is a repository-side, read-only/frozen integration audit of the CE package against the future full-scale successor wiring, restricted to proving that only the PCL lifetime/storage implementation changes while the frozen Exp073CA scientific inputs, `NmtField` semantics, runtime `pcl_lmax` receipt/assertion, `hp.alm2cl`, compact/checkpoint/finalizer/comparator lineages, thread policy, and <=60 s heartbeat contract remain unchanged. If that audit finds no additional independent hosted QA of scientific value, the next actual scientific frontier remains a fresh full-scale Wm_S2 successor only after the user explicitly re-enables the home runner and infrastructure preflight passes.