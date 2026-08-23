# DSIR RECOVERY MANUAL — chat-independent research backup

**Project:** Dark-Sector Influence Reconstruction (DSIR)  
**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`  
**Snapshot date:** 2026-08-24  
**Purpose:** allow a new researcher or a new ChatGPT conversation to recover the project, its mathematics, assumptions, negative results, gates, and the exact next research steps without access to the original chat.

> READ THIS FILE FIRST AFTER ANY CHAT/SESSION LOSS. Then read `docs/GATES.md`, `docs/STATUS.md`, `docs/RESEARCH_LOG.md`, `docs/PROVENANCE.md`, and the numbered scripts in `experiments/`.

---

## 0. Hard project boundary

DSIR is an independent project. **Do not edit, import, overwrite, or use the RTK repository as a prior.** A mature external model (including RTK, if/when mature) may later be embedded into DSIR only as an ordinary candidate theory subject to the same gates as every other model.

DSIR is currently a **reconstruction/meta-inference framework**, not a fundamental theory. No discovery claim is allowed before gate G8 (withheld/external prediction).

---

## 1. Core scientific question

The starting question is not “what is dark matter?” or “what is dark energy?”. It is:

> **What is the minimal observable influence structure that must exist to reproduce all empirically required dark-sector effects, and are there robust mathematical relations between those effects?**

The intended direction is inverse:

`data -> response functions -> cross-channel relations -> candidate dynamics -> candidate action/theory`

rather than the usual:

`assumed theory -> parameters -> predictions -> data`.

The key philosophical rule is that **DM, DE, modified gravity, interacting sectors, unified fluids, etc. are theory-layer labels**, not primary objects of the reconstruction.

---

## 2. Three-layer architecture

### Layer A — Data
Likelihood-level observables, covariances, calibrations, nuisance parameters, window functions, selection effects, and systematics.

Examples:

- BAO: `D_M/r_d`, `D_H/r_d`, `D_V/r_d`;
- RSD/ShapeFit: geometry + growth + shape compressed vectors;
- CMB spectra and lensing;
- weak lensing;
- cluster/halo/galaxy observables;
- GW propagation/standard sirens;
- local/fifth-force/equivalence-principle constraints.

### Layer B — Response (primary law-discovery layer)
Gauge-/frame-robust quantities that express **what the invisible sector does**:

- background expansion `E(z)=H(z)/H0`;
- Alcock–Paczynski response;
- growth `D(a)`, `f=d ln D/d ln a`, `f sigma8`;
- matter power response `P(k,z)`;
- gravitational responses `mu(k,a)`, `eta(k,a)`, `Sigma(k,a)`;
- Weyl/lensing potential;
- tensor propagation response;
- nonlinear/halo/screening response;
- possible nongravitational couplings.

### Layer C — Theory
Interpretations/embeddings: LambdaCDM, wCDM/quintessence, interacting DM-DE/vacuum, generalized dark matter (GDM), unified fluids, WDM, modified gravity, EFT/PPF, microphysical actions, etc.

**Law discovery is performed primarily in Layer B.** Layer C is used to map theory manifolds into common response space and to identify intersections/degeneracies.

---

## 3. Effective residual source X_{mu nu}

A useful theory-layer bookkeeping object is

`X_{mu nu} = M0^2 G_{mu nu} - T^{known}_{mu nu}`.

It collects whatever is required beyond explicitly modeled known matter/radiation. It can represent DM+DE stress-energy, effective modified-gravity terms, or a mixture.

Important caveat: `X_{mu nu}` is **not** the unique fundamental observable because its form depends on what is assigned to `T_known`, on the normalization `M0`, and at perturbation level on gauge/frame choices. Therefore the project architecture is

`data -> gauge/frame robust response space -> X_{mu nu}/EFT/GDM/theory interpretation`,

not the reverse.

For a homogeneous FLRW background, after choosing the bookkeeping split,

`rho_X = 3 M0^2 (H^2 + K/a^2) - rho_known`,

`p_X = -M0^2 (2 Hdot + 3 H^2 + K/a^2) - p_known`,

and, where meaningful,

`w_X = p_X/rho_X`.

At scalar perturbation level one may write the residual stress response schematically as

`delta X -> {delta rho_X, q_X, delta p_X, pi_X}`,

but law-search variables must first be converted to a gauge/frame-robust response basis.

---

## 4. Main observable response quantities

### 4.1 Background

For spatially flat constant-w cosmology used as a control:

`E^2(a) = Omega_m a^(-3) + (1-Omega_m) a^[-3(1+w)]`.

LambdaCDM is the special case `w=-1`:

`E^2(a) = Omega_m a^(-3) + 1-Omega_m`.

These formulas are controls, not assumptions imposed on the final DSIR reconstruction.

### 4.2 Linear growth

For subhorizon matter growth in a simple quasi-static control,

`D'' + [2 + d ln H/d ln a] D' - (3/2) Omega_m(a) mu(a,k) D = 0`,

