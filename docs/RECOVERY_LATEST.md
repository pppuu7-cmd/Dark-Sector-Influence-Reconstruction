# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. Historical negative/resource/infrastructure outcomes remain immutable.

`WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`. Exp073EL remains resource support PASS `+0/+0`.

`WW_S0_S1` remains admitted by Exp073EZ run/job `34017921734 / 101444964371`, exact token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`. Its Exp073EY candidate is run/job `34010599584 / 101425638857`, artifact `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`, selected exact A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`, full BPW SHA `eb6c2427c86e76225a39feab3a4788d3a0b7ba142809f79cecb2e362c0b44b98`, complete six-stage chains, file-backed MCM `19,327,352,832` bytes, public serialized BPW, exact equality/finiteness, no tolerance rescue.

Historical Exp073EZ first admission `34017884048 / 101444857315` remains `INFRASTRUCTURE_DEPENDENCY_FAIL +0/+0`; audit-only NumPy repair did not change science.

Immutable S0_S1→S0_S2 transition note: `docs/recovery/RECOVERY_2026-09-06_EXP073EZ_ADMITTED_WW_S0_S1_EXP073FA_PREREG.md`, commit `7b4a39e70ad2b9cde20fc33e43c8eff69a0d3254`.

## Current frontier — WW_S0_S2 / Exp073FA

Science prereg `experiments/073fa_ww_s0_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`, commit `a1ce88850d037b408eb5f8cdd3275dbc7cf629b4`, blob `edc044792be8ac7b796c8469943924942ae91932`.

Frozen semantics: ordered distinct `(S0,S2)` using authoritative R1 indices `[0,2]`; source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; NSIDE=4096; ell `0..12287`; 39 bands; PyMaster 2.7; public serialized `read_from(...,read_unbinned_MCM=True)->get_bandpower_windows()`; one regular-file-backed MCM exactly `19,327,352,832` bytes; full `[4,39,4,12288]`; selected `EE<-EE <f8 [39,12288]`; all finite; exact SHA plus `numpy.array_equal`; no rescue. Durable namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `...-b-v0-1`; exact six-stage chain; fail-closed restore; no historical WW numerical import or other-replica output read. Candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate alone never creates authority.

Exp073FA prerequisite static audit `34018080500 / 101445404866` = SUCCESS, raw token `PASS_EXP073FA_WW_S0_S2_PREREQUISITE_STATIC_AUDIT_V0_1`, classification support `+0/+0`.

## Exp073FB — generated driver implementation support

Transformation prereg `experiments/073fb_exp073fa_s0_s2_driver_transformation_v0_1_prereg.md`, blob `7ff28ad4239728c14d05094b55ffc713c52210e6`.

First run/job `34018169771 / 101445653251` is immutable implementation-static FAIL `+0/+0`: generation and Python compile passed, but semantic audit found omitted lowercase underscore identity substitution `s0_s1 -> s0_s2`. No home/science run occurred. Minimal repair commit `28c7afc1a83a5a5bf7019218eccc382abcdf0c3a` changed only that identity transform.

Repaired Exp073FB run/job **`34018241319 / 101445845648`** = SUCCESS. Raw token `PASS_EXP073FB_EXP073FA_S0_S2_DRIVER_TRANSFORMATION_STATIC_AUDIT_V0_1`, classification support `+0/+0`, no authority. Artifact `9984600349`, name `exp073fb-exp073fa-s0-s2-generated-drivers-v0-1`, GitHub digest and independently downloaded ZIP SHA256 exactly `b371821a77cb4a62051ceee45f82764a5486ea3b0bcf0939a9bcac0eff624cda`. Artifact transformation receipt binds:
- generated base driver SHA256 `fe354b95e9aeefe0772f4c7eecbba6e1944fb1f4955fceb3e9e72ed1c06b293a`;
- generated file-backed wrapper SHA256 `77f321e22c923d8d5996105487cae9afb6eecc5863174d849b092164a26824ba`;
- pair `S0->S2`, ordered `[0,2]`, historical numerical import false.

Those exact source files are committed as `ci/exp073fa_ww_s0_s2_durable_ab_production_v0_1.py` and `_v0_2.py`.

## Current authoritative process — Exp073FC

Purpose: bind the committed Exp073FA drivers byte-for-byte to repaired Exp073FB artifact before any home execution envelope is authorized.

Prereg `experiments/073fc_exp073fa_committed_driver_binding_v0_1_prereg.md`, commit `ea1f3f1b7e556db9afe0e4c0272178463cbed94b`, blob `9e194c2617114b88c46fa349c10dddf70cccd6da`.

Active hosted workflow:
- run **`34018341064`**;
- job **`101446155067`**;
- head **`3910e16b18e62464b1aa32b57e158552b6321b45`**;
- state at recovery update: **QUEUED**;
- expected token `PASS_EXP073FC_EXP073FA_COMMITTED_DRIVER_BINDING_V0_1`;
- PASS classification support/governance `+0/+0`, never WW authority.

FC independently re-downloads artifact `9984600349`, recomputes ZIP SHA, verifies transformation receipt, requires committed driver SHA256s to equal the artifact-generated SHA256s byte-for-byte, compiles them, and repeats critical `(S0,S2)`/checkpoint/shape/public-BPW/exactness/no-rescue assertions.

**Runner ownership:** no self-hosted DSIR job owns `DSIR-HOME-PC`; no Exp073FA science checkpoint exists yet.

On FC PASS: freeze a dedicated fail-closed home execution envelope referencing exact committed driver blobs, qualified read patch, R1 authority, live exclusivity/resource checks and dedicated FA checkpoints; run hosted implementation audit; verify zero competing self-hosted DSIR jobs; then launch exactly one Exp073FA A/B science run. On FC failure: diagnose first causal binding defect without changing frozen science.

## Frozen global boundaries

Unless prospectively superseded: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.