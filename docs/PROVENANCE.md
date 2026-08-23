# Data and solver provenance / correction ledger

## DESI DR1 ShapeFit compressed responses

**Accepted source:** the February 2026 erratum to DESI 2024 V (JCAP 02 (2026) E02; DOI 10.1088/1475-7516/2026/02/E02).

The erratum states that a numerical implementation error in Appendix A of the original paper affected all measurements involving `f sigma_s8` and the associated covariance entries. Figures, tables, conclusions, and the underlying analysis were not affected. DSIR therefore rejects the original Appendix-A growth datavectors/covariances and stores only the corrected values in `data/observations/desi_dr1_shapefit_erratum_2026.json`.

A regression test explicitly checks that the corrected LRG1 value `f_sigma_s8=0.513635` is used rather than the obsolete Appendix-A value `0.318967`.

The BGS `DH/DM` component is not used in the AP-growth stability diagnostic because the DESI paper warns it is strongly influenced by the bounded AP prior at low redshift.

## External solver: GDM_CLASS

**Repository:** `s-ilic/gdm_class_public`  
**Pinned audit commit:** `4c87916aab5ca124a68f1dd16f31846fc13d1829`

The pin is mandatory for Experiments 014 and the clean-room GDM zero-limit workflow. Relevant source facts at this pin:

- the background exposes `w_gdm(a)`, `ca2_gdm(a)` and `rho_gdm(a)`;
- the perturbation closure exposes `cs2_gdm(a,k)` and `cv2_gdm(a,k)`;
- all-zero `w` bins give a pressureless `rho_gdm ~ a^-3` background;
- all-zero `w,cs2,cv2` gives the CDM continuity/Euler limit with zero shear;
- the GDM-enabled IC branch uses leading radiation-era expressions and deliberately omits some finite-start `O(omega*tau)` corrections retained by the ordinary CDM branch; upstream requires `start_small_k_at_tau_c_over_tau_h <= 1e-6` when GDM is present.

**Consequence:** the full solver regression must scan/start-converge. A single finite-start mismatch is not automatically physical, and a bitwise-equality gate would be wrong.

No upstream upgrade is allowed silently. A changed pin requires a new provenance entry and rerun of source/full-solver gates.

## External solver: CLASS interacting vacuum (`class_iv`)

**Repository:** `kaeonikc/class_iv`  
**Pinned audit commit:** `ac627d54e9ce196a08878d1ba33999819925d19c`

At this pin the background source defines the interaction convention

`Q = H * (alpha_idm_iv * rho_idm_iv + beta_idm_iv * rho_iv)`.

The corresponding continuity equations inferred and independently checked from the exact source solution are

`d rho_m/d ln a = -(3+alpha) rho_m - beta rho_v`,

`d rho_v/d ln a = alpha rho_m + beta rho_v`.

Thus positive `Q` transfers energy from the interacting pressureless component into the vacuum component in this implementation convention. `alpha=beta=0` returns pressureless matter plus constant vacuum. Experiment 013 verifies the analytic source solution against direct ODE integration and freezes this sign convention.

A full Boltzmann regression is still required before this family is admitted as a precision G3B response surface. The code history includes a growth `D/f` correction involving baryons, so the exact commit must remain pinned.

## Clean-room execution policy

External-solver precision results should be produced by a recorded clean environment (currently GitHub Actions) that stores:

- DSIR commit SHA;
- upstream solver commit SHA;
- compiler/Python environment;
- exact input files;
- raw solver logs;
- output products;
- comparison metrics.

The first execution of a new solver regression is calibration-only unless a physically/numerically justified tolerance was fixed independently beforehand. Tolerance is frozen only after convergence behavior is observed and documented; it must not be chosen merely to make a run pass.

## Claim discipline
A correction to an input product, a source-level identity, or a solver-regression pass is not a DSIR discovery. Any result that changes when switching between superseded/corrected data or unstable solver settings is classified as provenance/numerics-sensitive and cannot pass G7/G8.
