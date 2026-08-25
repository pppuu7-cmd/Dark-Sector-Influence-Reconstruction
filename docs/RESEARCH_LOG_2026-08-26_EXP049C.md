# Research log — 2026-08-26 — Exp049C withheld designer-f(R) window crossing

## Frozen-before-output chronology

1. Started from `main` merge `63161436d647be1677530d33a7c597d166ae4812`.
2. Committed the experiment contract before any intermediate-B0 outputs: `experiments/049c_fr_window_crossing_validation_v0_1.md`.
3. Frozen withheld grid: `B0={1.5e-4,2e-4,3e-4,5e-4,7e-4}`.
4. Frozen source eligibility: terminal B0 error `<=1e-6`, every exact Compton transition inside `k<=0.1 h/Mpc` on at least one frozen z node, and decreasing minimum k_C with B0.
5. Frozen single scientific prediction: consecutive `k_I^geo` steps `<=+1e-6 h/Mpc`.
6. Explicitly did not predict `z_I`, `chi_I`, exact localization, shift magnitude, or survey significance.
7. Added analysis/workflow; scientific head before run: `a575a2e78b21eab36b88db8622e14509a30cae5a`.
8. GitHub Actions run `32907619613` generated all new models and passed every solver/source/operator/prediction step.

## Immutable artifact

- artifact ID: `9585579947`
- digest: `sha256:bc2145365d14939473c73f36c0ee2ca41920d7be8eb50a31a1858c6f66aed942`
- pinned H-EFTCAMB: `16d9c4e9f85751e30efd0a53b177941713078904`

## Outcome

`PASS_FR_WINDOW_CROSSING_VALIDATION_V0_1`.

`k_I^geo [h/Mpc]`:

`0.0480162166, 0.0472514062, 0.0459188421, 0.0437628123, 0.0420339320`.

Consecutive steps:

`-7.64810e-4, -1.33256e-3, -2.15603e-3, -1.72888e-3 h/Mpc`.

Minimum frozen-z exact inverse-Compton scales:

`0.0573747, 0.0496881, 0.0405703, 0.0314259, 0.0265600 h/Mpc`.

All source conditions pass. Maximum terminal B0 relative error `7.50777e-11`. Operator residual maximum `5.68411e-20` (orthogonality), all far below the `1e-12` algebraic gate.

Unpredicted descriptors were retained rather than post-selected: `chi_I` decreases from `0.270142` to `0.192356`; `z_I` increases from `0.94333` to `1.08437`.

## Interpretation

This is the second independent withheld directional validation of the finite-window transition/localization idea after GDM Exp049B/F21. It upgrades the two-family predictive evidence but does not universalize the claim. C4 high-k time dependence, observation-space projection, and broader family/domain tests remain missing. G7 and G8 stay open.
