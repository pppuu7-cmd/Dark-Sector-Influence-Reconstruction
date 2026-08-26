# Exp069E — C5 exact-zero source-native Return-to-GR function-floor audit v0.1

**Date:** 2026-08-27  
**Status:** PROSPECTIVE MECHANISM PREREGISTRATION — frozen before any Exp069E solver execution.

## Why this experiment is now allowed

Exp069B remains permanently `FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`: the literal designer-f(R) `B0=0` path differs from ordinary GR by slightly more than the frozen `5e-6` power criterion.

Exp069C showed that this is already present in same-node raw powers and does not converge away when `k_per_logint` is increased from 40 to 320.

Exp069D is not a formally complete mechanism audit because its `EFTCAMB_skip_RGR=True` B0 case is declared unstable by the pinned solver. Nevertheless its completed cases show three strong facts that are not reinterpreted here:

- changing `model_background_num_points=3000,6000,12000,24000` leaves the all-block power residual unchanged at about `5.302921926e-6`;
- ordinary-GR and designer-`B0=0` `H(z)`/comoving-distance geometry agree exactly at the frozen nodes;
- changing `EFTCAMB_GR_threshold=1e-10,1e-8,1e-6` leaves the same power residual unchanged.

Pinned upstream source supplies a more direct causal observable. `09_EFTCAMB_RGR.f90` constructs a Return-to-GR vector from EFT functions explicitly described as values relative to their GR values. The pinned Python wrapper exposes the already-computed timestep cache through `EFTCAMB.get_eft_functions(...)`. Exp069E therefore asks whether the literal exact-zero designer state contains a nonzero solver-native RGR-function residue even though its background geometry is GR-identical.

This is a mechanism audit only. It cannot certify C5, change Exp069B, authorize a support mask, or close G7/G8/G9.

## Frozen upstream and cosmology

Use exactly `EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904` and the Exp069B/069C/069D matched ordinary cosmology:

- `H0 = 67 km/s/Mpc`;
- `ombh2 = 0.0224`;
- `omch2 = 0.1200`;
- no massive neutrinos, `massless_neutrinos = 3.046`;
- `helium_fraction = 0.2404`;
- `scalar_amp(1)=2.10e-9`;
- `scalar_spectral_index(1)=0.965`;
- no reionization;
- linear power only;
- `kmax=0.30 Mpc^-1`, `k_per_logint=320`.

Designer settings are exactly the established explicit-EFT branch:

- `EFTflag=3`, `DesignerEFTmodel=1`, `EFTwDE=0`;
- `model_background_num_points=6000`;
- `EFTCAMB_skip_RGR=False`;
- `EFTCAMB_GR_threshold=1e-8`;
- all Exp069B stability options unchanged.

## Frozen B0 sequence

Run one ordinary-GR reference (`EFTflag=0`) and designer cases in this exact order:

`B0 = [0, 1e-12, 1e-10, 1e-8, 1e-6]`.

The positive points are mechanism controls only; `B0=1e-6` is the previously frozen production-scale point. Failure/instability of any tiny-positive case is recorded as a case result and must not be replaced by a different B0 after inspection.

## Frozen time and power nodes

For source-native EFT functions query scale factors

`a = [0.01, 0.1, 0.25, 1/(1+2.33), 1/(1+1.491), 1/(1+0.934), 1/(1+0.51), 1/(1+0.295), 1.0]`

in ascending order after numerical evaluation/deduplication.

Power comparison remains exactly at

- `z = [0.0, 0.295, 0.51, 0.934, 1.491, 2.33, 3.0]`;
- `k = [0.003, 0.01, 0.03, 0.10, 0.20] Mpc^-1`;
- blocks `P_mm`, signed `P_Wm`, and `P_WW` using `delta_nonu` and `Weyl` exactly as in Exp069B/C/D.

## Source-native RGR subset

