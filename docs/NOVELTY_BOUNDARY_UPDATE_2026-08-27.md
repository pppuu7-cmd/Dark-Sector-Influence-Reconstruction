# DSIR novelty-boundary update — 2026-08-27

Status: **PRIOR-ART / CLAIM-BOUNDARY NOTE — NOT PROOF OF NOVELTY**

## Why this update exists

The post-Exp071C interpretation uses terms such as response-space geometry, local charts, low-dimensional trajectories and channel-conditional equivalence. Those terms overlap mature literatures. This note narrows the claims DSIR may make before a deeper citation-graph/full-text novelty audit.

## Established prior art that blocks broad claims

### Model manifolds and information geometry

The general construction in which a parameterized model maps into a high-dimensional space of predictions, forming a model manifold, is established prior art. Nonlinear least-squares model manifolds, Fisher metrics, sloppy/stiff directions, manifold widths and curvature were developed well before DSIR.

Representative references:

- M. K. Transtrum, B. B. Machta, J. P. Sethna, *Geometry of nonlinear least squares with applications to sloppy models and optimization*, Phys. Rev. E 83, 036701 (2011), DOI: https://doi.org/10.1103/PhysRevE.83.036701
- Review: *Information geometry of multiparameter models: New perspectives on the origin of simplicity* (2023), https://pmc.ncbi.nlm.nih.gov/articles/PMC10018491/
- E. Giesel et al., *Information geometry in cosmological inference problems*, arXiv:2005.01057, https://arxiv.org/abs/2005.01057

Consequence: DSIR must **not** claim invention of a model manifold, Fisher geometry, sloppy/stiff dimensionality, or the idea that model predictions define an embedded manifold.

### Output-informed manifold learning / effective parameters

Output-informed diffusion maps and related manifold-learning methods already use model outputs to identify low-dimensional effective coordinates.

Representative reference:

- *Manifold learning for parameter reduction*, Journal of Computational Physics 388 (2019), https://pmc.ncbi.nlm.nih.gov/articles/PMC6528681/

Consequence: “infer low-dimensional coordinates from model responses” is not a novelty claim by itself.

### Model-independent dark-sector / modified-gravity reconstruction

Model-independent reconstruction of dark-sector interactions and modified-gravity functions is established.

Representative references:

- R. von Marttens et al., *A model-independent reconstruction of dark sector interactions*, arXiv:2011.10846, https://arxiv.org/abs/2011.10846
- Y. Mu, E.-K. Li, L. Xu, *Data-driven and Almost Model-independent Reconstruction of Modified Gravity*, arXiv:2302.09777, https://arxiv.org/abs/2302.09777

Consequence: DSIR must not claim that inverse/model-independent dark-sector reconstruction is itself new.

### 2026 close competitor: LambdaCDM as a fixed point in dark-sector theory space

A particularly close conceptual competitor is:

- *LambdaCDM as a fixed point: Controlled dark-sector deformations and late-time structure growth*, Annals of Physics 490 (2026) 170466, DOI: https://doi.org/10.1016/j.aop.2026.170466

It explicitly organizes LambdaCDM as a fixed point in dark-sector effective theory space, activates controlled perturbative deformations, and tracks their signatures into late-time growth and weak lensing.

Consequence: phrases such as “first dark-sector theory space”, “first systematic deformation away from LambdaCDM”, or “first observable fingerprint atlas” are prohibited without a much stronger audit.

## What remains potentially distinctive in DSIR

The currently defensible candidate is **not one mathematical ingredient**. It is a narrow pipeline-level conjunction that still has to survive G7/G8/G9:

1. heterogeneous microscopic families (DM fluid/microphysics, interactions, DE/MG) are mapped into a common response representation;
2. every family is bound to explicit solver provenance and same-solver reference closure before cross-family comparison;
3. equivalence is treated as **channel-conditional**, not as a global parameter conversion;
4. observable blocks are covariance-restricted/whitened and nuisance tangent directions are quotiented before relation discovery;
5. candidate cross-channel relations are frozen using eligible training families plus known-sector controls;
6. a genuinely unseen physical family is then used as a prospective falsification test;
7. only a relation that survives that sequence may be discussed as a candidate dark-sector regularity.

No searched source in this update was found implementing this exact complete conjunction. That is only a **search result**, not proof of global novelty.

## Revised claim language

Allowed now:

> DSIR investigates whether heterogeneous dark-sector and modified-gravity models admit reproducible, channel-conditional equivalence classes and cross-channel response relations after solver validation, covariance restriction and nuisance quotienting, with prospective withheld-family falsification.

Not allowed now:

- “DSIR discovered that cosmological models form a manifold.”
- “DSIR invented information geometry for the dark sector.”
- “DSIR is the first model-independent dark-sector reconstruction.”
- “DSIR discovered the first dark-sector theory space.”
- “Low-dimensional response trajectories are new physics.”

## Current scientific implication

Exp071C makes this boundary especially important. An ordinary baryon-fraction family passes the same normalized response-path gate as a withheld dark interaction family. Thus matter-only response geometry is best interpreted as a mechanism/shape diagnostic. A dark-specific claim, if one exists, must emerge from a stronger joint-channel relation — especially matter versus Weyl/lensing — that ordinary known-sector controls fail to reproduce under the same observational metric.

## Next novelty gate

Before manuscript-level novelty language, perform a dedicated N1 citation-graph/full-text audit centered on four combinations:

- `model manifold + cosmological multi-probe covariance`;
- `cross-model observational equivalence + modified gravity/dark sector`;
- `withheld model-family validation + cosmological theory banks`;
- `nuisance quotient + model-independent dark-sector reconstruction`.

Until N1 and G7/G8 are complete, novelty remains **pipeline-hypothesis only**.
