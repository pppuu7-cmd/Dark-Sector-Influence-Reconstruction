# DSIR recovery overlay — post Exp067E / pre Exp068A

**Date:** 2026-08-26  
**Purpose:** current chat-independent recovery overlay after the repository/chat audit and before the first Exp068A physical forward comparison.  
**Base main entering this overlay:** `502af6dc9789665d373868536ff5282af8d446bf`.

This file supplements `docs/RECOVERY_MANUAL.md`. The older manual remains authoritative for the derivations and chronology through F26; this overlay is authoritative for the later F27–F31 and ACT×unWISE/CAMB↔CLASS chain through Exp067E and for the exact next barrier.

## 0. Non-negotiable scientific discipline

- DSIR is independent of RTK.
- Preserve negative results; never relabel a frozen FAIL after diagnosis.
- Missing/undefined response cells are not zeros.
- Theory-space separation is not observational distinguishability.
- A retrospective relation is not a prospective prediction.
- No G7 law may be declared from a relation fitted after inspecting the validation family.
- No G8 discovery claim before a G7 relation is frozen and then survives a genuinely fresh withheld test.
- G9 remains downstream of G7/G8.

Core bookkeeping remains

\[
X_{\mu\nu}=M_0^2G_{\mu\nu}-T^{known}_{\mu\nu},
\]

with gauge-safe matter response

\[
\Delta_m=\delta_m+3(1+w_m)\mathcal H\theta_m/k^2.
\]

## 1. F27 — common raw-response centroid relation failed prospectively

Exp054A calibrated the full-response squared-energy scale centroid on C3+C5:

\[
q_k^R(k)=\frac{\sum_zR(z,k)^2}{\sum_{z,k}R(z,k)^2},\qquad
k_R^{geo}=\exp\left[\sum_kq_k^R\ln k\right],
\]

and froze the adjacent source-response slope band

\[
0.0022992620786061375\le
\mathcal C_i=\frac{\Delta\ln k_R^{geo}}{\Delta\ln k_*}
\le0.09951219222831723.
\]

C7 IDM–dark-radiation was then selected source-only and evaluated prospectively in Exp054C. Its measured `k_R_geo` increased toward the finite-window high-k boundary while the source scale decreased, giving all four adjacent slopes negative:

`[-1.3855941363,-0.6685100505,-0.2190645818,-0.0715651205]`.

**F27: HARD PROSPECTIVE FAIL.** This is a boundary-saturation failure of that scalar response coordinate, not a no-go for DSIR.

Standalone record: `docs/SCIENTIFIC_FINDING_F27_COMMON_RESPONSE_CENTROID_WITHHELD_FAILURE.md`.

## 2. F28 and F29 — endpoint half-transition retrospective candidate then fresh failure

Exp055A defined

\[
u(z,k)=\frac{R(z,k)-R(z,k_{min})}{R(z,k_{max})-R(z,k_{min})}
\]

and the unique `u=1/2` crossing `k50(z)`, summarized by

\[
k_{50}^{geo}=\exp\left[\frac17\sum_z\ln k_{50}(z)\right].
\]

C3, C5 and C7 all had positive adjacent source-response slopes retrospectively. This became F28, explicitly **retrospective only**.

Exp056A selected C8 IDM–photon couplings using source equations only. Exp056B then froze the F28 sign relation before the first C8 matter-power response. The C8 `k50_geo` sequence was

`[0.0161297511,0.0495901203,0.0181843976,0.0397209153,0.0158358347] h/Mpc`,

with adjacent slopes

`[-7.80810676,+4.94852776,-3.05902403,+5.46614189]`.

**F29 / Exp056B: HARD PROSPECTIVE FAIL.** The endpoint-normalized scalar relation is not universal across C8. No coupling replacement, node deletion, alternative crossing, normalization or sign redefinition may rescue v0.1.

Record: `docs/GATE_UPDATE_EXP056B_F29_2026-08-26.md`.

## 3. F30 — multicoordinate withheld-family path survives C9

The scalar failures motivated a training-only multicoordinate representation. Exp058A/060A froze a two-coordinate localization+shape/orientation operator before C9 IDM–baryon matter-power output.

Exp061A evaluated it prospectively with no C9-dependent retuning. Adjacent `(ell,q)` path-step norms were

`[0.4386749948,2.9102332590,5.7618606896,0.0477483350]`,

all above the frozen `1e-10` floor; there were no nonadjacent polyline intersections; all seven leave-one-redshift rebuilds also passed.

Run `32957427686`; artifact `9602537353`; digest `560f1fe127bfee1cd6fc14b91c455c11babf211a0854a37f6db30d6e5bbea6ed`.

**F30: HARD PROSPECTIVE PASS** for the frozen multicoordinate path gate v0.1. It is positive out-of-family evidence for a structured response representation, not by itself a G7 law.

## 4. F31 — eligible DESI ShapeFit common-plane law search is negative

