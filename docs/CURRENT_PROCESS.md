# DSIR current-process ledger

Updated: 2026-09-06
Scope: DSIR only; RTK/RQIR excluded.

## Preserved scientific authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. `WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`. Exp073EL resource readiness remains support PASS +0/+0, artifact `9980783193`, digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`.

`WW_S0_S1` is now admitted scientific authority by Exp073EZ run/job **`34017921734 / 101444964371`**. Raw admission token:
`PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.
Classification: `SCIENTIFIC_AUTHORITY_ADMITTED`; `science_gate_scored=true`; `ww_s0_s1_authority_created=true`.

Upstream candidate remains Exp073EY resume `34010599584 / 101425638857`, artifact `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`, exact selected A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`, full BPW SHA `eb6c2427c86e76225a39feab3a4788d3a0b7ba142809f79cecb2e362c0b44b98`, exact `numpy.array_equal=true`, all finite, no tolerance rescue.

Historical Exp073EZ first admission run `34017884048 / 101444857315` is immutable `INFRASTRUCTURE_DEPENDENCY_FAIL +0/+0` because hosted Python lacked NumPy before raw numerical/provenance audit. Minimal repair pinned audit-only `numpy==2.3.2`; science criteria were unchanged. Repair commit `a429b4a3b439bcca92e3adccfaa0de621137f6bc`.

## Current frontier

Frozen order advances to **`WW_S0_S2`**.

Exp073FA preregistration:
- file `experiments/073fa_ww_s0_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`;
- commit `a1ce88850d037b408eb5f8cdd3275dbc7cf629b4`;
- blob `edc044792be8ac7b796c8469943924942ae91932`;
- source pair ordered distinct `(S0,S2)`;
- source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- checkpoint namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `checkpoints/exp073fa-ww-s0-s2-b-v0-1`;
- expected candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`;
- candidate PASS alone creates no authority.

## Current authoritative process

Workflow: `Exp073FA WW_S0_S2 prerequisite static audit v0.1`.
- run **`34018080500`**;
- job **`101445404866`**;
- activation/head **`d2c1d5abb857d636eac586851f477e0c868c3dc9`**;
- state at ledger update: `IN_PROGRESS` with fail-closed audit step already SUCCESS, awaiting terminal workflow reconciliation;
- home/self-hosted ownership: **NONE**; this workflow is hosted-only;
- last durable science checkpoint for Exp073FA: none yet, because no Exp073FA science computation has started.

Expected static token: `PASS_EXP073FA_WW_S0_S2_PREREQUISITE_STATIC_AUDIT_V0_1`. This is support `+0/+0` only and can never create WW authority.

On terminal static PASS: implement/freeze the dedicated checkpointed Exp073FA S0_S2 production envelope, run a hosted fail-closed implementation audit, verify no queued/in-progress competing self-hosted DSIR job, then launch the sole home A/B science computation. On static failure: diagnose the first causal implementation/governance defect and repair without changing the preregistered science.

## Frozen global boundaries

`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.