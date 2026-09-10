# DSIR recovery V68 — Exp073JE infrastructure failure diagnosed, minimally repaired, rerun active

Date: 2026-09-10. Scope: DSIR only. Never mix RTK or RQIR.

## Preserved scientific authority
Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107 coordinate rows, atomic production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. No tolerance rescue. All earlier admitted DSIR authority remains unchanged. Exp073CM remains historical resource/performance `+0/+0`; Wm_S3 remains unopened.

## Exp073JD provenance correction
The validated JD numerical result remains support-only `EXACT_K_ORIGINAL_PAIR_OBSERVED_PLUS_0_PLUS_0`, run/job `34472918931 / 102856790715`, artifact `10150322510`, raw token `PASS_EXP073JD_EXACT_K_ORIGINAL_PAIR_OBSERVED_V0_1`.

Authority V0_1 contained incorrect SHA256 provenance fields. Immutable corrected authority V0_2 was added in commit `1fcc02d6d252d3f47184be565218cf29355c3c8c` without changing any scientific observation or classification. Correct independent hashes are: GitHub artifact digest and downloaded ZIP SHA256 `310939a4b4ef8d75cb027630e5f43f88003ab92045c0af6e83ab83764bcb6365`; contained JSON SHA256 `ba26c2a89a41d67e65bbf0b630659fccae33d85a7d05c2d0d4d493f8b33dfccb`.

## Exp073JE attempt 1 — infrastructure failure +0/+0
Original JE run/job `34474514433 / 102861967751`, head `257ef3295e09870df02e681275f828c9bceab8bf`, completed contract/lineage, dependency installation, capacity-patched pinned CLASS-IV build, then failed at the first diagnostic execution before writing/uploading a result artifact. First causal runtime symptom from the raw log: `malloc(): corrupted top size`; process aborted with exit code 134. Therefore this attempt is infrastructure/software failure `+0/+0`, not scientific PASS/FAIL and not a JE scaling observation.

Diagnosis: the original JE architecture enlarged perturbation `k_output_values` array capacity `_MAX_NUMBER_OF_K_FILES_ 30 -> 512` but retained parser `FileArg` / `_ARGUMENT_LENGTH_MAX_ = 1024`. JE serializes N={64,128,256} float64 physical-k nodes into one `k_output_values` argument. The N=256 serialization exceeds the original 1023 usable bytes, so the parser/input storage was not safely capacity-matched.

## Minimal prospective repair
Repair contract frozen before rerun in `docs/dsir4/prereg/EXP073JE_ARTICLE3_LAYERB_SHARED_FIXED_K_GRID_SCALING_INFRA_REPAIR_V0_2.md`, commit `16f984a9a81ac5e3d559d67e191f7bb9f6ffd85b`.

The only added source change is parser input storage capacity `_ARGUMENT_LENGTH_MAX_ 1024 -> 32768`, exactly once, with pre/post hashes recorded, in addition to the already preregistered `_MAX_NUMBER_OF_K_FILES_ 30 -> 512`. A static regression check requires all exact frozen JE serialized grids to fit below 32768 bytes and specifically requires N=256 to exceed 1023 bytes, demonstrating the original defect. No equations, d_m definition, cosmological input, k nodes, interpolation arithmetic, finite-difference h, REL_TOL or frozen science boundary changed.

Workflow repair/binding commit `6090af1b41b86bd878c4e348874a496c04a09053` also binds JE lineage to corrected JD authority V0_2.

## Current process — repaired Exp073JE
Workflow `exp073je-article3-layerb-shared-fixed-k-grid-scaling-v0-1`; rerun run/job `34474839354 / 102863020808`; head `6090af1b41b86bd878c4e348874a496c04a09053`; GitHub-hosted `ubuntu-24.04`; checkpoint namespace N/A; home/self-hosted ownership none. Last observed state IN_PROGRESS.

Expected gate remains the prospectively frozen support-only JE classification. Exact next action on terminal state: inspect first causal failure if any; otherwise download and independently hash the result artifact and capacity-patch record, verify both source replacement counts/hashes, fixed-node coordinate provenance, raw token and every scaling-candidate condition. A valid candidate only nominates a later separately preregistered full atomic-support audit; it does not PASS Exp073IR or authorize covariance restriction.

Global frozen science boundaries remain unchanged.
