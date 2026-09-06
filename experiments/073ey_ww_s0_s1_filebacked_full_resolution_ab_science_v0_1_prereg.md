# Exp073EY — WW_S0_S1 file-backed full-resolution A/B science gate v0.1

Date frozen: 2026-09-06. Scope: DSIR only. RTK/RQIR excluded.

## Authority prerequisites
Exp073EY is permitted only because:
1. `WW_S0_S0` is admitted by Exp073EO v0.2 run/job `34005373819 / 101411448176`, artifact `9980754356`, digest `sha256:0e1a4cff3b761fecc65d8e07df9e56f8109fd221fb4454746caa8c7d0f2fb4be`, token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_2`.
2. Exp073EL v0.3 resource admission run `34005467421`, hosted job `101411738320`, home job `101411728725`, artifact `9980783193`, digest `sha256:f66da69068532134aa91ee35c8beb51e4135123556518adea416802feee38e8e`, passed the unchanged v0.2 checker with token `PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2` and classification `RESOURCE_PASS +0/+0`.
3. Qualified support chain EM/EK/EP/ER/EU/EV/EW/EX remains preserved. Exp073ET remains historical support FAIL `+0/+0` and is not rewritten.

## Scientific question
For the prospectively ordered distinct-field WW cross-workspace `S0 -> S1`, does a fresh full-resolution DES NSIDE=4096 construction produce an exactly repeatable selected `EE<-EE` bandpower-window payload across two independent replicas A and B under the frozen file-backed NaMaster/PyMaster 2.7 route?

This is a scientific repeatability/admission gate. Resource/infrastructure failures remain `+0/+0` and are not scientific FAIL.

## Frozen domain and semantics
- DES NSIDE = 4096.
- `ell = 0..12287`, `LMAX_PLUS_ONE=12288`.
- 39 prospectively fixed bands from the authoritative Article-3 DES angular source contract.
- ordered source pair exactly `(S0,S1)`; never `(S1,S0)` and never same-field shadow.
- reconstruct source count maps prospectively from the frozen R1 authority using `source_count_map(r1_root,0)` and `source_count_map(r1_root,1)`.
- construct two distinct `pymaster.NmtField` Python objects with spin=2: `f0=NmtField(S0,None,spin=2)` and `f1=NmtField(S1,None,spin=2)`; require `id(f0) != id(f1)`.
- compute exactly `NmtWorkspace.compute_coupling_matrix(f0,f1,b)` in that order.
- WW component semantics remain selected `EE<-EE = wins[0,:,0,:]`.
- full public BPW shape exactly `[4,39,4,12288]`; selected canonical payload exactly `<f8 [39,12288]`.
- no effective ell/z/k, no fiducial-P shortcut, no same-field substitution.

## Frozen exact route
Reuse the already qualified DSIR NaMaster 2.7 file-backed MCM patch and direct public BPW route. The workspace MCM is constructed into a regular-file-backed mmap/memmap with exact expected geometry `49152 x 49152 x 8 = 19327352832` bytes. After workspace FITS serialization and verification, use the qualified exact public `get_bandpower_windows()` route in the fresh serialized state. Historical manual P/Q reconstruction, inverse/solver emulation, or a saved-FITS reconstruction rescue is forbidden.

The Exp073EY implementation may reuse proven Exp073EN environment/bootstrap, local Exp073EM storage activation, R1 validation, patch build and post-receipt pruning logic, but must use a new Exp073EY checkpoint namespace and a new ordered `(S0,S1)` durable driver. No Exp073EN numerical payload may be imported.

## Durable checkpoint contract
Replicas A and B are independent. Dedicated namespaces:
- `checkpoints/exp073ey-ww-s0-s1-a-v0-1`
- `checkpoints/exp073ey-ww-s0-s1-b-v0-1`

Each replica must complete, in order:
1. `fresh_sources_complete`: canonical persisted S0 and S1 maps with independent SHA256, R1 authority, source metadata and reconstruction counts.
2. `fresh_workspace_mcm_complete`: ordered distinct-field workspace FITS plus proof `same_field_object_handoff=false`, ordered field indices `[0,1]`, distinct object IDs, source-map SHA identities.
3. `mcm_fits_verified`.
4. `full_window_complete`: exact `[4,39,4,12288]` full BPW payload SHA256.
5. `selected_ee_complete`: exact canonical `<f8 [39,12288]` `EE<-EE` SHA256.
6. `replica_receipt_complete`.

Every manifest is fail-closed on experiment schema, stage, replica, checkpoint namespace, source head and contract fingerprint. Restore must verify every required payload SHA/shape/dtype before reuse. No incomplete stage is restorable. A verified complete stage is never recomputed unnecessarily.

The two replicas must never inspect the other replica's numerical output during construction. A/B comparison occurs only after both final replica receipts exist.

## 8-core execution contract
Home execution requires exactly 8 CPUs in process affinity and exactly 8 outer/OpenMP workers where the qualified native path applies. `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`, `OMP_NUM_THREADS` must not introduce nested oversubscription. Preserve resource telemetry. No arithmetic change is allowed for performance.

## Exact scientific classification
After both complete replicas:
- independently verify selected payload files and canonical metadata;
- require selected A SHA256 == selected B SHA256;
- require `numpy.array_equal(A,B) == true` on canonical `<f8 [39,12288]` arrays;
- require all values finite;
- require both receipts to prove ordered distinct `(S0,S1)` construction, no historical WW numerical import and no other-replica read.

Only if every frozen check passes emit:
`PASS_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`
and classify `WW_S0_S1` scientific PASS candidate pending a separate provenance-admission receipt if the workflow architecture keeps admission separated.

If A/B exact equality fails under an otherwise valid completed frozen run, emit:
`FAIL_EXP073EY_WW_S0_S1_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`
and classify genuine `WW_S0_S1` scientific FAIL. Never repair/tune the science post hoc.

Infrastructure, runner, transport, dependency, storage, checkpoint, source/provenance identity, malformed artifact or resource failures are `+0/+0` and must be repaired/resumed from the last verified checkpoint without changing science.

## Explicitly forbidden rescue
No tolerance, `allclose`, rounding, smoothing, averaging, threshold relaxation, reduced NSIDE/ell, effective ell/z/k, alternate banding, alternate field order, same-field substitution, fiducial-P shortcut, partial-output tuning, or historical numerical import may turn a failure into PASS.

## Launch governance
Before self-hosted activation, a hosted static auditor must verify the new driver/workflow against this preregistration, including ordered `f0,f1`, distinct-object assertion, six-stage checkpoint order, exact selection `[0,:,0,:]`, exact-only A/B comparison, 8-core/nested-thread constraints, file-backed route, source/contract/EO/EL bindings and absence of rescue patterns. The home runner must be live-exclusive at dispatch.