Use `pars.EFTCAMB.get_eft_functions(results, a)` without modifying upstream source. Construct exactly the subset of the pinned `EFTCAMBReturnToGR_functions` entries that can be reconstructed directly from returned timestep-cache fields without an external parameter-cache constant:

1. `abs(EFTOmegaV)`;
2. `abs(a * adotoa * EFTOmegaP)`;
5. `abs(EFTc/a^2)`;
7. `abs(EFTcdot/a^2)`;
8. `abs(EFTLambdadot/a^2)`;
9–16 and 18–21: `abs(EFTGamma{1..6}{V/P})` in the exact upstream order.

Do **not** silently reconstruct upstream entry 6, `abs(EFTLambda/a^2 + params_cache%grhov)`, because `params_cache%grhov` is not part of the same public Python timestep-cache interface. The output must explicitly call this the `RGR_SUBSET_EXCLUDING_LAMBDA_OFFSET` rather than the full RGR vector.

The primary exact-zero metric is

`F0 = max_{a, selected entries} RGR_subset(B0=0,a)`.

Also report every selected component at every scale factor, `F(B0)` for all successful designer cases, and `F0 / eps_float64`.

## Frozen exact-zero classification

No post-hoc amplitude threshold is introduced.

- If every selected exact-zero RGR-subset entry is bitwise/numerically exactly `0.0` as returned/reconstructed in float64, classify `EXACT_ZERO_RGR_SUBSET_BITWISE_ZERO`.
- Otherwise classify `EXACT_ZERO_RGR_SUBSET_NONZERO`.

This classification is deliberately stronger and simpler than choosing a new tolerance after seeing the values. Its scientific interpretation is limited: a nonzero entry localizes a numerical/branch residue in source-native EFT-function coordinates but does **not** prove that its magnitude causes the power residual.

## Frozen power-floor comparison

For every successful designer case compute the maximum absolute relative ordinary-GR residual over the same target power blocks, denoted `M(B0)`. Preserve signed residual arrays as well.

For `B0=0` record `M0` and compare it only descriptively to Exp069B/C/D. No threshold is changed.

For the positive B0 sequence report:

- whether `F(B0)` is monotone nondecreasing with B0 over successful positive points;
- whether `M(B0)` is monotone nondecreasing with B0 over successful positive points;
- Pearson correlation between `log10(B0)` and `log10(F)` when all involved `F>0` and at least three positive cases succeed;
- Pearson correlation between `log10(F)` and `log10(M)` when both are positive and at least three positive cases succeed.

These are descriptive mechanism diagnostics and have no pass threshold.

## Integrity controls

The workflow must require:

- pinned upstream SHA before and after execution;
- explicit designer readback matches all requested branch/stability/RGR/background-point parameters;
- `NonLinear_none` for every case;
- exact frozen `B0`, `a`, `z`, `k`, block and component order;
- no upstream source modification;
- no pseudoinverse, smoothing, interpolation of EFT functions, jitter, threshold retuning, or case replacement;
- ordinary GR is used only as the power reference, not as a fake EFT-cache provider;
- Exp069B stays FAIL and Exp069D stays formally incomplete regardless of Exp069E outcome;
- G7/G8/G9 remain OPEN.

## Interpretation tree

- `EXACT_ZERO_RGR_SUBSET_NONZERO` + persistent `M0`: evidence that the literal designer-zero branch is not represented as exact GR in at least one source-native EFT-function coordinate, consistent with a branch floor. It is **not** yet a corrective bridge.
- `EXACT_ZERO_RGR_SUBSET_BITWISE_ZERO` + persistent `M0`: the ppm discrepancy is pushed downstream of these background EFT coordinates, toward perturbation initialization/evolution/branch-switch semantics.
- case instability/failure: record it separately; do not substitute values.

A future C5 corrective bridge is allowed only after this mechanism is localized sufficiently to justify a separately preregistered physical route satisfying the unchanged hard GR-limit requirement.
