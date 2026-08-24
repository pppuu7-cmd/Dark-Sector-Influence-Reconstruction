# DSIR Novelty Gate N0 — prior-art and non-duplication audit

**Audit date:** 2026-08-24  
**Status:** **PASS-PROVISIONAL for non-duplication; NOT a proof of global novelty**  
**Scope:** conceptual/methodological prior art for DSIR as a reconstruction/meta-inference framework. This gate does not claim a new physical law or new fundamental theory.

## 1. Why this gate exists

DSIR deliberately combines ideas from several mature literatures. The scientific risk is not only false discovery in the data; it is also accidentally presenting an established formalism as new. N0 therefore separates:

1. ingredients already established in the literature;
2. combinations that are close competitors;
3. DSIR-specific integration choices for which no exact prior implementation was identified in this audit;
4. claims that are prohibited until stronger novelty and prediction gates pass.

A PASS at N0 means only: **the searched literature did not reveal an exact duplicate of the complete DSIR pipeline**. It does not prove that no such paper exists, and it is not a patent-style exhaustive search.

---

## 2. DSIR novelty axes used in the comparison

To avoid comparing titles or terminology, prior work is scored against explicit architectural axes.

- **A — effective residual/source:** represent unknown gravity/dark-sector influence by an effective stress tensor or equivalent residual, e.g. `X_{mu nu}=M0^2 G_{mu nu}-T_known`.
- **B — theory dictionary/common language:** map many theories into shared perturbation/response variables.
- **C — heterogeneous dark-sector coverage:** include, in one atlas, dark matter microphysics/fluids, dark energy, interactions, and modified gravity rather than only one sub-class.
- **D — response-to-reference representation:** describe new physics by changes/ratios/log-responses relative to a reference cosmology.
- **E — solver-lineage control:** model/reference are evaluated in the same solver, followed by an explicit cross-solver response bridge.
- **F — covariance-whitened latent dimension:** infer the number of distinguishable response directions after covariance whitening/noise calibration.
- **G — theory-family-prior sensitivity:** report `R_model(pi)` rather than one catalogue-frequency-dependent rank.
- **H — identity/measurement-degeneracy quotient:** project Bianchi identities, definitions, calibration modes, and measurement-induced degeneracy directions before law discovery.
- **I — cross-channel law discovery:** search for invariants/relations among independently reconstructed background, growth, lensing, GW, nonlinear, etc. responses.
- **J — withheld physical-channel prediction:** a candidate relation is not elevated to a discovery unless it predicts an observable channel excluded from discovery/training.
- **K — broad influence atlas:** explicitly connect background, scalar perturbations, tensor/GW, couplings, and nonlinear/halo sectors.

The potentially distinctive DSIR claim, if it survives later gates, is the **joint pipeline across these axes**, not any one ingredient by itself.

---

## 3. High-priority prior art

### 3.1 Dark degeneracy — Kunz (2007/2009)

**Martin Kunz, “The dark degeneracy: On the number and nature of dark components,” astro-ph/0702615; later PRD 80, 123001 (2009).**  
https://arxiv.org/abs/astro-ph/0702615

Established points that overlap DSIR:

- gravity measures the total energy-momentum tensor rather than a unique DM/DE decomposition;
- interacting and non-interacting descriptions can be gravitationally degenerate;
- it is preferable to parameterize observables rather than insist on a unique microscopic split.

**Overlap:** A, conceptual core of C/H.  
**Novelty consequence:** DSIR must not claim discovery of the dark degeneracy or of the idea that the observable total source is more fundamental than a DM/DE naming convention.

### 3.2 PPF effective-source equivalence — Hu & Sawicki (2007)

**Wayne Hu & Ignacy Sawicki, “A Parameterized Post-Friedmann Framework for Modified Gravity,” PRD 76, 104043 (2007).**  
https://doi.org/10.1103/PhysRevD.76.104043

The appendix explicitly defines an effective dark-energy stress tensor by moving modified-gravity effects to the right-hand side of Einstein’s equation. The paper also emphasizes the formal equivalence between modified gravity and generalized dark energy at the level of an effective stress tensor, with physical differences appearing through closure relations.

**Overlap:** A, B, part of H/K.  
**Novelty consequence:** `X_{mu nu}` is a useful DSIR organizing definition, **not** a novel mathematical construction.

### 3.3 General PPF dictionary — Baker, Ferreira & Skordis (2013)

