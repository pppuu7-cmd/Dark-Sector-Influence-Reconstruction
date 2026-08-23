# DSIR research log

Scientific claims are controlled by `docs/GATES.md`.

## 2026-08-24 — repository separation
Dedicated `Dark-Sector-Influence-Reconstruction` repository initialized. RTK explicitly excluded.

## 2026-08-24 — early synthetic/real gates
Experiments 001–006 establish: corrected global noise-edge rank recovery; separation of `R_obs` and projected `R_model`; quotient of known identities; DESI DR2 compressed-BAO covariance validation; calibration-free `F_AP`; relative flat-FLRW expansion reconstruction; and exact/controlled background response equivalences among theory families.

## 2026-08-24 — G3B linear controls
Added LambdaCDM, smooth constant-w, thermal-WDM, and designer-f(R)-like linear response controls. Rejected per-model `D(a=1)=1` power normalization because it erased real amplitude differences; power-ratio comparisons now preserve common early-time initial conditions.

## 2026-08-24 — provenance failure caught before G6B
A mismatch in old DESI 2024 V Appendix-A `f sigma_s8` values triggered an audit. The February 2026 erratum documents a numerical implementation error affecting all original Appendix-A growth entries and related covariance elements. Obsolete values were rejected and a regression guard added.

## 2026-08-24 — Experiment 009 / G6B
Corrected ShapeFit response vectors `[DV/rd, DH/DM, f sigma_s8, m+n]` and covariances were ingested. Five informative bins show stable negative AP-growth measurement covariance (mean rho=-0.5603, sample scatter=0.0389), classified as an observational identifiability direction rather than a dark-sector law. Fiducial three-channel control chi2=10.4445/15 (p=0.7909). G6B PASS.

## 2026-08-24 — Experiment 010 / covariance quotient
Gaussian conditional innovations remove within-bin AP/shape covariance from growth residuals. Aggregate growth innovation chi2=5.5304/5 (p=0.3546), AP innovation chi2=4.8921/5 (p=0.4292). No significant residual law-like signal; G7 remains OPEN.

## 2026-08-24 — Experiment 011 / whitening robustness
Injected latent rank 3 was tested over 30 synthetic cases with n_models=90,180,360 and strongly anisotropic/correlated feature transformations. Correct covariance whitening recovered rank 3 in 30/30 cases and preserved the singular spectrum to max relative error 1.564e-15. The intentionally invalid unwhitened iid-noise calibration returned false ranks 20–35. Conclusion: covariance whitening is a mandatory precondition for DSIR latent-rank claims. G5 becomes PARTIAL rather than OPEN; non-Gaussian/model-family sampling robustness remains to be tested.
