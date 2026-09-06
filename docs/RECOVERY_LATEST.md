# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR into this control/recovery plane.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. Historical negative, resource and infrastructure outcomes remain immutable.

`WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`.

Exp073EL resource readiness remains support PASS `+0/+0`, artifact `9980783193`, digest `sha256:c720233664be2e8a7666db6f95def0a2f13eb674732add6852f0c09e916e5e46`.

## WW_S0_S1 — admitted

Exp073EY checkpoint-resume run/job `34010599584 / 101425638857` produced candidate artifact `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`. Raw exact A/B selected `<f8 [39,12288]` SHA was `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`; full BPW SHA `eb6c2427c86e76225a39feab3a4788d3a0b7ba142809f79cecb2e362c0b44b98`; both six-stage chains, exact file-backed MCM `19,327,352,832` bytes, `/proc/self/maps`, public serialized-workspace route, exact array equality/finiteness and no tolerance rescue passed.

Exp073EZ first admission `34017884048 / 101444857315` remains historical `INFRASTRUCTURE_DEPENDENCY_FAIL +0/+0` because hosted Python lacked NumPy. Minimal audit-only `numpy==2.3.2` repair left science unchanged. Repaired Exp073EZ **`34017921734 / 101444964371`** emitted exact token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, classification `SCIENTIFIC_AUTHORITY_ADMITTED`, and therefore **WW_S0_S1 is admitted**.

Immutable transition note: `docs/recovery/RECOVERY_2026-09-06_EXP073EZ_ADMITTED_WW_S0_S1_EXP073FA_PREREG.md`, commit `7b4a39e70ad2b9cde20fc33e43c8eff69a0d3254`.

## Current frontier — WW_S0_S2 / Exp073FA

Exp073FA science prereg:
- file `experiments/073fa_ww_s0_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`;
- commit `a1ce88850d037b408eb5f8cdd3275dbc7cf629b4`;
- blob `edc044792be8ac7b796c8469943924942ae91932`.

Frozen semantics: ordered distinct `(S0,S2)` from authoritative R1 indices `[0,2]`; source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; DES NSIDE=4096; ell `0..12287`; 39 bands; PyMaster 2.7; public serialized-workspace BPW route; regular-file-backed unbinned MCM exactly `19,327,352,832` bytes; full `[4,39,4,12288]`; selected `EE<-EE <f8 [39,12288]`; exact A/B SHA plus `numpy.array_equal`; all finite; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.

Dedicated namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `...-b-v0-1`; exact six-stage order `fresh_sources_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`; fail-closed restore; no historical WW numerical import or other-replica output read. Candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate PASS alone creates no authority.

Exp073FA prerequisite static audit run/job `34018080500 / 101445404866` = SUCCESS, token `PASS_EXP073FA_WW_S0_S2_PREREQUISITE_STATIC_AUDIT_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`, no WW authority.

## Exp073FB driver-transformation control

Preregistered transformation contract `experiments/073fb_exp073fa_s0_s2_driver_transformation_v0_1_prereg.md`, commit `f2204c828a791e0111000776458e84b9df0eb8c5`, blob `7ff28ad4239728c14d05094b55ffc713c52210e6`, permits only experiment/pair/source identity substitutions from frozen Exp073EY durable drivers to Exp073FA S0_S2 and forbids changes to scientific arithmetic, geometry, shapes, dtype, checkpoint order, public BPW, storage byte count, equality/finiteness or rescue policy.

Historical first Exp073FB run/job `34018169771 / 101445653251` is **IMPLEMENTATION_STATIC_FAIL +0/+0**, not science. Frozen-input checks and generation passed; generated Python compiled. First semantic audit assertion detected that generator had changed hyphenated `s0-s1` and uppercase `S0_S1` identities but omitted lowercase underscore schema identity `s0_s1`. No self-hosted science ran and no generated artifact was admitted.

Minimal causal repair added only `s0_s1 -> s0_s2` to the identity transformation. No source index, numerical constant, arithmetic, checkpoint, file-backed BPW or acceptance rule changed. Repair commit **`28c7afc1a83a5a5bf7019218eccc382abcdf0c3a`**.

### Authoritative current process

Repaired Exp073FB:
- run **`34018241319`**;
- job **`101445845648`**;
- head **`28c7afc1a83a5a5bf7019218eccc382abcdf0c3a`**;
- state at recovery update: **IN_PROGRESS** on hosted runner;
- expected token `PASS_EXP073FB_EXP073FA_S0_S2_DRIVER_TRANSFORMATION_STATIC_AUDIT_V0_1`;
- expected artifact `exp073fb-exp073fa-s0-s2-generated-drivers-v0-1` containing generated candidate drivers plus transformation receipt;
- PASS classification support/governance `+0/+0`, never WW authority.

**Runner ownership:** no self-hosted DSIR job owns `DSIR-HOME-PC`; no Exp073FA science checkpoint exists yet.

On FB PASS: consume raw token and generated artifact/digest; freeze exact generated driver identities and dedicated fail-closed home envelope; hosted-audit the envelope; verify zero competing self-hosted runs; launch exactly one Exp073FA A/B home science process. On FB failure: diagnose first causal defect and repair without changing frozen Exp073FA science.

## Frozen global boundaries

Unless prospectively superseded by later authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.