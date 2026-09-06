# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. Historical negative/resource/infrastructure outcomes remain immutable.

`WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`.

`WW_S0_S1` remains admitted by Exp073EZ run/job `34017921734 / 101444964371`, exact token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`. Its Exp073EY candidate remains run/job `34010599584 / 101425638857`, artifact `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`, selected exact A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`.

## Current frontier — WW_S0_S2 / Exp073FA

Science prereg `experiments/073fa_ww_s0_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`, blob `edc044792be8ac7b796c8469943924942ae91932`. Frozen: ordered `(S0,S2)` / authoritative R1 indices `[0,2]`; source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; NSIDE=4096; ell `0..12287`; 39 bands; public serialized `read_from(...,read_unbinned_MCM=True)->get_bandpower_windows()`; one regular-file-backed MCM exactly `19,327,352,832` bytes; full `[4,39,4,12288]`; selected `EE<-EE <f8 [39,12288]`; exact SHA plus `numpy.array_equal`; all finite; no tolerance/rounding/smoothing/averaging/manual-reconstruction rescue. Durable namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `...-b-v0-1`; exact six-stage chain and fail-closed restore. Candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate alone never creates authority.

Exp073FA prerequisite audit `34018080500 / 101445404866` = exact support PASS `+0/+0`.

Repaired Exp073FB `34018241319 / 101445845648` = exact implementation support PASS `+0/+0`, artifact `9984600349`, independently verified ZIP SHA256 `b371821a77cb4a62051ceee45f82764a5486ea3b0bcf0939a9bcac0eff624cda`. Generated/committed driver SHA256s are v0.1 `fe354b95e9aeefe0772f4c7eecbba6e1944fb1f4955fceb3e9e72ed1c06b293a`, v0.2 `77f321e22c923d8d5996105487cae9afb6eecc5863174d849b092164a26824ba`.

Exp073FC run/job `34018341064 / 101446155067` is terminal raw-verified exact support PASS `+0/+0`: `PASS_EXP073FC_EXP073FA_COMMITTED_DRIVER_BINDING_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`. It independently binds the committed Exp073FA driver bytes to the repaired Exp073FB artifact. No WW authority was created.

## Exp073FD — audited home execution envelope

Prospective prereg `experiments/073fd_exp073fa_home_execution_envelope_v0_1_prereg.md`, Git blob `6636766b565956d6af28ae04bcdeec1a410259a1`; home envelope `ci/exp073fa_home_filebacked_fullres_v0_1.sh`, Git blob `309c464bbfbe4896bd560165985ee7f643d9ee22`; qualified FITS-read patch blob `d534b698f9131688d263eedcef27260386c58641`; R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

The envelope enforces local flock plus live GitHub self-hosted exclusivity, exactly 8 CPU affinity with `OMP_NUM_THREADS=8` and nested BLAS-family threads pinned to 1, >=50 GiB WSL and Windows C: free-space floors, qualified PyMaster 2.7 read-patch identity, local Exp073EM exact storage qualifier, R1 validation, independent A/B complete-stage checkpointing and compact terminal/partial evidence. The monolithic NaMaster workspace computation is not converted into an 8-outer-worker algorithm because doing so would alter the frozen arithmetic; the eight-core constraint is therefore enforced as CPU affinity/OMP for this gate.

First Exp073FD run `34020704615`, hosted job `101452648911`, is historical `INFRASTRUCTURE_STATIC_LOG_TRANSPORT_FAIL +0/+0`: GitHub job logs were treated as ZIP although the endpoint returned text; home science was skipped. Minimal repair changed only FC job-log transport/parsing to direct text grep. Science, drivers, envelope, source head, contract, patch, R1 identity and acceptance rules were unchanged.

## Authoritative current process

Repaired Exp073FD workflow run **`34020756634`**, head **`894885b2c2b811954d1724c2733d2a810a486d70`**, branch `main`, started `2026-09-06T08:02:37Z`.

Hosted audit job **`101452788638`** = terminal SUCCESS. Raw log was inspected and contains `PASS_EXP073FD_EXP073FA_HOME_ENVELOPE_STATIC_AUDIT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `ww_s0_s2_authority_created=false`.

Dependent home science job **`101452805620`** is currently **IN_PROGRESS** inside the frozen A/B step. `DSIR-HOME-PC` is exclusively owned by this job; no competing self-hosted DSIR workload may launch. Partial numerical output is not inspected. Last durable checkpoint is therefore recorded prospectively as `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`, never guessed.

Immutable current recovery note: `docs/recovery/RECOVERY_2026-09-06_EXP073FC_PASS_EXP073FD_HOME_RUNNING.md`, creation commit `ce5a786fbffabc02f759b83c8925c75f818a85c5`.

On terminal state: immediately consume job steps/logs and compact artifact; independently verify ZIP SHA256 against GitHub digest; verify source/contract/driver/patch/R1/checkpoint identities, complete six-stage chains, exact `19,327,352,832`-byte mmap proof, exact canonical A/B `EE<-EE`, finiteness and frozen token. Candidate PASS must then pass a separately frozen hosted provenance admission bound to the exact terminal run/job/artifact/digest before `WW_S0_S2` authority may exist. Infrastructure failure is a causal repair/resume condition preserving validated checkpoints; exact A/B mismatch is a genuine scientific FAIL.

## Frozen global boundaries

Unless prospectively superseded: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.