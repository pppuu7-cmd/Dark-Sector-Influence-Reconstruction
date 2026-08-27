# Exp073F — alternative perturbative observational-route landscape — result v0.1

**Date:** 2026-08-27  
**Scientific classification:** `PERTURBATIVE_OBSERVATIONAL_ROUTE_CANDIDATE_FOUND_EXP073F`

## Frozen question

Exp073F asked whether at least one public observational realization is plausibly auditable inside the already-certified common C3+C5 perturbative support,

- `0.295 <= z <= 2.33`;
- `0.000704833374744468 <= k <= 0.06664762008318016 Mpc^-1`;
- maximum positive-weight support leakage `5%`;

while retaining matter, Weyl/lensing and signed cross information without selecting the route using covariance, nuisance rank, G7 residuals or G8 performance.

The answer at landscape level is **yes**. One candidate is sufficiently reproducible and structurally compatible to justify a separate exact operator/support audit. This is not a support PASS and does not authorize covariance work.

## Primary candidate — KiDS-1000 + BOSS 3x2pt with prospective BNT physical-scale localization

**Landscape label:** `PROMISING_FOR_EXACT_SUPPORT_AUDIT`.

### Public/reproducible inputs

The KiDS-1000 public 3x2pt release provides data products for cosmic shear, BOSS-DR12 galaxy clustering, 2x2pt combinations and the fiducial 3x2pt analysis. The release explicitly provides the data vectors, covariance products and galaxy redshift distributions through its public/open-source analysis repository. Exp073F uses only the existence and public operator/redshift information; covariance values are not inspected or used for candidate ranking.

Primary release page:
- https://kids.strw.leidenuniv.nl/DR4/KiDS-1000_3x2pt_Cosmology.php

The KiDS-1000 cosmic-shear release separately publishes tomographic data vectors and source redshift distributions:
- https://kids.strw.leidenuniv.nl/DR4/KiDS-1000_cosmicshear.php

### Why this architecture is different from ACT x unWISE

The released 3x2pt structure contains the three required physical channel types:

1. BOSS galaxy clustering: matter-sensitive `P_mm` channel;
2. galaxy-galaxy lensing: signed matter-Weyl cross-sensitive `P_Wm` channel;
3. cosmic shear: Weyl/lensing auto-sensitive `P_WW` channel.

The observable architecture therefore does not require identifying a nonlinear `P_WW` or `P_Wm` from `P_mm`. In a future DSIR reconstruction the three physical blocks can remain explicit; the standard public cosmology implementation need not be adopted as a GR closure.

### BNT localization is the critical support mechanism

Ordinary weak-lensing kernels are broad and mix low-redshift/high-k contributions. The Bernardeau-Nishimichi-Taruya (BNT) transform is a linear transformation of tomographic shear observables that constructs kernels localized in redshift and physical scale. Published work explicitly shows that BNT can build observables independent of selected low-redshift/small-scale modes, and later work formulates k-cuts after BNT to control nonlinear scale leakage.

Evidence:
- Barthelemy et al., Phys. Rev. D 105, 043537 (2022): https://journals.aps.org/prd/abstract/10.1103/PhysRevD.105.043537
- Gu et al., Phys. Rev. D 111, 083530 (2025): https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.083530
- Gu et al., Phys. Rev. D 113, 023528 (2026): https://journals.aps.org/prd/abstract/10.1103/y7c6-t42s

A 2026 KiDS-Legacy application additionally demonstrates BNT on an actual KiDS weak-lensing data vector with a physical k-cut, which strengthens implementation plausibility but is not used as a downstream performance criterion:
- arXiv:2607.04384, https://doi.org/10.48550/arXiv.2607.04384

### Frozen F1-F8 landscape decision

