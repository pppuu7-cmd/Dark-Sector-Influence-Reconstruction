# DSIR-I referee-style adversarial audit — v0.1

**Purpose:** attack the manuscript as a skeptical referee would, and require every defense to be either (a) a frozen result, (b) a formal statement, or (c) an explicit limitation. This is not promotional prose and should remain stricter than the paper abstract.

## R1. “Dark degeneracy and model-independent parameterizations are old; what is actually new?”

**Risk:** HIGH.

**Valid criticism:** dark degeneracy, PPF/EFT, GDM, PCA, model-independent reconstruction and observable-space reasoning all predate DSIR-I. The paper must not claim invention of any one of these ingredients.

**Defensible DSIR-I contribution:** the manuscript combines a heterogeneous response atlas with (i) explicit channel-conditioned equivalence `A_B=Q_B W_B K_B`, (ii) scale-time nonseparability and finite-amplitude trajectory geometry, (iii) cross-mechanism withheld/falsification tests, and (iv) fail-closed observation-route admissibility down to exact realized-operator provenance.

**Paper action:** keep the novelty claim combinatorial and operational, not historical/absolute. Cite Kunz, PPF/EFT/GDM, PCA/model-breaking and modern DESI degeneracy work prominently.

**Status:** addressed in `LITERATURE_POSITIONING.md`; repeat fresh search before submission.

---

## R2. “`chi_I` is an arbitrary statistic that depends on the chosen grid and norm.”

**Risk:** HIGH.

**Valid criticism:** `chi_I` is representation- and domain-dependent. It is not a fundamental invariant.

**Evidence:**

- Exp045A prospectively falsifies the simpler additive `mu+T+tau` core on the frozen low-k atlas.
- Exp047A shows non-overlapping finite-amplitude descriptive envelopes.
- Exp047B preserves the family-tier ordering in all 12 deterministic single-node deletions.
- The paper explicitly records the smooth-w sensitivity to removal of the lowest-k node.

**Paper action:** call the result a robust **descriptive response hierarchy on the frozen tested domains**, never a universal dark-sector invariant.

**Status:** addressed.

---

## R3. “The impressive hierarchy may just be amplitude ranking rather than shape physics.”

**Risk:** MEDIUM-HIGH.

**Evidence:** the additive projection removes global, scale-only and time-only structure before defining `I`; `eta_I` localizes pairwise normalized shape separation specifically in irreducible `k x z` structure. GDM/f(R) pairs carry about 61% of normalized pairwise response-shape separation in `I` on the frozen low-k grid.

**Counterexample/guard:** GDM cs2/cv2 have large `eta_I~0.73` but tiny total matter angle `~0.323 deg`; therefore the paper reports `eta_I` together with absolute distance/angle and never treats it as signal-to-noise.

**Status:** addressed.

---

## R4. “The GDM pressure/viscosity distinction is trivial parameter relabeling or a numerical artifact.”

**Risk:** HIGH because this is a flagship channel-degeneracy example.

**Evidence:**

- frozen low-k matter response angle `~0.3226 deg`;
- Weyl-amplitude angle also small `~0.3007 deg`;
- metric-slip angle `~137.94 deg`;
- equalized Weyl+slip angle `~56.96 deg`.

The same pair changes its separability when an independent metric channel is added. This is precisely the channel-conditional claim.

**Numerical control:** C3 provider history is explicit. The original target-grid bridge FAIL remains failed; a separately frozen native-grid provider later passes its own closure/coherence/signed-cross/repeatability contract.

**Boundary:** these are theory-response angles, not survey detection significance.

**Status:** addressed.

---

## R5. “Designer-f(R) dominates `chi_I` because of solver accuracy or an incorrect GR limit.”

**Risk:** HIGH.

**Evidence/control:** the original C5 q=1 exact-GR bridge miss remains a permanent FAIL against the unchanged `5e-6` threshold. A prospectively frozen accuracy ladder shows convergence, after which a separately frozen q=3 provider passes exact-zero/tiny-positive/production/signed-spectrum/repeatability/source-integrity controls without floor subtraction or threshold relaxation.

**Paper action:** preserve both original FAIL and corrective-provider PASS in Figure 6 / provenance; never describe the original provider as successful.

**Status:** addressed.

---

## R6. “A one-parameter family producing several response modes is just bad parameter sampling; do not infer new degrees of freedom.”

**Risk:** MEDIUM.

**Agreement:** DSIR-I explicitly does **not** infer new microscopic degrees of freedom from linear span/SVD modes.

**Evidence:** finite-amplitude normalized response directions turn by about `7.18 deg` for GDM viscosity and `12.14 deg` for designer-f(R), while other one-parameter rays remain nearly straight.

**Formal guard:** keep distinct `N_micro`, `N_manifold`, `N_repr`, `N_disc`.

**Status:** addressed.

---

## R7. “WDM is being compared unfairly because it lives at high k while the other families use low k.”

