# Exp073R1 v0.6 transport EOF on attempt 1; exact rerun attempt 2

Date: 2026-08-29
Repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`
Branch authority at checkpoint creation: `main`

## Canonical run

- Workflow run: `33222848695`
- Workflow: `.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`
- Attempt 1 job: `99020389131`
- Attempt 1 conclusion: `failure`
- Attempt 2 job after exact GitHub Actions rerun: `99062223326`
- Attempt 2 initial state at checkpoint: `queued`

## Attempt 1 classification

Attempt 1 passed the evaluator/firewall check, immutable Stage-A and Exp073R0 metadata binding, runtime setup, artifact download, and internal parent rebinding. The authoritative `metacal-map` step then advanced through 37,748,736 rows and failed before any terminal Exp073R1 assertion.

The exception was:

`EOFError: whole stream ended after 18479432 of requested 40239104 bytes`

The failure occurred inside `read_exact(...)` while reading the remote DES whole-object HTTP response. The final genuine reproduction PASS assertion was therefore skipped.

Classification is frozen as:

`INFRASTRUCTURE_TRANSPORT_FAILURE_REMOTE_WHOLE_OBJECT_EOF`

This is **not** a scientific FAIL, **not** a support-validity result, and **not** evidence against any DSIR physical hypothesis. No downstream G7/G8 quantity is authorized by this failed attempt.

## Frozen scientific and reproduction contract

No acceptance criterion is changed. In particular:

- evaluator remains `ci/exp073r1_sequential_wholestream_v0_5.py` with frozen Git blob SHA-1 `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- source whole-object SHA256 remains `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- source index SHA256 remains `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`;
- metacal expected bytes remain `84075649920`;
- metacal expected SHA256 remains `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- required rows remain `136930995`;
- selection remains `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- mapper remains NSIDE=4096, RING, coordinates C, `lonlat=True`;
- required transport assertion remains zero Range requests with one whole-object GET as encoded by the frozen evaluator;
- `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false` remain required before the terminal reproduction PASS.

## Recovery action taken

Because no heavy Exp073R1 job remained active after attempt 1, a single exact GitHub Actions rerun of the failed job was started. This does not create a new scientific contract and does not alter the evaluator. It tests whether the remote premature EOF was transient while preserving the same frozen reproduction target.

No additional duplicate heavy run was started.

## Runtime provenance observed on attempt 1

The isolated environment installed and reported:

- NumPy `2.5.2`
- healpy `1.20.0`

The wheel tags show the self-hosted Python ABI was CPython 3.14 (`cp314`). These observed versions are provenance for this execution family and must not be silently changed when interpreting an exact rerun as equivalent.

## Gate order remains closed downstream

Until a genuine Exp073R1 terminal PASS exists, the required order remains:

1. validated physical forward/power-input bridges;
2. genuine Exp073R1 reproduction PASS prerequisite;
3. preregistered physical support-validity mask;
4. covariance restriction / whitening;
5. nuisance tangent rank / SVD;
6. quotient / relation / null control;
7. only then a fresh G8 withheld family.

Attempt-1 transport failure authorizes none of steps 3-7.
