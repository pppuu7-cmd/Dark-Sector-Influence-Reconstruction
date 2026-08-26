# Exp069F — C5 explicit-EFT general-accuracy convergence audit v0.1

**Date:** 2026-08-27  
**Status:** PROSPECTIVE MECHANISM PREREGISTRATION — freeze before any Exp069F solver execution.

## Motivation

Exp069E completed and found a source-native exact-zero EFT residue `F0=4.7401579076280133e-17`, while the all-block ordinary-GR power residual remains `M0=5.302921926164412e-6`. The source residue is smaller than one float64 epsilon in the frozen normalized coordinates and cannot plausibly account directly for the ppm power mismatch by amplitude.

A post-output immutable-artifact diagnostic also found that designer `B0=0,1e-12,1e-10,1e-8` have bitwise-identical stored raw and target `P_mm/P_Wm/P_WW`, even while `F(B0)` changes strongly. The common GR-vs-explicit-EFT residual is mainly scale-dependent, weakly redshift-dependent and highly correlated across the three power blocks.

Exp069C already ruled out matter-power k sampling density (`k_per_logint=40..320`) as the explanation. Exp069D ruled out designer background interpolation density (`model_background_num_points=3000..24000`) and RGR-threshold changes at B0=0. What has not been tested is the ordinary CAMB Boltzmann/integration accuracy itself.

Exp069F therefore asks one narrow causal question:

> Does increasing the solver's general integration/hierarchy accuracy, with all physical settings and k sampling fixed, recover the pre-existing hard `5e-6` designer-zero versus ordinary-GR power limit?

This is not a provider certification. It cannot reclassify Exp069B.

## Frozen upstream and physics

Use exactly:

