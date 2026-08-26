# DSIR recovery checkpoint — Exp064A / F31 (2026-08-26)

Start from main commit `4fedc62232347550e037564b7fd57b9c6190cc80` (Exp063A merged). Immutable prior state entering Exp064A: F27 HARD FAIL; F29 HARD PROSPECTIVE FAIL; F30 HARD PROSPECTIVE PASS; G7/G8/G9 OPEN.

Exp063A selected the corrected DESI DR1 ShapeFit AP/growth/shape block as observationally eligible and explicitly kept raw theory Weyl/slip ineligible for a G7 observational claim until a survey response kernel and covariance binding exist.

Exp064A tested exactly one training-side relation in that eligible block. Coordinates are `r_AP=AP/AP_fid-1`, `r_G=G/G_fid-1`, `r_S=m+n`, with covariance propagated by `J=diag(1/AP_fid,1/G_fid,1)`. The relation is a homogeneous plane through the fiducial origin. Its normal is the smallest generalized-eigenvalue vector of `sum r r^T` against `sum C_dimless`. Nontriviality was frozen to require both lower-tail p-values <=0.05 against 20,000 Gaussian covariance-consistent null realizations (seed 20260826), including leave-one-bin refits.

Clean run `32976353679` / job `98201925184` completed successfully. Artifact `9609613504`, SHA256 `7d5a7482f52a5ca3f6f420d44f206433a1be3fa64b3c4e9c00800e9e7f1c09b8`.

Measured training normal: `(0.6631539009610431, -0.32356655882320945, 0.6749308006391896)`. `lambda_min=0.09740761172177222`, `LOO_RMS=0.739104789926628`. Null p-values: `p_lambda=0.26533673316334183`, `p_LOO=0.3612319384030798`. Therefore F31 is a hard negative result: `NO_NONTRIVIAL_COMMON_PLANE_RELATION_V0_1`.

Do not promote or retune this plane and do not choose a withheld family to rescue it. The next admissible direction is a new recorded experiment that adds a genuinely independent observational block with an explicit survey response kernel/covariance binding; the strongest existing theory motivation is the Exp032 matter-degeneracy breaking by Weyl/slip, but it remains raw theory-space evidence until such a binding exists.

Top-level state remains: G7 OPEN, G8 OPEN, G9 OPEN.