- **F1 public reproducibility — plausible PASS.** KiDS-1000 3x2pt, cosmic-shear data vectors and n(z) products are public and versionable.
- **F2 redshift support — plausible PASS for exact audit, not yet certified.** BNT provides an explicit operator-level way to suppress low-redshift kernel support; BOSS lens/redshift selections can be restricted prospectively to the frozen `z>=0.295` domain. Exact positive-weight leakage must be computed later.
- **F3 k support — plausible PASS for exact audit, not yet certified.** BNT+k-cut methodology directly addresses angular-to-physical-scale leakage. The future audit must freeze and test `k<=0.06664762008318016 Mpc^-1`, substantially stricter than published cosmology cuts.
- **F4 matter/Weyl complementarity — PASS structurally.** 3x2pt contains clustering, galaxy-galaxy lensing and cosmic shear.
- **F5 independent cross semantics — PASS in principle.** The three observable classes can be written against independent `P_mm`, signed `P_Wm`, and `P_WW`; no DSIR GR matter-to-Weyl closure is required by the observable definitions themselves.
- **F6 linear-domain consistency — plausible PASS for exact audit.** The candidate permits a prospective BNT physical-k restriction; no nonlinear correction is required to define the proposed restricted route.
- **F7 minimum information architecture — plausible PASS.** Public tomography and the 3x2pt channel structure provide multiple independent coordinates. No covariance or rank was inspected.
- **F8 no downstream selection — PASS.** Ranking used only support geometry, public reproducibility and observable/channel structure.

Because F2/F3/F6 are deliberately only plausibility decisions at this stage, the candidate is not a support-validity result. It qualifies exactly for the preregistered `PROMISING_FOR_EXACT_SUPPORT_AUDIT` label.

## Other landscape candidates

### DESI DR1 spectroscopic clustering

**Label:** `PARTIAL_MATTER_ONLY`.

DESI DR1 provides public clustering-ready LSS catalogs for BGS/LRG/ELG/QSO and public redshift-bin products, with effective redshifts spanning the frozen DSIR interval, including LRG, ELG and QSO bins. Restricting Fourier modes to the frozen low-k region is straightforward in principle, but density clustering alone does not supply the independent Weyl/Weyl-cross structure required for a complete G7 route.

Evidence:
- https://data.desi.lbl.gov/doc/releases/dr1/
- https://data.desi.lbl.gov/doc/releases/dr1/vac/full-shape-cosmo-params/

### ACT DR6 CMB lensing alone

**Label:** `PARTIAL_WEYL_ONLY`.

ACT DR6 publicly releases CMB lensing convergence maps and lensing likelihood products with bandpowers/binning information. This is a reproducible Weyl-sensitive channel but not a complete matter/Weyl route by itself.

Evidence:
- https://act.princeton.edu/act-dr6-data-products
- https://lambda.gsfc.nasa.gov/product/act/actadv_dr6_lensing_maps_info.html
- https://lambda.gsfc.nasa.gov/product/act/actadv_dr6_lensing_lh_info.html

### DESI density + ACT DR6 CMB lensing auto/cross

**Label:** `UNCLEAR`.

This composition supplies matter auto, matter-Weyl cross and a Weyl auto channel with fully public ingredients, but ordinary CMB-lensing auto kernels are broad along the line of sight. Exp073F found no pre-existing public tomographic operator that guarantees the frozen `0.295<=z<=2.33` 5% leakage criterion. It therefore cannot be promoted to `PROMISING_FOR_EXACT_SUPPORT_AUDIT` without a separate prospective localization construction. This is deliberately not classified as a scientific support FAIL.

Public ingredients:
- DESI DR1 LSS: https://data.desi.lbl.gov/doc/releases/dr1/
- ACT DR6 lensing products: https://lambda.gsfc.nasa.gov/product/act/actadv_prod_table.html

## Scientific interpretation

Exp073E closed the strategy of forcing the frozen phenomenological C3 family through the nonlinear ACT x unWISE domain. Exp073F shows that this does **not** close G7 in general: a qualitatively different observational realization exists in which public 3x2pt tomography plus a prospective BNT physical-scale localization can be tested against the already-certified perturbative support without adding nonlinear GDM completion physics.

The key distinction is methodological. The next experiment must test the candidate's actual transformed kernels and released windows against the unchanged 5% support criterion. No claim is made that the candidate already passes.

## Authorized next step

Prospectively preregister and execute an exact KiDS-1000+BOSS/BNT operator-support audit. It must, before reading covariance or downstream results:

1. bind exact public KiDS-1000 3x2pt and n(z) release versions;
2. freeze the BNT construction and any retained tomographic combinations;
3. freeze BOSS lens/redshift selections with no post-output tuning;
4. map every retained angular/bandpower coordinate to positive-weight `(z,k)` support;
5. apply the unchanged `z` and `k` rectangle and `5%` leakage threshold;
6. require explicit `P_mm`, signed `P_Wm`, `P_WW` block semantics;
7. classify support independently of covariance, nuisance rank, relation quality or G8.

Only a later exact support PASS can authorize covariance restriction/whitening.

G7 OPEN. G8 OPEN. G9 OPEN.
