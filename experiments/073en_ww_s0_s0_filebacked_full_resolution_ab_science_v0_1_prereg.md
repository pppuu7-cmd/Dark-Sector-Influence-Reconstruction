# Exp073EN — WW_S0_S0 file-backed full-resolution A/B exact science v0.1 preregistration

Prepared prospectively on 2026-09-06 after terminal support-only `PASS_EXP073EM_NAMASTER27_FILEBACKED_MMAP_EXACT_STORAGE_V0_1` from hosted run `33993395728`, job `101379508508`, artifact `9977333691`, artifact digest `sha256:0ece75e489b6f413d96e85a099e42db96b5d5acdc03c3ee6901273357762cda1`.

Exp073EN replaces only the unsafe storage backend used by the historical Exp073DT full-resolution `WW_S0_S0` attempt. It does not change the frozen DSIR science arithmetic, masks, binning, field semantics, downstream exact adapter, source authority or acceptance target.

## Frozen science identity
- source authority: `de83e20a68f79ccf25b89b0d33eb4206e294c757`;
- contract fingerprint: `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- R1 artifact ID: `9720335366`;
- R1 artifact digest: `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- DES `NSIDE=4096`, ell `0..12287`, `nl=12288`, 39 frozen bands;
- spin-2 auto-field `S0 -> S0`, same `NmtField` object on both sides of each replica;
- full BPW semantics `[4,39,4,12288]`;
- selected authority payload `wins[0,:,0,:] = EE<-EE`, canonical `<f8 [39,12288]`;
- two independently reconstructed replicas A and B under distinct durable checkpoint namespaces;
- exact equality only: canonical SHA256 equality and `numpy.array_equal`; no tolerance, allclose, rounding, smoothing, averaging or rescue.

## Qualified storage backend
The only permitted change relative to the frozen Exp073DT arithmetic is the Exp073EM storage-only NaMaster 2.7 patch:
- NaMaster tag `v2.7`, exact source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- patch `patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch`;
- frozen patch SHA256 `9a80a756960afa8b4ddf61b5fbba7fba6ad5ed9ac919e093bb1365a636c789f0`;
- regular-filesystem `mmap(MAP_SHARED)` backing for `nmt_workspace::coupling_matrix_unbinned` only;
- all MCM formulas, OpenMP loop bodies/order, binning, GSL LU operations, FITS serialization and public PyMaster API remain unchanged.

Hosted Exp073EM established bit-for-bit equality between stock and patched PyMaster 2.7 for frozen small-NSIDE spin-2 `auto0`, `auto1` and ordered `cross01`: WSP, full BPW and selected `EE<-EE` all have equal shapes, `numpy.array_equal=true`, canonical SHA equality and max absolute difference `0.0`; regular-file mapping proof passed in all cases. Exp073EM is support-only `+0/+0` and created no WW authority.

Before full-resolution work, Exp073EN must also execute the same stock-vs-patched exact qualifier locally on `DSIR-HOME-PC` using the exact local stock runtime and the cloned patched runtime. Any bit difference blocks full-resolution science; it cannot be tolerance-rescued.

## Resource and durability contract
At full resolution the raw unbinned WW MCM is exactly `19,327,352,832` bytes (`18 GiB`; `49152 x 49152` float64). Full-resolution activation requires:
- at least 70 GiB free on the Windows host volume and at least 70 GiB available in the WSL filesystem at start;
- WSL memory/swap telemetry and mapped-file size telemetry throughout each expensive replica;
- proof in the persistent driver log that each newly computed full-resolution workspace used a regular file-backed mapping with exactly `19327352832` bytes and `49152` rows;
- no surviving `dsir-nmt-mcm-*` backing file after each replica process exits;
- exactly one heavy DSIR process under nonblocking `flock` ownership on `DSIR-HOME-PC`;
- OMP team 8 for the frozen downstream emulator and nested BLAS/MKL/OpenBLAS/NumExpr/BLIS threads pinned to 1.

Replica A and B are executed as separate processes. After a replica reaches its verified `replica_receipt_complete` durable checkpoint, its huge workspace FITS and canonical full-MCM intermediate may be pruned only after their hashes/provenance are already bound by the durable receipts. The selected `EE<-EE` payload, replica receipt and all checkpoint manifests must remain. This allows A to release roughly 36 GiB of temporary disk before B starts without altering any numerical result.

Interrupted replicas resume only through the existing fail-closed manifest/SHA validation of `ci/exp073dq_ww_s0_s0_durable_ab_production_v0_1.py`. No historical numerical WW output may be imported into a fresh replica.

## Terminal classification
`PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1` requires all of:
- hosted Exp073EM immutable PASS identity;
- local stock-vs-patched Exp073EM exact PASS;
- full-resolution regular-file mmap proof for every newly computed replica workspace;
- exact A/B selected payload equality with equal canonical SHA256 and `numpy.array_equal=true`;
- finite canonical `<f8 [39,12288]` selected payloads;
- all frozen source/contract/component identities and durable replica receipts valid;
- no tolerance rescue.

A terminal exact PASS is a prospective WW_S0_S0 science-candidate PASS. Final WW_S0_S0 authority admission remains withheld until the uploaded Exp073EN evidence artifact and complete A/B checkpoint provenance are independently consumed and admitted in the next provenance gate (Exp073EO, serving the role previously reserved for Exp073EB on the superseded DT route).

Any stock-vs-patched arithmetic difference is infrastructure/storage qualification failure `+0/+0`, not a dark-sector science FAIL. Runner loss, build failure, disk/resource exhaustion, provenance mismatch or malformed checkpoint is infrastructure/BLOCKED `+0/+0`. A genuine A/B numerical repeatability mismatch after all storage/provenance checks is a scientific repeatability FAIL.

Status before workflow activation: `PREREGISTERED`; `ww_s0_s0_authority_created=false`.
