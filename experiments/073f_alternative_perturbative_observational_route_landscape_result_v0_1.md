# Exp073F — alternative perturbative observational-route landscape result v0.1

**Date:** 2026-08-27  
**Landscape classification:** `PERTURBATIVE_OBSERVATIONAL_ROUTE_CANDIDATE_FOUND_EXP073F`

## Frozen target

Exp073F searched public observation architectures that could preserve the already-certified common C3+C5 linear physical domain

`z in [0.295,2.33]`, `k <= 0.06664762008318016 Mpc^-1`,

with the unchanged 5% positive-weight support-leakage gate, while retaining matter/Weyl complementarity and independent response semantics.

No covariance, nuisance rank, G7 relation/null, G8 output or held-out metric was used in candidate selection.

## Highest-value candidate

The strongest public candidate found is the **lowest-redshift DESI DR1 spectroscopic-quasar tomography bin (`g1`) cross-correlated with Planck PR4 CMB lensing**, using the public analysis of de Belsunce et al., *Cosmology from Planck CMB lensing and DESI DR1 quasar tomography*, JCAP 10 (2025) 077, arXiv:2506.22416, together with its public Zenodo supplementary release DOI `10.5281/zenodo.15749799`.

The frozen candidate is **not** the full three-bin published likelihood. It is the publicly measured/operator-defined `g1` sector considered prospectively under stricter DSIR physical scale cuts.

### Why g1 is structurally attractive

The DESI DR1 `g1` sample is spectroscopic and has the exact published redshift interval

`0.8 <= z < 2.1`,

with `z_eff = 1.44` and 856,831 quasars. Its tracer redshift interval lies wholly inside the current Exp071A common provider redshift support `[0.295,2.33]`, unlike the higher two DESI quasar bins.

The published analysis measures both

- quasar auto-spectrum `C_ell^{qq}`;
- Planck-PR4-lensing × quasar cross-spectrum `C_ell^{kappa q}`.

The observed quasar field includes a measured magnification-bias contribution (`s_mu≈0.099` for g1). Consequently the full projected theory is not matter-only: density, lensing magnification and CMB-lensing terms provide a natural route to the same solver-neutral matter/Weyl block architecture used by DSIR. In an exact DSIR reconstruction the independent physical inputs must remain `P_mm`, signed `P_Wm`, and `P_WW`; no GR matter-to-Weyl closure is authorized.

### Scale structure

The publication uses

- `ell_min=85` for quasar auto-spectrum;
- `ell_min=45` for CMB-lensing cross-spectrum;
- published g1 high-ell cuts up to `ell_max=605` and `805`, corresponding to approximately `k_max=0.13` and `0.18 Mpc^-1` at the bin effective redshift.

Those published high-ell cuts exceed the stricter DSIR common provider boundary and therefore are **not** accepted as-is.

However the public measurement contains many lower-ell bandpowers below 605. At `z_eff≈1.44`, a simple Limber center estimate places the DSIR `k_max≈0.06665 Mpc^-1` at multipoles of order a few hundred, so a stricter prospective low-ell subset exists in the released data vector. Exact bandwindow/kernel leakage—not this center estimate—must decide the gate.

The candidate therefore qualifies for an exact support audit but is not yet a support PASS.

## Public reproducibility

The 2025 publication states that data are publicly available, and the associated Zenodo record `10.5281/zenodo.15749799` provides the supplementary analysis materials. The paper gives the quasar binning, measured redshift distributions, magnification-bias parameters, pseudo-C_ell setup, HEALPix `Nside=2048`, scale cuts, pixel-window treatment and data-vector structure needed to reconstruct the operator semantics.

This satisfies the landscape-level F1 requirement and makes an immutable exact audit technically realistic.

## Other candidates considered

### DESI LRG × ACT DR6 / Planck PR4

The 2024/2025 DESI-LRG CMB-lensing analyses provide public high-significance `gg` and `kappa g` tomography over roughly `0.4<z<1.0`, including explicitly tested linear-theory scale restrictions. Their higher-redshift bins are potentially useful, but the lower-redshift support lies closer to the current `z_min=0.295` boundary and the analyses were designed to exploit substantially larger k than DSIR currently certifies. They remain secondary candidates pending the stronger g1 test.

Landscape label: `PROMISING_FOR_EXACT_SUPPORT_AUDIT`, lower priority than DESI-QSO g1.

### Full DESI DR1 quasar tomography

Bins `g2: 2.1<=z<2.5` and `g3: 2.5<=z<=3.5` extend beyond the current provider `z_max=2.33`. They are not candidates under the frozen Exp073F baseline without a separately certified high-z provider extension.

Landscape label for full three-bin route: `REDSHIFT_SUPPORT_INCOMPATIBLE` under current support.

### CMB-lensing auto-spectrum as the sole WW channel

A CMB-lensing auto-spectrum has a very broad line-of-sight kernel extending well beyond the current `z_max=2.33`; therefore it is not preferred as the primary way to introduce WW under the frozen provider support. The g1 magnification structure is more localized in source redshift and must be tested first.

## Frozen F1–F8 decision for DESI-QSO g1

- F1 public reproducibility: **plausible PASS** — paper + open Zenodo supplementary data;
- F2 redshift support: **strongly promising** — source interval `0.8–2.1` lies inside provider z support; magnification lower-z tail still requires exact audit;
- F3 k support: **promising only under stricter low-ell subset** — published high-ell cuts do not pass automatically;
- F4 matter/Weyl complementarity: **PASS in architecture** through density + CMB lensing + quasar magnification;
- F5 independent cross semantics: **compatible in principle** with DSIR independent `mm/Wm/WW` projector;
- F6 linear-domain consistency: **plausible** after prospective restriction to low ell, to be demonstrated exactly;
- F7 minimum information architecture: **plausible** because multiple released qq and kappa-q bandpowers remain below the prospective scale boundary; no covariance/rank is inspected here;
- F8 no downstream selection: **PASS**.

Therefore the preregistered landscape criterion is satisfied:

`PERTURBATIVE_OBSERVATIONAL_ROUTE_CANDIDATE_FOUND_EXP073F`.

## Scientific importance

This is the first post-Exp073A route that may preserve the original model-agnostic C3 semantics rather than inventing nonlinear C3 physics. The shift is from a low-redshift broad photometric tracer to a high-redshift spectroscopic tracer and from using most released multipoles to an explicitly perturbative low-ell operator subset.

The candidate succeeds only if an exact, positive-weight, unit-invariant support audit passes the unchanged 5% leakage threshold. No scale cut may be selected using covariance or later DSIR performance.

## Downstream state

Exp073F authorizes only a separately frozen exact DESI-QSO-g1/Planck-PR4 operator-support audit. It does not authorize covariance restriction, whitening, nuisance SVD/rank, relation/null fitting or G8.

G7 OPEN. G8 OPEN. G9 OPEN.

## Primary/public sources

- R. de Belsunce et al., JCAP 10 (2025) 077, DOI `10.1088/1475-7516/2025/10/077`, arXiv:2506.22416.
- Public supplementary dataset: Zenodo DOI `10.5281/zenodo.15749799`.
- J. Kim et al., ACT DR6 × DESI LRG structure-growth analysis, arXiv:2407.04606.
- N. Sailer et al., DESI LRG × Planck PR4/ACT DR6, arXiv:2407.04607.
