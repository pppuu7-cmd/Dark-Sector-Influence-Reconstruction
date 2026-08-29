# Exp073P v0.5 hosted prerequisite-join implementation authority freeze

**Frozen:** 2026-08-29 while bound Exp073R1 v0.8 run `33270843577` is still in progress and before any Exp073P v0.5 receipt exists.

## Exact frozen join package

The only join implementation eligible to produce the hosted prerequisite authority receipt is:

- preregistration `experiments/073p_v0_5_hosted_r1_v0_8_prerequisite_join_prereg.md` — Git blob `14572cff513d0efd362c68d3f8a74d18378fed23`;
- evaluator `ci/exp073p_v0_5_hosted_r1_authority_join.py` — Git blob `1fca8a3b45a0b591d9a8fc07c9e5d566a0b11478`;
- workflow `.github/workflows/exp073p-v0-5-hosted-r1-authority-join.yml` — Git blob `890009254a2590b365376270bd31a8219372c9ed`.

These were frozen before the bound R1 run reached a terminal conclusion. No later edit may inherit this authority silently.

## Bound upstream

The join remains bound only to:

- R1 run `33270843577`;
- R1 job `99148916507`;
- head `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- workflow ID `345506303`;
- workflow path `.github/workflows/exp073r1-desy1-github-hosted-wholestream-retry-v0-8.yml`;
- expected artifact `exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536`.

No replacement run may be selected after seeing results.

## Result authority

Only a receipt emitted by this frozen evaluator and satisfying all preregistered PASS checks may carry:

`PASS_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED`

with `synthetic=false` and `support_executor_authorized=true`.

Any bound upstream non-success remains `INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED`; any identity/contract contradiction remains `INVALID_FOR_SCIENCE_EXP073P_PREREQUISITE_BINDING_V0_5_HOSTED`.

This layer does not score physical support, covariance, nuisance structure, relation/null statistics or G7/G8/G9.

## Downstream boundary

A PASS receipt from this package may authorize only the separately frozen Article-3 real physical-support executor. It is not itself `PASS_PHYSICAL_SUPPORT_ARTICLE3` and cannot authorize covariance/whitening.