Exp063A first restricted G7-eligible observables to the corrected DESI DR1 ShapeFit AP/growth/shape block; raw Weyl/slip remained ineligible without a survey kernel/covariance binding.

Exp064A tested one homogeneous plane through the fiducial origin in

`r_AP=AP/AP_fid-1`, `r_G=G/G_fid-1`, `r_S=m+n`,

with covariance propagated by the frozen Jacobian and the plane normal defined by the smallest generalized eigenvalue. Nontriviality required both preregistered lower-tail p-values `<=0.05` against 20,000 covariance-consistent Gaussian nulls, including leave-one-bin refits.

Measured:

- normal `(0.66315390096,-0.32356655882,0.67493080064)`;
- `lambda_min=0.09740761172`;
- `LOO_RMS=0.73910478993`;
- `p_lambda=0.26533673316`;
- `p_LOO=0.36123193840`.

**F31: HARD NEGATIVE — `NO_NONTRIVIAL_COMMON_PLANE_RELATION_V0_1`.** Do not retune the plane or pick a withheld family to rescue it.

## 5. ACT DR6 × unWISE observational bridge chronology

### Exp065A — raw covariance eligibility FAIL

Pinned likelihood `ACTCollaboration/unWISExLens_lklh@6302c30...`; official archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`.

The naively assembled unselected 236×236 Blue+Green covariance had `lambda_min=-1.65028e-19`; Exp065A remains a permanent eligibility FAIL.

### Exp065B — exact official selected covariance PASS

Reproducing the literal upstream scale selection gives per tracer 6 `Clgg` + 7 `Clkg` bins and the frozen combined order

`[Blue gg(6), Blue kg(7), Green gg(6), Green kg(7)]`.

The selected 26×26 covariance has

`lambda_min=1.2742353176342933e-17`, `lambda_max=3.980349119528573e-15`,

passes direct Cholesky and inversion without regularization.

### Exp066A — solver-neutral raw projection algebra PASS

The no-CLEFT raw projector was separated from CAMB-provider semantics and made to accept independent

`P_WW(k,z), P_Wm(k,z), P_mm(k,z)`

in physical `k[Mpc^-1]`, plus geometry and tracer kernels. Analytic-mock equivalence to pinned upstream was exact and independent-spectrum scaling controls passed.

### Exp066B — selected-bandpower shortcut FAIL

The proposed cheap constant-mode white-noise shortcut assumed `C 1=w2 1`, but released ACT `gg` coupling gave relative residual `0.3615744168`. The shortcut is permanently forbidden.

### Exp066C — exact survey-only shot-noise template PASS

Use the exact solve

\[
C x=w_2\mathbf 1
\]

and then the released bandwindow/transfer path. Run `32989328863` passed with solve residual `6.52e-15` and selected-bin reference difference `4.22e-15`. The nonconstant-template control also passed (`max|x-1|=1.114`).

### Exp067A — selected observational covariance whitening PASS

Use the released selected 26×26 covariance directly, with

\[
\Sigma=LL^T,\qquad W=L^{-1},\qquad W\Sigma W^T=I.
\]

No repair, symmetrisation, shrinkage or eigenvalue clipping.

Frozen hashes:

- covariance: `df7e285c40009e0ba20cc5d920342e1066ceff69d277fdf3233ac63463ffddb9`;
- Cholesky `L`: `6a30b1792d8b3f29ae66102dadb285f394f6aa4c30cba29dc3c3234a1897f109`;
- whitener `W`: `b32e59a98b6910427ac5026bc3f882ea8b0934b65de9abe44c599e1c7ec66822`.

These hashes are binding targets for any later 26D G7 statistic under this convention.

## 6. CAMB ↔ CLASS physical Weyl/matter convention chronology

### Exp067B — frozen gate FAIL, despite spectral agreement

Correct convention:

\[
W=k^2(\phi+\psi)/2.
\]

CLASS may construct

\[
q_W=k^2\frac{\phi+\psi}{2d_m},\qquad
P_{Wm}=q_WP_m,\qquad P_{WW}=q_W^2P_m.
\]

All three cross-solver max-log differences passed the frozen 3% threshold (`~0.00922`) and the missing-`k^2` negative control failed strongly as intended. However CAMB rank-one coherence reached `9.25318e-8 > 5e-8`; therefore Exp067B remains **HARD FAIL**.

### Exp067C — defect localized to native CAMB power path

Native-grid maximum

\[
E_{native}=\max|P_{Wm}^2/(P_{WW}P_{mm})-1|=1.6160126437\times10^{-7}.
\]

Re-evaluating the interpolator on native knots reproduced the same field; spline interpolation is not the cause.

### Exp067D — causal precision mechanism confirmed

Pinned CAMB stores the relevant transfer table as default Fortran `real` / Python `c_float`. The first transfer multiplication is therefore performed in float32 before promotion to double-precision power output.

Explicit float32-first reconstruction gives

`E32=1.6160126426e-7`

and reproduces the official residual field to `6.66e-16`. Promoting the same stored transfer values to float64 before multiplication gives reported residual `0`.

Classification: `FLOAT32_TRANSFER_PRODUCT_CAUSALLY_CONFIRMED_V0_1`.

Exp067B is not reclassified; Exp067D explains its numerical floor.

### Exp067E — corrected convention passes prospectively out of sample

The corrected convention was frozen before fresh LambdaCDM references R1/R2. All R0/R1/R2 spectral comparisons passed the 3% max-log requirement:

- R0: about `0.009223`;
- R1: about `0.008819`;
- R2: about `0.008590`.

The CAMB float32 precision signature reproduced on all references and the deliberately missing-`k^2` convention remained catastrophically wrong (`median |Delta ln P|~11.98`).

Run `32998659859`; artifact `9617676816`; SHA256 `6e6419040b7295dfe4b1b4c126a5cfeaa6e1e24a76a7e29c05ccd7c706f65ee2`.

Classification: **`PASS_CAMB_CLASS_OUT_OF_SAMPLE_POWER_CONVENTION_V0_1`**.

This removes the power-normalization ambiguity needed for a solver-neutral ACT forward interface. It does not close G7/G8/G9.

## 7. Current exact next barrier — Exp068A

Exp068A is preregistered separately in

`experiments/068a_act_unwise_physical_forward_reproduction_v0_1.md`.

It must run before any nuisance quotient is frozen. It compares the exact pinned upstream raw no-CLEFT projector with `src/dsir/act_unwise_projection.py` using:

- pinned physical CAMB R0 spectra;
- released Blue/Green xmatch + xcorr + PCA redshift kernels;
- full raw `ell=0..6143` support;
- `z=0..3`;
- projector `kmax=10 Mpc^-1`;
- common Gauss-Legendre order 96;
- the inherited Exp066A `5e-13*max(1,max|reference|)` component tolerance.

Allowed outcomes are immutable PASS or FAIL. If FAIL, the nuisance quotient remains blocked.

## 8. Future nuisance tangent quotient — design only, NOT yet frozen/executed

After and only after Exp068A PASS, the selected 26D observable vector may be decomposed into physical dark-sector directions and nuisance directions.

Let `d` be the selected 26-vector and let `eta` denote nuisance parameters. Candidate nuisance Jacobian:

\[
J_\eta=\frac{\partial d}{\partial\eta}.
\]

Whiten with the already frozen Exp067A operator:

\[
A=WJ_\eta.
\]

Then compute

\[
A=U_\eta\Sigma_\eta V_\eta^T.
\]

For a preregistered effective nuisance rank `r_eta`, define the whitened nuisance-orthogonal quotient

\[
\boxed{Q=I-U_{\eta,r}U_{\eta,r}^T}.
\]

Candidate nuisance inventory from the released Blue/Green setup is at most 18 named directions (8 Blue + 10 Green in the current bookkeeping), but **the effective rank must not be declared equal to 18 by assumption**. The SVD rank rule/tolerance must be frozen prospectively after the physical forward adapter passes and before fitting any G7 relation.

This section is a recovery design note, not an executed experiment and not a scientific result.

## 9. Known historical documentation gap

The full repository tree does not contain standalone `experiments/042...` and `experiments/043...` files, although their negative scientific conclusion is preserved in the recovery manual and later documents: the attempted absolute GDM velocity/RSD gauge bridge did not meet the frozen validation requirement, and exploratory velocity science must not be treated as validated. Do not invent missing details; consult the preserved recovery/manual chronology and Git history when needed.

## 10. Current top-level gate state

- G1 PASS v0.1.1.
- G2 PASS v0.1.1.
- G3A PASS.
- G3B PASS block-aware and extended through C6/C8/C9 experiments.
- G4 PASS synthetic rank.
- G5 PARTIAL.
- G6A/G6B PASS.
- **G7 OPEN.** No surviving nontrivial observational residual law has yet been frozen and established.
- **G8 OPEN.** There are genuine withheld-family/interpolation results, including F30 PASS, but no G7 law has yet survived a fresh post-freeze G8 test.
- **G9 OPEN.**

## 11. Recovery continuation order

1. Read `docs/RECOVERY_MANUAL.md` for history through F26.
2. Read this overlay.
3. Read `docs/RESEARCH_CHECKPOINT_EXP067E_2026-08-26.md`.
4. Read `experiments/068a_act_unwise_physical_forward_reproduction_v0_1.md` and its first immutable result when available.
5. If Exp068A PASS, preregister the 26D nuisance tangent quotient/rank rule before any G7 fit.
6. If Exp068A FAIL, preserve it and diagnose only in a separately numbered experiment.
7. Do not choose a fresh G8 family before a G7 relation is frozen.