where primes here mean derivatives with respect to `ln a`.

`mu=1` gives the GR control. The logarithmic growth rate is

`f = d ln D / d ln a`.

**Normalization warning discovered in Experiment 007:** do not normalize `D(a=1)=1` independently in every model when comparing power amplitudes at fixed primordial amplitude `A_s`. Doing so erases real late-time growth differences. Use common initial conditions and compare the unnormalized growth histories; only use independently normalized `D` for shape-only diagnostics where explicitly intended.

### 4.3 Modified-gravity response basis

The quasi-static control uses

`k^2 Psi = -4 pi G a^2 mu(k,a) rho Delta`,

`eta(k,a) = Phi/Psi`,

and the lensing/Weyl combination

`Sigma(k,a) = mu(k,a) [1+eta(k,a)]/2`.

The frozen BZ-like f(R) control in the repository is designed so that its GR limit is recovered at small `q`, while at large `q` it tends toward a scalar-tensor-like `mu -> 4/3`, `eta -> 1/2`. In this particular control `Sigma=1` identically. **This identity is a known construction identity and must be quotiented out; it is not a discovery.**

### 4.4 Thermal WDM control

Thermal WDM is used as a scale-dependent suppression control. Its key DSIR role is that, to first control accuracy, it can be background-degenerate with CDM+Lambda while producing a negative scale-dependent suppression of `P(k)` on small scales.

### 4.5 Generalized Dark Matter (GDM)

The selected external implementation is `s-ilic/gdm_class_public`. Its closure language exposes three independent time-dependent functions:

`w_gdm(a)`, `c_s^2(a)`, `c_vis^2(a)`.

The strict CDM regression limit is

`w_gdm = 0`, `c_s^2 = 0`, `c_vis^2 = 0`.

This limit must reproduce the CDM reference within solver numerical tolerance before any nonzero GDM parameter is admitted to DSIR G3B.

### 4.6 Interacting-vacuum control

Use a clearly specified interaction four-vector; never use an undefined scalar `Q` alone at perturbation level. The current planned clean control is a geodesic interacting-vacuum realization with

`Q_c^mu = Q u_c^mu`,

so there is no momentum transfer in the CDM rest frame. The no-interaction regression limit is

`Q -> 0` (or the implementation coupling parameter `xi -> 0`) -> LambdaCDM.

The exact code-level sign convention must be read from the pinned external solver before comparing positive/negative `xi`.

---

## 5. Background degeneracies already established

### 5.1 Interacting vacuum versus wCDM background

For the control convention

`d rho_c/d ln a + 3 rho_c = xi rho_de`,

`d rho_de/d ln a = -xi rho_de`,

we get

`rho_de(a) = rho_de0 a^(-xi)`.

Integrating the CDM equation gives a background of the form

`E^2(a) = A a^(-3) + (1-A) a^(-xi)`

for an effective coefficient `A` fixed by present densities/coupling convention. This is exactly the same functional form as constant-w CDM with

`-3(1+w_eff) = -xi`,

therefore

`w_eff = -1 + xi/3`.

Hence a physically interacting model and a noninteracting wCDM interpretation can be **exactly background-degenerate**. DSIR must distinguish them using perturbations/velocity/momentum-transfer channels, not by `H(z)` alone.

### 5.2 Generalized Chaplygin gas intersection

The generalized Chaplygin gas has an exact parameter subspace (`alpha=0`) whose background reduces to a matter + constant-vacuum form. Numerically the repository found machine-level agreement with the corresponding Lambda+matter background. This is another example that model families form **intersecting response manifolds**, not disjoint boxes.

