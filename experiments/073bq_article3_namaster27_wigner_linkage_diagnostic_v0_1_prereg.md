# Exp073BQ — NaMaster 2.7 native Wigner linkage diagnostic v0.1

**Scope:** DSIR Article-3 only. **Classification:** NONCLASSIFYING infrastructure/source-linkage diagnostic. **Readiness:** `+0 Verified / +0 Draft-data` under every outcome.

## Purpose

Resolve the concrete post-BJ BO/BP infrastructure hypothesis without changing any scientific acceptance criterion: determine, with direct hosted NaMaster-2.7 evidence, whether the exact Wigner routine requested by the experimental native projected kernel (`drc3jj`) is dynamically exported by `pymaster._nmtlib`, exported by a directly linked runtime dependency, or absent from the runtime dynamic symbol closure and therefore requires a different source/link target.

This diagnostic MUST NOT rerun Exp073BJ, Exp073BO or Exp073BP and MUST NOT classify any scientific window/operator result.

## Frozen environment

- GitHub hosted `ubuntu-24.04`.
- Conda-forge environment: Python 3.11, `namaster=2.7`, `numpy`.
- Inspect the exact installed `pymaster._nmtlib` extension.

## Frozen observations to record

1. `pymaster` version and `_nmtlib.__file__`.
2. `ctypes.CDLL(_nmtlib).__getattr__('drc3jj')` success/failure.
3. `ldd` dependency closure for `_nmtlib`.
4. Dynamic-symbol evidence from `nm -D` and `readelf -Ws` for `_nmtlib` and each existing absolute dependency path; record every line containing `drc3jj`, case-sensitive and case-insensitive Wigner-related tokens (`drc3j`, `wig`, `wigner`).
5. For each dependency loadable by `ctypes.CDLL`, direct `drc3jj` lookup success/failure.
6. Search installed conda environment text/source/header/pkg-config files for literal `drc3jj`; record paths and matching lines, bounded to avoid binary dumps.
7. Preserve command return codes and stderr summaries sufficient to distinguish absent tools from absent symbols.

## Frozen outcome classes

- `BQ_Q1_EXTENSION_EXPORTS_DRC3JJ`: direct nonzero `drc3jj` address from `_nmtlib`.
- `BQ_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ`: extension does not export it, but at least one direct `ldd` dependency does, with a nonzero address and symbol-table evidence.
- `BQ_Q3_RUNTIME_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND`: no direct runtime export in extension/dependencies, but literal installed source/header/build metadata identifies one or more source/link locations containing `drc3jj`.
- `BQ_Q4_RUNTIME_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT`: no runtime export and no installed textual source/header/build reference found. This means the BO `ctypes` strategy is unsupported by the inspected packaged runtime; it does **not** prove the routine is absent from upstream source.
- `BQ_Q5_INFRASTRUCTURE_INCOMPLETE`: installation/inspection fails before the observations needed for Q1–Q4 are available.

The classification is exact with respect to the observed package/runtime state; no tolerance or scientific threshold exists.

## Authority firewall

Exp073AQ remains permanent historical scientific exact-repeatability FAIL. Exp073BJ remains terminal Track-A exact authority PASS. BQ cannot modify either state, cannot authorize Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7 or G8, and cannot raise scientific or draft/data readiness.

G7 order remains: validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family.
