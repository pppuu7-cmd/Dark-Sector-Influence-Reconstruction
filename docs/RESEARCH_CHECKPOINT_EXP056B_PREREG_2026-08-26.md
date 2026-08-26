# DSIR research checkpoint — Exp056A/Exp056B preregistration — 2026-08-26

## Starting state

Main before this cycle ended at Exp055A/F28, which retrospectively qualified a common endpoint-normalized half-transition direction across C3 GDM, C5 designer-f(R) and already-unblinded C7 IDM-DR:

`C50 = Delta ln(k50_geo) / Delta ln(k_source) > 0`.

The candidate survived every single-redshift deletion, but G7/G8 remained open because the operator was chosen after C7 output existed. The frozen next-step requirement was a genuinely fresh mechanism/family with the complete k50/sign contract committed before first response.

## Exp056A — C8 source-only selector

PR #46 was validated by GitHub Actions run `32922159744` and merged to main as `0e27dffc079b512c91b41898e3eda19fc84d50a6`.

Mechanism: C8 interacting dark matter–photon scattering in pinned CLASS `e85808324f51fc694d12e3ed7439552a3c3f9540`, `n_index_idm_g=0`, `m_idm=1e9 eV`.

Frozen source equation:

`Gamma_idm<-gamma = (4/3 rho_gamma/rho_idm) dmu_idm_g`, with `Gamma=Hconf` and `k_source=Hconf/h`.

Target source scales (`h/Mpc`):

`[0.08484582985947185, 0.07347864406347489, 0.05999506164903260, 0.04647197492427811, 0.03927598733289058]`.

Source-only selected `u_idm_g`:

`[1.9784961959913951e-13, 2.7180740724473660e-13, 4.2866377403625277e-13, 7.7340788471244140e-13, 1.1546648138593298e-12]`.

The contamination guard confirmed no C8 `P(k)`, transfer, source or `C_l` response product existed. Maximum source-rate and source-scale reconstruction errors were approximately `2.22e-16` and `1.78e-15`. The coupling grid is frozen against response retuning.

## Exp056B — prospective F28 test

Branch: `research/exp056b-idm-photon-half-transition-prospective-v0-1`.

The complete scientific contract was committed first as `84d05ad72af1aea4fe3beadf071ee20cadf93c19`, before any C8 matter-power response. Evaluator and workflow were added only afterwards.

Frozen response grid:

- `z={0.295,0.51,0.706,0.934,1.317,1.491,2.33}`;
- `k={0.001,0.003,0.01,0.03,0.1} h/Mpc`;
- matched reference is identical except `u_idm_g=0`.

At every model/redshift row:

`u=(R(k)-R(k_min))/(R(k_max)-R(k_min))`, with one and only one `u=0.5` crossing interpolated linearly in `ln k`. Global row monotonicity is not required. For each coupling, `k50_geo=exp(mean_z ln k50(z))`; adjacent `C50=Delta ln(k50_geo)/Delta ln(k_source)`.

Frozen PASS rule: all 35 rows have a valid unique crossing, all four full-sample C50 are strictly positive, and all 28 C50 values from the seven leave-one-redshift recomputations are strictly positive. There is no numerical slope-magnitude band and no post-output recalibration.

PR #47 triggers the first prospective C8 response. GitHub Actions run: `32925960293`.

## Interpretation boundary

PASS would be the first prospective validation of F28 on a fresh C8 response and would trigger a conservative G7/G8 provenance audit. FAIL must be retained as a hard prospective falsification of F28 v0.1 on C8 without erasing the positive retrospective F28 result or earlier mechanism-specific findings. Neither outcome establishes a fundamental action, intrinsic field count, observation-space detectability or a universal numerical slope coefficient.
