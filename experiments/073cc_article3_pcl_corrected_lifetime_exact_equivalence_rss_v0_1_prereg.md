# Exp073CC — hosted corrected-lifetime PCL exact-equivalence/RSS QA v0.1

Status: prospectively frozen, NONCLASSIFYING synthetic/infrastructure QA only.

Purpose: test whether a corrected one-target-mask-at-a-time lifetime implementation preserves exact PCL bytes while reducing peak RSS relative to the simultaneous-lifetime oracle. This does not close any real-survey gate and is always +0 Verified / +0 Draft-data.

Authority preserved: Exp073BJ terminal Track-A exact Wm_S1 PASS; Exp073AQ permanent historical exact-repeatability scientific FAIL; Exp073BD provisional/no downstream; Exp073BV/BW/BZ PASS. Exp073CA attempt3 remains infrastructure incomplete; home runner remains OFFLINE/LOCKED.

Frozen environment/inputs:
- GitHub-hosted ubuntu-24.04 only.
- Python 3.11; conda-forge `namaster=2.7`, healpy, astropy, numpy.
- one-thread policy: OMP/BLAS/MKL/NUMEXPR/VECLIB/BLIS = 1, OMP_DYNAMIC=FALSE.
- synthetic NSIDE cases exactly {64,128,256}; lmax=3*nside-1.
- lens mask formula exactly `((th>0.31)&(th<2.67)&(ph>0.17)&(ph<5.91)).astype(float64)`.
- source mask formula exactly `(((sin(3*ph)+0.35*cos(2*th))>0.05)&(th>0.42)&(th<2.55)).astype(float64)`.
- simultaneous oracle retains both requested masks/fields until both mask alms are produced.
- corrected sequential implementation must generate only one requested target mask per stage: lens -> field -> lens alm -> release; then source -> field -> source alm -> release; then the same `hp.alm2cl(aa,ab,lmax=lmax)`.
- no tolerance, ULP, rounding, averaging, smoothing, majority vote, or preferred-replica rescue.

Frozen exact comparator:
- output converted to contiguous canonical `<f8`.
- for every NSIDE, simultaneous and corrected sequential outputs must have identical shape `(3*nside,)`, all finite, `np.array_equal == True`, and identical SHA-256 over canonical C-order bytes.
- independent process `/usr/bin/time -v` measurements for simultaneous and sequential cases; RSS is descriptive infrastructure evidence only and is not an acceptance threshold.

Frozen branches:
- `CC_Q1_EXACT_EQUIVALENCE_PASS`: all complete exact comparators pass. RSS is reported descriptively only.
- `CC_Q2_COMPLETE_EXACT_MISMATCH_FAIL`: valid complete comparator inputs exist and any exact array/SHA condition fails.
- `CC_Q3_INFRASTRUCTURE_INCOMPLETE`: setup/execution fails before valid complete comparator inputs exist.

All branches are synthetic/nonclassifying +0/+0. A Q1 may support prospectively preregistering a future memory-only real-survey infrastructure successor only after the user explicitly re-enables the home runner. It does not authorize Wm_S2/WW authority, G7, or G8.