**Risk:** HIGH.

**Agreement:** direct zero-padded global comparison would be invalid.

**Method:** WDM is a separate high-k block; missing low/high-domain cells are masked, never zero-imputed. The paper uses WDM to demonstrate a qualitatively distinct mechanism: strong high-k transfer with almost no `k x z` interaction on its own frozen linear high-k domain.

**Boundary:** cross-family `chi_I` values from different k-domains are not presented as one common metric ranking.

**Status:** addressed.

---

## R8. “The withheld tests are not genuinely independent.”

**Risk:** HIGH.

**Classification:**

- Exp050B WDM masses are **withheld interpolation within an already represented family**.
- Exp053A DCDM is a **withheld mechanism** for a prospectively defined temporal-localization direction, but does not close G8 because no prior universal G7 law existed.
- Exp054C/F27 is the strongest prospective falsification: the C3/C5 positive centroid-slope interval was frozen before the withheld IDM-DR result, and all four slopes came out opposite-sign.

**Guard:** IDM-DR/C7 is not reused as “fresh withheld” for a law selected after observing F27.

**Status:** addressed.

---

## R9. “Your known-sector control could show that the entire geometry is generic and therefore uninformative.”

**Risk:** MEDIUM-HIGH.

**Evidence:** post-unblinding Exp071D shows an ordinary baryon-fraction path can itself look almost one-dimensional in matter response (`PC1~0.99904`) while strongly backtracking/turning (`~169.69 deg`).

**Interpretation:** this is a useful negative specificity control. It rules out matter-space simplicity as a dark-sector identity statistic, but it does not erase the demonstrated channel-dependent response differences. Instead it motivates multi-channel discrimination.

**Boundary:** Exp071D is retrospective descriptive evidence only and creates no prospective specificity threshold.

**Status:** addressed.

---

## R10. “`A_B=Q_BW_BK_B` is formal linear algebra. Where is the physical content?”

**Risk:** HIGH.

**Answer:** correct—the formula alone is not new physics. Its value in DSIR-I is as the explicit definition of what model equivalence means after a specified measurement operator and nuisance quotient. The physical/numerical content is in the examples where the equivalence relation changes with retained channels and in the fail-closed tests determining whether a proposed realized `K_B` is even admissible.

**Paper action:** never call the quotient theorem a physical law. Pair the formal section immediately with empirical channel-degeneracy and support-eligibility results.

**Status:** addressed.

---

## R11. “Why not simply compute the survey likelihood/covariance distance and let the data downweight unsupported scales?”

**Risk:** VERY HIGH; this is likely the central referee challenge to the late observation-route section.

**DSIR answer:** covariance weighting cannot repair undefined or physically unjustified theory support. The support/domain question is logically prior to statistical weighting. Exp072A gives `0/26` eligible ACTxunWISE coordinates on the current certified C3/C5 domain; the geometry that would recover 15 coordinates is nonperturbative under the tested linear route (Exp073A).

**Formal rule:** support restriction acts on both `K_B` and `C_B` before whitening.

**Boundary:** the paper does not quote a survey-level C3/C5 distance from an ineligible route.

**Status:** addressed.

---

## R12. “The 5% support threshold is arbitrary.”

**Risk:** MEDIUM-HIGH.

**Valid criticism:** any finite support threshold is a convention/analysis contract, not a law of nature.

**Defense:** the scientific point is not that 5% is universally correct; it is that the threshold was frozen before reading downstream covariance/nuisance/model-distance output and was not relaxed after failure. Exp072A/B/C and Exp073N/O preserve the same future physical-support criterion through route changes.

**Paper action:** describe 5% as a preregistered eligibility contract and report sensitivity only through prospectively defined alternatives if added later.

**Status:** addressed in claim boundary; possible supplement sensitivity study only if prospectively specified.

---

## R13. “Your support fraction itself may be ill-defined for oscillatory kernels.”

**Risk:** HIGH.

**Evidence:** DSIR found exactly this issue instead of hiding it. Exp073L extends the frozen absolute-response ladder and classifies all 8 Wm and all 8 WW components as nonnormalizable. Local exponents remain near `p~1.5`, with stable order-unity dyadic-shell contributions `~0.645--0.651`; half-step numerical discrepancy is `~1.94e-6` vs `0.005` tolerance.

**Policy:** no retrospective high-ell cutoff or fiducial-power weighting is introduced merely to obtain a finite denominator.

**Constructive result:** finite-positive harmonic operators can be selected by construction, motivating the later DES/BOSS route.

**Status:** addressed.

---

## R14. “If DES Y3 galaxy–galaxy lensing is published, why call the route non-reproducible?”

**Risk:** HIGH and subtle.

**Distinction:** published existence of an observable/operator class is not the same as exact reproducibility of the specific frozen real-data realization required for a support calculation.

