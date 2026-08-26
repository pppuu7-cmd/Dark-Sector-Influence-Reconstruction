# DSIR recovery checkpoint — Exp065A (2026-08-26)

Exp065A audited the public ACT DR6 × unWISE likelihood/data binding after F31. The pinned likelihood is `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`; the official data archive SHA256 is `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`.

Hard run `32978244624` passed provenance, Blue/Green ACT `Clgg` and `Clkg` bandpowers, bandwindow/transfer matrices, redshift auxiliary files and likelihood source binding. It failed only the covariance-binding check because the naively assembled *unselected* 236×236 Blue+Green covariance had `lambda_min=-1.65028271985107e-19` while `lambda_max=3.229098231297519e-13`.

This FAIL is permanent and must not be relabelled. A post-failure source audit identified a narrower issue: the official likelihood does not use the full raw matrices directly. It constructs `cond_gg` and `cond_kg` from the configured scale cuts, maps them to `ell_selection`, applies `select_from_matrix` separately to auto- and cross-covariances, and only then assembles the covariance used by the likelihood. Default ACT cuts are `Clgg: 100<ell-edge ... <402` and `Clkg: 51<...<402` as encoded by the pinned defaults.

Therefore the next scientifically admissible step is a distinct **Exp065B corrective eligibility audit** that reproduces the official selection path exactly and checks the selected covariance. This is not a rescue of Exp065A; it tests a different, more faithful eligibility statement revealed by the failure. No G7 law candidate and no withheld theory family may be selected before the corrected observational binding is known.

Top-level state remains: **G7 OPEN, G8 OPEN, G9 OPEN**.
