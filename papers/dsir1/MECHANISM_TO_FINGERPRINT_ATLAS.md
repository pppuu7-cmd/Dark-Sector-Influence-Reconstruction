# DSIR-I mechanism-to-response atlas — evidence-graded causal map v0.2

**Date:** 2026-08-27  
**Scope:** Paper I synthesis of already-frozen DSIR theory-response evidence.  
**Historical path note:** the filename retains the earlier `FINGERPRINT` wording for provenance, but v0.2 deliberately uses **mechanism-to-response map** because dark-energy “fingerprinting” is explicit prior art (see the N1B novelty audit).  
**Gate effect:** none. This document does not close G7/G8/G9 and does not convert a mechanism cue into a universal physical law.

## 1. Question

Can the known microphysical/effective structure of a dark-sector mechanism be mapped to the *type* of response geometry that DSIR should inspect before any survey-level inference?

The useful direction is

`mechanism -> equation structure -> characteristic scale/time -> response block -> response geometry`,

not `model name -> one global parameter distance`.

This map is intentionally **many-to-many**. The same equation structure may occur in known-sector physics, and one mechanism may activate several response blocks. Therefore a response pattern is a diagnostic/search prior, not an identity theorem. The general idea that dark-sector perturbation properties map to observable “fingerprints” predates DSIR; Paper I claims only the specific evidence-graded cross-mechanism response geometry and validation architecture documented here.

## 2. Evidence grades

- **HARD-ATLAS:** supported by frozen DSIR calculations/controls on the stated domain.
- **WITHHELD:** supported by a prospectively withheld/interpolation or withheld-mechanism test, with the exact scope stated.
- **DESCRIPTIVE:** observed after inspection; useful for organization but not a prospective rule.
- **STRUCTURAL:** follows from the form/definition of the equations or response operator, but is not by itself a dark-sector-specific empirical result.
- **HYPOTHESIS:** candidate cross-mechanism rule requiring a future prospective test; must not be promoted in Paper I.

## 3. Mechanism -> equation structure -> DSIR response pattern

| Mechanism / control | Equation-level structure or physical scale | A priori block to inspect | Frozen DSIR response pattern | Evidence grade and boundary |
|---|---|---|---|---|
| C1 smooth non-phantom DE | altered homogeneous equation of state and expansion history; no new small-scale propagation scale in the frozen smooth setup | background/AP, time-dependent growth | background active; weak low-k irreducible scale-time component; finite-amplitude path nearly straight | **HARD-ATLAS** on frozen C1 rays; not a theorem for all scalar-field DE |
| C2 IDE | component continuity equations contain exchange/source terms while total conservation is maintained | background/growth, temporal and sign structure | exchange-active response; tested low-k rays are extremely close to scale-time separable (`chi_I` near the numerical morphology floor) | **HARD-ATLAS** for tested IDE directions; exchange does not imply universal near-separability |
| C3 GDM pressure `c_s^2` | pressure-gradient / effective propagation term introduces scale-sensitive clustering response | low-k matter + time evolution | perturbation-active with frozen background/AP null; moderate irreducible `k x z` interaction | **HARD-ATLAS** for frozen linear C3 definition |
| C3 GDM viscosity `c_v^2` | anisotropic-stress/shear closure modifies metric-potential relation in addition to matter clustering | matter + Weyl/slip | pressure and viscosity are nearly collinear in matter (`~0.3226 deg`) but strongly separated in metric slip (`~137.94 deg`); viscosity ray bends at finite amplitude | **HARD-ATLAS**; theory-response angles, not survey significance; qualitative viscosity-channel discrimination has prior art |
| C4 thermal WDM | collisionless free streaming introduces a characteristic high-k cutoff scale | high-k transfer and its redshift drift | strong high-k suppression but almost time-separable shape (`chi_I ~ 2e-10` on its own high-k block); `k_0.1` moves monotonically with withheld mass | **HARD-ATLAS + WITHHELD interpolation**; do not compare its `chi_I` numerically to low-k families as one common-domain rank |
| C5 designer `f(R)` | extra scalar / Compton-like transition modifies scale- and time-dependent metric response while frozen background matches LCDM | low-k matter, Weyl/slip, temporal evolution | strongest low-k `k x z` interaction in the current atlas; visibly curved finite-amplitude response trajectory; exact GR boundary exists in the pinned theory | **HARD-ATLAS** for certified theory-response products; direct survey-level detectability remains outside Paper I |
| C6 DCDM -> dark radiation | finite decay lifetime introduces an epoch/source scale and transfers energy between components | temporal localization, matter response, possible sign structure | response centroid moves with `Gamma/H0`; descriptive scale-sign pivot appears on sampled ray | **WITHHELD mechanism** for temporal-localization direction; pivot remains **DESCRIPTIVE** |
| C7 IDM-DR | interaction with dark radiation introduces drag/interaction dynamics with a distinct scale/time response | scale/time localization | the C3/C5-calibrated positive common centroid-slope rule fails: all frozen withheld slopes have opposite sign | **WITHHELD prospective FAIL**; this failure forbids promoting a one-scalar universal transition law |
| K2 baryon-fraction known-sector control | ordinary baryonic transfer changes the matter spectrum without dark-sector novelty | matter-response geometry | path can be almost one-dimensional (`PC1~0.99904`) yet strongly backtrack/turn (`~169.69 deg`) | **DESCRIPTIVE known-sector control**; proves low-dimensional matter geometry is not dark-specific |

