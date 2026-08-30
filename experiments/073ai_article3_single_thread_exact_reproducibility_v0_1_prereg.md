# Exp073AI — Article 3 single-thread exact Wm_S0 reproducibility route v0.1

**Frozen:** 2026-08-30 after Exp073X2 Q was classified `SCIENTIFIC_REPEATABILITY_FAIL`, after Exp073AH2 localized the mismatch to tiny workspace-output-only numerical divergence, and before any Exp073AI hosted output exists.

## Purpose

Exp073AI opens a **new prospective reproducibility route**. It does not reclassify, erase, weaken, or rescue the historical Q failure. Its sole question is whether the exact frozen Wm_S0 angular operator becomes bitwise reproducible across two fresh independent GitHub-hosted runners when the relevant numerical thread controls are prospectively fixed to one thread and the runtime/hardware environment is captured more completely.

This is a reproducibility/infrastructure authority gate, not a dark-sector model test. A PASS adds **0 scientific-readiness points**. A FAIL is retained as new negative reproducibility evidence and also adds 0 readiness.

## Historical evidence that remains immutable

- Exp073X2R P canonical within-chain exact PASS SHA: `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`.
- Exp073X2 Q: `SCIENTIFIC_REPEATABILITY_FAIL` under its frozen exact criterion.
- Exp073AH2: `WORKSPACE_OUTPUT_ONLY_NUMERICAL_DIVERGENCE`, no detected frozen input/contract drift, max absolute A/B difference `2.0816681711721685e-17`.

Exp073AI may compare its result with historical hashes descriptively, but historical agreement is **not** required for Exp073AI PASS. Exp073AI PASS requires only exact equality between its own two prospectively controlled replicas.

## Frozen scientific/angular contract

Unchanged from Exp073X2:

- real DES Y1 source-mask authority Exp073R1;
- public DES Y1 redMaGiC lens mask, original positive weights retained iff `mask>0.5`;
- `NSIDE=4096`, RING, C coordinates;
- NaMaster/PyMaster 2.7 lineage;
- 39 frozen bandpowers;
- true ell axis `0..12287`;
- spin-0 x spin-2;
- selected physical response `TE <- TE`;
- canonical selected window `<f8 [39,12288]`;
- no effective ell/z/k, radial kernel, fiducial-P, support, covariance, nuisance geometry, quotient/relation/null, or G8.

The exact replica implementation is reused unchanged from commit `df2eecd73ed0d8de080348ba155a2f1a3e84d7e1`:

`ci/exp073x2_des_n4096_wm0_maskonly_angular_replica_v0_1.py`.

The exact comparator is reused unchanged from commit `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`:

`ci/exp073x2_compare_replicas_v0_1.py`.

## New prospective execution controls

For both replicas A and B, before Python starts, freeze:

- `OMP_NUM_THREADS=1`
- `OPENBLAS_NUM_THREADS=1`
- `MKL_NUM_THREADS=1`
- `NUMEXPR_NUM_THREADS=1`
- `VECLIB_MAXIMUM_THREADS=1`
- `BLIS_NUM_THREADS=1`
- `OMP_DYNAMIC=FALSE`

No tolerance, rounding, ULP allowance or majority voting is allowed.

## Runtime/environment capture

Each replica must persist a text/JSON environment receipt before exact workspace construction containing at least:

- GitHub run/job/replica identity;
- runner OS/image labels available to the job;
- `uname -a`;
- `lscpu` output;
- `/proc/cpuinfo` model-name and flags summary;
- `nproc`;
- `ulimit -a`;
- memory and filesystem inventory;
- exact values of all frozen thread environment variables;
- Python version;
- PyMaster, NumPy, Healpy and Astropy versions;
- `numpy.show_config()` output.

Hardware/runtime receipts are diagnostic and need not be identical across A and B. They may not be used post hoc to select one replica or alter the exact PASS criterion.

## Frozen PASS / FAIL criterion

After both independently persisted artifacts exist, the unchanged Exp073X2 comparator must be run on them.

`PASS_EXP073AI_SINGLE_THREAD_EXACT_REPRODUCIBILITY_V0_1` iff all are true:

1. both replicas independently completed the exact frozen Wm_S0 computation;
2. unchanged frozen metadata compared by the inherited comparator are identical;
3. canonical `<f8 [39,12288]` SHA256 values are identical;
4. `numpy.array_equal(A,B) == True`.

Otherwise, if both replicas completed and comparison reaches a numerical mismatch, classify:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AI_SINGLE_THREAD_EXACT_V0_1`.

If execution ends before a valid comparison, preserve the appropriate infrastructure-INCOMPLETE class and do not infer repeatability.

## Relation to production

Exp073AI is exploratory governance/reproducibility work after the old route was blocked. **It does not by itself authorize Exp073AA production**, even if it PASSes. Any future production succession from Exp073AI requires a separate prospectively frozen authority-selection amendment after Exp073AI outcome exists; this prevents retroactive substitution for the failed Q route.

## Scientific-readiness and anti-leakage firewall

Throughout Exp073AI:

- strict Article-3 scientific repository readiness remains `52%`;
- readiness increment is `0`;
- G7/G8/G9 remain OPEN;
- Layer A/B remain OPEN;
- no scientific model PASS may be claimed;
- no support/covariance/nuisance/G8 quantity may be read or computed.
