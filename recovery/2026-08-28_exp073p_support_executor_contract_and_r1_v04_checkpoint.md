# Exp073P prospective support-executor contract + Exp073R1 v0.4 checkpoint — 2026-08-28

## Classification

This checkpoint is prospective implementation/reproducibility work only. It does **not** evaluate the real Exp073P support mask, compute a real-data `f_invalid`, or authorize covariance/whitening, nuisance SVD, relation/null, or G8.

## Live Exp073R1 state

Canonical whole-stream-bound microshard run: `33160570463`, workflow `.github/workflows/exp073r1-desy1-canonical-microshards-v0-4.yml`, head SHA `e61c61a370cdc4cee5da2aa26cc677a6ad373c70`.

At this checkpoint:

- preflight: success;
- canonical source whole-stream manifest: success;
- canonical metacal whole-stream manifest: success;
- shard 0/32: in progress inside the deterministic canonical-bound microshard step;
- later visible shards: queued;
- no final Exp073R1 classification exists yet.

No duplicate R1 run is dispatched. The canonical manifests remain non-science provenance components and cannot substitute for the final exact `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` mask-reproduction status.

## Prior Exp073P split-provenance join verified

Workflow run `33166411136` completed `success` for `Exp073P split-provenance join contract self-test v0.1`. This is a reproducibility-contract PASS only, not a physical-support PASS.

## Independent prospective package added

The preregistered Exp073P P3--P8 semantics now have an additional synthetic executable contract:

- `ci/exp073p_support_executor_contract_selftest_v0_1.py`;
- `.github/workflows/exp073p-support-executor-contract-selftest-v0-1.yml`.

The self-test freezes/tests without reading real observables:

1. the exact finite DES harmonic band edges and explicit multipole coverage; no effective-ell compression, hidden ell cut, or tail extrapolation;
2. signed Wm response remains signed while only the support envelope uses `abs(response)`;
3. positive support normalization is over the full supplied radial domain before rectangle membership, so low/high-z and high-k tails remain in the denominator and invalid numerator;
4. the exact inclusive `f_invalid <= 0.05` boundary;
5. non-positive envelope normalization is reproduction/numerical failure rather than support FAIL;
6. forbidden fiducial/model weighting, covariance/whitening, nuisance, relation/null, G8/held-out, and ad-hoc cut keys fail closed;
7. full coordinates are formed only by intersection after Wm, WW and BOSS-mm block-local masks exist;
8. the retained-dimension boundary remains exactly `>= 15`;
9. a final genuine R1 PASS is necessary before the real support executor can be authorized; root manifests/checksums alone are insufficient.

This package is intentionally synthetic and cannot classify Exp073P on real data.

## Gate state

- validated forward/input lineage: complete up to the still-running final R1 reproduction prerequisite;
- Exp073P physical-support mask: preregistered, **not evaluated**;
- covariance/whitening: BLOCKED;
- nuisance rank/SVD: BLOCKED;
- quotient/relation/null: BLOCKED;
- fresh G8 withheld family: BLOCKED.

No frozen scientific criterion was changed.