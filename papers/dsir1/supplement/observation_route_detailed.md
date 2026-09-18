# Supplementary observation-route eligibility chronology

**Status:** detailed provenance-facing companion to the compact main-text observation-space admissibility section.  
**Rule:** statuses below retain their exact scientific meaning; infrastructure-incomplete runs are not physical results, prerequisite PASSes are not physical-support PASSes, and no row implies covariance whitening, nuisance quotienting, survey significance, G7/G8/G9 closure, or new fundamental physics.

## S1. Current-domain support mask

With the preregistered support-leakage threshold fixed at 5%, Exp072A retained none of the 26 candidate ACTxunWISE coordinates: the nominal and tightened retained dimensions were both zero. The result was therefore a scientific FAIL for the proposed current-domain support mask, not a low-significance detection. Even a post-hoc blockwise diagnostic did not reveal a hidden convention-dependent rescue: every applicable block minimum remained above the same 5% level.

Exp072B then asked whether increasing the upper-k boundary alone could recover an eligible mask. It could not. All 26 coordinate-level upper-k-only targets remained non-finite under the frozen criterion. The median out-of-domain fractions were approximately 0.971 in k and 0.456 in redshift; in 60 of 64 source-pair cases the k leakage exceeded the redshift leakage, while the redshift contribution itself was overwhelmingly toward lower redshift rather than higher redshift. The appropriate diagnostic response was therefore not to extrapolate the existing providers, but to search prospectively for a joint lower-z/upper-k support frontier.

Exp072C found a single Pareto frontier point for the 5% criterion,

\[
z_{\min}=0.0087346,\qquad
k_{\max}=4.81826\ {\rm Mpc}^{-1},
\]

with a retained observational dimension of 15. Relative to the then-current common theory support this corresponds descriptively to an upper-k extension by a factor 72.29 and a lower-z extension by a factor 33.77. This frontier is **planning geometry only**: it does not certify that C3 and C5 can be predicted reliably over that enlarged domain.

## S2. Perturbativity and nonlinear-provider eligibility

That physical question was tested separately in Exp073A using a GR-reference linear/no-CLEFT perturbativity eligibility contract. At the primary \(\Delta^2\le1\) criterion only 7 of 64 source pairs passed; the median incremental nonperturbative fraction was 0.331 and the maximum was 0.840. The median maximum \(\Delta^2\) encountered inside the proposed geometry was 10.11. The retained dimension remained zero under the frozen diagnostic thresholds 0.5, 1, and 2. The resulting machine classification is `INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`.

Prospectively frozen follow-up audits localized the obstruction. After an initial infrastructure-only checkout failure, Exp073B was rerun with the historically certified pinned C3 source and completed without changing its frozen scientific criteria. Its classification, `GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B`, separates the projection architecture from the missing physics: the solver-neutral projector and the ACTxunWISE interface can accept independent \(P_{mm}\), signed \(P_{Wm}\), and \(P_{WW}\) blocks, but the currently certified C3 and C5 providers do not supply a justified nonlinear three-block realization over the required domain. Thus the projector is not the limiting component.

Exp073C prospectively searched the public nonlinear-provider landscape and found no complete public or composable candidate satisfying the joint requirements of nonlinear matter, signed Weyl--matter cross response, Weyl auto response, model-specific nonlinear semantics for both C3 and C5, versionable provenance, and plausible coverage of the Exp072C frontier. This is not a claim that nonlinear modelling is impossible; it says that the missing physical layer cannot presently be filled by silently importing one established package under the frozen DSIR contract.

Exp073D identifies an asymmetry in the model definitions themselves. The frozen C5 designer-\(f(R)\) family is a linear numerical realization of an underlying covariant theory whose nonlinear field equations are defined in principle; its current obstruction is therefore a provider/calibration problem. The frozen C3 generalized-dark-matter family is different: its phenomenological pressure and shear parameters define a background/linear perturbation closure but do not uniquely specify nonlinear stress evolution, shell crossing, velocity dispersion, nonlinear anisotropic stress, or nonlinear metric response. A nonlinear C3 continuation therefore requires additional physical assumptions and is not uniquely inferable from the frozen C3 vector.