**Evidence:** Exp073M identifies the candidate class. Exp073N reproduces the frozen repository but fails the mandatory exact-realization provenance gate because the pinned public source does not provide the required real-data Y3 GGL configuration/workspace path. No support statistic is evaluated.

**Constructive response:** Exp073O prospectively selects a public Cosmotheka DES Y1 redMaGiC×Metacal pseudo-`C_ell` replacement while keeping the future 5% support threshold and minimum retained dimension unchanged.

**Boundary:** Exp073N is a provenance FAIL, not a physical-support FAIL.

**Status:** addressed and should be emphasized in supplement, not overexpanded in main text.

---

## R15. “The DES replacement chain looks like cherry-picking after failure.”

**Risk:** HIGH.

**Defense:** the failed parent is retained; the replacement is selected under a separately frozen O1--O8 contract; downstream covariance/nuisance/relation/G8 quantities remain unread; the future physical-support rectangle/threshold/minimum dimension are not changed.

Subsequent Exp073P2/S0/R0 close exact input identity, mask/`n(z)` reproduction, and raw-row/HEALPix equivalence in order. R0 explicitly records `science_gate_scored=false`.

**Boundary:** a replacement route can be prospectively selected after a provenance failure, but it cannot inherit a PASS from the failed parent and cannot change the physical gate to suit itself.

**Status:** addressed.

---

## R16. “Why include infrastructure failures? They are not science.”

**Risk:** LOW-MEDIUM.

**Agreement:** infrastructure-incomplete runs are not physical results.

**Reason to retain:** they establish that retry/hardening did not alter frozen scientific criteria. This is provenance, not evidence for or against physics.

**Paper action:** main text should mention only when needed to explain chronology; detailed INCOMPLETE records belong in repository/supplement.

**Status:** addressed by status semantics in `OBSERVATION_ROUTE_LEDGER.md`.

---

## R17. “The article is becoming two papers: response geometry plus a survey reproducibility project.”

**Risk:** VERY HIGH editorial risk.

**Assessment:** this is currently the most important scope-control issue.

**Recommended structure:**

- Main scientific center: response geometry, channel-conditional equivalence, nonseparability, curvature, mechanism diversity and prospective falsification.
- Main observation-route result: one concise section demonstrating why a formal quotient cannot be evaluated before admissibility.
- Supplement: detailed Exp073M/N/O/P2/S0/R0 ladder and status table.

The late route is relevant because it operationalizes the formal equivalence definition, but it should not dominate the main narrative unless a future physical-support result materially changes the paper.

**Status:** active editorial constraint.

---

## R18. “The article makes too many claims for one paper.”

**Risk:** HIGH.

**Mitigation:** the manuscript claim ledger explicitly distinguishes allowed statements from prohibited overclaims. The conclusion should stay at five high-level findings and avoid promoting every validation result to a headline discovery.

**Paper action:** detailed provider and operator histories live in Figures 6–7 / supplement; Abstract should contain only results needed to support the central thesis.

**Status:** active editorial polishing item.

---

## R19. “Where is the final observational detection significance?”

**Risk:** EXPECTED, not fatal.

**Answer:** DSIR-I is a methods/phenomenology/identifiability paper. It explicitly shows that the current attempted route is not yet authorized for the full survey quotient and refuses to manufacture one. A valid support PASS could enable a later covariance/nuisance result, but publication of DSIR-I must not be conditional on obtaining a favorable distance.

**Paper action:** target JCAP first under this scope; consider PRD if the formal/admissibility contribution becomes sufficiently dominant.

**Status:** accepted limitation.

---

## R20. “What observation would falsify the broader DSIR program?”

**Risk:** MEDIUM.

**Answer:** DSIR as a bookkeeping/quotient framework is not a physical theory to falsify in one observation. Its empirical generalizations are falsifiable. F27 already demonstrates this: a proposed common raw-response centroid law was frozen and failed on a withheld mechanism. Future universal residual claims must be frozen before a fresh withheld-family test; G7/G8/G9 remain OPEN.

**Paper action:** distinguish framework validity from falsifiable empirical relations constructed within it.

**Status:** addressed.

---

# Pre-submission referee gate

Before submission, all of the following must be true:

- every Abstract/Conclusion number maps to a provenance row;
- no theory-response angle is described as survey significance;
- no masked channel is zero-imputed;
- every PASS/FAIL/INCOMPLETE/PRE-RESULT status is used consistently;
- Exp073N remains a provenance FAIL after Exp073O replacement;
- Exp073R0 remains a reproduction prerequisite PASS, not a support PASS;
- any future Exp073R1 or Exp073P result enters the article only after a completed frozen output and a deliberate scope decision;
- `G7=OPEN`, `G8=OPEN`, `G9=OPEN` unless prospectively and independently closed;
- literature search is refreshed immediately before submission;
- the observation-route chronology is pushed to supplement if it begins to obscure the central response-geometry argument.
