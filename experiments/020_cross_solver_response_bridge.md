# Experiment 020 — cross-solver same-reference response bridge

**Date:** 2026-08-24  
**Status at write time:** calibration complete; hard threshold frozen before final rerun.

## Question

Can two different CLASS-family lineages be used in one DSIR response space without mistaking solver-version differences for dark-sector physics?

Absolute spectra are not the object of the bridge. For each solver lineage `S`, compute the same physical deformation relative to its own matched reference:

\[
r_S(k,z)=\ln\frac{P_\Delta^{\rm model,S}(k,z)}{P_\Delta^{\rm ref,S}(k,z)}.
\]

Then compare

\[
\Delta r_{\rm bridge}=r_A-r_B.
\]

This tests the DSIR v0.1.1 same-solver quotient rule.

## Solver lineages

A. `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`  
B. repaired `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`

The class_iv repair is the previously validated assertion-checked compile-only removal of one premature brace. No physical equation is modified.

## Common physical deformation

Reference: LambdaCDM.  
Model: smooth constant-w fluid:

\[
w_0=-0.9,\qquad w_a=0,\qquad c_s^2=1.
\]

Matched cosmological parameters include

- `h=0.67`
- `omega_b=0.0224`
- `omega_cdm=0.1200`
- `A_s=2.10e-9`
- `n_s=0.965`
- synchronous gauge
- frozen DSIR redshift nodes
- frozen k nodes `{0.001,0.003,0.01,0.03,0.1} h/Mpc`.

## Calibration A — asymmetric precision

The first successful bridge used p8 precision in GDM_CLASS but default perturbation precision in class_iv.

Result:

\[
\max|\Delta r_{\rm bridge}|=1.0474971491\times10^{-5}.
\]

The largest residual appeared at high k, especially `k=0.1 h/Mpc`, while low-k residuals were often `1e-8--1e-7`. This suggested numerical sampling/precision asymmetry rather than different wCDM physics.

No PASS threshold was imposed.

## Calibration B — identical p8 precision

Both solver lineages were then run with the same p8 precision preset, including matched `k_step_*`, start/tight-coupling, perturbation tolerance and sampling parameters.

Result:

\[
\boxed{\max|\Delta r_{\rm bridge}|=2.3747404043\times10^{-10}}.
\]

The physical response itself reaches about

\[
\max|r_S|\simeq5.0204\times10^{-2}.
\]

Therefore the bridge residual is only about

\[
\frac{2.37\times10^{-10}}{5.02\times10^{-2}}\simeq4.7\times10^{-9}
\]

of the response amplitude.

Interpretation: once numerical precision is matched, the same-solver quotient removes essentially all of the observable code-lineage discrepancy for this nontrivial smooth-wCDM deformation.

## Frozen hard gate

**Before** the final hard rerun, DSIR freezes the conservative threshold

\[
\boxed{\max|\Delta r_{\rm bridge}|\le10^{-9}}.
\]

This is about 4.2 times the matched-p8 calibration maximum and remains many orders of magnitude below the physical response amplitude.

The hard workflow must rerun the full calculation from clean clones. If it exceeds `1e-9`, this experiment does not pass and v0.1.1 remains a candidate.

## Scope

A PASS validates the cross-solver response-quotient architecture for a nontrivial overlapping smooth-wCDM deformation. It does **not** prove that all possible theories or all Boltzmann codes agree at `1e-9`.

Every additional production solver family still requires:

1. a same-solver reference quotient;
2. a source/observable-definition audit;
3. its own zero/control limit;
4. a bridge on an overlapping deformation when practical.

No new dark-sector physics is claimed in Experiment 020.
