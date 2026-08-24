# DSIR observational-whitening research log — 2026-08-25

This log continues `docs/RESEARCH_LOG_OBSERVATIONAL_2026-08-24.md`. Scientific claim status is controlled by `docs/GATES.md`; evolving interpretation status is mirrored in `docs/SCIENTIFIC_FINDINGS_REGISTER.md`.

## Experiment 036 — pinned-artifact AP family geometry v0.1

### Goal

Map the exact frozen C1 smooth-w and C2 interacting-vacuum full `H(z)` histories through the validated Experiment 035 AP operator and corrected DESI DR1 `D_H/D_M` marginal geometry block. Do not extrapolate the seven-node structure atlas below `z=0.295`.

### Frozen inputs

C1:

- run `32771133024`;
- artifact `9536242626`;
- digest `sha256:ece064524a3efe0bc83d19dc98cc674a9a88f405aa56e9886cdf4ebd30d8134b`.

C2:

- run `32760042765`;
- artifact `9532491954`;
- digest `sha256:408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`.

### Hard control

Finite-difference relative-L2 convergence ceiling `0.005` was frozen before target pair angles were used. No pair-angle or rank threshold was defined.

Successful hard run `32782545098`, artifact `9540273287`, SHA256 `553faa2ef7ddbc44e25ddd6faca237d0be7fc265b9c23cfafb2a32570534d126`.

Convergence (`1e-3` vs `1e-4`):

- smooth-w `0.0015563369`;
- IDE negative-alpha `0.00013881894`;
- IDE beta `2.25987e-7`.

Corrected-DESI marginal-whitened acute angles:

- smooth-w / IDE negative-alpha `72.803493 deg`;
- smooth-w / IDE beta `64.151094 deg`;
- IDE negative-alpha / beta `9.0379006 deg`, oriented `170.962099 deg`.

The same IDE alpha/beta directions are `58.9338 deg` apart in the frozen structure block.

**Interpretation:** AP geometry alone cannot identify these two IDE interaction directions; structure/growth information is complementary.

---

## Experiment 037 — GDM background/AP-zero audit v0.1

### Goal

Test the expected C3 geometry null numerically instead of zero-imputing it from the statement that `cs2/cv2` are perturbation closure parameters with `w_gdm=0`.

### Frozen provenance