`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

Use the same Exp069B/C/D/E cosmology:

- `H0=67 km/s/Mpc`;
- `ombh2=0.0224`;
- `omch2=0.1200`;
- no massive neutrinos;
- `massless_neutrinos=3.046`;
- `helium_fraction=0.2404`;
- `A_s=2.10e-9`;
- `n_s=0.965`;
- no reionization;
- linear power only.

For explicit designer zero use the unchanged branch:

- `EFTflag=3`;
- `DesignerEFTmodel=1`;
- `EFTwDE=0`;
- `EFTB0=0`;
- `model_background_num_points=6000`;
- `EFTCAMB_skip_RGR=False`;
- `EFTCAMB_GR_threshold=1e-8`;
- all established stability flags unchanged.

Ordinary GR remains `EFTflag=0`.

## Frozen accuracy ladder

Use paired ordinary-GR and designer-zero runs at exactly

`AccuracyBoost = [1.0, 2.0, 3.0, 4.0]`.

For each pair set through the public Python API:

- `AccuracyBoost = q`;
- `lAccuracyBoost = q`;
- `lSampleBoost = 1.0`;
- `DoLateRadTruncation = True`.

`high_accuracy_default` and `transfer_high_precision` remain as inherited from the same pinned base configuration; they are not toggled in this experiment.

No accuracy point may be added, removed or replaced after output inspection.

## Frozen power sampling

Keep the Exp069E high-k-density settings fixed:

- `kmax=0.30 Mpc^-1`;
- `k_per_logint=320`;
- `z=[0.0,0.295,0.51,0.934,1.491,2.33,3.0]`;
- `k=[0.003,0.01,0.03,0.10,0.20] Mpc^-1`;
- blocks `P_mm`, signed `P_Wm`, `P_WW` from `delta_nonu` and `Weyl` exactly as in Exp069E.

Store both solver-native raw grids/powers and target-grid powers. Require ordinary-GR and designer-zero raw k/z grids within each accuracy pair to be exactly identical before same-node raw residuals are interpreted.

## Frozen primary metric

For each accuracy level `q`, compute

`M_q = max_{z,k,blocks} abs(P_designer0/P_GR - 1)`

on the frozen target grid.

Also compute the analogous same-node raw maximum `R_q` if raw grids are exactly identical.

The hard closure scale is **not changed**:

`M_q <= 5e-6`.

This is the same scientific GR-limit scale whose violation made Exp069B a permanent FAIL.

## Frozen primary classification

Let the four frozen values be `M_1,M_2,M_3,M_4`.

- If at least one accuracy point with `q>1` satisfies the unchanged hard limit `M_q<=5e-6`, classify
  `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`.
- Otherwise classify
  `GENERAL_ACCURACY_DOES_NOT_RECOVER_FROZEN_GR_LIMIT`.

If recovery occurs, report the first passing accuracy level in the pre-frozen ascending ladder. This is only a candidate setting for a separately preregistered provider-certification experiment; Exp069F itself still does not certify C5.

No new ratio or significance threshold is used for the primary classification.

## Frozen convergence diagnostics

Report, without additional pass thresholds:

- `M_q` and `R_q` for all q;
- pairwise ratios `M_q/M_1` and `R_q/R_1` where defined;
- whether `M_q` is monotone nonincreasing with q;
- whether `R_q` is monotone nonincreasing with q;
- signed target residual arrays for every block and q;
- correlation of each higher-q residual array with the q=1 residual array;
- max block-to-block residual differences within each q.

These are mechanism diagnostics only.

## Frozen early-background / transfer diagnostics

At every q, store ordinary-GR and designer-zero values from the public CAMB results interface for the following derived quantities when available:

- `age`;
- `zstar`, `rstar`, `thetastar`, `DAstar`;
- `zdrag`, `rdrag`;
- `kd`, `thetad` or equivalent returned damping-scale keys;
- `zeq`, `keq`, `thetaeq` when returned.

Also query both runs on the fixed redshift set

`z_bg=[0,3,10,100,1000,1100,1e4,1e6]`

for public `H(z)` and conformal-time values when supported by the pinned API.

Missing derived keys are recorded as missing and are not replaced after inspection. Relative differences are descriptive; no new acceptance threshold is assigned to them in Exp069F.

## Integrity controls

Require:

1. pinned upstream SHA before and after all cases;
2. exact requested/readback designer branch settings;
3. exact public `AccuracyBoost/lAccuracyBoost/lSampleBoost/DoLateRadTruncation` values for each case;
4. `NonLinear_none` for every run;
5. exact frozen pair order `q=[1,2,3,4]`, with GR followed by designer zero inside each pair;
6. fixed `k_per_logint=320`, power nodes and block definitions;
7. no upstream source modification;
8. no pseudoinverse, smoothing, power-floor subtraction, normalization fit, jitter or residual correction;
9. no change to the `5e-6` hard GR-limit scale;
10. Exp069B remains permanent FAIL, Exp069D remains formally incomplete, Exp069E remains its own completed mechanism result;
11. no support-validity mask, covariance/nuisance advance or G7 promotion from this audit alone.

## Interpretation tree frozen before execution

### A. `GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`

The ppm floor is sufficiently solver-accuracy-sensitive that an unmodified high-precision EFTCAMB route may be viable. The next step is a separately preregistered C5 provider certification at the first frozen passing accuracy, including exact-zero closure, positive production B0 signal, signed `P_Wm/P_WW/P_mm`, repeatability and no-state-mutation controls.

### B. `GENERAL_ACCURACY_DOES_NOT_RECOVER_FROZEN_GR_LIMIT`

General solver accuracy is not an authorized corrective explanation. The next mechanism audit must target the explicit-EFT early background/thermal handoff (`EFTCAMB_back_turn_on`) and/or branch-specific transfer initialization, guided by the early-background diagnostics. Do not special-case zero or subtract the floor without a new preregistration.

### C. Infrastructure/case failure

Record failure separately. Do not replace accuracy values or lower the criterion.

## Gate state

Regardless of outcome:

- C5 provider remains NOT CERTIFIED by Exp069F itself;
- common support mask remains unauthorized;
- G7=OPEN;
- G8=OPEN;
- G9=OPEN.
