# DSIR recovery checkpoint — Exp073BF->BA coverage audit, BA/BD active

**Date:** 2026-08-31  
**Authority scope:** Article 3 / G7 pre-support angular production  
**Scientific authority readiness:** **52.0% — unchanged**  
**Draft/data readiness:** **53.7% — unchanged**

Repository/hosted authority outranks chat wording. This checkpoint does not authorize covariance/whitening, G7 closure, or G8.

## 1. Exp073BA clean rerun status

Hosted run `33345968620` remains `in_progress`.

Both independent compact replicas A/B have successfully completed:

- prospective freeze enforcement;
- exact NaMaster 2.7 installation;
- immutable Exp073AZ artifact download;
- exact admitted AZ PCL binding.

Both are still inside `Compute low-memory compact Wm_S1 replica`. No BA artifact exists yet; compact comparator, finalizers and final comparator have not run. Therefore no scientific PASS/FAIL is assigned.

## 2. Exp073BD provisional Wm_S2 status

Hosted run `33342265114` remains `in_progress`.

Both provisional branches A/B are still inside `Compute independent Wm_S2 provisional branch` after passing setup, Track-P enforcement, exact NaMaster installation, artifact download and DES Y1 mask download. No BD artifact exists yet. No preferred branch is selected and no duplicate heavy run was launched.

## 3. New independent implementation-coverage audit

Created `docs/EXP073BF_TO_EXP073BA_IMPLEMENTATION_COVERAGE_AUDIT_2026-08-31.md` in commit `e927675fc31a85fbe39a5c0cb01b424bf4f5ef42`.

Audit conclusion:

`PASS_EXP073BF_TO_EXP073BA_IMPLEMENTATION_COVERAGE_AUDIT_2026_08_31`

The hosted Exp073BF small-scale route independently exercises the same Wm low-memory algebraic sequence used by BA: `G02=get_general_coupling_matrix(pcl,0,2,0,2)`, fixed-order row compression, fixed-order construction of `K`, and `solve(K,A)`. The audit explicitly records that BF does not validate full-scale resource behavior, DES physical inputs, BA cross-run exact reproducibility, artifact serialization, compact/final exact comparators, support validity, Layer A/B, covariance or later G7/G8 stages.

The synthetic BF `1e-12` criterion remains synthetic QA only and cannot be transferred to BA. BA remains exact-equality only.

## 4. Immutable negative result

Exp073AQ remains permanent:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

No tolerance/ULP/rounding/preferred-replica rescue is introduced.

## 5. Accounting and firewall

- Verified scientific authority: **52.0%**.
- Draft/data readiness: **53.7%** (`53.714285714285715%` exact ledger value).
- BF->BA static audit: `+0` scientific, `+0` draft/data.
- Synthetic/infrastructure/provenance QA never raises scientific authority readiness.
- G7 order remains: validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family.
- G8 must not be jumped.

## 6. Exact next gate

1. Inspect Exp073BA run `33345968620` first on the next cycle. Consume immutable compact A/B artifacts and exact comparator only when they exist.
2. Inspect Exp073BD run `33342265114` without launching a duplicate. Preserve both branches.
3. If BA terminal exact authority is PASS, admit Wm_S1 only under the frozen low-memory authority class and proceed prospectively to Track-A Wm_S2.
4. If BA terminates before scientific output, classify infrastructure/resource failure separately; if it reaches exact comparator and differs, classify under the frozen scientific rule without rescue.

`Verified: 52.0% | Draft/data: 53.7%`