## 4. What is structurally predictable before solving the full model?

### 4.1 Exact/near background null is informative but not unique

If a frozen family is constructed to share the reference homogeneous expansion, the DSIR background/AP coordinate is structurally null under the same background convention. A nonzero perturbation response can nevertheless remain. Thus

`background-null + structure-active`

is a useful mechanism class, but not a unique signature of modified gravity: C3 and C5 already provide distinct examples.

### 4.2 A finite physical scale tells us *where to look*, not what theory caused it

Pressure support, free streaming and Compton-like dynamics each introduce a characteristic scale. They therefore motivate scale-localization coordinates. The atlas supports the weaker rule

`finite dynamical scale -> inspect localized scale-response structure`,

but **not** the stronger rule

`localized scale feature -> unique dark-sector mechanism`.

Known-sector transfer physics and multiple dark mechanisms can produce scale features.

### 4.3 Time evolution of a feature permits nonseparability but does not guarantee a large `chi_I`

A moving characteristic scale can generate an irreducible `I(k,z)` component because the shape at one redshift cannot in general be obtained by adding independent scale-only and time-only terms. However the WDM high-k block is an explicit warning: a strong moving/cutoff feature can remain almost time-separable over a finite tested window.

Therefore the statement

`d k_*/d z != 0  =>  large chi_I`

is **not** an allowed DSIR-I law.

The safer Paper-I hypothesis is only:

> mechanism-dependent motion of characteristic response features is a useful coordinate family for organizing scale/time morphology.

### 4.4 Anisotropic stress / metric closure makes an independent metric channel high-value

When two mechanisms are nearly degenerate in matter clustering but differ in anisotropic stress or in the metric closure, a slip/Weyl-sensitive block can split the equivalence class. C3 pressure/viscosity is the flagship frozen DSIR example.

The qualitative principle is not claimed as new: dark-kinetics and dark-energy viscosity literature already maps anisotropic stress to additional observable information. DSIR-I contributes a frozen quantitative channel-conditional response example and embeds it in the same cross-family/provenance framework.

This does not mean `Phi != Psi` is dark-specific or a violation of the equivalence principle. The claim is about **channel information**, not a fundamental-principle violation.

### 4.5 Exchange or lifetime scales motivate temporal/sign diagnostics, not a universal temporal law

IDE and DCDM both contain source/exchange structure, but their frozen morphology is not captured by one universal scalar rule. C7/IDM-DR prospectively falsifies an attempted cross-family positive centroid-slope law. Paper I should therefore present temporal centroids, sign pivots and channel migration as a *basis of diagnostics*, not as one conserved dark-sector coordinate.

## 5. Minimal evidence-backed mechanism grammar

The strongest current Paper-I grammar is:

1. **background activation** — does the mechanism change homogeneous expansion?
2. **scale localization** — is there a finite propagation/free-streaming/interaction/Compton-like scale?
3. **temporal localization** — is there a finite epoch/lifetime or evolving transition?
4. **metric closure / slip** — can matter-response lookalikes differ in the potentials?
5. **scale-time nonseparability** — does response shape evolve in a way not representable by `mu+T(k)+tau(z)`?
6. **trajectory curvature** — does a one-parameter physical ray rotate in normalized response space?
7. **sign structure** — are there zero crossings/pivots that survive a frozen response definition?
8. **domain localization** — is the mechanism visible only on a restricted k/z block?

These are response **types**, not eight fundamental parameters.

## 6. Paper-I claim that this table supports

Draft-safe statement:

> Building on prior dark-kinetics and perturbation-fingerprinting work, the tested DSIR families occupy different combinations of background activation/nulls, scale and temporal localization, metric sensitivity, scale-time nonseparability, sign structure and trajectory curvature. This mapping is many-to-many and is used as an evidence-graded response atlas rather than as a unique classifier or universal dark-sector law.

Forbidden upgrades:

- “DSIR invented dark-sector fingerprinting”;
- “periodic table of fundamental dark-sector particles”;
- “one-to-one inversion from response pattern to microphysics”;
- “proof that a new physical scale implies modified gravity/dark matter”;
- “large `chi_I` is a dark-sector detector”;
- “metric slip proves equivalence-principle violation”;
- “the atlas closes G7/G8/G9”.

## 7. Falsifiable next steps by paper boundary

### Paper I

Close only the **descriptive/structural atlas**. A final Paper-I audit should verify that every row above resolves to a frozen experiment or an explicitly structural statement and that known-sector non-uniqueness and the historical fingerprinting prior are visible in the main text.

### Paper II

Test whether flagship theory-space channel splitting survives an independently validated physical `P_mm/P_Wm/P_WW` realization on a common preregistered support mask. The signed Wm semantics and physical-support gate remain prior to covariance.

### Paper III / later discovery stage

Only after support, covariance, nuisance quotient and a frozen G7 relation may a fresh withheld family test whether any mechanism-to-response relation has predictive cross-family content beyond known-sector controls.

## 8. Current scientific verdict

`PASS_PAPER1_MECHANISM_TO_RESPONSE_SYNTHESIS_V0_2`

This PASS means the **table is internally consistent with the existing frozen DSIR-I evidence, prior-art boundary and claim contract**. It is a synthesis/reproducibility PASS, not an empirical discovery gate and not a substitute for a fresh withheld-family test.
