# DSIR recovery checkpoint — Exp073BI frozen parallel-execution QA active

**Date:** 2026-08-31
**Scope:** Article 3 / G7 pre-support angular production, DSIR only
**Scientific authority readiness:** **52.0% — unchanged**
**Draft/data readiness:** **53.714285714285715% (display 53.7%) — unchanged**

Repository state and immutable hosted artifacts outrank chat wording. Synthetic/infrastructure/provenance QA gives `+0` scientific readiness and `+0` draft/data readiness unless a frozen ledger explicitly states otherwise.

## 1. Authority inherited at entry

- Exp073AQ remains permanent hosted exact-repeatability scientific FAIL under its original authority class. Numerical closeness never rescues it.
- Exp073BA clean rerun `33345968620` remains terminal infrastructure/execution incomplete, with no scientific classification.
- Exp073BH run `33370998182` remains terminal infrastructure diagnosis `BH_D2_TIMEOUT_OR_EXTERNAL_CANCELLATION_EVIDENCED`; both BA compact jobs reached the configured 360-minute execution boundary. BH is `+0/+0`.
- Exp073BD run `33342265114` remains terminal `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, `+0/+0`; branch B is not preferred and is not downstream-usable.

## 2. New non-repeating gate

A new prospective gate was frozen before any Exp073BI outcome existed:

- preregistration commit `00893e3e41ce6062d42e9c61cd5357eb54a41333`;
- implementation commit `b5b82e30fd0e02995281121d5776ec687f0fb829`;
- hosted workflow commit `54e4f5c07ec7c9ab6ca177f092fd18437813537b`;
- trigger commit `c4586c02471a0bb096bb82cfe855e9fbeff30677`;
- hosted run `33375467713`.

Exp073BI is a synthetic/infrastructure feasibility test for a fixed two-thread execution policy after Exp073BH_D2. It does not run the full-scale DES classifying problem and cannot create scientific PASS/FAIL.

## 3. Frozen Exp073BI contract

The only execution change under test is fixed two-thread execution (`OMP_NUM_THREADS=2` and matching BLAS/thread controls) on a deterministic small Wm spin-0 x spin-2 problem. The Wm algebra remains:

`general coupling -> fixed band compression -> K -> solve`.

Two independent Python processes must produce complete outputs. `BI_Q1_PARALLEL_EXACT_QA_PASS` requires exact `numpy.array_equal` between the independent outputs plus stock-workspace implementation-equivalence error `<1e-12`. The `1e-12` threshold is synthetic QA only and is forbidden from any future scientific comparator.

All Exp073BA scientific requirements remain inherited unchanged for any later classifying successor: DES `NSIDE=4096`, true ell `0..12287`, 39 bands, Wm `TE <- TE`, exact Exp073AZ PCL binding, exact NaMaster 2.7 lineage, exact compact and final comparators, no tolerance/ULP/rounding/averaging/preferred-replica rescue, and all frozen physical/support thresholds.

## 4. Hosted state at checkpoint

Run `33375467713` is active. The prospective freeze-enforcement step has passed. Exact NaMaster 2.7 environment installation is in progress; the two-thread Wm QA has not yet produced a terminal result or artifact at this checkpoint.

No heavy classifying successor has been launched. This avoids creating a competing control plane while the feasibility gate is unresolved.

## 5. External execution constraint recorded

Current GitHub documentation states that a GitHub-hosted job has a six-hour maximum execution time. This is consistent with the already-frozen Exp073BH_D2 evidence that the BA single-thread jobs reached the configured 360-minute boundary. This external documentation is operational context only; the repository's hosted BA/BH metadata remains the experiment authority for DSIR classification.

## 6. G7 firewall

Required order remains exactly:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

Exp073BI may not authorize Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null control, G7 or G8.

## 7. Exact next gate

1. Consume terminal hosted Exp073BI run `33375467713` and its immutable artifact.
2. If and only if outcome is `BI_Q1_PARALLEL_EXACT_QA_PASS`, prospectively freeze a separate full-scale two-thread Track-A successor before launching it.
3. If BI_Q2 or BI_Q3 occurs, do not launch that full-scale route; instead freeze a different execution-engineering successor.
4. Any future classifying successor must still complete two immutable compact replicas -> frozen exact compact comparison -> both finalizers -> frozen exact final comparison -> immutable hosted authority before scientific PASS exists.

`Verified: 52.0% | Draft/data: 53.7%`
