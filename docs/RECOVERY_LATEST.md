# DSIR authoritative recovery — latest

Updated: 2026-09-06. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 exact scientific PASS remain preserved. Historical negative/resource/infrastructure outcomes remain immutable.

`WW_S0_S0` remains admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`.

`WW_S0_S1` remains admitted by Exp073EZ run/job `34017921734 / 101444964371`, exact token `PASS_EXP073EZ_WW_S0_S1_FILEBACKED_PROVENANCE_ADMISSION_V0_1`, `classification=SCIENTIFIC_AUTHORITY_ADMITTED`. Its Exp073EY candidate remains run/job `34010599584 / 101425638857`, artifact `9983630139`, independently verified ZIP SHA256 `12291c1c9f6100ebfb03a6db1e613f422bd48bc6c02720f89ee613c8646cf9d6`, selected exact A/B SHA `49af7a3d165daaf7cc6781e2286e45cd5baa0042ed9770800588bced7d700e79`.

## Current frontier — WW_S0_S2 / Exp073FA

Science prereg `experiments/073fa_ww_s0_s2_filebacked_full_resolution_ab_science_v0_1_prereg.md`, blob `edc044792be8ac7b796c8469943924942ae91932`. Frozen: ordered `(S0,S2)` / authoritative R1 indices `[0,2]`; source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; NSIDE=4096; ell `0..12287`; 39 bands; public serialized `read_from(...,read_unbinned_MCM=True)->get_bandpower_windows()`; one regular-file-backed MCM exactly `19,327,352,832` bytes; full `[4,39,4,12288]`; selected `EE<-EE <f8 [39,12288]`; exact SHA plus `numpy.array_equal`; all finite; no tolerance/rounding/smoothing/averaging/manual-reconstruction rescue. Durable namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `...-b-v0-1`; exact six-stage chain and fail-closed restore. Candidate token `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`; candidate alone never creates authority.

Exp073FA prerequisite audit `34018080500 / 101445404866` = exact support PASS `+0/+0`. Repaired Exp073FB `34018241319 / 101445845648` = exact implementation support PASS `+0/+0`, artifact `9984600349`, independently verified ZIP SHA256 `b371821a77cb4a62051ceee45f82764a5486ea3b0bcf0939a9bcac0eff624cda`. Exp073FC `34018341064 / 101446155067` = terminal raw-verified support PASS `+0/+0`, token `PASS_EXP073FC_EXP073FA_COMMITTED_DRIVER_BINDING_V0_1`.

## Authoritative current science process

Repaired Exp073FD workflow run **`34020756634`**, head **`894885b2c2b811954d1724c2733d2a810a486d70`**, branch `main`, started `2026-09-06T08:02:37Z`. Hosted audit job **`101452788638`** = terminal SUCCESS `+0/+0`. Dependent home science job **`101452805620`** remains **IN_PROGRESS** inside the frozen A/B step. `DSIR-HOME-PC` is exclusively owned by this job; no competing self-hosted DSIR workload may launch. Partial numerical output is not inspected. Last durable checkpoint remains `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`, never guessed.

## Exp073FE — checkpoint/restore hardening support CLOSED

While Exp073FA was still running and before any terminal numerical output was inspected, static audit found a result-independent implementation/provenance issue: after completing and pruning A and B, the home wrapper invokes the driver again as `--replica AB`; v0.1 `validated_finished()` then restores a completed replica after checking only the terminal receipt and selected EE payload, not the entire six-stage chain and all prior payloads. The Exp073FA preregistration requires complete-stage restores to occur only after exact identity and payload verification. This does **not** change frozen science and does not imply a scientific FAIL.

Exp073FE prereg `experiments/073fe_exp073fa_terminal_compare_checkpoint_restore_hardening_v0_1_prereg.md`, blob `43ff6dfe8d1eb682202b142e6ed2408a4beb00f7`. Comparator `ci/exp073fe_compare_exp073fa_terminal_receipts_v0_1.py`, blob `14841dc412d3989e6f86294072479424f26cec93`, compares terminal A/B receipts and selected EE payloads without restoring completed replicas merely to compare them; it fail-closes frozen identities, selected SHA/size, exact SHA equality, `numpy.array_equal`, finiteness, no-cross-read/no-historical-import and no-tolerance policy.

First hosted Exp073FE audit **`34023253707 / 101459598645`** remains immutable `INFRASTRUCTURE_DEPENDENCY_FAIL +0/+0`: raw logs show `ModuleNotFoundError: No module named 'numpy'` before comparator testing. Minimal repair only installed NumPy in the hosted audit environment; comparator, prereg and science were unchanged.

Repaired Exp073FE **`34023325339 / 101459798149`**, head **`a4e832e9e275f2baa4958279c7b4a01d220df934`**, is terminal raw-verified exact support PASS `+0/+0`. Raw log contains `PASS_EXP073FE_EXP073FA_TERMINAL_COMPARE_RESTORE_HARDENING_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `ww_s0_s2_authority_created=false`. The synthetic audit proves exact PASS for byte-identical arrays, exact scientific FAIL after a one-ULP mismatch, and fail-closed rejection of receipt tampering. No WW authority was created.

Immutable current recovery note: `docs/recovery/RECOVERY_2026-09-06_EXP073FE_PREREG_RESTORE_HARDENING_FA_RUNNING.md`, creation commit `f800d5b3889726baa5ef9ebc7b1b750abfcd644e`.

On terminal Exp073FA: immediately consume job steps/logs and compact artifact; independently verify ZIP SHA256 against GitHub digest; verify source/contract/driver/patch/R1/checkpoint identities, complete six-stage chains, exact `19,327,352,832`-byte mmap proof, exact canonical A/B `EE<-EE`, finiteness and frozen token. Exact A/B mismatch remains genuine scientific FAIL. A matching candidate remains non-authoritative; if the complete frozen checkpoint/provenance contract cannot be proven, classify provenance/infrastructure `+0/+0`, preserve validated evidence, and apply the smallest prospective repair. Only a separately frozen hosted provenance admission may create `WW_S0_S2` authority.

## Frozen global boundaries

Unless prospectively superseded: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.