# DSIR literature map

| Topic | Reference anchor | DSIR use |
|---|---|---|
| dark degeneracy | Kunz 2007, astro-ph/0702615 | gravity alone need not uniquely split DM and DE |
| generalized dark matter | Hu 1998, astro-ph/9801234 | full-stress/closure control |
| PPF modified gravity | Hu & Sawicki 2007, arXiv:0708.1190 | common response language and screening regimes |
| thermal WDM transfer | Viel et al. 2005, astro-ph/0501562; Bode et al. 2001 | frozen scale-dependent suppression control |
| f(R) perturbations | Tsujikawa et al. 2007, arXiv:0712.0082; Chiu et al. 2015, arXiv:1505.03323 | Compton-scale modified-growth control |
| DESI DR1 full-shape | DESI 2024 V/VII, arXiv:2411.12021 / 2411.12022 | public growth/RSD target for G6B |
| DESI DR2 BAO | DESI DR2 II (2025) | current G6A geometry data |
| DESI DR2 Ly-alpha AP | DESI DR2 IV (2026) | additional AP cross-check |

## Novelty guardrail
PCA, symbolic regression of w(z), PPF/EFT parameterizations, GDM, AP inversion, and modified-gravity mu/Sigma consistency tests all have prior literature. Any DSIR novelty must come from the combined workflow: response-manifold intersections + identifiability quotient + known-identity quotient + cross-channel law discovery + adversarial discriminant-channel selection + withheld prediction.

<!-- F23_LITERATURE_UPDATE_2026-08-26 -->
## Source anchors added for Exp049A/F23 and Exp050A

### f(R) Compton-wavelength parameter

- Song, Hu & Sawicki, **The Large Scale Structure of f(R) Gravity**, arXiv:astro-ph/0610532. Establishes the stable `B>0` branch and parameterization of linear f(R) deviations by the B quantity tied to `d^2f/dR^2`.
  - https://arxiv.org/abs/astro-ph/0610532
- Hu & Sawicki, **Models of f(R) Cosmic Acceleration that Evade Solar-System Tests**, Phys. Rev. D 76, 064004 (2007), arXiv:0705.1158. Describes B as the Compton-wavelength parameter and states that its square-root is essentially the scalaron Compton wavelength in horizon units in the relevant limit.
  - https://arxiv.org/abs/0705.1158

These references independently support the physical interpretation of the exact B definition audited in pinned EFTCAMB; DSIR still derives its numerical scale from the pinned source rather than importing a fitted approximation.

### thermal/non-cold relic Boltzmann implementation

- Official CLASS pinned for Exp050A: `lesgourg/class_public@e85808324f51fc694d12e3ed7439552a3c3f9540`.
- The pinned `explanatory.ini` explicitly states that the ncdm sector covers massive neutrinos, warm dark matter and other non-cold relics; if both `m_ncdm` and `omega_ncdm` are supplied, CLASS renormalizes the phase-space distribution to satisfy both; `T_ncdm` is independently specified.
- Exp050A uses the pinned upstream `pk_ref.pre` as the initial high-precision ncdm calibration, where `ncdm_fluid_approximation=3` corresponds to `ncdmfa_none` in the same pinned source enum.

This is a solver/provenance anchor, not an observational WDM constraint.

