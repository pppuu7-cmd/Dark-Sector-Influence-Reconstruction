# Exp073CE v0.1 — Exp073BU integrated A/B driver static audit preregistration

Status: PROSPECTIVE / SUPPORT-ONLY / +0/+0 / NO Wm_S3 AUTHORITY.

## Purpose
Before any Exp073BU self-hosted scientific activation, freeze and statically audit one integrated A/B driver contract that composes the already validated fresh-input/fresh-PCL lineage, exact NaMaster 2.7 full ncls=2 operation order, stock workspace persistence, verified OS-mmap downstream path, and Exp073CD durable checkpoint design.

This gate performs no Wm_S3 numerical science and cannot create Wm_S3 scientific authority.

## Frozen scientific domain (unchanged)
- 0.295 <= z <= 2.33.
- 0 < k <= 0.06664762008318016 Mpc^-1.
- Layer-A operator_f_invalid <= 0.05.
- Layer-B invalid-row fraction <= 0.05.
- retained dimension >= 15.
- DES NSIDE=4096; ell=0..12287; 39 bands.
- Wm uses TE <- TE; WW uses EE <- EE.
- canonical Wm output is little-endian float64 `<f8` shape [39,12288].
- no effective ell/z/k and no fiducial-P shortcut.
- exact-threshold ambiguity is `numerically_unresolved`; no tolerance, rounding, smoothing or averaging rescue.

## Frozen integration requirements
1. Replica A and replica B each start from the same immutable admitted S3/lens provenance but must independently build fresh masks and fresh replica-local PCL. Historical Wm_S3 PCL, reference bands, numerical checkpoints or candidate output payloads are forbidden inputs.
2. Exact NaMaster 2.7 full-component ncls=2 stock arithmetic is required. The historical compact/selected construction is forbidden as an exact substitute.
3. Full unbinned MCM persistence must use the stock workspace writer path (`write_to()` / native writer) without `get_coupling_matrix()` materialization.
4. The workspace owning the full MCM must be destroyed before the persisted FITS MCM is consumed through an OS-backed read-only mmap route. The downstream route may stream complete rows and may not create a second full MCM heap copy.
5. Durable per-replica checkpoint boundaries, in this exact order, are:
   - fresh_masks_complete
   - fresh_workspace_mcm_complete
   - mcm_fits_verified
   - full_window_complete
   - selected_te_complete
   - replica_receipt_complete
6. A and B own separate checkpoint namespaces. Cross-replica numerical restore is forbidden. Every restore is fail-closed and binds checkpoint identity, contract fingerprint, source/head identity, immutable provenance and canonical payload SHA256.
7. Home heavy architecture, where outer parallelism is applicable, is exactly 8 outer workers with nested BLAS/OpenMP/MKL/OpenBLAS threads pinned to 1. Work units are complete independently durable units; verified units are never recomputed unnecessarily.
8. Final scientific comparison may occur only after both replicas independently reach valid `replica_receipt_complete` under identical frozen provenance/contract. PASS requires both whole canonical array SHA256 equality and `numpy.array_equal(A,B)`. A valid exact mismatch is `SCIENTIFIC_REPEATABILITY_FAIL`. Missing/malformed provenance, checkpoint, source-head or contract identity is infrastructure/BLOCKED, never a scientific mismatch.
9. Exp073BU scientific activation is a separate explicit future action after this hosted static audit PASS and a fresh live Actions no-competition check. Exp073CE itself must not queue a self-hosted scientific job.

## Static-audit token
`I1_EXP073BU_INTEGRATED_DRIVER_STATIC_AUDIT_PASS` only if every requirement above is machine-checked against the integrated contract/driver source. Otherwise emit `I2_INTEGRATION_CONTRACT_STATIC_FAIL` or `I3_INFRASTRUCTURE_INCOMPLETE` and remain +0/+0.

## Accounting
All Exp073CE outcomes are +0/+0 and create no Wm_S3 scientific authority. Historical negative/infrastructure results remain historical and are not rewritten.
