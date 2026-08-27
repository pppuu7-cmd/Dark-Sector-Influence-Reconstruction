# Exp073H — public Fourier-space mm-operator source/binding audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073H SUPPORT FRACTION IS EVALUATED

## 1. Parent binding

Bind the Exp073G operator-completeness outcome exactly as

`FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE`.

That outcome is not a 5%-support scientific rejection of KiDS+BOSS+BNT. It establishes only that the frozen BOSS **configuration-space** `xi_wed` mm operator cannot define the required finite solver-neutral positive all-k support measure without an extra theory weight or high-k cutoff.

Exp073H may replace only the mm-sensitive observational operator. It may not weaken the C3+C5 physical rectangle, the 5% support rule, the signed Wm/WW semantics, or any downstream gate.

## 2. Frozen purpose

Determine whether a public BOSS/eBOSS **Fourier-space** galaxy-clustering release can be immutably bound with explicit finite k coordinates/windows suitable for a later common KiDS-BNT + clustering physical-support audit.

Exp073H is a source/operator feasibility and provenance experiment only. It does not compute the final KiDS+BNT support fractions and cannot authorize covariance restriction.

## 3. Frozen preferred source order

Audit candidates in this order, without choosing based on covariance, fit quality, G7 relations or G8 performance:

1. official SDSS/BOSS DR12 public results material for the final-sample Fourier-space clustering wedges of Grieb et al.;
2. an exact public release linked from the official SDSS results page that contains the corresponding Fourier-space wedge/multipole measurements and survey/window operators;
3. if the exact Grieb release is no longer immutably retrievable, a public BOSS DR12 power-spectrum multipole release with explicit k bins and immutable survey-window/operator files, clearly labeled as a replacement candidate rather than the original Exp073F construction.

Documentation pages may identify candidates but cannot substitute for immutable data/operator objects.

## 4. Frozen physical-support inheritance

Any later support audit using a successful Exp073H binding must retain exactly:

- `z_min = 0.295`;
- `z_max = 2.33`;
- `k_min = 0.000704833374744468 Mpc^-1`;
- `k_max = 0.06664762008318016 Mpc^-1`;
- maximum positive invalid-support fraction `0.05`.

No unit reinterpretation may change these physical Mpc^-1 limits.

## 5. Required source/operator properties H1-H8

### H1 — immutable public identity
The measurement and every operator/window object required for k-support must have a stable URL/archive/repository identity and recorded SHA256.

### H2 — explicit Fourier coordinate
The released observable must be defined directly in finite k bins or through a finite public k-space window/operator. A configuration-space-only measurement does not pass.

### H3 — finite positive support normalization
The released k-bin/window operator must admit a finite non-negative support envelope without multiplying by a fiducial cosmological `P(k)`, nonlinear damping, or a post-hoc integration cutoff.

### H4 — physical-unit traceability
The release k convention (`h/Mpc` or `Mpc^-1`) must be explicit and exactly convertible to physical `Mpc^-1` using the already-frozen geometry when needed. Unit roundtrip tolerance remains `2e-8`.

### H5 — high-z compatibility
The selected clustering sample must have released redshift support compatible with the existing geometrical choice that excludes the low-z `0.2<z<0.5` BOSS bin. Prefer the public high-z/CMASS-like sample overlapping `0.5<z<0.75` unless the exact release defines a different immutable redshift selection.

### H6 — mm semantics
The observable must be demonstrably matter/galaxy-density clustering sensitive. Exp073H does not certify nuisance marginalization or a dark-sector nonlinear galaxy-bias model; it only binds the observational mm-sensitive operator.

### H7 — no covariance dependence
Covariance values may not be read or used to choose candidate bins/windows. Covariance file identity may be recorded only if inseparable from an archive manifest, but its numerical contents remain unread.

### H8 — no downstream leakage
No nuisance SVD/rank, relation/null residual, G8 response, held-out performance or article-selection result may be read or used.

## 6. Frozen classifications

If H1-H8 all pass for at least one public Fourier-space clustering operator, classify

`PASS_FOURIER_MM_OPERATOR_SOURCE_BINDING_EXP073H`.

This PASS only authorizes a separately preregistered common physical-support audit combining that mm operator with the already-bound KiDS+BNT Wm/WW operator. It is not a support PASS.

If trustworthy public evidence shows that the preferred sources exist but the required measurement/window objects cannot be immutably bound or do not define a finite positive k support measure, classify

`FAIL_FOURIER_MM_OPERATOR_SOURCE_BINDING_EXP073H`.

If retrieval/infrastructure prevents a trustworthy decision, classify

`INCOMPLETE_EXP073H`.

## 7. Downstream boundary

Even an Exp073H PASS does **not** authorize covariance restriction. The next step must first prospectively freeze and execute a new common physical-support gate with the unchanged C3+C5 rectangle and 5% threshold.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