**T. Baker, P. G. Ferreira, C. Skordis, “The Parameterized Post-Friedmann Framework for Theories of Modified Gravity: Concepts, Formalism and Examples,” PRD 87, 024015 (2013).**  
https://doi.org/10.1103/PhysRevD.87.024015

Builds a unified perturbation framework for broad classes of modified-gravity theories and maintains a direct “dictionary” between theory space and PPF variables.

**Overlap:** B, substantial part of K for MG.  
**Novelty consequence:** a theory-to-common-variable dictionary is prior art. DSIR must distinguish itself by the heterogeneous DM+DE+interaction+MG response manifold and subsequent rank/law/prediction gates.

### 3.4 Generalized Dark Matter — Hu (1998)

**Wayne Hu, “Structure Formation with Generalized Dark Matter,” ApJ 506, 485 (1998), astro-ph/9801234.**  
https://arxiv.org/abs/astro-ph/9801234

Introduces a phenomenological dark-matter stress-tensor description with equation of state, sound speed, and viscosity/anisotropic-stress information, explicitly designed to expose gravitational signatures beyond CDM.

**Overlap:** A/B/C for the dark-matter-fluid sector.  
**Novelty consequence:** the use of `(w, c_s^2, c_vis^2)` as a common dark-fluid language is prior art.

### 3.5 EFT of Dark Energy / Horndeski theory space

**N. Frusciante & L. Perenon, “Effective field theory of dark energy: A review,” Physics Reports 857 (2020) 1–63.**  
https://doi.org/10.1016/j.physrep.2020.02.004

EFT-DE provides a model-independent language for a wide class of single-field DE/MG models, background plus linear perturbations, with mappings from specific scalar-tensor theories to EFT functions and implementations in Einstein–Boltzmann codes.

**Overlap:** B, K for DE/MG; theory-space reduction.  
**Novelty consequence:** DSIR is not a replacement for EFT/PPF and must not claim that a common DE/MG parameter basis is new.

### 3.6 Theory-space compression / observable parametrization — Gleyzes (2017)

**J. Gleyzes, “Parametrizing modified gravity for cosmological surveys,” PRD 96, 063516 (2017), arXiv:1705.04714.**  
https://arxiv.org/abs/1705.04714

Explores how a complex EFT theory space can be compressed by simple parametrizations while preserving observable predictions, with stability conditions reducing viable theory space.

**Overlap:** B and a conceptual precursor to F.  
**Novelty consequence:** “compress theory space into fewer observable degrees of freedom” is not by itself new.

### 3.7 PCA built from representative modified-gravity theories — Zanoletti & Leonard (2025)

**C. M. A. Zanoletti & C. D. Leonard, “Principal Components for Model-Agnostic Modified Gravity with 3x2pt,” arXiv:2503.20951 (2025).**  
https://arxiv.org/abs/2503.20951

Constructs principal components from nonlinear matter-power features of representative gravity theories and uses the transformed space to retain information while reducing model dependence.

**Overlap:** F in an MG-specific setting; parts of B/D.  
**Novelty consequence:** PCA/SVD over a bank of representative theories is prior art. DSIR novelty cannot be “we run PCA on many cosmologies.”

### 3.8 Effective rank — Roy & Vetterli (2007)

**O. Roy & M. Vetterli, “The Effective Rank: A Measure of Effective Dimensionality,” EUSIPCO 2007.**

Defines entropy-based effective rank from normalized singular values.

**Overlap:** mathematical core of an entropy-style `R_D`.  
**Novelty consequence:** the entropy effective-rank formula is prior art. DSIR’s contribution, if any, is its cosmological calibration/interpretation (`R_obs`, `R_model(pi)`, whitening, null calibration), not the formula itself.

### 3.9 Ratio/reaction methods relative to LambdaCDM — Cataneo et al. (2019) and ReACT

**M. Cataneo et al., “On the road to percent accuracy: non-linear reaction of the matter power spectrum to dark energy and modified gravity,” MNRAS 488, 2121 (2019).**  
https://doi.org/10.1093/mnras/stz1836

Defines nonlinear “reaction” functions as ratios of a target beyond-LambdaCDM spectrum to a designed reference/pseudo cosmology. Related N-body code-comparison work also compares fractional deviations from LambdaCDM across codes.

