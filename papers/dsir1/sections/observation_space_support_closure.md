## Observation-space support closure and perturbativity

A survey-level quotient is meaningful only after the physical support of the observational operator has been shown to lie inside a certified theory domain. This requirement is logically prior to covariance whitening and nuisance projection. To test it explicitly, DSIR applied the frozen ACTxunWISE angular projection to the current common C3/C5 physical domain before reading any downstream covariance- or nuisance-quotiented model distance.

With the preregistered support-leakage threshold fixed at 5%, Exp072A retained none of the 26 candidate ACTxunWISE coordinates: the nominal and tightened retained dimensions were both zero. The result was therefore a scientific FAIL for the proposed current-domain support mask, not a low-significance detection. Even a post-hoc blockwise diagnostic did not reveal a hidden convention-dependent rescue: every applicable block minimum remained above the same 5% level.

Exp072B then asked whether increasing the upper-k boundary alone could recover an eligible mask. It could not. All 26 coordinate-level upper-k-only targets remained non-finite under the frozen criterion. The median out-of-domain fractions were approximately 0.971 in k and 0.456 in redshift; in 60 of 64 source-pair cases the k leakage exceeded the redshift leakage, while the redshift contribution itself was overwhelmingly toward lower redshift rather than higher redshift. The appropriate diagnostic response was therefore not to extrapolate the existing providers, but to search prospectively for a joint lower-z/upper-k support frontier.

Exp072C found a single Pareto frontier point for the 5% criterion,

\[
z_{\min}=0.0087346,\qquad
k_{\max}=4.81826\ {\rm Mpc}^{-1},
\]

with a retained observational dimension of 15. Relative to the then-current common theory support this corresponds descriptively to an upper-k extension by a factor 72.29 and a lower-z extension by a factor 33.77. This frontier is **planning geometry only**: it does not certify that C3 and C5 can be predicted reliably over that enlarged domain.

That physical question was tested separately in Exp073A using a GR-reference linear/no-CLEFT perturbativity eligibility contract. At the primary \(\Delta^2\le1\) criterion only 7 of 64 source pairs passed; the median incremental nonperturbative fraction was 0.331 and the maximum was 0.840. The median maximum \(\Delta^2\) encountered inside the proposed geometry was 10.11. The retained dimension remained zero under the frozen diagnostic thresholds 0.5, 1, and 2. The resulting classification was therefore `INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`.

Prospectively frozen follow-up audits localize the obstruction more sharply. After an initial infrastructure-only checkout failure, Exp073B was rerun with the historically certified pinned C3 source and completed without changing its frozen scientific criteria. Its classification, `GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B`, separates the projection architecture from the missing physics: the solver-neutral projector and the ACTxunWISE interface can accept independent \(P_{mm}\), signed \(P_{Wm}\), and \(P_{WW}\) blocks, but the currently certified C3 and C5 providers do not supply a justified nonlinear three-block realization over the required domain. Thus the projector is not the limiting component.

Exp073C then prospectively searched the public nonlinear-provider landscape and found no complete public or composable candidate satisfying the joint requirements of nonlinear matter, signed Weyl--matter cross response, Weyl auto response, model-specific nonlinear semantics for both C3 and C5, versionable provenance, and plausible coverage of the Exp072C frontier. This is not a claim that nonlinear modelling is impossible; it says that the missing physical layer cannot presently be filled by silently importing one established package under the frozen DSIR contract.

More importantly, Exp073D identifies an asymmetry in the model definitions themselves. The frozen C5 designer-\(f(R)\) family is a linear numerical realization of an underlying covariant theory whose nonlinear field equations are defined in principle; its current obstruction is therefore a provider/calibration problem. The frozen C3 generalized-dark-matter family is different: its phenomenological pressure and shear parameters define a background/linear perturbation closure but do not uniquely specify nonlinear stress evolution, shell crossing, velocity dispersion, nonlinear anisotropic stress, or nonlinear metric response. A nonlinear C3 continuation therefore requires additional physical assumptions and is not uniquely inferable from the frozen C3 vector.

Exp073E tested whether that completion freedom could be represented prospectively by a finite labelled ensemble while preserving the full frozen C3 linear semantics. Under its frozen E1--E8 requirements the available completion classes were not sufficient: existing constructions either omit part of the pressure/viscosity content, lack independent nonlinear Weyl blocks, or introduce additional theory content that refines/replaces the original phenomenological family. The classification `C3_COMPLETION_ENSEMBLE_NOT_FEASIBLE_EXP073E` therefore forbids hiding a retrospectively chosen nonlinear closure inside a provider and then treating it as the unchanged C3 model.

The methodological consequence is important. If \(M_{\rm supp}\) selects only observation coordinates whose kernels satisfy a prospectively frozen physical-support criterion, then the covariance and theory projection entering the quotient must be restricted consistently,

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

For Exp072A the eligible row set is empty on the current C3/C5 domain. The Exp072C extension that would recover 15 rows is nonperturbative under Exp073A; Exp073B/C show that the required independent nonlinear three-block layer is not available from the existing certified/public stack; and Exp073D/E show that, for C3, forcing such an extension would additionally require new model-defining physics rather than a neutral numerical upgrade. Consequently DSIR does **not** compute or quote a C3/C5 ACTxunWISE covariance-whitened, nuisance-quotiented survey distance from this route. G7, G8, and G9 remain open.

Figure 7 summarizes the quantitative support-closure part of this chain: the failed 26-coordinate leakage mask, the required joint support extension, and the subsequent perturbativity ineligibility. The later provider/model-definition audits explain why this failure cannot be repaired by a hidden nonlinear extrapolation. The negative result strengthens rather than weakens the operator construction because it identifies explicit physical and model-definition conditions under which the formal quotient must not yet be evaluated.
