# ACT × unWISE nuisance-tangent inventory — 2026-08-26

## Scope

This is a source-level methodological audit for the pinned ACT DR6 × unWISE likelihood used by DSIR. It is **not** a G7 relation fit, not a nuisance-rank measurement, and not a reinterpretation of Exp068A. Its purpose is to prevent the later covariance-whitened nuisance quotient from silently equating the number of named nuisance parameters with the numerical tangent rank.

Pinned likelihood source:

`ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`.

The relevant ACT cross-correlation configuration is `XCorrACT.yaml`, with samples `Blue_ACT` and `Green_ACT` and the released ACT scale cuts already bound by Exp065B/Exp067A.

## 1. Exact named nuisance inventory

The pinned ACT nuisance prior files contain 18 named nuisance parameters in total.

### Blue_ACT — 8 named parameters

1. `b_Blue_ACT` — galaxy bias;
2. `log10SN_Blue_ACT` — shot-noise amplitude;
3. `s_Blue_ACT` — magnification slope;
4. `Blue_ACT_pca_0`;
5. `Blue_ACT_pca_1`;
6. `Blue_ACT_pca_2`;
7. `Blue_ACT_shift_cleft_cb2`;
8. `Blue_ACT_shift_cleft_cbs`.

### Green_ACT — 10 named parameters

1. `b_Green_ACT` — galaxy bias;
2. `log10SN_Green_ACT` — shot-noise amplitude;
3. `s_Green_ACT` — magnification slope;
4. `Green_ACT_pca_0`;
5. `Green_ACT_pca_1`;
6. `Green_ACT_pca_2`;
7. `Green_ACT_pca_3`;
8. `Green_ACT_pca_4`;
9. `Green_ACT_shift_cleft_cb2`;
10. `Green_ACT_shift_cleft_cbs`.

The likelihood defaults explicitly set

- `shift_cleft_b2: True`,
- `shift_cleft_bs: True`,
- `shift_cleft_b3: False`,
- `scale_cleft_b2: False`,
- `scale_cleft_bs: False`,
- `scale_cleft_b3: False`,
- `do_pca_dndz_marg: True`.

Thus the four listed CLEFT-shift parameters are real baseline nuisance directions; they are not bookkeeping aliases.

## 2. No-CLEFT visibility boundary

Exp068A deliberately validates a **linear/no-CLEFT physical forward adapter**. In this contract the raw CLEFT tensors are algebraically zero. Therefore derivatives with respect to the four CLEFT-shift parameters are exactly zero in the no-CLEFT observable map:

\[
\frac{\partial d_{\rm no\mbox{-}CLEFT}}{\partial\eta_{\rm CLEFT\ shift}}=0.
\]

Consequently, the no-CLEFT tangent Jacobian can contain at most 14 potentially nonzero named columns:

- Blue: `b`, `log10SN`, `s`, and 3 dN/dz PCA coefficients = 6;
- Green: `b`, `log10SN`, `s`, and 5 dN/dz PCA coefficients = 8.

Hence

\[
\boxed{\operatorname{rank}J_{\eta,\rm no\mbox{-}CLEFT}\le 14}
\]

before any numerical SVD is performed. The inequality is only an upper bound: covariance projection, finite scale cuts, and accidental or physical collinearities can reduce the actual rank further.

This means that a future statement such as “the ACT nuisance quotient is 18-dimensional” would be invalid if inferred merely from the 18 parameter names or from the no-CLEFT Exp068A adapter.

## 3. Full-baseline versus bridge-level quotient

Two distinct objects must remain separate:

### Bridge-level no-CLEFT quotient

For a frozen 26-coordinate observable vector `d` and Exp067A whitener `W`, define

\[
A_0=WJ_{\eta,0},
\]

where `J_{eta,0}` contains only nuisance directions that actually act in the validated no-CLEFT forward map. The numerical rank must be measured under a preregistered SVD threshold; it must not be set to 14 by definition.

### Full-baseline quotient

A quotient intended to represent the public baseline likelihood must include the nonzero free-CLEFT basis and its nuisance dependence. That requires a separately validated **physical CLEFT forward bridge**, not merely the synthetic algebraic CLEFT closure already tested in Exp066B.

Only after that bridge exists may one form the full

\[
A_{\rm full}=WJ_{\eta,\rm full}
\]

and determine its numerical tangent rank.

## 4. Frozen discipline for the future SVD gate

The future nuisance-rank experiment must preregister, before seeing singular values:

1. the exact fiducial cosmology and nuisance point;
2. the 26-coordinate ordering inherited from Exp065B/Exp067A;
3. the exact Exp067A whitener hash;
4. derivative construction and finite-difference step rules or analytic derivatives;
5. column scaling/parameter normalization;
6. the SVD rank threshold;
7. stability checks under a frozen step-size ladder;
8. whether the gate is no-CLEFT bridge-level or full-baseline CLEFT-aware.

If

\[
A=U\Sigma V^T
\]

and the preregistered rule yields rank `r_eta`, the nuisance-orthogonal projector is

\[
Q=I-U_{[:,1:r_\eta]}U_{[:,1:r_\eta]}^T.
\]

No post-output change of `r_eta`, SVD threshold, parameter scaling, derivative step, or nuisance subset is allowed to improve a later G7 relation.

## 5. Current scientific boundary

- The named ACT nuisance inventory is exactly 18 parameters.
- In the Exp068A no-CLEFT contract, 4 CLEFT-shift columns are identically invisible.
- Therefore the no-CLEFT tangent rank is bounded above by 14, but its actual value is **unknown** until a preregistered numerical rank gate is executed.
- A full-baseline 18-parameter tangent analysis requires a validated physical CLEFT bridge first.
- G7/G8/G9 remain OPEN.