**Overlap:** D and the general idea of using reference ratios to suppress model/systematic structure.  
**Novelty consequence:** response-to-reference ratios are not new. The DSIR-specific item is narrower: **same-solver model/reference quotient + independently validated cross-solver response bridge as a mandatory provenance gate for a heterogeneous response manifold**.

### 3.10 Model-independent interacting-dark-sector reconstructions

Examples:

- R. von Marttens et al., “A model-independent reconstruction of dark sector interactions,” arXiv:2011.10846.
- L. A. Escamilla et al., “Model-independent reconstruction of the Interacting Dark Energy Kernel,” arXiv:2305.16290.

These reconstruct dark-sector interaction functions directly from cosmological data without fixing one microscopic interaction law.

**Overlap:** reconstruction philosophy within a restricted interacting-DE sector.  
**Novelty consequence:** inverse reconstruction of a dark-sector function is prior art.

### 3.11 Dark degeneracy at perturbation level — von Marttens et al. (2020)

**R. von Marttens et al., “Dark degeneracy I: Dynamical or interacting dark energy?”, Physics of the Dark Universe 28, 100490 (2020).**  
https://doi.org/10.1016/j.dark.2020.100490

Explicitly derives background and linear-perturbation conditions under which dynamical DE and interacting vacuum DE are degenerate.

**Overlap:** H and DSIR’s equivalence/intersection graph.  
**Novelty consequence:** identifying specific background/perturbation degeneracies is prior art; DSIR must add systematic graph/rank/discriminant machinery across many families rather than claim the existence of such degeneracies as new.

### 3.12 LambdaCDM as a fixed point in dark-sector theory space — 2026 close competitor

**“LambdaCDM as a fixed point: Controlled dark-sector deformations and late-time structure growth,” Annals of Physics 490, 170466 (July 2026).**  
https://doi.org/10.1016/j.aop.2026.170466

Treats LambdaCDM as a fixed point in dark-sector effective theory space, activates controlled perturbative operators while preserving the background and gravitational sector, and follows their signatures into growth, `S8`, `f sigma8`, and weak lensing.

**Overlap:** B/C conceptually, theory-space organization, observable fingerprints, part of I.  
**Threat level:** **HIGH — closest conceptual competitor found in N0.**  
**Current distinction:** this work organizes controlled deformations around a fixed LambdaCDM point, whereas DSIR is designed to ingest heterogeneous pre-existing theories (DM microphysics, unified fluids, interacting sectors, DE, MG), quotient known degeneracies/systematics, estimate the dimension of the resulting observable manifold, and then search for cross-channel laws with withheld prediction.

This distinction must be tested again at manuscript stage; wording such as “first dark-sector theory space” is prohibited.

### 3.13 Symbolic regression in cosmology — 2025/2026

Examples:

- A. Sousa-Neto et al., “Symbolic regression analysis of dynamical dark energy with DESI-DR2 and SN data,” Physics of the Dark Universe 50, 102108 (2025), DOI 10.1016/j.dark.2025.102108.
- S. M. Koksbang & A. Heinesen, “Model-independent constraints on generalized FLRW consistency relations with bootstrap-based symbolic regression,” accepted PRD May 2026, arXiv:2604.05822.

**Overlap:** I as a mathematical tool for data-driven relation/equation reconstruction.  
**Novelty consequence:** “apply symbolic regression to cosmology/dark energy” is prior art. DSIR must use symbolic regression only after identity/degeneracy quotienting and validate any relation by withheld physical-channel prediction.

---

## 4. Prior-art matrix

Legend: `Y` = strong overlap, `P` = partial/nearby, `-` = not identified in this work, `?` = requires deeper full-text audit.

| Prior work | A | B | C | D | E | F | G | H | I | J | K |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Kunz dark degeneracy | Y | P | P | - | - | - | - | Y | - | - | P |
| Hu–Sawicki PPF | Y | Y | P | - | - | - | - | P | - | - | P |
| Baker–Ferreira–Skordis PPF | P | Y | P | - | - | - | - | P | - | - | Y(MG) |
| Hu GDM | P | Y | P | - | - | - | - | P | - | - | P |
| EFT of DE | P | Y | P | - | - | P | - | P | - | - | Y(DE/MG) |
| Gleyzes theory-space compression | - | Y | - | - | - | P | - | - | - | - | P |
| Zanoletti–Leonard PCA | - | P | - | P | - | Y | - | - | - | - | P |
| Roy–Vetterli effective rank | - | - | - | - | - | Y(math) | - | - | - | - | - |
| Cataneo/ReACT | - | P | P | Y | P | - | - | - | - | - | P |
| IDE model-independent reconstruction | - | P | P | - | - | - | - | P | P | - | P |
| Dark degeneracy I | P | P | P | - | - | - | - | Y | - | - | P |
| LambdaCDM fixed-point 2026 | P | Y | P | P | - | P | - | P | P | - | P |
| Symbolic-regression cosmology | - | - | - | - | - | - | - | P | Y | P/? | - |
| **DSIR target architecture** | Y | Y | **Y** | Y | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** |

