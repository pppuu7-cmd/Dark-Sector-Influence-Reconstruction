# DSIR recovery checkpoint — Exp073R1 v0.6 self-hosted runtime repair active

Date: 2026-08-29
Branch: `main`

## What failed

The first self-hosted Stage-B run was GitHub Actions run `33212521957`, job `98988824629` (`metacal-map-longrun`) on runner `DSIR-HOME-PC` / machine `win-ws338`.

The runner itself connected and accepted the job correctly. The preregistered evaluator-blob firewall and immutable parent-metadata binding both passed. The job then failed before any authoritative 84 GB metacal streaming began because the runner's distro-managed Python 3.14 rejected:

`python3 -m pip install --user numpy healpy`

with PEP-668 `externally-managed-environment`.

Classification: **infrastructure/runtime failure only**. It is not an Exp073R1 scientific FAIL, not a DES-data mismatch, and not a parent-provenance failure.

## Repair

Workflow file:

`.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`

Runtime-only repair commit:

`5f773b3600defd5c5a2e94b8ef9489bb9ba32787`

The mapper runtime is now created in an isolated runner-temp virtual environment. `numpy` and `healpy` are installed only inside that venv and its `bin` directory is exported through `GITHUB_PATH` for subsequent steps.

The frozen science evaluator remains unchanged:

`ci/exp073r1_sequential_wholestream_v0_5.py`

blob:

`46fe1271d97ddd9e2164d24e7d79cf27bfda805d`

No source/metacal identity, row semantics, selection, HEALPix convention, serialization, gate criterion, covariance policy, or downstream science contract was changed.

## Relaunch authority

Trigger commit:

`98c4b8783a95932949947d9e214706c4ec7eaf8c`

New canonical heavy run:

- workflow: `Exp073R1 DESY1 self-hosted long-run Stage-B v0.6`;
- run ID: `33222848695`;
- job ID: `99020389131`;
- head SHA: `98c4b8783a95932949947d9e214706c4ec7eaf8c`.

Protocol guard run `33222848631` completed successfully and asserted the single canonical frozen v0.6 Stage-B route.

At checkpoint creation the heavy run had already passed:

1. checkout;
2. preregistered unchanged-evaluator firewall;
3. immutable Stage-A / Exp073R0 metadata binding;
4. repaired isolated mapper-runtime installation;
5. Stage-A artifact download;
6. Exp073R0 artifact download;
7. downloaded-parent internal-contract re-binding.

The run had entered the canonical step:

`Sequentially stream authoritative 84GB metacal object and execute unchanged frozen mapper`

No duplicate heavy run is authorized while run `33222848695` remains active.

## Frozen authoritative identities

Stage-A source authority:

- source whole-object SHA256: `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- source rows: `136930995`;
- source-index bytes: `273861990`;
- source-index SHA256: `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`.

Metacal authority:

- bytes: `84075649920`;
- SHA256: `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- rows: `136930995`.

The transport remains exactly one ordinary whole-object HTTP GET, no Range requests, `Accept-Encoding: identity`, exact byte count and exact full-object SHA256.

## Resource audit of the unchanged mapper

The 84 GB metacal object is streamed and hashed; it is not staged as an 84 GB local file.

For `NSIDE=4096`, `npix = 12 * NSIDE^2 = 201326592`.

Main local resources are therefore bounded approximately by:

- Stage-A source index: `273861990` bytes (~261 MiB), memory-mapped;
- one mask-count scratch memmap: `201326592 * 4 = 805306368` bytes (768 MiB), one bin/pass at a time;
- pixel-record files: at most `136930995 * 4 = 547723980` bytes (~522 MiB) in the impossible worst case that every source row is selected exactly once across bins;
- four bit-packed masks: `4 * (201326592 / 8) = 100663296` bytes (96 MiB);
- one metacal row chunk: `65536 * 614 = 40239104` bytes (~38.4 MiB), plus bounded NumPy working arrays.

Thus the long-run design is network/time dominated rather than requiring 84 GB of local disk or RAM. The dominant temporary disk object is the ~768 MiB uint32 count memmap.

## Scientific state

Exp073R1 remains **INCOMPLETE**, not PASS, until run `33222848695` finishes the whole 84 GB object, verifies its exact SHA256, reconstructs all four masks twice, and the terminal post-execution assertions pass.

Current gates remain:

- G7: OPEN;
- G8: OPEN;
- G9: OPEN;
- Exp073P physical support: BLOCKED;
- covariance/whitening: BLOCKED;
- nuisance quotient: BLOCKED.

A genuine Exp073R1 PASS closes only the exact DES-Y1 reproduction prerequisite. Per the frozen v0.6 preregistration, the next scientific action after immutable R1 PASS is Exp073P under its already frozen physical-support contract. Only an explicit Exp073P support PASS may authorize covariance restriction/whitening.
