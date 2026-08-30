# DSIR recovery manual addendum — Exp073AV covariance admission

Read with `docs/RECOVERY_MANUAL.md`, the live 2026-08-30 overlay, Exp073AT/AU addenda, and `docs/RECOVERY_LATEST.md`.

## Immutable scientific state

- strict Article-3 scientific repository readiness: **52%**;
- Layer A/B: OPEN;
- covariance/whitening: BLOCKED until real Layer-A PASS + real Layer-B PASS on the same authority chain;
- G7/G8/G9: OPEN;
- synthetic/provenance/release QA contributes +0 readiness;
- RTK/RQIR remain outside DSIR authority.

## Exp073AV authority

Frozen before any real successor support output or covariance read:

- prereg `b799530c48f8f5325ba1c44e202ebd3ab945e5f2`;
- validator `06e697265927f1139add635c6f9f033502d9689c`;
- workflow `c6363d3c4fef08679ab035cb884943c4d4e99bcc`;
- workflow freeze `5ae1e1e7373a9665e7c20630beab57aae2c8631a`;
- trigger/head `c33404273e54b0645e291f4096c0c38dd9be6add`;
- hosted run `33332732811`, job `99314123379`;
- artifact `9738105208`;
- digest `sha256:96d708a11f2b631aa4e75b121ab2fc3b8aab4fd724b6df3b0d834ce637ff3933`;
- token `PASS_EXP073AV_EXECUTION_QUALIFIED_COVARIANCE_ADMISSION_SYNTHETIC_V0_1`;
- 26/26 synthetic checks passed;
- classification `HOSTED_SYNTHETIC_PASS_NON_SCIENTIFIC_PLUS_0_READINESS`.

## Binding rule

Real covariance may be read only when a single `controlled_single_thread_exact_v1` candidate chain proves all of:

- complete real Exp073AS candidate manifest;
- real Exp073AT-admitted Layer-A terminal PASS `PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`;
- real Exp073AU-admitted Layer-B terminal PASS `PASS_PHYSICAL_SUPPORT_ARTICLE3`;
- exact same candidate-manifest SHA through both support layers;
- Layer-B parent `S_op` SHA equals Layer-A `S_op` SHA;
- final retained coordinate count >=15 in inherited Exp073U order;
- Layer-A and Layer-B exact-threshold ambiguity counts both zero;
- no covariance/nuisance/relation/G8 leakage used to obtain support PASSes.

Any support FAIL/INVALID/infrastructure-INCOMPLETE or authority/provenance mismatch blocks covariance.

## Covariance numerical semantics are NOT superseded

Continue to use `docs/ARTICLE3_COVARIANCE_WHITENING_FAILCLOSED_CONTRACT_V0_1.md` unchanged after Exp073AV admission. In particular preserve:

- exact retained-coordinate binding;
- raw symmetry gate before roundoff-only symmetrization;
- ordinary lower Cholesky with no rescue;
- frozen `tau_sym(d)` and `tau_chol(d)`;
- frozen whitening residual `tau_white=sqrt(eps64)`;
- triangular solves, no explicit inverse;
- no jitter, eigenvalue clipping, nearest-SPD, pseudowhitening or covariance-driven mode deletion.

Covariance invalid states remain numerical/representation invalidity, not evidence for or against dark-sector physics.

## Current production blocker

Exp073AQ run `33327372191` remains active on Wm_S1 replicas A/B. Until it resolves, do not launch Wm_S2 or a duplicate Wm_S1.

## Current order

`AQ Wm_S1 -> remaining exact controlled twins -> Exp073AR -> Exp073AS -> Exp073AT/real Layer A -> Exp073AU/real Layer B -> Exp073AV/real covariance+whitening -> nuisance geometry -> quotient/relation/null -> fresh withheld G8`.