- source run `32759738560`;
- artifact `9532247349`;
- digest `sha256:126c839ce948b5b25ec46b687af70e230c31d87071e6526727d1551a3c0f136d`;
- upstream `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Audited:

- `cs2={1e-8,1e-7,1e-6}`, `w=0`, `cv2=0`;
- `cv2={1e-8,1e-7,1e-6,1e-5,1e-4}`, `w=0`, `cs2=0`.

Pre-frozen hard tolerances: `1e-12` on redshift grid, relative `H`, and absolute AP log response; INI contracts required.

### Hard result

Run `32783243120`: `PASS_GDM_AP_ZERO_AUDIT_V0_1`.

For every nonzero audited point:

- redshift grid exact;
- all saved numerical background columns exactly equal to reference;
- `max_relative_H=0`;
- `Delta ln(D_H/D_M)=(0,0,0,0,0)` at the five DESI target redshifts.

Result artifact `9540510596`, SHA256 `ba1fa93e348f9685d84a675311c79f9c746574463086710b4a46911d125f4edf`.

**Hard scientific consequence:** frozen GDM `cs2/cv2` directions are background/AP-null but perturbation-active. C3 geometry may now be encoded as validated zero, not missing data.

---

## Experiment 038 — designer-f(R) background/AP-zero audit v0.1

### Goal

Test whether the frozen C5 designer-f(R) `B0` direction is genuinely background/AP-null, rather than inserting zero from the expectation `EFTwDE=0`.

### Immutable provenance

Pinned upstream:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Frozen hard-production configuration artifact:

- source run `32759477319`;
- artifact `9532245261`;
- artifact name `eftcamb-mgs1-hard-92350bb5087d17c874626c75b96779ae264dd1f6`;
- SHA256 `9e16460bc04605456383a30655cc5314597bfbb356bbc99af7eb5cfa9b7a8635`;
- hard config lineage `dsir_mgs1_hp_*`.

The pinned source maps `EFTwDE=0` to `wDE_LCDM_parametrization_1D`, whose value is exactly `w=-1` with zero derivatives.

### Infrastructure chronology before scientific execution

Several path/provenance assumptions failed before the scientific hard script was reached:

1. older `dsir_mgs1_*` names were initially used, while the immutable hard artifact uses `dsir_mgs1_hp_*`;
2. the standard `EFTflag=0` branch did not emit the EFT-specific background file through this path, so the exact designer `B0=0` point was adopted as the same-branch numerical reference while the pinned source supplies the LCDM background contract;
3. CAMB appends `_` to nonempty `output_root`, while frozen roots already end in `_`, so actual output names contain `__background.dat`.

These were infrastructure fixes only. The scientific tolerances were not changed.

### Frozen hard thresholds

Before any scientific target output:

- redshift-grid mismatch `<=1e-10`;
- relative `H` mismatch `<=1e-8`;
- relative nonzero-row `D_M` mismatch `<=1e-8`;
- absolute `Delta ln(D_H/D_M)` `<=1e-8`;
- source/config contracts required.

No angle/rank/significance threshold.

### Hard result

Run `32785800977`: `PASS_EFTCAMB_FR_AP_ZERO_AUDIT_V0_1`.

Result artifact:

- ID `9541598468`;
- SHA256 `24b7fa5951c06d4cea72e6c0bf6baad2d2174f2d86794ec0818cf57c309b81c8`.

For every

`B0={0,1e-7,1e-6,1e-5,1e-4,1e-3}`:

- redshift-grid mismatch `0`;
- `max_relative_H=0`;
- `max_relative_DM_nonzero_rows=0`;
- `max_abs Delta ln(D_H/D_M)=0`;
- all saved numerical background columns exactly equal to designer `B0=0` at saved solver precision.

The result is therefore an exact saved-solver zero, stronger than merely passing the `1e-8` tolerance.

**Hard scientific consequence:** the frozen designer-f(R) B0 direction is background/AP-null on its source-proven LCDM expansion branch while its structure response is nonzero.

### Cross-family implication

Experiments 037 and 038 hard-reproduce the same response-space topology in two qualitatively different classes:

\[
K_{AP}t=0,\qquad K_{perturbation}t\neq0,
\]

for GDM closure physics and designer modified gravity respectively.

This supports **block-sparse influence trajectories**, but not a universal law: both frozen families deliberately hold their background sectors fixed.

---

## Experiment 039 — ShapeFit growth/RSD operator contract

### Correct quantity

The corrected ShapeFit growth coordinate is `f_sigma_s8`, with

\[
s=r_d/r_d^{ref},\qquad R=s\,8h^{-1}{\rm Mpc}.
\]

A fixed-radius textbook `f sigma8` cannot be substituted without a bridge.

### Scale-dependent-growth representability

Define density/velocity moments at the ShapeFit smoothing scale and

\[
{\cal D}_{RSD}=1-
\frac{S_{\delta\Theta}^2}{S_{\delta\delta}S_{\Theta\Theta}}.
\]

A scalar growth amplitude is justified only if the tracer-relevant density/velocity fields are sufficiently close to the single-amplitude limit under a pre-frozen tolerance. Otherwise retain a multi-k/window-aware RSD operator.

### Negative output-quality finding

The frozen C5 H-EFTCAMB logs print `sigma8` and `sigma8^2_vd/sigma8` only to roughly four decimal places. At `B0=1e-7` this quantizes away most of the small response and creates an artificial sparse/unstable finite-difference tangent.

**Decision:** printed summary logs are rejected for small-B0 growth-tangent calibration. Use machine-readable high-precision density/velocity transfer or cross-power products.

Pinned CAMB exposes `delta_tot`, `v_newtonian_cdm`, and `v_newtonian_baryon` transfer variables, so the required bridge is feasible.

---

## Experiment 040 — finite-bin structure-growth response v0.1

### Goal

Before building tracer RSD, isolate how much model separation is carried specifically by temporal evolution of the already validated total-matter structure response.

Define for adjacent frozen early->late nodes

\[
\Delta\bar f_P(k)=
\frac{r_\Delta(k,z_{late})-r_\Delta(k,z_{early})}
{2[\ln a_{late}-\ln a_{early}]}.
\]

This is a **theory-space temporal response**, not `f_sigma_s8`.

### Hard controls

Frozen before pairwise interpretation:

- endpoint reconstruction `<=1e-12`;
- constant-mode annihilation `<=1e-14`;
- linearity `<=1e-12`;
- finite/nonzero direction outputs;
- no pairwise angle threshold.

Hard run `32785987735`: `PASS_FINITE_BIN_GROWTH_RESPONSE_V0_1`.

- endpoint error `1.1102230246251565e-16`;
- constant residual `0`;
- linearity residual `9.769962616701378e-15`.

Artifact `9541462864`, SHA256 `0457823510fead4ff56e8e29843e39de47805f8fbfda86f4d9d33585be556ac9`.

### Key pairwise comparisons

#### IDE alpha/beta ladder

- AP `9.0379006 deg` acute;
- finite-bin growth `29.3978236 deg`;
- full frozen structure `58.9337977 deg`.

Temporal information restores part of the mechanism distinction lost by AP, but the complete structure history contains more.

#### Smooth-w / IDE-alpha reversal

- AP `72.803493 deg`;
- full structure `52.194293 deg`;
- temporal growth `10.310585 deg`.

The temporal operator makes this pair nearly degenerate even though AP separates it strongly.

#### IDE-alpha / GDM enhancement

Full structure about `24.8-24.9 deg` -> temporal growth about `60.9 deg`.

#### GDM cs2/cv2 persists

`0.322616 deg` full low-k structure -> `1.334013 deg` temporal growth. Time helps weakly but does not replace metric slip.

#### GDM / designer-f(R)

- leading scale-only modes `0.078-0.102 deg`;
- finite-bin growth `16.05-17.28 deg`;
- full structure `25.18-25.49 deg`.

Time is a genuine separator relative to scale-only shape, but full `(k,z)` structure is more informative than growth-only compression.

### New hard interpretation

**Pairwise degeneracies migrate between response operators.** Adding a new channel can separate one model pair while collapsing another; distinguishability is not monotonically improved by choosing one supposedly optimal scalar observable. Joint multi-channel geometry is the relevant object.

---

## Gate consequences and continuation

Experiments 038/040 do **not** close G5. Geometry is now substantially controlled across C0/C1/C2/C3/C5, but observation-space growth and survey/window-aware shape remain incomplete. C4 WDM remains a deliberately separate small-scale block.

G7 and G8 remain OPEN.

Immediate continuation:

1. preserve high-precision C5 transfer outputs from pinned H-EFTCAMB hard configs;
2. define the total-matter/tracer velocity convention and build numerical `S_dd`, `S_dTheta`, `S_ThetaTheta`;
3. create matched transfer-output runs for C3 GDM and C2 IDE under consistent gauge semantics;
4. freeze and run the numerical `D_RSD` representability gate;
5. replace/calibrate the finite-node `m+n` proxy with survey/window-aware shape forward modelling;
6. only then form the full corrected ShapeFit whitening block and perform rank/prior/channel-removal stress tests;
7. continue slip/lensing and WDM high-k observational blocks in parallel;
8. no residual-law claim before stable observation-space geometry; no discovery before G8.
