# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-05
**Scope:** DSIR only; RTK/RQIR excluded.
**Article-3 readiness:** **Verified 52.0% | Draft/data 54.6%**.

Repository state, immutable recovery notes, validated Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Frozen science boundaries remain unchanged.

## Scientific frontier — Exp073BU Wm_S3 fresh-independent-PCL A/B
Wm_S1 Track-A exact PASS and admitted Wm_S2 authority are preserved. Exp073CR v0.3 remains RESOURCE PASS `+0/+0`. **Wm_S3 scientific angular authority remains absent.** The original Exp073BU v0.4 self-hosted run did not produce a consumable terminal comparator; one checkpoint-preserving resume process is authoritative and currently in progress.

Original science prereg commit/blob: `e1a0332c128c87049fb8699018a3a3e71c9c5321 / 816542c7eb7a8ba4e72d6e01228aa62d05c7c805`.
A/B namespaces remain `checkpoints/exp073bu-wm-s3-a-v0-1` and `checkpoints/exp073bu-wm-s3-b-v0-1`.
Science PASS still requires whole canonical `<f8 [39,12288]` SHA256 equality **and** `numpy.array_equal`; workflow success is never enough and no tolerance rescue is permitted.

Exact band authority remains `[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`, 39 bands, ell `0..12287`, full window `[2,39,2,12288]`, selected `wins[0,:,0,:] = TE<-TE`.

## Historical Exp073BU 8-core v0.4 terminal classification
Frozen workflow `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-8core-v0-4.yml`, run/job `33901458494 / 101116305364`, frozen head `c02c018ede6a1fcf7aef1a848c0118a0669ed67f`, workflow blob `f8c70a4206321b0dc10b57f63a2a06163da2249a`, contract fingerprint `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`.

The run became terminal `failure` at `2026-09-04T18:30:00Z` while the science step remained reported `in_progress`; all following always-evidence/upload/classification steps stayed pending and no Actions artifact exists. GitHub job-log blob retrieval returned `BlobNotFound`. Therefore the historical run is **INFRASTRUCTURE_INCOMPLETE / runner-loss-like termination `+0/+0`**, not scientific repeatability FAIL. No terminal A/B comparator was available, so Wm_S3 authority was not created.

Historical checkpoint root is preserved exactly at `~/.cache/dsir/exp073bu-wm-s3-fresh-ab-8core-v0-4-33901458494`. It must not be deleted, migrated, or rebound to a new science identity.

Immutable detailed recovery authority: `recovery/2026-09-04_exp073bu_v04_runner_loss_and_resume_support_chain.md`.

## Validated checkpoint-resume repair chain — all support `+0/+0`
- **Exp073DE:** run `33908858642`, artifact `9950549286`, independently verified ZIP SHA256 `4b0f21f407f66659dae89e488c34ab65c56fcf4ce77fb24415272ee44b91b91e`; raw `PASS_EXP073DE_SPLIT_IDENTITY_RESUME_BINDING_V0_1`.
- **Exp073DF:** run `33909072007`, artifact `9950629085`, ZIP SHA256 `494b5f98242fef972fb632995f3553293ed452a0bc21d9da4168eeb94ca5e8c1`; raw `PASS_EXP073DF_LEGACY_COMPLETE_RESUME_PASSTHROUGH_V0_1`.
- **Exp073DG:** run `33909299159`, artifact `9950710099`, ZIP SHA256 `75b8837c71f2592c5fbadd5e37ec32159e4f7e47aa7d9807da900f72523cc19f`; raw `PASS_EXP073DG_BOUNDARY_SAFE_RESUME_V0_1`.
- **Exp073DH:** run `33909572046`, artifact `9950808508`, ZIP SHA256 `e0803731b8c6b76aaf6d1295e9cb9f625355f5ca6258bbb5f0c95652c33182a1`; raw `PASS_EXP073DH_MASK_WORKSPACE_LINEAGE_RESUME_V0_1`.
- **Exp073DI:** run `33909833283`, artifact `9950924076`, independently verified ZIP SHA256 `518594fcc23bf7ad793d726e23e7c4b65e02a4cbd0ec6080d877caaff98432c5`; raw `PASS_EXP073DI_RESTORED_ADAPTER_RUNTIME_PROVENANCE_V0_1`.

Validated repair blobs:
- lineage driver `ci/exp073bu_wm_s3_fresh_ab_production_v0_5.py` = `a0b3f399cb26457c03b57dd16e79245aec4fbca0`;
- 8-core resume wrapper `ci/exp073bu_wm_s3_fresh_ab_production_8core_resume_v0_7.py` = `d0fd545ef7b1245f21a5d7cba2f3b2eed459d87b`;
- resume-only provenance launcher `ci/exp073bu_wm_s3_science_launcher_8core_resume_v0_4.py` = `0026c9607c935b4b2ad90a396cecee735b893738`;
- frozen original launcher = `8a725ba135e3e120ce6e8d0db3dd14d95d4ffd6e`;
- exact OMP8 adapter = `63ee393791bba43d3eabbea654efdb9d439d477e`;
- exact parametric downstream source = `be4f381de4c5c043a9c0fcd107e63ef3f2079578`.

