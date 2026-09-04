# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-04
**Scope:** DSIR only; RTK/RQIR excluded.
**Article-3 readiness:** **Verified 52.0% | Draft/data 54.6%**.

Repository state, immutable recovery notes, validated Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Frozen science boundaries remain unchanged. This file supersedes older live-process wording; historical details remain recoverable from immutable notes and Git history.

## Scientific frontier — Exp073BU Wm_S3 fresh-independent-PCL A/B
Wm_S1 Track-A exact PASS and admitted Wm_S2 authority are preserved. Exp073CR v0.3 remains RESOURCE PASS `+0/+0`. **Wm_S3 scientific angular authority remains absent until the active Exp073BU v0.4 comparator reaches a valid terminal result and the raw evidence is independently consumed against the frozen gate.**

Original science prereg commit/blob: `e1a0332c128c87049fb8699018a3a3e71c9c5321 / 816542c7eb7a8ba4e72d6e01228aa62d05c7c805`.
A/B namespace semantics: `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`.
Exact science PASS requires whole canonical `<f8 [39,12288]` SHA256 equality AND `numpy.array_equal`; no tolerance rescue.

Exact band authority remains `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`, 39 bands, ell `0..12287`, full window `[2,39,2,12288]`, selected `wins[0,:,0,:] = TE<-TE`.

## Current authoritative process — Exp073BU exact science 8-core v0.4
Exactly one heavy/scientific process is active:
- workflow: `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-8core-v0-4.yml`;
- run/job: `33901458494 / 101116305364`;
- activation/source head: `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`;
- run start: `2026-09-04T17:36:14Z`;
- science workflow blob: `f8c70a4206321b0dc10b57f63a2a06163da2249a`;
- fresh checkpoint root: `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`;
- current live state: `IN_PROGRESS`, step `Fresh live exclusivity and Exp073BU 8-core A-then-B science`;
- hosted preflight completed PASS before the self-hosted numerical job;
- live Actions reconciliation: exactly one `in_progress` run (this one), `queued=0`;
- DSIR-HOME-PC is **RESERVED BY EXP073BU**; no competing home/heavy run is permitted.

Partial numerical/checkpoint payloads are not inspected while the frozen run is active. The ledger therefore claims no terminal durable checkpoint identity yet; terminal evidence must establish exact checkpoint provenance. Detailed process ledger and success/fail/blocked actions: `docs/CURRENT_PROCESS.md` (ledger sync commit `4d51ad0b4f504c308818e5172ea175c1efa897c3`).

