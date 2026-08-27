# Exp073I — finite true-k clustering-window matrix source binding — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073I MATRIX-SUPPORT CLASSIFICATION IS EVALUATED

## 1. Parent binding

Bind Exp073H exactly as

`FAIL_FOURIER_MM_OPERATOR_SOURCE_BINDING_EXP073H`.

Exp073H passed H1, H2 and H4-H8 but failed frozen H3 because the official 2016/2017 Beutler DR12 release supplies separation-space `W_l^2(s)` multipoles rather than a finite non-negative true-k mixing matrix. No 5%-support fraction was evaluated.

Exp073I may change only the public mm-sensitive clustering release/operator. It may not weaken the inherited physical rectangle or any downstream gate.

## 2. Frozen purpose

Determine whether the public matrix products accompanying Beutler & McDonald (2021), arXiv:2106.06324 / JCAP 11 (2021) 031, can be immutably bound as an explicit finite true-k to observed-k BOSS DR12 operator suitable for a later common KiDS-BNT + clustering physical-support audit.

Exp073I is still a source/operator feasibility experiment. It does not evaluate the final 5% common support fraction and cannot authorize covariance restriction.

## 3. Frozen source order

Audit without using covariance values, likelihood quality, relation residuals or G8 information:

1. the publication-linked public BOSS DR12 matrix products at the Beutler & McDonald 2021 data page;
2. the companion `fbeutler/pk_tools` repository only to establish matrix/file semantics and reading conventions;
3. if the publication data page is unavailable, a stable mirror or release explicitly identified by the publication/authors, with exact hashes and no change of matrix definition.

Do not substitute a different survey/sample based on downstream performance during Exp073I.

## 4. Frozen physical-support inheritance

Any later support audit using an Exp073I PASS must retain exactly:

- `z_min = 0.295`;
- `z_max = 2.33`;
- `k_min = 0.000704833374744468 Mpc^-1`;
- `k_max = 0.06664762008318016 Mpc^-1`;
- maximum positive invalid-support fraction `0.05`.

No unit reinterpretation may change these physical Mpc^-1 limits.

## 5. Required properties I1-I8

### I1 — immutable public identity
Every measurement and matrix object needed for the BOSS DR12 true-k mapping must have a stable public identity and recorded SHA256. The exact `pk_tools` commit used for semantics must also be pinned.

### I2 — explicit finite matrix map
The release must provide a finite numerical matrix mapping a finite theory-k grid into a finite observed/convolved power-spectrum grid, not merely a configuration-space window or procedural recipe.

### I3 — finite true-k grid
The matrix input grid must have explicit finite `k_th` coordinates/bins and documented units. The matrix shape and the number/order of multipoles must be reproducible from the release/tooling.

### I4 — positive support-envelope constructibility
For each observed coordinate retained for later testing, the finite matrix must permit a finite non-negative support envelope constructed prospectively from absolute matrix contributions (or an equivalent positive domination) without multiplying by a fiducial cosmological `P(k)`, nonlinear damping, covariance weights or a post-hoc k cutoff.

I4 does not require the physical 5% threshold to be evaluated in Exp073I; it only asks whether the finite operator makes that later calculation mathematically well-defined.

### I5 — physical-unit traceability
The release k convention must be explicit (`h/Mpc` or `Mpc^-1`) and exactly convertible to physical `Mpc^-1` using the frozen geometry. Unit roundtrip tolerance remains `2e-8`.

### I6 — compatible BOSS sample/mm semantics
At least one bound BOSS DR12 product must correspond to a high-z/CMASS-compatible clustering sample (prefer `0.5<z<0.75` if available) and represent galaxy-density power-spectrum multipoles suitable as the mm-sensitive observable block. This does not certify galaxy-bias nuisance modeling.

### I7 — no covariance dependence
Covariance file identities may be recorded if inseparable from the public product manifest, but covariance numerical contents may not be read or used to choose matrices/bins.

### I8 — no downstream leakage
No common-support fraction, nuisance SVD/rank, quotient/relation/null residual, G8 response, held-out result or article-selection result may be read or used.

## 6. Frozen classifications

If I1-I8 all pass, classify

`PASS_FINITE_TRUE_K_WINDOW_MATRIX_SOURCE_BINDING_EXP073I`.

This PASS authorizes only a separately preregistered common physical-support audit using the unchanged C3+C5 rectangle and 5% threshold.

If trustworthy public evidence shows the publication products are reproducible but one or more of I2-I6 fails, classify

`FAIL_FINITE_TRUE_K_WINDOW_MATRIX_SOURCE_BINDING_EXP073I`.

If retrieval/infrastructure or provenance prevents a trustworthy decision, classify

`INCOMPLETE_EXP073I`.

## 7. Downstream boundary

No Exp073I outcome changes Exp073G or Exp073H. Even an Exp073I PASS does not authorize covariance restriction; a new common physical-support gate must be preregistered and executed first.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
