# Article 3 / Exp073P physical-support semantic reconciliation checkpoint

**Date:** 2026-08-29  
**Status:** pre-real-support-score semantic audit; no scientific gate scored.

## Finding

Two independently preregistered support contracts exist in the repository and must not be silently collapsed into one quantity merely because both use the label `f_invalid` and the same numerical threshold `0.05`.

### A. Exp073P operator-support fraction

Authoritative source:

`experiments/073p_cosmotheka_desy1_boss_exact_common_physical_support_prereg_v0_1.md`

For every finite harmonic Wm/WW response row, Exp073P propagates the **positive absolute bandpower-window response envelope** through the frozen redshift kernels into `(k,z)`. Its support fraction is

`operator_f_invalid = positive envelope weight outside the frozen rectangle / total positive envelope weight`.

The coordinate-level acceptance is `operator_f_invalid <= 0.05`; only after block-local Wm and WW masks are valid may they be combined with the frozen BOSS mm component, and the retained complete-coordinate dimension must be at least 15.

The existing executable contract self-test `ci/exp073p_frozen_contract_selftest_v0_1.py` deliberately introduces no independent lower-k cut. In the classifying Cosmotheka bookkeeping, however, the frozen Limber mapping `k=(ell+1/2)/chi(z)` is expected to yield positive physical k for valid positive comoving distance. That physical consequence must be checked rather than assumed when the real executor is built.

### B. Article-3 final-coordinate support fraction

Authoritative source:

`docs/ARTICLE3_PHYSICAL_SUPPORT_GATE_CONTRACT_2026-08-28.md`

This later Article-3 contract instead defines a geometrically eligible **final observation coordinate** using canonical float64 `z` and `k_Mpc^-1`, explicitly requiring finite strictly positive `k`, the same upper k boundary, and the same z interval. For every geometrically eligible coordinate it then requires every preregistered component in `final_response_abs_values` to be finite and strictly positive.

Its fraction is therefore

`article3_coordinate_f_invalid = N(geometrically eligible but final-response-envelope invalid) / N(geometrically eligible)`.

This is a count fraction over final coordinates, not an integral/weight fraction over an operator response envelope.

## Consequence

These quantities have different denominators and answer different questions. Therefore:

- `operator_f_invalid` and `article3_coordinate_f_invalid` must have distinct field names in any future combined manifest;
- a PASS of either contract must not be copied into the other contract's `f_invalid` field;
- a PASS of Exp073P does not by itself constitute `PASS_PHYSICAL_SUPPORT_ARTICLE3`;
- a synthetic Article-3 PASS does not constitute an Exp073P operator-support classification;
- failure of one must retain its own frozen scientific/reproduction taxonomy and must not be relabelled as failure of the other;
- no covariance, whitening, nuisance, relation/null or G8 data may be consulted to reconcile the two.

## Frozen pre-output reconciliation rule

Until a dedicated real-execution interface explicitly maps the two stages without changing either scientific definition, **neither support result may be treated as a substitute for the other and covariance restriction remains unauthorized**.

This checkpoint does not add a new scientific threshold and does not require both tests to PASS as a new combined scientific criterion. It only prevents accidental aliasing while the execution architecture is being recovered.

The next implementation task is to reconstruct the intended producer of Article-3 `coordinate_id`, inherited `ordinal`, `(z,k)` and `final_response_abs_values`, and to determine whether that final-coordinate representation is downstream of the Exp073P Wm/WW+BOSS support audit or is an alternative formulation. That determination must be frozen before any real support output is read.

## Current authority state

The prospective upstream authority remains the genuine real Exp073P v0.4 prerequisite receipt bound to Exp073R1 v0.7 run `33240490287`, attempt `3`, job `99142692261`. At this checkpoint no real Exp073P operator-support fraction and no real Article-3 coordinate-support fraction has been evaluated.

Gate state remains:

- G7: OPEN
- G8: OPEN
- G9: OPEN
- covariance restriction/whitening: BLOCKED

**Article-3 scientific readiness remains 44%.**