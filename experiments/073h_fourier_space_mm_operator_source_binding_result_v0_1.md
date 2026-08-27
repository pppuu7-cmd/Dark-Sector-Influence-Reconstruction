# Exp073H — public Fourier-space mm-operator source/binding audit — result v0.1

**Date:** 2026-08-27  
**Classification:** `FAIL_FOURIER_MM_OPERATOR_SOURCE_BINDING_EXP073H`

## Immutable execution

- parent `main` before implementation: `3d9d7e5382cd74bd588854296c5da49864fc0b88`;
- execution head: `d66c0c064ca597fc7f72e0151b3ab8e4fe6190b7`;
- workflow run: `33039103109`;
- workflow job: `98408423778`;
- artifact: `9633155256`;
- artifact digest: `sha256:1f3543c1459d5349791cbba6ddeb4c2908960527411cf12cf95ba450b3f59ce5`;
- official Beutler archive SHA256: `23bb7813a7b6ae0e041f070f40716511ff21243e11f6c2783fec64d72de5b823`.

The workflow completed successfully. This is therefore a scientific/source-operator classification under the frozen Exp073H contract, not an infrastructure failure.

## Frozen H1-H8 outcome

- H1 immutable public identity: PASS;
- H2 explicit Fourier coordinate: PASS;
- H3 finite positive support normalization: **FAIL**;
- H4 physical-unit traceability: PASS;
- H5 high-z compatibility: PASS;
- H6 mm semantics: PASS;
- H7 no covariance dependence: PASS;
- H8 no downstream leakage: PASS.

The six public `Beutleretal_window_z{1,2,3}_{NGC,SGC}.dat` objects each contain 5000 rows and seven numeric columns. Their first coordinate runs monotonically from about `0.100115` to `9988.5`, consistent with the released separation-space window multipoles `W_l^2(s)` in `Mpc/h` described in Beutler et al., arXiv:1607.03150, Appendix A / Eq. 22.

The high-redshift `z3` public measurements are genuine finite Fourier tables for `P0`, `P2`, and `P4` at `0.5<z<0.75`, with k in `h/Mpc`. Thus the failure is not lack of a Fourier measurement, redshift mismatch, or unit ambiguity.

## Why H3 fails

The frozen H3 criterion requires the released k-bin/window operator itself to admit a finite non-negative support envelope without multiplying by a fiducial `P(k)`, nonlinear damping, or introducing a post-hoc high-k cutoff.

The 2016/2017 Beutler release supplies the survey window as configuration/separation-space multipoles. Its theory convolution is performed through correlation-space multipoles and Hankel transforms. It does not publish a finite non-negative true-k mixing matrix for the observed multipoles. Therefore a solver-neutral positive all-k support measure cannot be constructed from the release alone under the frozen rule.

This preserves the same methodological boundary exposed by Exp073G in a different operator representation: finite observed k centers do not by themselves prove finite true-k support once survey-window mixing is included.

## Downstream boundary

No KiDS+BNT common support fraction was computed. No covariance numerical values, nuisance rank/SVD, relation/null residuals or G8 information were read.

Exp073H therefore does **not** authorize covariance restriction. The next admissible branch is a prospectively frozen source-binding audit of a public clustering release that explicitly publishes finite true-k window/mixing matrices. Beutler & McDonald (2021), arXiv:2106.06324, is the leading candidate because it explicitly publishes BOSS DR12 window matrices mapping finite theory-k bins to finite observed-k bins.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
