# Experiment 016 — interacting-vacuum perturbation zero-limit source audit

**Date:** 2026-08-24  
**Pinned upstream:** `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`

## Purpose

Extend Experiment 013 from the background to the linear perturbation source before running a full clean-room Boltzmann comparison.

## Gauge restriction discovered

The pinned `class_iv` implementation explicitly aborts if `IDM_IV` is evolved in Newtonian gauge:

`IDM IV implementation not supporting newtonian gauge (yet)`.

Therefore **all precision validation of this specific upstream implementation must use synchronous gauge**. This is an implementation limitation, not a physical statement about interacting-vacuum theories in general.

## Zero-coupling equation

For ordinary pressureless CDM in synchronous gauge the source has

`delta_cdm' = - metric_continuity`.

For the interacting pressureless component the pinned source has

`delta_idm_iv' = - metric_continuity + delta_idm_iv/rho_idm_iv * a * H * (alpha rho_idm_iv + beta rho_iv)`.

With the background convention

`Q = H (alpha rho_idm_iv + beta rho_iv)`, 

the extra term is proportional to the interaction. Hence at

`alpha = beta = 0`

one obtains exactly

`delta_idm_iv' = - metric_continuity`,

identical to synchronous-gauge CDM.

The synchronous gauge fixes the pressureless-matter velocity variable to zero; the IDM_IV branch likewise does not evolve a separate velocity variable there.

## Initial conditions

The adiabatic initialization sets

`delta_idm_iv = 3/4 delta_gamma`,

which is the standard pressureless-matter adiabatic relation at leading order. In Newtonian-gauge conversion code, a velocity is present, but Newtonian time evolution for IDM_IV is not implemented at this pin and must not be used for the full gate.

## Full-solver consequence

A zero-coupling validation should use a matched synchronous-gauge pair:

1. baseline: ordinary CDM + closure-filled Lambda;
2. IDM_IV case: start from the same CDM density, set `f_idm_iv=1` to transfer it into the interacting pressureless component; set `f_iv=1` to transfer the closure-filled Lambda into interacting vacuum; set `alpha_idm_iv=beta_idm_iv=0`; set `fluid_equation_of_state=IDM_IV`.

The source adds a tiny ordinary-CDM floor in synchronous gauge when converting the entire CDM component, and subtracts the same amount from IDM_IV to preserve the total density. Therefore the correct regression is on **total physical responses**, not component-by-component bitwise files.

## Gate status

- IDE-S0 background source regression: PASS (Experiment 013).
- IDE-S0P perturbation source zero-coupling audit: PASS in synchronous gauge.
- Newtonian-gauge precision gate: NOT APPLICABLE for this pinned upstream implementation.
- IDE-S1 full Boltzmann regression: OPEN; clean-room workflow is the next step.

No physical-law claim follows from this source identity.
