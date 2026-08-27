# Exp073G — KiDS-1000 + BOSS + BNT exact physical-support audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY TRANSFORMED-KERNEL SUPPORT RESULT IS EVALUATED

## 1. Parent binding

Bind Exp073F exactly as `PERTURBATIVE_OBSERVATIONAL_ROUTE_CANDIDATE_FOUND_EXP073F` with primary candidate `KiDS-1000 + BOSS 3x2pt with prospective BNT physical-scale localization` and landscape label `PROMISING_FOR_EXACT_SUPPORT_AUDIT`.

Exp073F is not a physical-support PASS. Exp073G is the first experiment allowed to decide whether this candidate actually fits inside the already-certified perturbative C3+C5 domain.

## 2. Frozen physical support

No threshold may be changed after the first transformed-kernel support output.

- `z_min = 0.295`;
- `z_max = 2.33`;
- `k_min = 0.000704833374744468 Mpc^-1`;
- `k_max = 0.06664762008318016 Mpc^-1`;
- maximum positive-weight invalid-support fraction per retained observation coordinate/block: `0.05`.

The support rectangle is inherited from Exp071A. The 5% rule is inherited unchanged from the ACT x unWISE support work.

## 3. Frozen public source targets

The implementation must bind exact downloaded release objects and record SHA256 digests before support evaluation. Initial source targets are:

- KiDS-1000 3x2pt public release page: `https://kids.strw.leidenuniv.nl/DR4/KiDS-1000_3x2pt_Cosmology.php`;
- KiDS-1000 cosmic-shear public release page: `https://kids.strw.leidenuniv.nl/DR4/KiDS-1000_cosmicshear.php`;
- the public/open-source KiDS-1000 analysis/data repository linked by those releases;
- BOSS DR12 clustering inputs used by the released KiDS 3x2pt construction.

If the release page points to a versioned repository/tag/archive, that exact identity must be frozen in the first implementation commit before any support classification.

A source that cannot be bound immutably is an infrastructure/provenance failure, not a scientific support FAIL.

## 4. Frozen physical block semantics

The exact candidate operator must preserve separate channels for

- `P_mm(k,z)` from galaxy-density clustering;
- signed `P_Wm(k,z)` from galaxy-galaxy lensing;
- `P_WW(k,z)` from cosmic shear.

The audit may reconstruct the projection kernels independently from the standard KiDS cosmology backend. It must not import a GR matter-to-Weyl closure merely because the public likelihood uses one for standard parameter inference.

Absolute-value replacement of `P_Wm` is forbidden.

## 5. Frozen BNT construction rule

BNT is an observational linear transformation, not a nonlinear theory correction.

Before support classification the implementation must freeze:

1. the exact source tomographic n(z) inputs;
2. the exact continuous-bin BNT matrix convention;
3. normalization/sign convention for transformed kernels;
4. treatment of the first/second transformed bins whose localization properties differ from higher BNT bins;
5. whether any transformed bins are excluded for purely predeclared geometric reasons;
6. the exact angular/bandpower coordinates supplied by the public release.

No BNT combination may be selected using covariance, measured residuals, nuisance rank or later G8 behavior.

## 6. Frozen prospective density/lens selections

BOSS density/lens coordinates may be excluded only for predeclared support reasons:

- released lens/redshift support materially below `z=0.295`;
- released support materially above `z=2.33`;
- scale geometry that cannot possibly satisfy `k<=0.06664762008318016 Mpc^-1` under the exact window.

Any selection must be committed before calculating the candidate's final retained dimension.

## 7. Exact support operator

For each candidate observation coordinate `i` and physical block `b in {mm,Wm,WW}`, construct a non-negative support-envelope weight `W_ib(z,k)` adequate to answer only the geometric question of where the released observable receives physical support.

Signed physics response and positive support weight are distinct objects: `P_Wm` remains signed in the future forward model, while support leakage uses a non-negative envelope so cancellation cannot hide invalid-domain weight.

Define

`f_invalid(i,b) = integral_outside_rectangle W_ib / integral_all W_ib`.

A coordinate is support-valid only if every physical block required by that coordinate has

`f_invalid(i,b) <= 0.05`.

Broad bandpower/window support must be integrated; evaluating only at an effective ell, effective z or effective k is forbidden.

## 8. Frozen hard controls G1-G10

### G1 — immutable source provenance
Every public data/operator object used in the audit has URL/repository identity and SHA256.

### G2 — parent/support reproduction
Exp073F parent classification and Exp071A rectangle are reproduced exactly.

### G3 — BNT algebra
The frozen BNT matrix satisfies its defining nulling constraints to numerical tolerance `1e-10` on the bound n(z) discretization, and repeated construction is deterministic to `1e-12` relative tolerance.

### G4 — kernel normalization
Original and transformed kernel numerical quadratures are finite; positive support envelopes have strictly positive finite normalization for every tested retained coordinate.

### G5 — block separation
The implementation exposes `mm`, signed `Wm`, and `WW` paths separately and does not infer either Weyl block from `mm`.

### G6 — exact window integration
Released angular/bandpower windows are used when available; no effective-coordinate shortcut is accepted where a window exists.

### G7 — physical-unit roundtrip
All `k` values used for support classification are explicitly physical `Mpc^-1`; any h/Mpc conversion roundtrip must agree to relative tolerance `2e-8`.

### G8 — no hidden extrapolation
The support integration grid covers all non-negligible released kernel/window support used to compute invalid fractions. Missing tails cannot be silently assigned zero.

### G9 — deterministic classification
A second identical evaluation reproduces every invalid fraction to absolute tolerance `1e-10` and the retained coordinate set exactly.

### G10 — no downstream leakage
No covariance entries, covariance-derived whitening, nuisance SVD/rank, G7 relation residuals, G8 outputs or held-out performance may be read or used.

## 9. Frozen dimensional viability criterion

A support PASS requires all G1-G10 controls and all of the following:

1. at least one retained `mm`-sensitive density/clustering coordinate;
2. at least one retained signed `Wm`-sensitive galaxy-galaxy-lensing coordinate;
3. at least one retained `WW`-sensitive cosmic-shear coordinate;
4. at least `15` total retained observation coordinates across the three channel classes.

The `15`-coordinate minimum is frozen prospectively to retain the same planning floor used in the prior ACT x unWISE observational-route search; it is not a covariance-rank claim.

## 10. Frozen classifications

If all G1-G10 pass and the dimensional viability criterion is met, classify

`PASS_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073G`.

If all required provenance/operator controls are trustworthy but one or more support/dimensional criteria fail, classify

`FAIL_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073G`.

This is a permanent scientific negative result for this exact observational construction and frozen support rectangle.

If exact released operator/window objects cannot be reproduced or bound well enough for a trustworthy support calculation, classify

`FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE`.

An interrupted run without a complete trustworthy evaluation is `INCOMPLETE_EXP073G` and is not a scientific result.

## 11. Downstream boundary

Only `PASS_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073G` authorizes a new prospectively frozen covariance-restriction/whitening experiment for the retained coordinates.

A PASS does not itself authorize nuisance rank/SVD or relation fitting until covariance restriction has separately completed.

G7 OPEN. G8 OPEN. G9 OPEN.