### 5.3 Consequence

The correct object is not

`model name -> one class`,

but

`theory family -> manifold M_i in response space`.

Different manifolds may intersect:

`M_i ∩ M_j != empty`.

DSIR therefore constructs a **discriminant graph**: for each unresolved intersection, identify the minimal additional observable channel required to separate the physical interpretations.

---

## 6. DESI DR2 BAO / AP reconstruction (G6A)

The stored DESI DR2 compressed BAO product contains 13 entries of `D_V/r_d`, `D_M/r_d`, and `D_H/r_d` with a 13x13 covariance.

For bins where both transverse and radial distances are available define the sound-horizon-free Alcock–Paczynski response

`F_AP(z) = (D_M/r_d)/(D_H/r_d) = D_M/D_H`.

In a flat FLRW geometry,

`D_M(z) = (c/H0) integral_0^z du/E(u)`,

`D_H(z) = c/[H0 E(z)]`.

Therefore

`F_AP(z) = E(z) integral_0^z du/E(u)`.

Let

`I(z) = integral_0^z du/E(u)`.

Then `F=E I` and `I'=1/E`. Because `E=F/I`,

`I'/I = 1/F`.

Integrating between `z1` and `z2` gives

`ln[I(z2)/I(z1)] = integral_z1^z2 dz/F(z)`.

Using `E=F/I`,

`E(z2)/E(z1) = [F(z2)/F(z1)] exp[- integral_z1^z2 dz/F(z)]`.

Thus **both `H0` and `r_d` cancel**. This is a calibration-independent relative expansion reconstruction under the assumptions of flat FLRW and the chosen interpolation of `F_AP(z)`.

Repository validation: piecewise-linear interpolation was tested on several smooth wCDM controls; maximum node-level reconstruction error was about `0.795%`, below the statistical uncertainty of the first DESI test. This is a geometric identity/control, not a new law.

Representative reconstructed results already obtained include approximately

`E(0.934)/E(0.510) = 1.219 (+0.037,-0.036)`,

`E(2.33)/E(0.510) = 2.525 (+0.093,-0.089)`.

---

## 7. Real multi-channel DESI DR1 response (G6B)

The first real geometry+growth+shape response uses the **corrected 2026 erratum** values for DESI DR1 ShapeFit. The originally published Appendix-A `f sigma_s8` values/covariances contained a numerical error. Old values are forbidden by provenance/regression checks.

Across five informative redshift bins, the measured correlation between AP geometry and the growth response is approximately

`rho(AP,g) = (-0.551, -0.542, -0.527, -0.554, -0.627)`

with simple mean about `-0.560` and bin-to-bin scatter about `0.039`.

**Interpretation:** this is classified as an observational identifiability/measurement-degeneracy direction of the joint AP/RSD fit, not a dark-sector law.

---

## 8. Conditional innovation: removing measurement-induced correlation

Before looking for a new relation involving a target response `t` (e.g. growth), condition out nuisance/known measurement directions `N` (e.g. AP and shape). For a Gaussian residual vector `r` with block covariance,

`r_t_perp = r_t - C_tN C_NN^(-1) r_N`.

The conditional covariance is

`C_t|N = C_tt - C_tN C_NN^(-1) C_Nt`.

This is the Schur-complement conditional innovation. It removes the component of the target residual statistically predictable from the nuisance response because of their covariance.

It is **not automatically causal**.

Current aggregate innovation test gave approximately

`chi2 = 5.53 for 5 dof`, `p = 0.355`.

Therefore there is no significant residual anomaly in this first real multi-channel test; G7 remains OPEN.

---

## 9. Whitening and latent-rank methodology

Let a response vector be `x` with observational/noise covariance `C`. Define whitened coordinates

`z = C^(-1/2) (x - x_ref)`.

The theory catalog produces a matrix `Z` whose rows are whitened model-response vectors. Apply

`Z = U S V^T`.

The singular spectrum measures occupied response directions **only after whitening**.

### Failure discovered
An early criterion compared each ordered singular value to the same ordered singular value from noise. Strong low-rank spikes deform the remaining spectrum, causing a false rank of about 22 when the injected rank was 3.

