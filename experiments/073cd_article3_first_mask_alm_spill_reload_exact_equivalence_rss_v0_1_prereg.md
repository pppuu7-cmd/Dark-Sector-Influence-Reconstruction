# Exp073CD — Article-3 first-mask-ALM spill/reload exact-equivalence + RSS QA v0.1

Date: 2026-09-01
Scope: hosted-only synthetic/infrastructure QA; nonclassifying `+0/+0`.

## Motivation

Exp073CC established exact PCL equivalence for a corrected one-target-at-a-time mask lifetime on frozen hosted NSIDE 64/128/256 geometries. Full-scale accounting still leaves a narrow memory margin under the current 6 GiB WSL cap because the first mask ALM remains resident during the second SHT. Exp073CD tests a prospective memory-only design in which the first mask ALM is persisted, released before the second SHT, and reopened read-only only for the unchanged final `healpy.alm2cl` call.

This experiment cannot close any real-survey/scientific gate and cannot authorize home-runner execution while the overnight lock is active.

## Frozen environment and geometry

- GitHub-hosted `ubuntu-24.04` only.
- conda-forge Python 3.11, NaMaster/pymaster 2.7, healpy, astropy, numpy.
- single-thread policy: OMP/BLAS/MKL/NUMEXPR/VECLIB/BLIS = 1; OMP_DYNAMIC=FALSE.
- NSIDE cases: exactly `{64,128,256}`.
- `lmax = 3*nside - 1`.
- Synthetic lens/source mask definitions must be byte-for-byte inherited from the frozen Exp073CC helper.

## Oracle and candidate

Oracle = Exp073CC-style corrected sequential lifetime:
1. construct lens mask/field, release caller lens mask, compute first mask ALM `aa`, release lens field;
2. construct source mask/field, release caller source mask, compute second mask ALM `ab`, release source field;
3. compute unchanged `hp.alm2cl(aa,ab,lmax=lmax)`.

Candidate spill/reload lifetime:
1. construct lens mask/field, release caller lens mask, compute `aa`, release lens field;
2. canonicalize `aa` as contiguous little-endian complex128 `<c16`;
3. record SHA-256 of the in-memory canonical `aa` bytes;
4. save `aa` with NumPy `allow_pickle=False`, then delete in-memory `aa` and collect garbage;
5. construct source mask/field, release caller source mask, compute `ab`, release source field;
6. reopen saved `aa` read-only with `np.load(...,mmap_mode='r',allow_pickle=False)`;
7. verify reloaded shape/dtype and SHA-256 of canonical array bytes exactly match the pre-save SHA before scientific use;
8. compute unchanged `hp.alm2cl(aa_reloaded,ab,lmax=lmax)`.

No scientific input, transform, reduction order inside `alm2cl`, mask definition, or threshold may be altered.

## Frozen exact acceptance

For every NSIDE case all inputs/results must be complete and finite.

Required simultaneously:
- saved/reloaded first-ALM shape equality;
- saved/reloaded first-ALM canonical `<c16` SHA-256 equality;
- final oracle/candidate PCL `np.array_equal == True`;
- final oracle/candidate canonical contiguous `<f8` SHA-256 equality.

No tolerance, ULP, rounding, averaging, smoothing, majority vote, or preferred-replica rescue is permitted.

Frozen classifications:
- `CD_Q1_SPILL_RELOAD_EXACT_EQUIVALENCE_PASS`: all cases complete and all exact conditions pass;
- `CD_Q2_COMPLETE_EXACT_MISMATCH_FAIL`: complete valid numerical inputs exist but any required exact condition fails;
- `CD_Q3_INFRASTRUCTURE_INCOMPLETE`: provisioning/execution fails before complete valid comparator inputs exist.

## RSS semantics

Oracle and candidate must run as independent processes under `/usr/bin/time -v`. Peak RSS is diagnostic only and cannot alter Q1/Q2 classification. Record maximum RSS for each mode/case and the ratio candidate/oracle. Do not extrapolate hosted small/medium RSS to a claim that NSIDE=4096 fits in 6 GiB.

## Authority and readiness

Always `science_gate_scored=false`, `verified_delta=0.0`, `draft_data_delta=0.0`. Preserve Exp073BJ PASS, Exp073AQ permanent historical FAIL, Exp073BD no-downstream, Exp073BV/BW/BZ PASS, Exp073CC Q1, and Article-3 Verified 52.0% / Draft-data 53.7%.
