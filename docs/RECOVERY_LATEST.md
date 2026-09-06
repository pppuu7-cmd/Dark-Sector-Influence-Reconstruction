# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR into this control/recovery plane.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. Historical negative, resource and infrastructure outcomes remain immutable and are never rewritten.

`WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`, token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`.

Exp073EL resource readiness remains support PASS `+0/+0`: artifact `9980783193`, digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`.

## WW_S0_S1 — admitted scientific authority

Authoritative candidate producer: Exp073EY checkpoint-resume run `34010599584`, hosted repair audit `101425618749` SUCCESS, home science job `101425638857` SUCCESS, head `4c570bf6b7f3f53547f43e2882149defa125da89`.

Candidate artifact `9983630139`, name `exp073ey-ww-s0-s1-filebacked-ab-resume-v0-2`, GitHub digest and independently downloaded ZIP SHA256:
`12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`.

Raw candidate evidence: source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; ordered distinct `(S0,S1)`; complete A/B six-stage checkpoint chains; regular-file-backed MCM exactly `19,327,352,832` bytes with `/proc/self/maps` proof; public serialized-workspace BPW route; full BPW SHA `eb6c2427c86e76225a39feab3a4788d3a0b7ba142809f79cecb2e362c0b44b98`; selected canonical `<f8 [39,12288]` exact A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`; `numpy.array_equal=true`; all finite; no tolerance rescue; candidate token `PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Exp073EZ v0.3 terminal-binding blob is `d3c6c1ba9c6f6f4d41d1d123e765f8de5ead0fec`. First admission run/job `34017884048 / 101444857315` remains immutable `INFRASTRUCTURE_DEPENDENCY_FAIL +0/+0` because hosted Python lacked NumPy after all earlier identity/artifact/digest checks passed. Minimal repair pinned audit-only `numpy==2.3.2`; science criteria were unchanged.

Repaired Exp073EZ run/job **`34017921734 / 101444964371`** completed SUCCESS and raw log emitted exactly `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`, `science_gate_scored=true`, `ww_s0_s1_authority_created=true`. The hosted admission independently re-downloaded candidate artifact, reverified ZIP SHA, frozen blobs/run/jobs, raw checkpoint/receipt chains, canonical array equality/finiteness, mmap/public-BPW provenance, live exclusivity and post-receipt pruning. Therefore **WW_S0_S1 is admitted**.

Immutable transition note: `docs/recovery/RECOVERY_2026-09-06_EXP073EZ_ADMITTED_WW_S0_S1_EXP073FA_PREREG.md`, commit `7b4a39e70ad2b9cde20fc33e43c8eff69a0d3254`.

## Current frontier — WW_S0_S2 / Exp073FA

Exp073FA science preregistration:
- file `experiments/073fa_ww_s0_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`;
- commit `a1ce88850d037b408eb5f8cdd3275dbc7cf629b4`;
- blob `edc044792be8ac7b796c8469943924942ae91932`.

Frozen semantics: ordered distinct `(S0,S2)` reconstructed independently from authoritative R1 source indices 0 and 2; DES NSIDE=4096; ell `0..12287`; 39 bands; two spin-2 fields; exact ordered coupling; PyMaster 2.7; serialized `read_from(..., read_unbinned_MCM=True) -> get_bandpower_windows()`; regular-file-backed unbinned MCM exactly `19,327,352,832` bytes; full `[4,39,4,12288]`; selected `EE<-EE <f8 [39,12288]`; all finite; exact A/B SHA equality plus `numpy.array_equal`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.

Dedicated durable namespaces: `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `checkpoints/exp073fa-ww-s0-s2-b-v0-1`; exact stage order `fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`; fail-closed identity/payload verification; no historical WW numerical import or other-replica output read.

Candidate token frozen as `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate PASS alone will not create authority.

### Exp073FA prerequisite static audit — PASS +0/+0

Run/job `34018080500 / 101445404866` completed SUCCESS at head `d2c1d5abb857d636eac586851f477e0c868c3dc9`. Raw token: `PASS_EXP073FA_WW_S0_S2_PREREQUISITE_STATIC_AUDIT_V0_1`; classification `SUPPORT_PLUS_0_PLUS_0`; `ww_s0_s2_authority_created=false`. It verified exact FA prereg/task-runner/read-patch identities, authoritative source-2 support, upstream Exp073EZ SUCCESS, fixed MCM-size contract and exact/no-rescue policy. This is readiness only.

## Current authoritative process — Exp073FB

Before any home S0_S2 science run, driver transformation is prospectively governed by `experiments/073fb_exp073fa_s0_s2_driver_transformation_v0_1_prereg.md`, commit `f2204c828a791e0111000776458e84b9df0eb8c5`, blob `7ff28ad4239728c14d05094b55ffc713c52210e6`.

It permits only pair/experiment identity substitutions from the already validated Exp073EY durable architecture to Exp073FA `(S0,S2)` and forbids changes to NSIDE/ell/bands/shapes/dtype/checkpoint order/public BPW arithmetic/storage byte count/exactness/finiteness. No S0_S1 numerical artifact is an input.

Active hosted workflow:
- `Exp073FB Exp073FA S0_S2 driver transformation v0.1`;
- run **`34018169771`**;
- job **`101445653251`**;
- head **`fdfbfa161e5661f9eb32dc70804f5ac9cd145adf`**;
- current state: **IN_PROGRESS** on hosted runner;
- expected token `PASS_EXP073FB_EXP073FA_S0_S2_DRIVER_TRANSFORMATION_STATIC_AUDIT_V0_1`;
- PASS classification support/governance `+0/+0`; never WW authority;
- expected artifact contains generated S0_S2 v0.1/v0.2 candidate drivers and transformation receipt.

**Runner ownership:** no self-hosted DSIR run owns `DSIR-HOME-PC`; Exp073FB is hosted-only. No Exp073FA science checkpoint exists yet.

On FB PASS: consume generated artifact/digest and raw audit token, freeze exact generated driver identities and a dedicated fail-closed home execution envelope, perform hosted implementation audit, live-check self-hosted exclusivity, then launch exactly one Exp073FA A/B science process. On FB failure: diagnose first causal transformation/audit defect and repair without changing frozen Exp073FA science.

## Frozen global science boundaries

Unless a later authoritative recovery note prospectively supersedes them: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.