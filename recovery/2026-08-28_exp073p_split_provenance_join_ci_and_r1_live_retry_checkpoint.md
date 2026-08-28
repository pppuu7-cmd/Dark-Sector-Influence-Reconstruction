# Exp073P split-provenance join CI + Exp073R1 live retry checkpoint — 2026-08-28

## Classification

This checkpoint records reproducibility/infrastructure state only. It is **not** an Exp073P scientific classification and it does not authorize covariance restriction/whitening or any later G7/G8 stage.

## Exp073R1 live state

Canonical sharded Exp073R1 workflow run: `33135622749`.

At this checkpoint, latest-attempt job state is:

- shard 0: `success`;
- shards 1, 2, 3, 4: `in_progress`;
- shards 5, 6, 7: `failure`.

The prior successful shard-0 result remains a non-science reproduction component only. There is no full Exp073R1 PASS while any required shard is missing or failed. No new heavy workflow is dispatched from this checkpoint, because live shard jobs are still executing and duplicate compute is forbidden.

## Independent work closed in this iteration

The preregistered Exp073P split-provenance aggregate-join contract already present on `main` now has an executable lightweight GitHub Actions self-test:

`.github/workflows/exp073p-split-provenance-join-contract-selftest-v0-1.yml`

The workflow compiles and executes:

`ci/exp073p_split_provenance_join_contract_selftest_v0_1.py`

and additionally asserts that:

1. the join remains explicitly non-science;
2. a genuine `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` remains mandatory;
3. frozen Exp073P bookkeeping constants remain represented in the contract;
4. the CI script does not acquire covariance/whitening or map-reading evaluation logic.

First CI run: `33166411136`.

Result: `success`, including compile, contract execution, and the explicit non-science/R1-mandatory binding assertion. This is a **reproducibility-contract PASS only**; it is not a physical-support PASS.

## Gate order preserved

The admissible order remains:

1. validated physical forward/power-input bridges;
2. complete Exp073R1 reproduction PASS and the preregistered aggregate provenance join;
3. preregistered Exp073P physical support-validity mask;
4. covariance restriction/whitening;
5. nuisance tangent rank/SVD;
6. quotient/relation/null control;
7. only then a fresh G8 withheld family.

No frozen scientific acceptance criterion was changed. Existing infrastructure failures remain infrastructure/reproduction INCOMPLETE rather than scientific FAIL.
