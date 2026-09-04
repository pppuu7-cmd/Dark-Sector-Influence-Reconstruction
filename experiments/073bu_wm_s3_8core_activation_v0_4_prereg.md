# Exp073BU Wm_S3 8-core activation infrastructure repair v0.4

Frozen prospectively on 2026-09-04 after run `33901049626 / 101114995516` stopped before DES numerics.

## Historical v0.3 failure

The v0.3 hardware-matched run passed source binding, live `home_affinity_cpus=8`, PyMaster 2.7 setup with `OMP_NUM_THREADS=8`, R1 staging, DES lens-mask staging/hash verification, and OpenMP-8 compilation. It then failed in the tiny runtime probe because that probe invoked system `python3`, whose environment did not contain NumPy. The log records `ModuleNotFoundError: No module named 'numpy'` before the OpenMP executable was invoked. The science step was skipped and no Wm_S3 numerical authority was created.

This is infrastructure-only history, not a science failure and not an OpenMP-team failure.

## Sole admitted repair

v0.4 changes only the runtime-probe interpreter from system `python3` to the already frozen exact NaMaster environment `$NMT_PY`, which had just been verified as PyMaster 2.7 with `OMP_NUM_THREADS=8` in the same job.

The following remain byte-identical to the v0.3 science execution branch:
- original science preregistration and all science boundaries;
- 8-core execution preregistration;
- base production driver;
- 8-core production wrapper;
- 8-core exact adapter;
- worker-count-parametric OpenMP C source compiled with `-DDSIR_WORKERS=8`;
- 8-core science launcher;
- DES/R1 inputs, masks, band edges, TE<-TE semantics;
- A then B ordering and fresh-run checkpoint isolation;
- exact SHA256 plus `numpy.array_equal` comparator and terminal classes.

The immutable hosted exact-equivalence authority `PASS_EXP073BU_8CORE_EXACT_EQUIVALENCE_V0_3` remains applicable because no numerical implementation blob changes. A v0.4 hosted activation audit must verify this unchanged lineage and the corrected probe interpreter before science activation.
