# DSIR recovery checkpoint — Exp063A (2026-08-26)

Start from `main` commit `5731cb18a842f41c5ae28c9a19081f6c67b21382`: F27 HARD FAIL; F29 HARD PROSPECTIVE FAIL; F30 HARD PROSPECTIVE PASS; G7/G8/G9 OPEN.

Exp063A is the next minimal gate after Exp062A. It audits which existing channel blocks are eligible for a genuine G7 law search. The corrected DESI DR1 ShapeFit AP/growth/shape block is selected because its measured covariance and Gaussian conditional-innovation quotient are already implemented and reproducible. The raw GDM Weyl/slip separator remains masked from G7 observational-law claims until a survey response kernel and covariance binding exist.

Run `.github/workflows/g7-observable-eligibility-v0-1.yml`. A clean result must report `PASS_OBSERVABLE_ELIGIBILITY_AUDIT`, preserve `zero_imputation=false`, and leave `G7/G8/G9` OPEN.

If Exp063A passes, the next admissible research step is to preregister exactly one mathematical residual relation inside the DESI ShapeFit AP/growth/shape block, including exact covariance quotient, channel/bin mask, scalar statistic, tolerance, and null/permutation control, all frozen before selecting a new withheld family for G8.

Do not reinterpret F27/F29, retune F30, or use C9/future withheld outputs to select the G7 relation. Preserve all negative results.