### Corrected criterion
Calibrate against a **global upper noise spectral edge** (from null simulations in the same weighted/whitened geometry) and count only singular values that emerge above that bulk edge. Experiment 001 then correctly recovers injected rank 3.

### Coordinate robustness (Experiment 011)
30/30 synthetic cases with true rank 3, sample sizes 90/180/360, strong anisotropic feature rescalings and correlated linear transformations recovered rank 3 **after transforming the covariance consistently and whitening**.

Maximum singular-spectrum mismatch after whitening was about `1.6e-15` (machine precision).

Invalid unwhitened analysis returned false ranks `20–35`.

Therefore **no DSIR rank claim is valid without covariance whitening**.

---

## 10. R_obs versus R_model

Two different dimensions must never be conflated:

`R_obs` = number of independent response directions the data/response operator can actually distinguish after covariance and null-space treatment.

`R_model` = number of independent directions occupied by the viable theory manifold after projection into identifiable space.

Interpretation:

- low `R_obs` + large underlying theory complexity -> observational blindness/non-identifiability;
- `R_model << R_obs` robustly -> potentially interesting low-dimensional physical structure/unification;
- `R_model ~ R_obs` -> theories fill the available observable space;
- neither number is automatically the number of fundamental fields/particles.

---

## 11. Theory-catalog prior sensitivity (Experiment 012)

A finite catalog has an implicit prior: densely sampled/popular model families carry more weight in naive SVD.

Synthetic test: three independent true response modes were sampled with family multiplicities `900/90/10`.

Naive catalog-frequency weighting detected only

`R_model = 2`.

Equal-family weighting, **with the same weights propagated into the noise-null calibration**, recovered

`R_model = 3`.

The third/first singular-value ratio moved approximately

`0.259 -> 0.853`.

Therefore DSIR does not report a single scalar `R_model`; it must report a sensitivity profile

`R_model(pi)`

over defensible theory-family priors/stratifications/bootstrap schemes.

Equal-family weighting is a diagnostic, not uniquely correct physics.

---

## 12. Response-orientation diagnostic (Experiments 007–008)

Define the matter-power response ratio

`R_P(k,a)=P_model(k,a)/P_LCDM(k,a)`.

A coarse scale orientation can be measured by a logarithmic slope

`S_k = Delta ln R_P / Delta ln k`,

and a time orientation by

`S_a = Delta ln R_P / Delta ln a`.

The frozen controls produced approximately

- smooth wCDM (`w=-0.9`): `(S_k,S_a) ~ (0,-3.80e-2)`;
- thermal WDM 3 keV: `(S_k,S_a) ~ (-1.69e-2,0)` in the simple frozen control;
- designer/BZ-like f(R): `(S_k,S_a) ~ (+9.23e-2,+2.87e-1)`.

This is not a new law. It demonstrates a useful discriminator: two models can both be scale dependent yet have opposite scale orientation and different time evolution.

---

## 13. Quotient known identities BEFORE symbolic/law search

Symbolic regression will rediscover definitions and conservation laws unless they are removed first.

Examples of relations that must not be claimed:

- Bianchi/conservation identities;
- definitions of `f`, `Sigma`, AP variables, etc.;
- exact identities deliberately built into a control parameterization;
- shared-calibration relations;
- gauge/frame artifacts;
- covariance-induced AP/RSD correlations.

The law-search space is therefore a quotient space:

`candidate response space / known-identity subspace / measurement-degeneracy subspace`.

Only residual relations in this quotient can advance toward G7/G8.

---

## 14. Claim hierarchy

Always label a result with one of these levels:

1. **control identity** — algebraic or code-regression truth;
2. **observational identifiability pattern** — caused by covariance/operator geometry;
3. **empirical residual relation** — survives known identity and measurement quotients;
4. **predictive law candidate** — stable and predicts a withheld response;
5. **physical model candidate** — a consistent dynamics/action explains the relation and makes new predictions.

**No discovery claim before level 4 / G8.**

---

## 15. Current gates at this recovery snapshot

