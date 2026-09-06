# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Historical negative/resource/infrastructure outcomes remain immutable.

WW admitted authorities:
- `WW_S0_S0` — Exp073EO v0.2 `34005373819 / 101411448176`;
- `WW_S0_S1` — Exp073EZ `34017921734 / 101444964371`;
- `WW_S0_S2` — Exp073FF `34032384956 / 101484177968`;
- `WW_S0_S3` — **Exp073FN `34050154578 / 101532191756`**, token `PASS_EXP073FN_WW_S0_S3_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

Exp073FG candidate provenance remains run/job `34034377795 / 101489679508`, artifact `9993520467`, exact artifact/independent ZIP SHA256 `8ddd1e1b81e5fa9c3a4de16c6d72b35353cb42bba04bb77c736aa4998340bde0`, selected exact A/B SHA `db58af980e2997ebbe327ce91dfafb682c38fda1ba841c3d5acba78e429007d3`, public full BPW SHA `6a9fe87ab5ae44db5d475686cbc6024174b8c8384433c9d98f48e182557fc942`, workspace FITS SHA `af870ad38f5d74796519f18ab135bf1c0129d888206079606081e3bb7653fc5d`. Both complete six-stage/prune chains, public file-backed `read_unbinned_MCM=True -> get_bandpower_windows()` route and exact `19,327,352,832`-byte `/proc/self/maps` proof were independently verified before admission.

Governance correction remains immutable: Exp073FL already belonged to the S1S1 driver-generation static audit. Later collided S0S3 admission run/job `34047839320 / 101525992295` remains `INFRASTRUCTURE_LOG_TRANSPORT_FAIL_PLUS_0_PLUS_0`; it created no authority. Exp073FN prospectively corrected the label collision and the log transport defect using only `--allow-escape-sequences`, without changing candidate evidence or science.

## Current frontier — WW_S1_S1 / Exp073FM

Science prereg creation commit `391af1d14ca61f20ef42cccde348453ca84a1aaa`, blob `da64cbb6d0f7553387b5b635812cfa25ec7fb8fa`.

Frozen science: authoritative `[1,1]`; reconstruct S1 exactly once per replica; exactly one spin-2 field; pass the exact same Python field object on both coupling sides; equal-but-distinct second field forbidden; DES NSIDE=4096; ell `0..12287`; 39 bands; public file-backed BPW; full `[4,39,4,12288]`; selected canonical `<f8 [39,12288]` `EE<-EE`; exact A/B SHA plus `numpy.array_equal`; finiteness; no tolerance/allclose/isclose/rounding/smoothing/averaging/manual reconstruction/effective-coordinate/fiducial rescue. Candidate token `PASS_EXP073FM_WW_S1_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate alone creates no authority.

### Newly closed hosted support

- Exp073FO `34050224161 / 101532385479`: `PASS_EXP073FO_WW_S1_S1_PRODUCTION_TRANSFORMATION_READINESS_V0_1`, support `+0/+0`.
- Exp073FP `34050445433 / 101532983406`: raw-log token `PASS_EXP073FP_WW_S1_S1_EXACT_PRODUCTION_DRIVER_STATIC_AUDIT_V0_1`, support `+0/+0`, no authority/no home science.
- Exp073FQ `34050588344 / 101533366352`: raw-log token `PASS_EXP073FQ_WW_S1_S1_HOME_ENVELOPE_STATIC_AUDIT_V0_1`, support `+0/+0`, no authority/no home science.

Committed exact implementation blobs:
- `ci/exp073fm_ww_s1_s1_durable_ab_production_v0_1.py` = `477647c5164264665cc16e20d1577fb25cd245f4`;
- v0.2 file-backed adapter = `8e3edff39aae95d3abc3196806802c5f0ae59832`;
- complete-chain verify/prune = `8e04e99084aed582f9586e3f316c023650ce6c63`;
- terminal receipt comparator = `02d69d5d517c676b3ec0963380f93d13f2b9874e`;
- fail-closed home envelope = `873232cc96f9a97afefeff1ff0a433fd5b49a5a2`.

The implementation preserves one S1 source checkpoint and one field construction, same-object `compute_coupling_matrix(f1,f1,...)`, six-stage durable A/B namespaces, strict completed-restore payload revalidation, exact public BPW route, exact 19,327,352,832-byte MCM backing + `/proc/self/maps`, complete-chain verification before pruning, terminal comparison without restoring replicas, and exact-only A/B scoring.

### Authoritative current process — Exp073FM home-science workflow

- run **`34050657030`**;
- head **`f0caca0c3e812710e5958ee13348a150d045a7d8`**;
- hosted-launch job **`101533554310`**, latest state **IN_PROGRESS** at this recovery write;
- self-hosted job not yet created at this exact write; `DSIR-HOME-PC` remains FREE until the hosted dependency passes;
- checkpoint namespaces `checkpoints/exp073fm-ww-s1-s1-a-v0-1` and `...-b-v0-1`;
- hosted launch fail-closes on Exp073FN S0S3 authority, Exp073FQ PASS, frozen blobs, S1 R1 authority, syntax and no-rescue checks;
- on hosted PASS GitHub may start exactly one self-hosted job; never duplicate it;
- on terminal home SUCCESS consume compact artifact and independently verify digest, complete chains, S1 same-object semantics, MCM proof, selected arrays and frozen identities before classifying candidate;
- on infrastructure failure preserve verified checkpoints and repair only the first causal implementation/transport defect;
- on exact numerical mismatch record genuine scientific FAIL and do not rescue with tolerances.

Research log supplement: `docs/research_log/RESEARCH_LOG_2026-09-06_EXP073FN_FO_FP.md`.

## Frozen global boundaries

Unless prospectively superseded: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
