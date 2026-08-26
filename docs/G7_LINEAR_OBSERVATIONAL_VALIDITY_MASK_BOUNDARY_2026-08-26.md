# G7 linear observational validity-mask boundary — 2026-08-26

## Purpose

This note corrects the sequencing of the prospective linear/no-CLEFT G7 path. Exp068A validates a physical **forward-interface reproduction**, but its numerical integration domain is intentionally broad (`kmax=10 Mpc^-1`) so that the DSIR implementation can be compared to the upstream projector without artificial truncation. That numerical interface domain must not be confused with the physical validity domain of linear dark-sector / modified-gravity predictions.

No G7/G8/G9 gate is closed here.

## 1. Interface support is not theory-validity support

For an angular mode,

\[
k(\ell,\chi)=\frac{\ell+1/2}{f_K(\chi)}.
\]

The ACT×unWISE projector integrates this over each tracer kernel in redshift/comoving distance and then applies the released mask-coupling/bandwindow operator. Thus even a selected low-ell bandpower can receive contributions from a range of physical `(k,z)` values.

Exp068A sets

\[
k_{max}^{interface}=10\ {\rm Mpc}^{-1}
\]

only to reproduce the upstream raw projection algebra. A PASS would mean that DSIR computes the same linear/no-CLEFT projection for supplied spectra. It would **not** certify that linear C3/C5 physics is reliable to `10 Mpc^-1`.

## 2. DSIR mask rule applies before whitening and quotienting

The project-wide rule is that unavailable/invalid response is **missing, never zero**.

Therefore a future G7 analysis may not obtain an apparently complete angular vector by setting the integrand to zero outside a family-valid region:

\[
P(k,z)\stackrel{\rm forbidden}{=}0\quad\text{for invalid }(k,z).
\]

Instead, each candidate observable coordinate must pass a preregistered support/leakage test showing that the survey kernel and bandwindow place an acceptable fraction of its response inside a domain where every training family entering that relation has a validated physical prediction.

Coordinates that fail are masked from the G7 analysis.

## 3. Consequence for the Exp067A 26D whitener

Exp067A validly binds the full public selected covariance and its 26D Cholesky whitener. However, if physical theory validity removes any of those 26 coordinates, simply applying the full 26D whitener and then deleting coordinates is not generally equivalent to whitening the covariance of the retained observable subset.

For a retained index set `M`, the rigorous path is

\[
\Sigma_M = S_M\Sigma S_M^T,
\]

followed by a fresh direct Cholesky factor

\[
\Sigma_M=L_ML_M^T,
\qquad W_M=L_M^{-1},
\]

where `S_M` is the deterministic coordinate-selection matrix. No covariance repair is allowed unless separately preregistered.

Thus the **physical validity mask must be frozen before the nuisance tangent rank/SVD gate**.

## 4. Required prospective support/leakage audit

After Exp068A passes, but before nuisance quotienting, define a separately numbered experiment that freezes:

1. the candidate training-family set (training only; no fresh G8 withheld family);
2. each family's validated `(k,z)` linear physical domain;
3. the exact released Blue/Green redshift kernels;
4. the exact upstream bandwindow/transfer operators and official scale selections;
5. a deterministic measure of how much each selected angular coordinate depends on valid versus invalid physical support;
6. the maximum permitted invalid-support fraction;
7. the rule for family intersection: a coordinate is eligible only if it passes for every family used in the relation;
8. a robustness check under a frozen tightening of the physical support boundary.

The leakage statistic must be defined before evaluating family outputs. Candidate examples include a positive kernel-weight fraction or a response-norm fraction, but the choice cannot be selected after seeing which bins survive.

## 5. Why a common mask is required for a common G7 law

Let family `f` have validity domain `V_f`. A common relation may compare only observables whose effective support lies in

\[
V_{common}=\bigcap_f V_f.
\]

If one family lacks a valid prediction in a bin, that bin is not a zero response for that family. It is absent from the common comparison space.

This prevents a false separator caused merely by unequal theory coverage.

## 6. Corrected sequencing

The rigorous linear/no-CLEFT G7 path is now:

1. **Exp068A:** validate real-kernel raw physical forward equivalence;
2. validate C3/C5 physical `P_WW/P_Wm/P_mm` input bridges;
3. freeze family-specific physical `(k,z)` validity domains;
4. perform the released-kernel/bandwindow support-leakage audit and freeze the common observable mask;
5. bind the covariance submatrix for that mask and construct its no-repair Cholesky whitener;
6. validate the selected-bandpower/nuisance closure on the retained coordinates, including the chosen PCA noise-bias contract;
7. only then build the nuisance tangent Jacobian and preregister its rank/SVD rule;
8. quotient nuisance directions and fit one training-only G7 relation plus null/permutation control;
9. freeze the complete relation before selecting a fresh G8 withheld family.

This supersedes any informal plan to perform the nuisance-rank gate immediately on all 26 Exp067A coordinates after Exp068A. Exp067A itself remains a valid PASS for the full released covariance/whitening prerequisite; the change is only the scientifically necessary ordering of later theory-validity operations.

## 7. Gate state

- G7: OPEN.
- G8: OPEN.
- G9: OPEN.

No discovery/universality claim follows from this methodological correction.