Exp073E tested whether that completion freedom could be represented prospectively by a finite labelled ensemble while preserving the full frozen C3 linear semantics. Under its frozen E1--E8 requirements the available completion classes were not sufficient: existing constructions either omit part of the pressure/viscosity content, lack independent nonlinear Weyl blocks, or introduce additional theory content that refines/replaces the original phenomenological family. The classification `C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E` therefore forbids hiding a retrospectively chosen nonlinear closure inside a provider and then treating it as the unchanged C3 model.

## S3. Support-measure normalizability

A support fraction such as

\[
f_{\rm out}
=\frac{\int_{\Omega\setminus D}|\mathcal K(x)|\,d\mu(x)}
{\int_{\Omega}|\mathcal K(x)|\,d\mu(x)}
\]

is meaningful only if the prospectively chosen positive normalizer in the denominator is finite and non-zero. This matters for transforms whose absolute response has an ultraviolet tail. A preliminary Exp073G BOSS audit already exposed the mechanism: for a configuration-space Fourier--Bessel kernel \(K_\ell(k;s)\propto k^2j_\ell(ks)\), the asymptotic relation \(j_\ell(ks)=O(k^{-1})\) makes the absolute operator response generically grow as \(O(k)\), so an all-\(k\) positive-operator-only normalizer is not finite. Exp073G is retained only as methodological corroboration because its formal status is a reproduction/provenance failure, not a scientific support FAIL.

Exp073L supplied the completed numerical normalizability test under frozen criteria. Extending the KiDS absolute-response ladder to \(\ell=1.2\times10^5,2.4\times10^5,4.8\times10^5\), all eight Wm components and all eight WW components were classified as nonnormalizable; none was finite. The final local exponent ranges were approximately 1.494--1.518 for Wm and 1.493--1.516 for WW, while the final dyadic-shell fractions remained approximately 0.645--0.651. The half-step convergence discrepancy was only \(1.94\times10^{-6}\), far below the frozen 0.005 numerical tolerance. For a pure dyadic power-law normalization,

\[
f_{\rm shell}=1-2^{-p},
\]

so a positive exponent near \(p\simeq1.5\) leaves an order-unity fraction in every newly opened ultraviolet shell rather than converging to a finite absolute-response normalizer.

DSIR therefore does not impose a retrospective high-\(\ell\) cutoff or multiply by a fiducial power spectrum chosen after seeing the divergence merely to manufacture a finite support fraction.

## S4. Finite operator class and exact-realization provenance

Exp073M demonstrated that the normalizability requirement is restrictive but not a universal no-go. At the operator-class level, a prospectively classified finite-positive candidate was found using harmonic-space DES Y3 galaxy--galaxy lensing for Wm, DES Y1 harmonic cosmic shear for WW, and the already finite BOSS matrix component for mm. The candidate passed all frozen M1--M8 preconditions and no support fraction or downstream covariance/nuisance quantity was read.

A separate exact-realization gate then produced a negative result. Exp073N reproduced the frozen public operator repository itself, but the exact published DES Y3 real-data Wm realization could not be reconstructed from the frozen public binding: the available Y3 configurations at that pin are flask configurations, and the frozen `ggltest.py` path does not execute a real-data GGL realization. Exp073N therefore remains `FAIL_EXP073N_REPRODUCTION_OR_PROVENANCE`. This is **not** a physical-support FAIL because no \(f_{\rm invalid}\), Wm/WW support fraction, or combined retained dimension was evaluated.

Rather than relaxing that provenance requirement, Exp073O prospectively searched for a public real-data replacement and found one in Cosmotheka DES Y1 redMaGiC\(\times\)Metacal pseudo-\(C_\ell\). The replacement passes the frozen O1--O8 criteria: immutable real-data provenance, finite NaMaster bin/workspace construction with bounded harmonic range, exact public input binding, signed Wm semantics, no GR closure, no model/downstream weighting, sufficient redshift information, and later applicability of the unchanged support-only audit. The parent Exp073N failure is preserved, and the future physical criteria remain unchanged: common rectangle \(0.295\le z\le2.33\), \(k\le0.0666476201\,\mathrm{Mpc}^{-1}\), \(f_{\rm invalid}\le0.05\), and minimum retained dimension 15.