## Current authoritative process — Exp073DJ checkpoint-preserving Exp073BU resume
Exactly one scientific/self-hosted resume process is live:
- workflow `.github/workflows/exp073dj-exp073bu-checkpoint-resume-v0-1.yml`;
- run `33910213781`;
- activation/head `c0f5959b3edb0957cfb14a1d06f7715242d57f48`;
- hosted preflight job `101144603730`: **SUCCESS**;
- self-hosted science-resume job `101144660519`: **IN_PROGRESS**;
- completed SUCCESS steps include exact hardware/checkpoint-root binding, NaMaster environment, fail-closed checkpoint inventory, frozen S3 authority staging, DES lens hash verification, deterministic OpenMP-8 downstream compilation and actual 8-thread runtime certification;
- active step is `Live exclusivity and checkpoint-preserving Exp073BU A-then-B resume`;
- evidence/upload/classification steps remain pending;
- DSIR-HOME-PC is **RESERVED BY THIS SINGLE RESUME JOB**; latest live reconciliation shows `1 in_progress / 0 queued`, so no competing DSIR workload may be started;
- frozen checkpoint identity remains old science head `c02c018ede6a1fcf7aef1a848c0118a0669ed67f` and fingerprint `b38687bf5aa6cf4cfe01b2f38a7091e96d97196ad38bdf2ea771f7b649ac73da`;
- historical checkpoint root must already exist; the workflow may not silently create a replacement root;
- existing manifests must form an ordered six-stage prefix per replica and every accepted durable payload is hash/identity checked;
- valid complete stages are read-only and never recomputed;
- terminal resume output is `terminal_science_receipt_resume_v0_1.json`, leaving historical terminal evidence untouched.

Decoded active-job logs currently return GitHub `BlobNotFound`; therefore exact partial checkpoint values/hashes beyond successful inventory status are not asserted and no partial numerical output has been inspected.

Detailed process ledger: `docs/CURRENT_PROCESS.md`.

## Prospective terminal evidence successor — Exp073DK support `+0/+0`
Exp073DK v0.1 is prospectively preregistered to close an evidence/reproducibility gap **without modifying the frozen science comparator**.
- prereg: `experiments/073dk_exp073bu_terminal_payload_evidence_export_v0_1_prereg.md`;
- prereg commit/blob: `286b6dace47cd2c2dc631be544a998401557cef2 / 1e8f29f8552475748680439924c13590d352549a`;
- original successor workflow commit: `75c0d7d8197bc29d7a06037a355aaf34b17f8d59`;
- original preregistration note: `recovery/2026-09-05_exp073dk_terminal_payload_evidence_successor_preregistered.md`, commit `6d1cf0c83eb063e3a635b86dd5d40c7cfeb4513b`.

Independent audit while Exp073DJ remained active found an evidence-orchestration TOCTOU defect in the original successor: the DSIR home lock was acquired in one shell step but released before the later step that touched the historical checkpoint root. This is an infrastructure/evidence issue only, not a scientific result.

Prospective repair authority:
- lock-scope repair commit `65c73cf736b081b1964fd951732c1ecccbc4b0c0` keeps FD9/flock held across live noncompetition and **all** historical checkpoint-root reads;
- hosted lock-scope static regression audit commit `ce4df169b9ae91bf64b2288b42dbfbcd2c37101c` verifies lock-before-root ordering, forbids pre-lock payload/receipt access and gates the self-hosted export job with `needs: static-audit`;
- immutable repair note `recovery/2026-09-05_exp073dk_lock_scope_toctou_repair.md`, commit `7d1d6188a14fd682f90942d14986a60792991885`.

The static audit is currently **ARMED, NOT YET A VALIDATED PASS**; Exp073DJ is still running, so Exp073DK has not yet been triggered. No current-science code or criterion changed.

The successor remains `workflow_run`-triggered only after completion of Exp073DJ and additionally hard-binds upstream run `33910213781`. It performs no NaMaster/mask/workspace/MCM/PCL/scientific recomputation. It only exports already-final A/B canonical `selected_te.bin`, exact-validates provenance and receipt/manifests, recomputes whole-file SHA equality and independently reruns `numpy.array_equal` on `<f8 [39,12288]`. Missing/malformed terminal evidence or payload is fail-closed infrastructure/BLOCKED `+0/+0`. Exp073DK cannot create or rescue Wm_S3 authority by itself.

## Frozen execution/science contract
Exactly 8 affinity CPUs; `OMP_NUM_THREADS=8`; OpenBLAS/MKL/NumExpr/BLIS/Veclib nested threads=1; runtime must prove `DSIR_OMP_TEAM=8`. Six durable stages remain `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`.

Frozen boundaries: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Preserved historical/support authorities
Exp073CM remains historical resource/performance FAIL `+0/+0`, not Wm_S3 arithmetic failure. Exp073DD remains `D1_RESUME_LINEAGE_PROVENANCE_PASS +0/+0`, run/job `33892969489 / 101088831684`, artifact `9944582651`. Exp073CW remains `H1_SINGLE_MASK_INTEGRATED_DRIVER_PASS +0/+0`, run/job `33860891989 / 100984835847`, artifact `9932088071`. Exp073CV v0.3 remains `I1_PRODUCTION_INTERFACE_EXACT_INTEGRATION_PASS +0/+0`, run/job `33847132443 / 100941396500`, artifact `9926971841`. All historical negative/infrastructure/support outcomes remain immutable.

## Exact next gate
Track `33910213781 / 101144660519` without duplication. While active, do not inspect partial numerical values or tune the frozen gate. When terminal, immediately consume the Exp073DJ raw science receipt/artifact and classify it under the frozen contract. Then consume the automatically triggered Exp073DK hosted static audit and terminal canonical-payload evidence artifact. Only an independently validated raw `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_8CORE_V0_3` may admit Wm_S3 authority. Exact A/B inequality is scientific repeatability FAIL; checkpoint/runner/provenance/dependency failures are `INFRASTRUCTURE_INCOMPLETE` or `BLOCKED` `+0/+0` and must preserve valid checkpoints.
