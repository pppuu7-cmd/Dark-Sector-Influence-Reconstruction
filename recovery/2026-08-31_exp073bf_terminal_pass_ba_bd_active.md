# DSIR recovery checkpoint — Exp073BF terminal synthetic QA PASS; Exp073BA/BD heavy runs remain active

**Date:** 2026-08-31  
**Authority scope:** Article 3 / G7 pre-support angular route only  
**Scientific authority readiness:** **52.0% — unchanged**  
**Draft/data readiness:** **53.7% — unchanged**

Repository/hosted authority outranks chat wording. RTK/RQIR are excluded.

## Exact chronology

1. Read `recovery/2026-08-31_exp073be_ba_harness_rerun_wms2_active.md`, then `docs/RECOVERY_LATEST.md`, the frozen dual-readiness/accounting state and the latest Exp073BF checkpoint.
2. Re-inspected Exp073BA clean rerun `33345968620`. Both independent compact replicas passed prospective-freeze enforcement, exact NaMaster 2.7 installation, immutable Exp073AZ artifact download and exact admitted-PCL binding. Both remain in `Compute low-memory compact Wm_S1 replica`. No BA artifact exists yet, so no scientific PASS/FAIL classification is permitted.
3. Re-inspected Exp073BD provisional Wm_S2 run `33342265114`. Both A/B branches passed Track-P freeze enforcement, NaMaster 2.7 installation, frozen input-artifact download and DES Y1 lens-mask acquisition. Both remain in `Compute independent Wm_S2 provisional branch`. No BD artifact exists yet and no preferred branch is selected.
4. Checked latest Actions to avoid a duplicate user-started heavy control plane. No newer heavy DSIR production run superseding BA/BD was present; Exp073BF was the latest workflow and had become terminal.
5. Consumed terminal hosted Exp073BF run `33349183295` and its artifact rather than launching another heavy calculation.
6. Exp073BF terminal token is `PASS_EXP073BF_WM_STOCK_EQUIVALENCE_QA_V0_1` under the prospectively frozen **synthetic numerical/infrastructure QA** contract.
7. Recorded terminal Exp073BF result in `docs/RECOVERY_MANUAL_ADDENDUM_EXP073BF_2026-08-31.md` in commit `ec273e12def50716932c5878dc75ff91f00d9df9`.

## Exp073BF terminal hosted result

Frozen hosted environment/contract: NaMaster/PyMaster 2.7, deterministic synthetic Wm spin-0 x spin-2 case, NSIDE=16, L=48, six fixed bands, single-thread controls.

Result:

- stock selected window shape `[6,48]`;
- low-memory reconstructed shape `[6,48]`;
- all finite: `true`;
- `max_abs(stock-reconstructed) = 8.326672684688674e-16`;
- frozen synthetic-QA acceptance threshold: `< 1e-12`;
- repeated same-input `get_general_coupling_matrix(PCL,0,2,0,2)` exact equality: `true`;
- stock SHA-256 `4699aea68c2e6c6bb0ff3d5938bb5bda18352e0287f093ea7b8c133af36ec35c`;
- reconstructed SHA-256 `fcd98c4bb21be5dda8dc1cf6d33971a5d4e33333ebaf0fb4e122e8d789c0fb3e`;
- artifact ID `9743025349`;
- artifact digest `sha256:b39c8449f1752c4f7cd985829620da82be4de86fde8f135206453c91baddf9b1`.

Interpretation is deliberately narrow: this closes the previously identified implementation-QA gap for the Wm spin-0 x spin-2 low-memory algebra. It does **not** classify Exp073BA, does not prove cross-runner exact reproducibility, and cannot supply a tolerance rescue to any scientific exact comparator.

## Frozen authority/accounting state

Exp073AQ remains permanently:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.

No scientific acceptance threshold was changed. No tolerance, rounding, ULP, preferred-replica or majority-vote rescue was introduced.

Exp073BF is synthetic/infrastructure QA and therefore contributes:

- scientific readiness increment: `+0`;
- draft/data readiness increment: `+0`.

Current dashboard remains:

`Verified: 52.0% | Draft/data: 53.7%`

## Current status

- ✅ Exp073AZ exact mask-PCL predecessor: hosted exact PASS, +0 readiness.
- ✅ Exp073BC immutable AZ->BA binding receipt: frozen.
- ✅ Exp073BE provenance/harness diagnostic: PASS, +0 readiness.
- ✅ Exp073BF Wm spin-0 x spin-2 stock-equivalence QA: terminal hosted synthetic-QA PASS, +0/+0 readiness.
- 🟡 Exp073BA run `33345968620`: both real compact Wm_S1 replicas still computing; no artifact/authority yet.
- 🟡 Exp073BD run `33342265114`: both provisional Wm_S2 branches still computing; no artifact yet.
- ❌ Exp073AQ: permanent exact-repeatability scientific FAIL.
- ❌ Layer A, Layer B, covariance/whitening, nuisance SVD, quotient/relation/null, G7, G8 and G9 remain open/not authorized.

## Exact next gate

The next authority-changing gate is **terminal Exp073BA run `33345968620`**. When its compact replicas finish, consume the frozen exact comparator/finalizer and its immutable hosted artifact before any Track-A Wm_S2 succession. If BA is still active at the next inspection, consume any newly completed Exp073BD provisional A/B artifacts together under Track P and perform only non-competing validation/prerequisite work. Never use provisional BD to substitute for Track-A authorization.

G7 ordering remains immutable: validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> factual G7 authorization -> fresh G8 withheld family.