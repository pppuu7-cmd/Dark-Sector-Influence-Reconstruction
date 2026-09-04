# Exp073BU hardware-matched 8-core execution v0.3 — exact-equivalence PASS

Date: 2026-09-04
Scope: DSIR only.

## Status

`PASS_EXP073BU_8CORE_EXACT_EQUIVALENCE_V0_3`

Support/implementation result only (`+0/+0`). No DES-scale Exp073BU science numerics were executed by this audit and no Wm_S3 science authority was created.

## Hardware boundary

The immediately preceding 10-core activation reached `DSIR-HOME-PC` and reported `home_affinity_cpus=8`, then stopped at the hardware gate before science. Ten real CPUs are therefore not available to the current WSL runner. The v0.3 execution contract uses the eight CPUs actually exposed by Linux and forbids oversubscribed ten-thread execution as a substitute for ten real cores.

## Frozen implementation authority

- original science prereg blob: `816542c7eb7a8ba4e72d6e01228aa62d05c7c805`
- hardware-matched 8-core prereg blob: `1da32a7647601c2c876c2392bf9e17dfd5a8593e`
- admitted serial downstream v0.1 blob: `acafb095deafae7602101d8305e239341010ba79`
- worker-count-parametric OpenMP source blob: `be4f381de4c5c043a9c0fcd107e63ef3f2079578`
- 8-core exact adapter blob: `63ee393791bba43d3eabbea654efdb9d439d477e`
- 8-core production driver blob: `2b44ddd2c1167739f643a0f1c23cfbf7905fa464`
- 8-core science launcher blob: `8a725ba135e3e120ce6e8d0db3dd14d95d4ffd6e`
- science_workflow_blob=c65464d661ac0361cac6f55153bbd7c4bfb05f76

## Hosted audit authority

- workflow: `Exp073BU 8-core exact-equivalence audit v0.3`
- run/job: `33900913648 / 101114517184`
- activation head: `7147d68819d185bd9eab9fd76784f810860f3de6`
- artifact ID: `9947594382`
- artifact digest: `sha256:5b5b42dd6a60dbd7f33de5719630424beff6a18e622295445b04d66e59328418`

All audit steps completed successfully.

Three deterministic nontrivial canonical matrices were processed by both the admitted serial v0.1 downstream and the worker-count-parametric OpenMP source compiled with `-DDSIR_WORKERS=8`. For every case, output files were byte-identical (`cmp`) and SHA256-identical. The OpenMP executable emitted `DSIR_OMP_TEAM=8` for every case, proving that an actual eight-thread team was created.

The science workflow audit also verified `OMP_NUM_THREADS=8`, nested BLAS/MKL pins at one, self-hosted affinity gate >=8, run-specific fresh checkpoint root, compile flag `-fopenmp -DDSIR_WORKERS=8`, runtime team proof, and the unchanged whole-array SHA256 plus `numpy.array_equal` A/B comparator.

## Activation consequence

The hardware-matched 8-core science workflow is authorized for one fresh self-hosted activation after a fresh repository noncompetition preflight and live self-hosted exclusivity check. Partial state from both the cancelled low-CPU attempt and blocked 10-core attempt is excluded by the run-specific fresh checkpoint root.
