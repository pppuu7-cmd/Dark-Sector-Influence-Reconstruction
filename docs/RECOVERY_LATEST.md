# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-08-31  
**Article-3 scientific authority readiness:** **52.0%**  
**Article-3 draft/data readiness:** **53.714285714285715%** (display **53.7%**)  
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state and immutable hosted artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical-QA work gives `+0` scientific readiness. Track-P provisional work never becomes Track-A authority retroactively.

## Read first

1. `recovery/2026-08-31_exp073bd_p3_incomplete_ba_active.md`
2. `recovery/2026-08-31_exp073be_ba_harness_rerun_wms2_active.md`
3. this file
4. `docs/EXP073BA_BD_TERMINAL_OUTCOME_DECISION_TABLE_2026-08-31.md`
5. `experiments/073bg_article3_active_ba_bd_terminal_outcome_policy_v0_1_prereg.md`
6. `docs/RECOVERY_MANUAL_LIVE_2026-08-30.md`
7. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`
8. `recovery/2026-08-31_dual_readiness_accounting_frozen.md`
9. `experiments/073bb_article3_provisional_dual_track_evidence_policy_v0_1_prereg.md`
10. `docs/ARTICLE3_PROVISIONAL_RECOMPUTE_LEDGER_2026-08-31.md`
11. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
12. Exp073AZ/BC/BA/BF preregistration and recovery records as needed.

## Current authority state

- Exp073AQ remains permanent hosted exact-repeatability scientific FAIL under its historical class. It is never erased or rescued by numerical closeness.
- Exp073AZ exact mask-PCL predecessor authority is PASS and remains only a predecessor authority.
- Exp073BC AZ->BA binding is frozen and Exp073BE provenance diagnostic passed with `+0` scientific readiness.
- Exp073BF hosted small-scale Wm stock-equivalence QA passed, but is synthetic/infrastructure QA only and gives `+0` readiness.
- Exp073BA clean rerun `33345968620` remains active. Both A/B jobs passed frozen enforcement, NaMaster 2.7 installation, immutable AZ artifact download, and exact PCL binding; both are in `Compute low-memory compact Wm_S1 replica`. No BA comparator authority exists yet, so no BA scientific PASS/FAIL may be claimed.
- Exp073BD provisional Wm_S2 run `33342265114` is terminal `cancelled` and is frozen-classified as **`P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`**. Branch A was cancelled during science compute and preserved only a PCL `<f8 [12288]` intermediate; branch B completed a full `<f8 [39,12288]` object; pair diagnostic was skipped. This is an incomplete provisional outcome, **not** a scientific FAIL. Branch B is not preferred and receives no standalone draft/data credit.

## Exp073BD terminal evidence

Run `33342265114`, source head `2990c51ec1ec263eb883398b21356770401ee83a`, terminal update `2026-08-31T05:33:05Z`.

Branch A:

- job `99339920252`: `cancelled` during `Compute independent Wm_S2 provisional branch`;
- artifact `9746718704`, digest `sha256:e7ab0b3859070441532d8778f51faf9c3d7e7a0d6afe8af2546995067b5e15e5`;
- payload is only PCL `<f8 [12288]`, SHA `16e00d60e8298f94ab6e5d223db823231b84df3b7b588a017acbb208a1dbdb64`.

Branch B:

- job `99339920262`: success;
- artifact `9746250767`, digest `sha256:3bd4850d9f768fd36cad34788394b913507d71ec828dee7a68544b44ce6f7481`;
- full payload `<f8 [39,12288]`, SHA `10d12a10965b49c9dbba4638c91bd81c0b40cc35bd0d464c8ca837b5231dcb26`;
- metadata remains `provisional_only=true`, `science_use=FORBIDDEN`.

Pair diagnostic job `99339920344` was skipped. Under the prospectively frozen Exp073BG rule, missing/incomplete branch => `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`; therefore Wm_S2 earns `+0` Verified and `+0` Draft/data in this run.

Both inspected BD metadata JSONs also contain `experiment="Exp073AZ"` despite `contract_version="exp073bd_v0_1"`. Preserve this as a metadata/provenance defect only; do not claim it caused branch-A cancellation and do not repair history post hoc.

## Exp073BG — terminal-outcome interpretation frozen before results

Normative decision table commit:

`e4a8391d671c3835c00f729a4743e7c07cb3199e`

Preregistration commit:

`acaf245a7ecde87633c87b30d54e160bbb7b928f`

The policy was frozen while both heavy runs were still `in_progress`, before terminal numerical outcomes were known.

### BA classification

- Timeout/OOM/runner/dependency/harness failure or missing valid artifact before a frozen exact comparator has two complete valid inputs => infrastructure/resource/harness failure, **not** scientific FAIL.
- Frozen exact comparator supplied two complete valid Track-A replicas and reports inequality => scientific exact-repeatability FAIL for that BA stage, irrespective of numerical magnitude.
- BA scientific PASS requires the complete frozen chain: exact compact PASS -> both finalizers -> exact final PASS -> immutable valid authority artifact.
- BA individual angular authority itself adds `+0` scientific readiness under the frozen ledger.

### BD classification

- Incomplete/missing branch => `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`; no Wm_S2 draft/data credit.
- Two complete finite `[39,12288]` branches plus valid pair diagnostic would have formed a provisional branch-pair object eligible for downstream sensitivity propagation; that condition was not met in run `33342265114`.
- Exact A/B equality, if ever observed in a Track-P successor, does not turn Track P into Track-A authority.
- `downstream_claim_classification=NOT_YET_EVALUATED` is not a P1/P2 manuscript-claim authorization.

## Frozen physical/support boundaries

Never alter post hoc:

- `0.295 <= z <= 2.33` inclusive;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- Layer-A `operator_f_invalid <= 0.05` inclusive;
- Layer-B invalid-row fraction `<= 0.05` inclusive;
- final retained observation dimension `>=15`;
- DES `NSIDE=4096`;
- true ell `0..12287`, 39 frozen bands;
- Wm `TE <- TE`, WW `EE <- EE`;
- canonical selected window `<f8 [39,12288]`;
- positive absolute operator/window envelope only for support bookkeeping; measured Wm remains signed;
- no effective ell/z/k or fiducial-P shortcut;
- exact-threshold ambiguity remains `numerically_unresolved`;
- no covariance/whitening/nuisance/quotient/relation/null/G8 leakage into earlier support selection.

## Required G7 order

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

G8 may not be selected/exposed before actual G7 authorization. Individual angular-window completion does not authorize covariance/whitening or G8.

## Exact next operating gate

1. Inspect Exp073BA `33345968620` first and classify its terminal state strictly under Exp073BG and the frozen BA comparator artifacts.
2. If both complete compact replicas reach the frozen comparator, consume only the frozen exact comparator result.
3. Exact compact PASS is required before both finalizers; BA authority requires final exact PASS plus immutable hosted authority artifact.
4. If BA remains active, perform only independent prerequisite/validation/audit work; do not create a competing heavy control plane.
5. Do not salvage/relaunch historical Exp073BD as though it were complete. Any future Wm_S2 attempt must be a separately prospectively frozen successor after the required upstream authorization.
6. Continue angular authority in order, then real 14-window aggregate and physical support prerequisites before Layer A/B and covariance/whitening.

## Current shorthand

- ✅ Exp073AZ predecessor PCL authority: PASS.
- ✅ Exp073BC/BE provenance binding route: closed, `+0` scientific readiness.
- ✅ Exp073BF Wm algorithm QA: PASS, synthetic/infrastructure only, `+0`.
- ✅ Exp073BG terminal-outcome decision policy: prospectively frozen, `+0/+0`.
- ✅ Exp073BD `33342265114`: terminal **P3 provisional incomplete**, `+0/+0`; no downstream use.
- 🟡 Exp073BA `33345968620`: active heavy Track-A Wm_S1 computation.
- ❌ Exp073AQ: permanent exact-repeatability scientific FAIL.
- ❌ Layer A/B: not yet authorized.
- ❌ covariance/whitening: blocked.
- ❌ G7: open.
- ❌ G8: open and forbidden to jump.
- ❌ G9: open.

`Verified: 52.0% | Draft/data: 53.7%`
