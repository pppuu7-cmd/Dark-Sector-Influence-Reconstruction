# Exp073BU 10-core execution v0.2 — exact-equivalence PASS

Date: 2026-09-04
Scope: DSIR only.

## Status

`PASS_EXP073BU_10CORE_EXACT_EQUIVALENCE_V0_2`

This is a support/implementation result only (`+0/+0`): no DES-scale science numerics were executed and no Wm_S3 science authority was created.

## Prospective authority

- 10-core preregistration: `experiments/073bu_wm_s3_fresh_ab_exact_repeatability_10core_v0_2_prereg.md`
- prereg blob: `56bdbca1217b4213603734a96665dae33e3fc4c5`
- serial downstream v0.1 blob: `acafb095deafae7602101d8305e239341010ba79`
- OpenMP-10 downstream v0.2 blob: `be4f381de4c5c043a9c0fcd107e63ef3f2079578`
- 10-core adapter blob: `c5cd7ae0113ec280e363e46850af33d841ff16f8`
- 10-core production-driver wrapper blob: `08fba42876c1e3a42847a677473dfc8fb20ff592`
- 10-core science-launcher blob: `77eb05659f2baebe1f72f93fb620dcc95d0249b6`

## Authoritative hosted audit

- workflow: `Exp073BU 10-core exact-equivalence audit v0.2b`
- run: `33900434766`
- job: `101112969938`
- head: `3f7b49e64b03ce6153d0fbafee38d1d77fd71b2d`
- artifact: `9947413649`
- artifact digest: `sha256:f291660477a5abff179793d48baf594e1c0ba3536173b39a001efa8fab777dfa`

All audit steps completed successfully.

The audit compiled the admitted serial v0.1 full-window downstream and the prospective OpenMP-10 v0.2 downstream, executed three deterministic nontrivial synthetic canonical matrices, and required both byte equality (`cmp`) and SHA256 equality for every output. All three cases passed exactly.

The OpenMP implementation also emitted `DSIR_OMP_TEAM=10` in every case, proving that a real ten-thread OpenMP team was created. Parallelization is restricted to independent output cells/rows; each scalar accumulation retains the serial ordering.

The science workflow contract was also audited to require `OMP_NUM_THREADS=10`, nested BLAS thread pins of one, at least ten CPUs in the self-hosted affinity set, a fresh run-specific checkpoint root, compilation with `-fopenmp -DDSIR_WORKERS=10`, and the unchanged whole-array SHA256 + `numpy.array_equal` A/B science comparator.

## Historical audit boundary

The preceding hosted audit run `33900320962` failed before arithmetic comparison solely because the hosted image lacked NumPy (`ModuleNotFoundError: No module named 'numpy'`). It is immutable infrastructure history and is not a serial-vs-OpenMP equivalence failure. v0.2b added only `python3-numpy`; science implementation blobs were unchanged.

## Activation consequence

The prospective 10-core science workflow may now be activated, subject to a fresh no-competing-Actions check and the live self-hosted exclusivity gate. The cancelled one-core Exp073BU attempt remains non-authoritative infrastructure history and its partial checkpoints must not be imported.