- **G0 PARTIAL:** LambdaCDM background/growth controls work; full common Boltzmann reference still pending.
- **G1 OPEN:** full conservation/Bianchi + gauge-invariant bookkeeping audit pending.
- **G2 IN PROGRESS:** response basis not yet completely frozen.
- **G3A PASS/PARTIAL:** six broad classes represented at background/equivalence level.
- **G3B PARTIAL:** LambdaCDM, smooth wCDM, thermal WDM, designer f(R) linear controls exist; GDM and interacting-vacuum solver regression is next.
- **G4 PASS:** corrected synthetic low-rank recovery.
- **G5 PARTIAL:** whitening robustness and theory-prior failure mode passed/identified; broader non-Gaussian/model-family stress tests remain.
- **G6A PASS:** real DESI DR2 AP/relative expansion.
- **G6B PASS:** corrected DESI DR1 geometry+growth+shape covariance integrated.
- **G7 OPEN:** no nontrivial residual law yet.
- **G8 OPEN:** no withheld prediction yet.
- **G9 OPEN:** no reconstructed fundamental dynamics/action.

Use `docs/GATES.md` as the authoritative live table; this section is a recovery snapshot.

---

## 16. Numbered experiment map

The repository intentionally uses numbered scripts as a chronological spine:

- `experiments/001_synthetic_rank.py` — injected low-rank recovery and corrected noise-edge logic.
- `experiments/002_identifiability.py` — separates observable rank from model rank/null directions.
- `experiments/003_identity_quotient.py` — known-identity removal control.
- `experiments/004_desi_dr2_bao_ingest.py` — DESI DR2 compressed BAO + covariance and AP construction.
- `experiments/005_ap_relative_expansion.py` — calibration-free relative `E(z)` reconstruction.
- `experiments/006_control_background_equivalence.py` — exact/controlled background intersections between theory families.
- `experiments/007_linear_response_controls.py` — first beyond-background controls.
- `experiments/008_response_orientation.py` — time/scale orientation diagnostic.
- `experiments/009_desi_dr1_multichannel_identifiability.py` — corrected DESI DR1 geometry+growth+shape covariance.
- `experiments/010_conditional_innovations.py` — covariance-conditioned growth innovation.
- `experiments/011_rank_whitening_robustness.py` — coordinate/covariance robustness suite.
- `experiments/012_model_catalog_prior_sensitivity.py` — implicit theory-catalog prior failure mode.

When adding new experiments, **never renumber old ones**. Add `013_...`, `014_...`, etc., and append the result to `docs/RESEARCH_LOG.md` and gate status to `docs/GATES.md`/`docs/STATUS.md`.

---

## 17. Provenance / external solver pins

### GDM
External repository: `s-ilic/gdm_class_public`.

Current recovery anchor identified during research: commit `4c87916aab5ca124a68f1dd16f31846fc13d1829` (verify whether this remains the desired frozen pin before a precision run; do not silently upgrade).

Regression requirement:

`w=cs2=cvis2=0 -> CDM`.

Then vary one closure direction at a time before allowing combined variation.

### Interacting vacuum
External implementation under evaluation: `kaeonikc/class_iv`.

Current recovery anchor identified during research: commit `ac627d54e9ce196a08878d1ba33999819925d19c` (verify implementation/sign conventions before precision use).

Regression requirement:

`coupling -> 0 -> LambdaCDM`.

A code-history entry explicitly fixed growth `D` and `f` to include baryons; provenance must therefore pin a post-fix commit.

### DESI
Never use superseded DESI DR1 ShapeFit Appendix-A growth vectors. Use the corrected erratum product preserved in the repository provenance/data layer.

---

## 18. Exact next research sequence after recovery

If resuming from this snapshot, do **not** start symbolic regression yet. Execute in this order:

### Step 1 — GDM solver regression
1. Freeze the exact GDM_CLASS commit and build/runtime environment.
2. Run matched baseline cosmology in standard CLASS and GDM_CLASS.
3. Set `w_gdm=0`, `cs2_gdm=0`, `cv2_gdm=0`.
4. Compare at minimum: `H(z)`, CMB spectra, linear `P(k,z)`, growth outputs available from the solver.
5. Define numerical tolerances before looking at nonzero GDM results.
6. Only after baseline pass, activate separately:
   - `w != 0`,
   - `cs2 != 0`,
   - `cv2 != 0`.
7. Map each change into the common response vector.

