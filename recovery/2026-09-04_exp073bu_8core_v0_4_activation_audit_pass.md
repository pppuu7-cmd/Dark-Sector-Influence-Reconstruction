# Exp073BU 8-core activation v0.4 — hosted audit PASS

Date: 2026-09-04
Scope: DSIR only.

## Status

`PASS_EXP073BU_8CORE_ACTIVATION_AUDIT_V0_4`

Support-only result (`+0/+0`); no DES-scale science numerics and no Wm_S3 authority.

## Historical v0.3 infrastructure stop

Run/job `33901049626 / 101114995516` verified `home_affinity_cpus=8`, PyMaster 2.7 with `OMP_NUM_THREADS=8`, exact R1 staging, exact DES lens-mask staging, and OpenMP-8 compilation. It stopped before science because the tiny runtime probe invoked system `python3`, which lacked NumPy. The OpenMP executable was not reached by that probe. This is infrastructure-only history.

## Prospective v0.4 repair

The sole repair is that the runtime probe now uses the already verified frozen NaMaster interpreter `$NMT_PY` instead of system `python3`. All numerical implementation blobs remain unchanged from the exact-equivalence-certified 8-core branch.

science_workflow_blob=f8c70a4206321b0dc10b57f63a2a06163da2249a
v04_prereg_blob=819ead893b45f93270133dde32ccaf942401a6c4
original_science_prereg_blob=816542c7eb7a8ba4e72d6e01228aa62d05c7c805
eightcore_prereg_blob=1da32a7647601c2c876c2392bf9e17dfd5a8593e
driver_blob=2b44ddd2c1167739f643a0f1c23cfbf7905fa464
adapter_blob=63ee393791bba43d3eabbea654efdb9d439d477e
omp_source_blob=be4f381de4c5c043a9c0fcd107e63ef3f2079578
launcher_blob=8a725ba135e3e120ce6e8d0db3dd14d95d4ffd6e

The immutable exact-equivalence authority remains `PASS_EXP073BU_8CORE_EXACT_EQUIVALENCE_V0_3` from run/job `33900913648 / 101114517184`.

## Hosted activation audit authority

- run/job: `33901386471 / 101116035558`
- activation head: `960b6a06095d28bbe7d2a5f0111d31641d12fc82`
- artifact ID: `9947758011`
- artifact digest: `sha256:1517ccb3cfb2a6f8ee036de1062c7e181494a4b519441089530b418d967d1f7c`

All steps passed. The audit bound the immutable science and exact-equivalence authorities, verified the v0.4 workflow blob, verified that the runtime-probe section uses `$NMT_PY` and not system `python3`, and confirmed that the 8-core driver, adapter, OpenMP source, launcher, exact comparator, worker count, and fresh-root policy remain unchanged.

## Activation consequence

One fresh v0.4 self-hosted science activation is authorized after a fresh noncompetition check. PASS still requires whole canonical `<f8 [39,12288]` SHA256 equality and `numpy.array_equal`; no tolerance rescue is permitted.
