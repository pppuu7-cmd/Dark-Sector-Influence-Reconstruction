# DSIR current-process ledger

Updated: 2026-09-14. Scope: **DSIR only**; RTK/RQIR/KMQGB/KMDSB excluded.

## Current authoritative frontier — V0.15 terminal

Terminal authority: `docs/dsir4/authority/LAYERB_BETA_CROSS_HOST_FINGERPRINT_V0_15.json`, creation commit `e974d09d9fc4a687da582384da290c8fcb3989e6`.

Run `34792546153`, head `64968099805f6701424881562b1b5263a56d0e0b`; invariant + all 16 `GRID768/GRID1024 × R1..R8` lanes + decision are terminal `success`. Decision job `103820921014`; decision artifact `10328836120`, SHA256 `147aedae7d660c7554078151ee5ed6ba5985b7317ad5b1f3e18e4cb0f75ca1a4`.

Classification: `HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED`, effect `+0/+0`.

The exact V0.13 cross-job response branches reproduce. On all three frozen replay-failure cells, jobs sharing the same prospectively recorded combined hardware/software fingerprint are exactly stable within group (`max within-group spread = 0.0`), while distinct repeated fingerprint groups have group-mean separation at or above the unchanged `<1e-5` technical threshold. Frozen anchors remain valid; fingerprint integrity, finite-value and exact-binding invariants pass; no ephemeral runner/job identifier entered scientific grouping.

This is numerical reproducibility localization only. It does not validate Layer-B science and is not evidence for a dark-sector signal.

## Parent V0.15 factor evidence available for the authorized successor

Representative repeated fingerprint groups show:

- `AMD EPYC 9V74 80-Core Processor` and `INTEL(R) XEON(R) PLATINUM 8573C` occupy the same response branch on the overlapping GRID768 witness and share the same V0.15 software fingerprint; despite different CPU vendor/model, both have the same NumPy-config hash in the frozen fingerprint.
- `AMD EPYC 7763 64-Core Processor` occupies the alternate response branch; relative to the AMD EPYC 9V74 group, every frozen software field is identical except the NumPy-config hash, while CPU model/flags differ.
- Therefore CPU vendor alone is already an implausible separator. The highest-information prospectively testable candidate family is runtime SIMD/AVX-512 capability versus finer CPU-model/runtime confounding.

These parent observations select candidates for the next prospective gate; they are not themselves a causal host-factor claim.

## Authorized successor

V0.15 authorizes exactly:

`PROSPECTIVELY_FROZEN_HOST_FACTOR_ISOLATION_AUDIT`.

The next gate must be frozen before new substantive compute. It should retain the unchanged numerical object/thresholds and use new independent hosted jobs to test a small predeclared factor hierarchy, with a decisive `UNDERPOWERED/CONFOUNDED` outcome if the hosted allocation does not populate the required factor strata.

Recommended frozen factor hierarchy for V0.16:

1. runtime `AVX512F` present vs absent, read directly from `/proc/cpuinfo` flags;
2. exact CPU model key (vendor/family/model/stepping/model name) as a finer nested factor;
3. NumPy runtime/config SIMD signature as a recorded correlated factor, not automatically a causal factor;
4. stable OS/kernel/compiler/toolchain fields as controls.

A confirmatory AVX-512-class result requires independent replication in both factor classes, within-class stability below `1e-5`, between-class failure-cell separation at/above `1e-5`, and valid anchors. If AVX-512 and another candidate remain perfectly confounded, classify as confounded rather than causal.

## Frozen boundaries / anti-duplication

Production `h=1e-4`; scientific response threshold `<1e-3`; replay/determinism threshold `<1e-5`; production sampling `0.00035`; `tol_perturb_integration=1e-12`; exact binding `<=1e-12`; CLASS commit and baseline/precision/extraction identities remain frozen. No full 107-row Layer-B traversal, covariance/whitening/nuisance/relation-null, `Wm_S3`, global 65537 or downstream science gate is authorized.

Frozen readiness remains `ARTICLE3_REPOSITORY_READINESS: 68%` and scientific frontier `67%`; reproducibility diagnosis alone changes neither.

No active DSIR ChatGPT automation and no repository cron/schedule research loop were found in the latest task-state check. Do not launch competing production gates.