### Step 2 — Interacting-vacuum regression
1. Freeze exact `class_iv` commit and read its parameter/sign convention in source/config.
2. Run `coupling=0` against matched LambdaCDM.
3. Confirm background **and perturbation** equality within numerical tolerance.
4. Activate a small positive and negative coupling inside the implementation's stable domain.
5. Record `Delta E`, `Delta f sigma8`, `Delta P(k,z)`, potential/lensing response if available.
6. Do not compare opposite signs until the code convention is explicitly documented.

### Step 3 — G3B unified response matrix
Combine six control families in a common feature grid, with missing/unavailable channels represented as missing (not guessed). Do not fill unknown model responses with zero.

Suggested first frozen feature set:

`{E(z), F_AP(z), f sigma8(z), ln P(k,z)/P_ref(k,z), mu(k,z), eta(k,z), Sigma(k,z)}`

plus provenance flags specifying whether a quantity is directly computed, derived, or undefined for a family.

### Step 4 — observational projection
Project the theoretical response matrix through an observational covariance/operator appropriate to each channel. Whiten consistently.

### Step 5 — rank profile
Compute `R_obs` and `R_model(pi)` with null simulations and multiple defensible family priors. Record stability/instability; do not compress into one number if prior-sensitive.

### Step 6 — G7 search
Only then search for residual relations using conditional innovations/known-identity quotient. Candidate methods may include PCA/SVD, canonical correlations, mutual information, sparse/symbolic regression, but every candidate must pass invariance and holdout gates.

---

## 19. Withheld prediction policy (future G8)

A candidate relation found using channels A/B/C must predict at least one deliberately withheld channel D without refitting the law to D.

Potential holdouts:

- weak lensing/Weyl response withheld from expansion+growth fit;
- CMB lensing withheld from low-z reconstruction;
- GW luminosity-distance response withheld from scalar-sector fit;
- nonlinear/halo statistic withheld from linear-response discovery.

A relation that only interpolates the same data used to discover it is **not** a DSIR law candidate.

---

## 20. Safety rules against false discovery

1. Never infer physics from raw feature units; whiten first.
2. Never treat catalog multiplicity as a physical prior without sensitivity tests.
3. Never claim Bianchi/conservation/definition identities.
4. Never claim a covariance degeneracy as a dark-sector law.
5. Never normalize away amplitude differences before power comparisons.
6. Never invent missing response values.
7. Never mix statistically overlapping datasets as independent without joint covariance or an explicit approximation warning.
8. Never use superseded data products when an erratum exists.
9. Never change an upstream solver version silently.
10. Never declare DSIR a fundamental theory unless an effective dynamics/action with new predictions is actually reconstructed.

---

## 21. Minimum commands/checks for a new session

A new session should first inspect:

`git log --oneline --decorate -20`

`cat docs/RECOVERY_MANUAL.md`

`cat docs/GATES.md`

`cat docs/STATUS.md`

`cat docs/RESEARCH_LOG.md`

Then run the repository test suite according to `pyproject.toml` and reproduce the latest numbered experiment(s) before modifying methodology.

If a test fails after environment recreation, classify the failure first as one of:

- environment/dependency;
- data/provenance;
- numerical tolerance;
- implementation bug;
- actual scientific gate failure.

Do not change physics to make a test pass until these categories have been ruled out.

---

## 22. Short recovery summary for another ChatGPT

**Mission:** infer the minimal common observable influence structure of the dark sector and search for cross-channel laws without assuming DM/DE ontology.  
**Current scientific state:** reconstruction framework, not a theory; no discovery.  
**Strongest completed controls:** DESI DR2 calibration-free AP reconstruction; corrected DESI DR1 geometry+growth+shape covariance; synthetic rank recovery; whitening invariance; theory-catalog-prior failure mode.  
**Important negative result:** first conditional real-data growth innovation is not significant (`chi2~5.53/5`, `p~0.355`).  
**Main open task:** finish G3B by validated GDM and interacting-vacuum Boltzmann-solver embeddings.  
**Then:** construct common multi-channel response matrix -> observational projection/whitening -> `R_obs`, `R_model(pi)` -> quotient known/measurement relations -> G7 residual-law search -> G8 withheld prediction -> only then attempt G9 dynamics/action reconstruction.  
**Never touch RTK from this project.**