Execution order remains fresh A -> release replica-local live state -> fresh B -> exact comparator. Required science PASS token is `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3`. Allowed terminal classes remain `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, `BLOCKED`. Workflow success alone is never sufficient.

## 8-core support/activation authority
Exact-equivalence authority is `PASS_EXP073BU_8CORE_EXACT_EQUIVALENCE_V0_3`, run/job `33900913648 / 101114517184`; support-only `+0/+0`.

Exp073BU 8-core v0.4 hosted activation authority is `PASS_EXP073BU_8CORE_ACTIVATION_AUDIT_V0_4`, run/job `33901386471 / 101116035558`, activation head `960b6a06095d28bbe7d2a5f0111d31641d12fc82`, artifact `9947758011`, artifact digest `sha256:1517ccb3cfb2a6f8ee036de1062c7e181494a4b519441089530b418d967d1f7c`. Immutable recovery: `recovery/2026-09-04_exp073bu_8core_v0_4_activation_audit_pass.md`; record commit `422f4b33b77e199112ccf1277739946576d23939`. This is support-only `+0/+0`; no DES-scale Wm_S3 authority.

Prospective v0.4 repair changed only the runtime-probe interpreter from system `python3` to frozen `$NMT_PY`. Numerical implementation blobs remained unchanged from the exact-equivalence-certified 8-core branch. Frozen v0.4 bindings include: workflow blob `f8c70a4206321b0dc10b57f63a2a06163da2249a`, v0.4 prereg blob `819ead893b45f93270133dde32ccaf942401a6c4`, original science prereg blob `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`, 8-core prereg blob `1da32a7647601c2c876c2392bf9e17dfd5a8593e`, driver blob `2b44ddd2c1167739f643a0f1c23cfbf7905fa464`, adapter blob `63ee393791bba43d3eabbea654efdb9d439d477e`, OpenMP source blob `be4f381de4c5c043a9c0fcd107e63ef3f2079578`, launcher blob `8a725ba135e3e120ce6e8d0db3dd14d95d4ffd6e`.

Execution contract: actual home affinity must expose exactly 8 CPUs; `OMP_NUM_THREADS=8`; OpenBLAS/MKL/NumExpr/BLIS/Veclib nested threads pinned to 1; full-window source compiled with `-DDSIR_WORKERS=8`; runtime must prove `DSIR_OMP_TEAM=8` before DES numerics.

## Historical self-hosted attempts — immutable infrastructure/resource history
- `33885834557 / 101065302520`: cancelled after discovery that the claimed worker count did not create actual parallel workers; no terminal science comparator. Infrastructure/resource failure `+0/+0`, not Wm_S3 scientific FAIL.
- `33900526972 / 101113324481`: blocked before science because live affinity exposed 8 CPUs rather than the prospectively requested 10; no science authority.
- `33901049626 / 101114995516`: 8-core v0.3 passed affinity, PyMaster 2.7, exact R1/lens staging and OpenMP-8 compilation, then stopped before science because the tiny runtime probe invoked system `python3` without NumPy. Infrastructure-only failure; the v0.4 repair was prospectively frozen before activation.
- Exp073CM remains historical resource/performance FAIL `+0/+0`, not Wm_S3 arithmetic failure.

None of these historical attempts is rewritten or promoted to a scientific repeatability result.

## Resume/checkpoint authority
Six durable stages remain frozen: `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`. Restore is fail-closed on replica, namespace, source head, contract fingerprint, payload SHA and provenance. A and B restore domains remain isolated; cross-replica numerical restore/import is forbidden.

Exp073DD remains authoritative support/readiness PASS `D1_RESUME_LINEAGE_PROVENANCE_PASS +0/+0` from run/job `33892969489 / 101088831684`, artifact `9944582651`. It separates invocation-new reconstruction counts from immutable cumulative mask lineage but **does not silently replace the frozen implementation of the active v0.4 run**. Any interrupted-run repair/resume must be prospectively bound and must preserve existing verified durable checkpoints and their original science identity.

Independent resume binding note: `recovery/2026-09-04_exp073bu_v0_2_resume_activation_binding_audit.md`. Historical checkpoint manifests must never be rewritten to fit a repair.

## Preserved integration authorities
Exp073CW v0.1 remains `H1_SINGLE_MASK_INTEGRATED_DRIVER_PASS +0/+0`, run/job/head `33860891989 / 100984835847 / b7e42a5a9d215990f97943e3ee270ad09127d612`, artifact `9932088071`.
Exp073CV v0.3 remains `I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS +0/+0`, run/job/head `33847132443 / 100941396500 / 77cc6ba35aac41d2f6af12c7b865787db2bb3e44`, artifact `9926971841`.
Historical Exp073BW G2 exactness-negative support evidence and all other recorded negative/support outcomes remain immutable.

## Frozen boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gate
Consume run/job `33901458494 / 101116305364` immediately when terminal. Download the raw evidence artifact and independently verify artifact digest, frozen source/implementation/contract lineage, A/B checkpoint identity, dtype/shape, whole canonical payload SHA equality and `numpy.array_equal`, plus the frozen terminal token. Only a fully validated raw PASS admits Wm_S3 authority. Infrastructure termination instead triggers first-cause diagnosis plus prospective checkpoint-preserving resume; a genuine exact comparator mismatch is preserved as scientific repeatability FAIL and is never numerically rescued.
