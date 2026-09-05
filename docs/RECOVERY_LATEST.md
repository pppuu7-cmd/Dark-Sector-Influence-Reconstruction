# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-06
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Frozen science boundaries remain unchanged.

## Preserved scientific authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0`, Exp073BU runner-loss infrastructure `+0/+0`, and Exp073DT attempts 1–4 infrastructure outcomes remain historical. Current scientific target remains `WW_S0_S0`.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

## Exp073DT attempt 5 — terminal manual resource-safety cancellation, no science classification
Run `33940588308`, attempt 5; hosted preflight job `101374977192` SUCCESS; self-hosted science job `101374976626` terminal `failure` because the full science step was manually cancelled for resource safety. Frozen head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`; source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`.

The cancellation is infrastructure/resource `+0/+0`, not a WW arithmetic FAIL. `Upload terminal science evidence` was skipped and no terminal science receipt exists, so no `WW_S0_S0` authority was created.

### Measured full-resolution resource diagnosis
The home machine has about 7.68 GiB physical RAM. WSL is configured with 6 GiB memory and 16 GiB swap. At frozen WW geometry `ncls=4`, `nl=12288`, the unbinned MCM has `49152 x 49152` float64 values = exactly `19,327,352,832` bytes = `18 GiB` before field/GSL/Python overhead.

Attempt 5 telemetry established the causal resource bottleneck under the stock heap-backed NaMaster 2.7 path. During the full-resolution workspace build, WSL RAM reached approximately 5.7–5.8/5.8 GiB, available RAM fell as low as about 10 MiB, swap rose from about 4.6 GiB to 8.1 GiB, and the Python process alternated between running and uninterruptible I/O wait. After manual cancellation the science Python disappeared and memory recovered to about 490 MiB used with about 114 MiB swap. This directly binds the pressure to the stock full-resolution workspace construction rather than to a science comparison or downstream exactness check.

Windows `Microsoft-Windows-Resource-Exhaustion-Detector` and `Microsoft-Windows-Hyper-V-Compute-Operational` produced no matching events in the earlier requested diagnostic interval; previous runner shutdowns therefore remain infrastructure history, but the measured attempt-5 memory/swap telemetry independently establishes that stock heap-backed full WW MCM is unsafe on this host.

Do not re-run Exp073DT on stock heap-backed NaMaster 2.7 on DSIR-HOME-PC.

Exp073EB remains mandatory support-only provenance closure for any future valid `WW_S0_S0` authority attempt.

## Distinct-field exact-adapter investigation — Exp073EK closes the hosted exact-operation qualifier
Historical support-only chain remains: Exp073DU/DW qualifier FAIL; Exp073DX excluded FITS orientation; Exp073ED excluded low-level/public BPW tensor layout; Exp073EE established formula mismatch; Exp073EF localized mismatch before solve; Exp073EG established manual P/bin mismatch while Q/unbin was exact; Exp073EH showed official P/Q plus NumPy inversion still not exact; Exp073EI showed NumPy inverse differs bitwise from official decoupling operator; Exp073EJ showed columnwise public `decouple_cell` composition still differs bitwise from public `get_bandpower_windows()`.

### Exp073EK — terminal `DIRECT_PUBLIC_BPW_ADAPTER_EXACT +0/+0`
Run/job `33988956806 / 101367596573`, head `51f8a7d7dd481e79b734ba174bffa29236f2fc0b`, artifact `9976033816`. GitHub artifact digest is `sha256:f39351cddec695559686126fc15e212556eea370fe3eeab73d5f20f80c288c06`.

Frozen token `PASS_EXP073EK_DIRECT_PUBLIC_BPW_ADAPTER_EXACT_V0_1`. Two independent reloads of the same serialized distinct S0->S1 PyMaster 2.7 workspace followed by only public `NmtWorkspace.get_bandpower_windows()` are exact under the qualifier: full A/B SHA `aa883a13c305641e6e1aab5feca4692a8da1cdbcca16e8c124f12e601608d628`, selected `EE<-EE` A/B SHA `9e7a0e169d752e56d4a1f14244c58ac9a14a5c1a3782c27b3a6562a69cb0cf5e`, full and selected `numpy.array_equal=true`, no tolerance rescue. `science_gate_scored=false`; `ww_authority_created=false`.

Direct serialized-workspace reload + public BPW is therefore the sole currently qualified exact cross-workspace adapter candidate.

### Exp073EL — preregistered, not activated
`experiments/073el_ww_cross_direct_public_bpw_full_resolution_resource_gate_v0_1_prereg.md` freezes the full-resolution readiness contract for the EK-qualified direct-public-BPW operation. It must not be activated on stock heap-backed NaMaster 2.7 because the attempt-5 resource telemetry now shows that the prerequisite full workspace construction is unsafe on DSIR-HOME-PC.

### Exp073EM — preregistered low-memory exact-storage qualifier, not activated
Commit `54a4e2732f3af8226609c7d9bd45eee01531ac3b` adds `experiments/073em_ww_namaster27_filebacked_mmap_unbinned_exact_storage_qualifier_v0_1_prereg.md`.

Exp073EM changes infrastructure only: when explicitly enabled, NaMaster 2.7's dense unbinned MCM storage is to move from heap `calloc` rows to a regular-file-backed `mmap(MAP_SHARED)` region while preserving the public API, MCM formulas, loop ordering, binning arithmetic, GSL LU operations, FITS serialization and public BPW arithmetic. It must prove stock-vs-patched bitwise equality on frozen small-NSIDE spin-2 auto and ordered cross cases before any full-resolution use. Support-only `+0/+0`; no WW authority.

The raw full-resolution mapped MCM is exactly 18 GiB. Mapping plus serialized workspace may overlap at about 36 GiB, so full-resolution activation requires a real disk-free gate with at least about 40 GiB free plus telemetry. Anonymous mmap/tmpfs/memfd is forbidden for the full MCM because it would return pressure to RAM/swap.

## Frozen science/execution boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gates
1. Keep all stock heap-backed full-resolution WW runs disabled on DSIR-HOME-PC.
2. Implement Exp073EM as a pinned NaMaster/PyMaster 2.7 storage-only patch and run the prospectively frozen small-NSIDE exact qualifier on hosted infrastructure or another non-competing environment.
3. Only after `PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1`, freeze patch/source/compiler/build hashes and run a disk/RAM/swap readiness check before any full-resolution home activation.
4. Re-run the frozen `WW_S0_S0` authority path using the exact-qualified file-backed storage backend without changing science arithmetic; consume exact A/B evidence plus Exp073EB provenance before authority creation.
5. Keep Exp073EL and Exp073DV inactive until the low-memory storage path is exact-qualified and a valid `WW_S0_S0` authority exists. Then proceed to the ordered distinct-field frontier under the EK-qualified public-BPW semantics.
