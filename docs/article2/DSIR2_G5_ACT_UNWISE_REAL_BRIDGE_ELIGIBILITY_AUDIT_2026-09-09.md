# DSIR-2 G5 ACT x unWISE real-bridge eligibility audit — 2026-09-09

Status: SUPPORT / BLOCKER-NARROWING AUDIT. Scope: Article 2 G5 only. No G5 real stress output is scored here.

## Question

Can the already-existing ACT x unWISE real observational/covariance chain be used immediately as the real observation/operator+covariance bridge required by `DSIR2_G5_DATA_WHITENED_CROSS_FAMILY_STRESS_CONTRACT_V0_1.md`?

## What is already authoritative enough

The existing ACT x unWISE chain reconstructs a concrete real observable vector and covariance:

- samples `Blue_ACT`, `Green_ACT`;
- per sample: six selected `gg` bandpowers and seven selected `kg` bandpowers;
- exact joint observable order of 26 coordinates;
- exact released same-sample covariances plus released Blue/Green cross covariance;
- selected joint covariance shape `26 x 26`;
- direct Cholesky route with explicit symmetry/factorization/whitening/roundtrip controls;
- pinned external likelihood/code commit and data archive digest.

The existing physical-forward reproduction also proves a pinned linear/no-CLEFT CAMB-based physical provider can be propagated through the released ACT x unWISE tracer/kernel implementation while reproducing the pinned upstream raw forward semantics.

Therefore the **real covariance and observation-operator machinery exists** and should be reused rather than rebuilt.

## Missing cross-family compatibility proof

The G5 closure contract is stronger: it requires multiple DSIR family/model response rows mapped into the **same exact 26-coordinate vector** on which the bound covariance acts.

At this audit no committed authority was located proving that the current C1/C2/C3/C5 (or another frozen representative multi-family set) has already been propagated through the exact same ACT x unWISE 26-coordinate forward operator with:

- immutable model-instance/family IDs;
- exact common-valid coordinate mask;
- matched units/order;
- no zero imputation;
- no family-specific observable redefinition;
- the same frozen 26 x 26 covariance.

The current physical-forward reproduction is therefore an eligible **baseline/provider bridge**, not yet a complete cross-family G5 input matrix.

## Consequence

Do not run the classifying real G5 stress by inserting existing theory-atlas vectors directly into the ACT x unWISE covariance. Their coordinates are not identical.

The shortest admissible Article-2 path is:

1. prospectively freeze a model-provider interface that accepts the already-frozen representative DSIR family perturbations/manifolds and produces the exact ACT x unWISE raw provider quantities required by the pinned forward code;
2. propagate a frozen representative multi-family inventory through the exact same 26-coordinate operator;
3. create one immutable machine-readable `model_instance x 26` response matrix plus validity/family/provenance metadata;
4. verify exact coordinate/order/unit compatibility with the already-bound 26 x 26 covariance;
5. only then execute the already-frozen G5 stress cases A-E and closure audit.

## Current Article-2 state

- G5 closure contract: FROZEN;
- G5 synthetic implementation QA: PASS;
- real covariance/operator machinery: LOCATED / REUSABLE;
- cross-family theory -> exact 26-coordinate bridge: NOT YET BOUND;
- classifying G5 real execution: NOT YET TESTABLE;
- Article-2 strict repository readiness remains `83.3%`.

This is now an interface/mapping blocker, not a covariance-acquisition or whitening-implementation blocker.
