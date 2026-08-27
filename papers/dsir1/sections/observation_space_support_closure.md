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

For Exp072A the eligible row set is empty on the current C3/C5 domain, while the Exp072C extension that would recover 15 rows fails the tested linear perturbativity route in Exp073A. Consequently DSIR does **not** compute or quote a C3/C5 ACTxunWISE covariance-whitened, nuisance-quotiented survey distance from this route. G7, G8, and G9 remain open.

Figure 7 summarizes this support-closure chain: the failed 26-coordinate leakage mask, the required joint support extension, and the subsequent perturbativity ineligibility. The negative result strengthens rather than weakens the operator construction because it identifies an explicit condition under which the formal quotient must not yet be evaluated.
