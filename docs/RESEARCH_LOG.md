# DSIR research log

All timestamps are project chronology markers; scientific claims are controlled by `docs/GATES.md`.

## 2026-08-24 — repository separation
Dedicated `Dark-Sector-Influence-Reconstruction` repository initialized. RTK explicitly excluded from this project boundary.

## 2026-08-24 — G3B linear controls
Added LambdaCDM, smooth constant-w, thermal-WDM, and designer-f(R)-like linear response controls. Rejected an initial per-model `D(a=1)=1` power comparison because it erased real amplitude differences; switched power-ratio comparisons to common early-time initial conditions.

Experiment 008 found a useful control-space orientation: smooth wCDM is time-dependent but scale-flat in the frozen linear control; thermal WDM is scale-suppressing and time-frozen; the designer-f(R) control is scale-enhancing and increasingly active at late times. This is a discriminant diagnostic, not a law.

## 2026-08-24 — provenance failure caught before G6B
Attempted to use the Gaussian ShapeFit vectors from Appendix A of DESI 2024 V. A mismatch with the paper's tabulated growth ratios triggered a source audit. The February 2026 erratum was found; it documents a numerical implementation error affecting all `f sigma_s8` entries and related covariance elements in the original Appendix A. The obsolete values were rejected and a regression guard was added.

## 2026-08-24 — Experiment 009 / G6B
Ingested the corrected ShapeFit-only response vectors `[DV/rd, DH/DM, f sigma_s8, m+n]` and full per-bin Gaussian covariances. All six covariance matrices are symmetric positive definite.

BGS AP is excluded from the correlation/control summary because DESI states that its low-z AP result is strongly prior affected. For LRG1, LRG2, LRG3, ELG2, and QSO the AP-growth correlation is consistently negative: `[-0.5511,-0.5425,-0.5268,-0.5540,-0.6274]`, mean `-0.5603`, sample scatter `0.0389`.

This is classified as an observational identifiability direction, not a dark-sector law. A fiducial `[DH/DM, f sigma_s8, m+n]` response control gives chi2 `10.4445` for 15 dof (`p=0.7909`) under the per-bin Gaussian approximation and independent-bin control sum. No anomaly is claimed. G6B is marked PASS.

## 2026-08-24 — Experiment 010 / covariance quotient
Introduced Gaussian conditional innovations to prevent the stable AP-growth measurement covariance from masquerading as a law. Growth is conditioned on AP and shape; AP is separately conditioned on growth and shape. Across the five informative bins the conditional growth innovations give chi2 `5.5304/5` (`p=0.3546`), and AP innovations give `4.8921/5` (`p=0.4292`). No significant aggregate innovation is present under this control. G7 remains OPEN.
