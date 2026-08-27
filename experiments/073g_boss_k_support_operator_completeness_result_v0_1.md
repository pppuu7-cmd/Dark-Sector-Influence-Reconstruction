# Exp073G — BOSS k-support operator completeness result v0.1

**Date:** 2026-08-27  
**Classification:** `FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE`

## Immutable execution provenance

- implementation merge: `3a57bf6c8ef32b17ba32093a3afe041c7cf41844`;
- workflow run: `33036220112`;
- workflow job: `98399367147`;
- artifact: `9632090063`;
- artifact digest: `sha256:b0d65987c6007489cfbdbb1719963d2b4c65f089b1f5827cf5a5a3d2bf92ed53`;
- extracted result JSON SHA256: `06809d44c2436a1cd682bbb49107f5163a55ad69737057c0a544861a60626768`.

The workflow completed successfully. Exact KiDS source identity and the frozen BOSS high-z dataset, radial-band and window SHA256 values all reproduced.

## Result

The public high-z BOSS coordinate bound in Exp073G is a configuration-space `xi_wed` observable. Its linear power-spectrum response contains Fourier–Bessel kernels proportional to `k^2 j_l(k s)`.

The signed Fourier–Bessel integral may converge through oscillatory cancellation, but Exp073G deliberately requires a **non-negative** support envelope so cancellation cannot hide invalid support. At large k, `j_l(k s)=O(1/k)`, hence the absolute P-independent kernel is generically `O(k)` and does not provide a finite all-k normalization. A finite released radial/window matrix does not by itself supply a unique high-k damping or cutoff.

Making the support fraction finite would therefore require an additional ingredient that was not prospectively frozen: a fiducial `P(k)` weight, nonlinear damping, a high-k cutoff, or another theory response. Adding such an ingredient now would violate the frozen solver-neutral geometric-support question.

## Interpretation boundary

This result is **not** `FAIL_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073G`.

No `f_invalid` and no retained dimension were computed. The KiDS+BOSS+BNT candidate has therefore not been scientifically rejected by the 5% support criterion. Instead, the exact public configuration-space BOSS operator is insufficient to define the particular positive solver-neutral k-support measure required by the frozen Exp073G contract.

The 5% threshold, C3+C5 support rectangle, BNT selection and prior scientific classifications are unchanged.

No covariance values, nuisance rank/SVD, relation residuals or G8 information were read.

## Consequence

Exp073G cannot authorize covariance restriction/whitening. The next admissible branch must be prospectively frozen before new support output and must replace only the mm-sensitive observational operator with one whose public k-space support is finite and immutable. A public Fourier-space BOSS/eBOSS power-spectrum statistic with released k bins/windows is the preferred next candidate; the signed Wm and WW KiDS+BNT side remains only a candidate until a complete common support audit passes.

G7 OPEN. G8 OPEN. G9 OPEN.