No audited work was found with `Y` across the DSIR-specific combination **C+E+F+G+H+I+J**.

---

## 5. What DSIR is NOT allowed to claim as novel

The following claims are prohibited unless a later audit overturns this assessment:

1. “We invented the effective dark-sector stress tensor.”
2. “We discovered the dark degeneracy.”
3. “We introduced a common fluid language for dark matter.”
4. “We introduced PPF/EFT-style theory dictionaries.”
5. “We are the first to apply PCA/SVD to modified-gravity/dark-sector model banks.”
6. “We invented entropy effective rank.”
7. “We invented ratios/responses relative to LambdaCDM.”
8. “We are the first to reconstruct dark-sector interactions model-independently.”
9. “We are the first to use symbolic regression in dark-energy/cosmology studies.”
10. “We are the first to organize LambdaCDM as a point/fixed point in dark-sector theory space.”

---

## 6. Provisional DSIR novelty statement after N0

The strongest wording currently defensible is deliberately narrow:

> **DSIR is a provenance-controlled inverse reconstruction pipeline that maps heterogeneous dark-sector and modified-gravity theories into a common observable-response manifold, uses same-solver reference quotients with explicit cross-solver bridges, covariance-whitened and theory-prior-sensitive latent-dimension tests, removes known physical/measurement identity directions before relation discovery, and requires prediction of a withheld physical channel before elevating a residual relation to a new law.**

This is a **provisional methodological novelty hypothesis**, not yet a publication claim.

The most scientifically valuable result would not be the framework itself. Strong novelty would arise if the completed theory/data atlas reveals a robust low-dimensional structure or a cross-channel relation that survives solver, basis, prior, dataset and holdout tests.

---

## 7. N0 pass/fail criteria

### N0 PASS-PROVISIONAL

N0 is provisionally passed if the searched literature contains prior art for individual ingredients but no identified work implements the complete DSIR-specific chain:

`heterogeneous DM+DE+interaction+MG atlas`
` -> common observable response`
` -> same-solver quotient + cross-solver bridge`
` -> covariance whitening/noise calibration`
` -> R_model(pi) prior-sensitivity profile`
` -> quotient of identities and measurement degeneracies`
` -> cross-channel law discovery`
` -> withheld physical-channel prediction`.

### Automatic N0 FAIL / reframe

Reopen N0 immediately if a prior work is found that already implements substantially the same chain, even under different terminology. Then DSIR must be reframed around a narrower empirical or computational contribution.

---

## 8. Next novelty gates

- **N1 — citation-graph/full-text audit:** follow references and citing papers of the closest competitors (Kunz, PPF, EFT, ReACT, 2025 PCA, 2026 fixed-point work) and search adjacent terms such as response manifold, observable manifold, intrinsic/effective dimension, information geometry, model manifold, emulator latent space, and theory-space learning.
- **N2 — claim decomposition:** for every planned abstract/introduction novelty sentence, attach the exact prior-art sources it excludes and the DSIR experiment that supports it.
- **N3 — manuscript-stage fresh audit:** rerun the search immediately before any preprint because this field is active and 2026 work can appear during DSIR development.

---

## 9. Search log (N0)

Representative search concepts used on 2026-08-24:

- dark degeneracy total energy-momentum tensor;
- PPF effective stress tensor / theory dictionary;
- EFT dark energy theory space;
- generalized dark matter stress tensor;
- PCA representative modified-gravity theories;
- model-agnostic modified gravity principal components;
- dark-sector theory space / LambdaCDM fixed point;
- model-independent dark-sector interaction reconstruction;
- matter-power reaction / ratio to LambdaCDM;
- modified-gravity code comparison fractional deviations;
- effective rank singular-value entropy;
- symbolic regression dark energy / FLRW consistency relations;
- withheld/cross-validation cosmological reconstruction.

Absence from this search log is not evidence of absence from the literature.