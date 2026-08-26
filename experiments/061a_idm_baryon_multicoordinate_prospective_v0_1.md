# Experiment 061A — prospective C9 IDM–baryon multicoordinate response test v0.1

Date: 2026-08-26

## Purpose
Execute the first C9 matter-power response after the C9 source family and the exact `(ell,q)` operator were independently frozen. This is a prospective validation of the Exp058A candidate and must not alter any previously frozen scientific choice.

## Immutable ancestry
- Exp058A preregistered the 2D localization+shape path hypothesis before C9 existed as response evidence.
- Exp059A selected C9 = IDM–baryon and froze `cross_idm_b={1e-30,1e-29,1e-28,1e-27,1e-26} cm^2`, `n_index_idm_b=0`, `m_idm=1e9 eV`, source-only.
- Exp060A froze the exact operator from C3/C5/C7/C8 only and passed the no-C9 contamination guard in workflow run 32947173401.

## Frozen response domain
- CLASS upstream: `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.
- Matched reference: identical cosmology with `cross_idm_b=0`.
- `k=[0.001,0.003,0.01,0.03,0.1] h/Mpc`.
- `z=[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`.
- Response: `R(z,k)=ln P_C9(z,k)-ln P_ref(z,k)`.

## Frozen operator
For each response matrix, `ell` is the `R^2`-weighted log-k localization coordinate. `q` is projection of the unit-normalized response minus the training mean onto PC2 fitted only to immutable C3/C5/C7/C8 responses. PC2 sign is deterministic: the first component with magnitude above `1e-12` is positive. `(ell,q)` is standardized by the training-only sample mean and ddof=1 sample standard deviation.

## Prospective gate
PASS requires all of the following, with no exceptions:
1. all four adjacent standardized path step norms are strictly greater than `1e-10`;
2. no two non-adjacent polyline segments intersect using orientation/on-segment tolerance `1e-10`;
3. every leave-one-redshift rebuild, dropping the same redshift from training and C9 blocks and rebuilding PC2/standardization from training only, independently passes the same path gate.

A scientific FAIL is retained as a scientific result. Infrastructure success and scientific PASS are deliberately separated so a negative result is still uploaded and auditable.

## Forbidden after first C9 response
No threshold change, mode rotation, PC sign flip, k/z range change, redshift deletion, coupling deletion/reordering, alternative normalization, tolerance change, or new coordinate definition may be used to relabel this test. Any later hypothesis must receive a new experiment identifier and fresh withheld evidence.

## Prior gate state
- F27: HARD FAIL.
- F28: retrospective only.
- F29: HARD PROSPECTIVE FAIL.
- G7: OPEN.
- G8: OPEN.
- G9: OPEN.