## S5. Public-input and catalogue-to-pixel prerequisites

The subsequent DES input chain closes increasingly deep prerequisites without crossing the physical-support boundary. Exp073P2 completed SHA256 identity binding for every DES Y1 release object frozen by the replacement route, including the 84.08 GB metacalibration catalogue and the 2.74 GB source-redshift-binning file. Exp073S0 then exactly reproduced the public redMaGiC mask and lens/source \(n(z)\) prerequisites: the native \(N_{\rm side}=4096\) mask remained an identity under same-resolution `ud_grade`, 6,536,725 pixels exceeded the frozen 0.5 mask cut (sky fraction 0.0324683), and both lens and source redshift distributions reproduced their 400-row public tables.

Exp073R0 subsequently passed the preregistered raw-row/HEALPix equivalence prerequisite after two earlier infrastructure-incomplete transport attempts were preserved. The machine classification is `PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0`. The frozen audit sampled 16 windows of 8192 rows, or 131,072 rows, from the 136,930,995-row parent catalogue. Required source and metacalibration fields reproduced exactly, all four source bins were populated, and every sampled raw-row sky coordinate mapped to exactly the expected HEALPix pixel at \(N_{\rm side}=4096\), `coords=C`. The four bins contained 7,674, 7,667, 7,272, and 3,618 selected rows, spanning 4,300, 4,277, 4,178, and 2,650 unique pixels.

The R0 artifact explicitly records `science_gate_scored=false`: R0 is an operator-reproduction prerequisite PASS, not the Exp073P physical-support result. Exp073R1 was preregistered before the relevant output and a gated implementation exists, but no completed R1 result is used as a Paper-I scientific claim in this snapshot.

## S6. Quotient-order consequence

If \(M_{\rm supp}\) selects only observation coordinates whose kernels satisfy a prospectively frozen physical-support criterion, then the covariance and theory projection entering the quotient must be restricted consistently,

\[
K_{B,{\rm supp}}=M_{\rm supp}K_B,
\qquad
C_{B,{\rm supp}}=M_{\rm supp}C_BM_{\rm supp}^{T},
\]

followed only then by

\[
W_{B,{\rm supp}}=C_{B,{\rm supp}}^{-1/2},
\qquad
A_{B,{\rm supp}}=Q_{B,{\rm supp}}W_{B,{\rm supp}}K_{B,{\rm supp}}.
\]

For Exp072A the eligible row set is empty on the current C3/C5 domain. The Exp072C extension that would recover 15 rows is nonperturbative under Exp073A; Exp073B/C show that the required independent nonlinear three-block layer is not available from the existing certified/public stack; Exp073D/E show that, for C3, forcing such an extension would additionally require new model-defining physics rather than a neutral numerical upgrade; and Exp073L shows that even an otherwise reproducible observational transform is unusable for a frozen support fraction if its chosen positive absolute-response measure is nonnormalizable. Exp073M--R0 add a further requirement: a finite operator class must be reduced to an exact reproducible real-data realization before the physical-support statistic is allowed to run.

Consequently DSIR does **not** compute or quote a covariance-whitened, nuisance-quotiented survey distance from any route that fails finite normalization, exact reproducibility, physical-domain support, or provider semantics. G7, G8, and G9 remain open.

## S7. Canonical machine provenance

Exact workflow runs, artifacts, commit/source bindings, SHA256 digests and frozen thresholds are canonical in:

- `papers/dsir1/PROVENANCE_MATRIX.md`;
- `papers/dsir1/OBSERVATION_ROUTE_LEDGER.md`;
- `papers/dsir1/SUPPORT_OPERATOR_PROVENANCE.md`;
- manuscript-scoped evidence JSON under `papers/dsir1/evidence/`.

The supplement may summarize those records but must not replace them as the immutable provenance source.
