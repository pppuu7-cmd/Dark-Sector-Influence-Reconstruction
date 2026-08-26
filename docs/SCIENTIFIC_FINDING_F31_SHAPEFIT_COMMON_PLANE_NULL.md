# F31 — ShapeFit common-plane candidate is not nontrivial against covariance null

Date: 2026-08-26

Exp064A tested the most economical observationally eligible three-channel residual law after Exp063A: one homogeneous plane in dimensionless DESI DR1 ShapeFit AP/growth/shape residuals, with the corrected 2026 covariance propagated into the same coordinates.

The fitted training normal is

`a = (0.6631539009610431, -0.32356655882320945, 0.6749308006391896)`

for

`a_AP r_AP + a_G r_G + a_S r_S = 0`.

The raw fit looks compact: `lambda_min=0.09740761172177222`, train absolute standardized orthogonal residuals are all below 0.45, and `LOO_RMS=0.739104789926628`.

However this compactness is **not statistically nontrivial** once the same fitting procedure is repeated on 20,000 independent Gaussian covariance-consistent null realizations. The frozen dual criterion requires both lower-tail p-values <=0.05; measured values are

- `p_lower(lambda_min)=0.26533673316334183`,
- `p_lower(LOO_RMS)=0.3612319384030798`.

Therefore the scientific result is

`NO_NONTRIVIAL_COMMON_PLANE_RELATION_V0_1`.

The plane is not promoted to a law, no withheld family is selected to rescue it, and no coefficients, channel subset, redshift subset, centering/intercept choice, covariance transform, statistic, seed or alpha are retuned inside Exp064A.

Interpretation: with only the five informative ShapeFit bins, the apparent three-channel planar coherence is compatible with ordinary measurement covariance plus finite-sample fitting freedom. This closes an important false-positive route but does not disfavor DSIR's broader characteristic-scale or multicoordinate findings.

Consequence: **G7 OPEN, G8 OPEN, G9 OPEN**. The next scientifically cleaner route is to add a genuinely independent observable block with an explicit survey kernel/covariance binding (for example a lensing/Weyl-sensitive block) rather than increase functional flexibility on the same five ShapeFit points.

Provenance: GitHub Actions run `32976353679`, job `98201925184`, artifact `9609613504`, artifact SHA256 `7d5a7482f52a5ca3f6f420d44f206433a1be3fa64b3c4e9c00800e9e7f1c09b8`.