# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. Historical negative/resource/infrastructure outcomes remain immutable.

`WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`.

`WW_S0_S1` remains admitted by Exp073EZ run/job `34017921734 / 101444964371`, exact token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`. Its Exp073EY candidate remains run/job `34010599584 / 101425638857`, artifact `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`, selected exact A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`.

`WW_S0_S2` is admitted by Exp073FF run/job `34032384956 / 101484177968`, exact token `PASS_EXP073FF_WW_S0_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`. The admitted lineage preserves source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

## Current science frontier — WW_S0_S3 / Exp073FG

Preregistration: `experiments/073fg_ww_s0_s3_filebacked_full_resolution_ab_science_v0_1_prereg.md`, blob `50c64a3f7e341f0a180b9c8dbc83a074f6cae150`.

Frozen target: ordered `(S0,S3)`, authoritative R1 indices `[0,3]`, two independently reconstructed source count maps and two distinct spin-2 fields; never `(S3,S0)` and never same-field. Numerical/storage semantics: DES NSIDE=4096; ell `0..12287`; 39 bands; PyMaster/NaMaster 2.7 lineage; serialized workspace `read_from(...,read_unbinned_MCM=True)` then public `get_bandpower_windows()`; one regular-file-backed unbinned MCM exactly `19,327,352,832` bytes with `/proc/self/maps` proof; full BPW `[4,39,4,12288]`; selected `EE<-EE`, canonical `<f8 [39,12288]`; exact A/B SHA plus `numpy.array_equal`; all finite; no tolerance/allclose/rounding/smoothing/averaging/manual reconstruction/effective-coordinate/fiducial rescue.

Candidate token is frozen as `PASS_EXP073FG_WW_S0_S3_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`. Candidate alone creates no authority; a separate provenance-admission gate remains mandatory.

### Immutable pre-science wrapper failures

Exp073FG run `34033970885`, home job `101488568727`: both GitHub-hosted audits passed, but home wrapper failed immediately on an over-strict transformation check requiring absent optional literal `WW_S0_S2`. Classification: infrastructure/wrapper FAIL `+0/+0`; no heavy numerical science began; no authority.

Exp073FG run `34034127464`, home job `101488993099`: hosted audits passed, but home wrapper again failed immediately because it required the candidate PASS literal to exist in the shell source even though that token is produced dynamically by the Python driver. Classification: infrastructure/wrapper FAIL `+0/+0`; no heavy numerical science began; no authority.

These failures are preserved and must never be relabeled as scientific FAILs.

### Hardened implementation now active

Frozen current files:

- `ci/exp073fg_ww_s0_s3_durable_ab_production_v0_1.py`, blob `d919da63ad5ccd1b94255d9e45face1c922c4f44`;
- `ci/exp073fg_ww_s0_s3_durable_ab_production_v0_2.py`, blob `8749c20f41e5259787307bbd5d556cb772ceba18`;
- `ci/exp073fg_home_filebacked_fullres_v0_1.sh`, blob `77e7f7dafc91ee79767eb31a288633ca1285c66e`;
- `ci/exp073fg_verify_and_prune_replica_v0_1.py`, blob `d925840c60035b30ed1375657585967ec2644e0d`;
- `ci/exp073fg_compare_terminal_receipts_v0_1.py`, blob `74a1a2f8d3b44eaab66e834d69156e1810b75a8e`.

The wrapper prospectively closes the known Exp073FA completed-replica restore weakness rather than relying on a later repair. If a completed, unpruned replica is restored, all six stage manifests plus all still-present source/workspace/full-window/selected/receipt payload hashes must validate. For the normal uninterrupted path, each replica is fully verified across all six stages **before** large intermediates are pruned. The prune receipt binds the SHA256 of every stage manifest and all verified payload hashes. Terminal A/B comparison reads only the bound terminal/prune evidence and selected EE arrays; it does not invoke `--replica AB` and does not restore completed replicas.

Current authoritative workflow run: **`34034377795`**, head `4a02952ee3bcb368a088d87608f61243cd9f7056`. Hosted lineage job `101489652912` = SUCCESS; hosted code/checkpoint audit job `101489652945` = SUCCESS. Home science job **`101489679508`** on `DSIR-HOME-PC` is **IN_PROGRESS** in the frozen `S0->S3` A/B step at this recovery update. Live reconciliation finds exactly one in-progress DSIR run and zero queued runs. Do not inspect/interpret partial numerical output and do not launch a second self-hosted DSIR workload while this job remains queued/in-progress. Exact durable checkpoint stage is `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`, never guessed.

## Parallel GitHub-hosted support — next frontier WW_S1_S1 / Exp073FH

The frozen 14-task manifest orders `WW_S1_S1` immediately after `WW_S0_S3`. Exp073FH preregistration `experiments/073fh_ww_s1_s1_same_field_architecture_v0_1_prereg.md`, blob `0fc09948c7cfb5c05868538544554dc8001a9126`, freezes only a support/static audit; no self-hosted science and no `WW_S1_S1` authority.

`WW_S1_S1` has a materially different semantic boundary from cross-pair `S0_S3`: reconstruct authoritative S1 once, create one spin-2 `NmtField`, and pass the **same field object** on both sides. The generic frozen Article-3 task runner encodes `if bmap is a: fb=fa`; equal-but-distinct field objects are forbidden for this auto-pair.

Exp073FH workflow run **`34034445222`**, head `8856c7df19253310ca286b0e0fc2d4348e5df97a`, completed **SUCCESS**. It verified the frozen S1 R1 constants, unordered `i<=j` task rule, same-field object reuse, WW EE extraction, and no science/radial/covariance/G8 scoring. Classification remains `SUPPORT_PLUS_0_PLUS_0`, `ww_s1_s1_authority_created=false`. This support may be used to prepare the future S1_S1 implementation while Exp073FG computes, but a heavy S1_S1 run must not compete with the current home science job.

## Exp073FI — terminal comparator synthetic hardening CLOSED

Hosted workflow **`34034555778`**, job **`101490139309`**, head `e7159f685f8e848a27bd41e1db9a1f95076d36bb` completed SUCCESS. Raw job log contains exact token `PASS_EXP073FI_EXP073FG_TERMINAL_COMPARE_SYNTHETIC_HARDENING_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, and `ww_s0_s3_authority_created=false`; therefore workflow success is classified only as exact support `+0/+0`, not scientific PASS.

The workflow froze comparator blob `74a1a2f8d3b44eaab66e834d69156e1810b75a8e` and synthetic audit blob `3823687f61cd04489431e3d480c2fae8805bac0d`, compiled them, rejected `np.allclose`/`np.isclose` and rounding/smoothing/averaging rescue patterns, and verified exact identical-array PASS, one-ULP FAIL, and receipt-tamper rejection. No `WW_S0_S3` authority was created and the running Exp073FG arithmetic was not inspected or altered.

Immutable note: `docs/recovery/RECOVERY_2026-09-06_EXP073FI_TERMINAL_COMPARATOR_SYNTHETIC_PASS_FG_RUNNING.md`.

## Frozen Article-3 angular manifest

Exactly 14 unique tasks remain the production inventory: four Wm workspaces and ten unordered WW workspaces. Existing authority includes the admitted S0-row WW tasks through `WW_S0_S2`; `WW_S0_S3` is the active candidate frontier. The ordered 14-window join, radial multiplication, physical-support scoring, covariance/whitening, nuisance quotient/relation/null and G8 remain forbidden until their frozen prerequisites are satisfied.

## Frozen global boundaries

Unless prospectively superseded: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
