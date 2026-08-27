# Exp073A — GR-reference linear/no-CLEFT perturbativity eligibility audit — preregistration v0.1

**Date frozen:** 2026-08-27  
**Status:** PREREGISTERED BEFORE ANY Exp073A PERTURBATIVITY OUTPUT IS EVALUATED

## 1. Motivation

Exp072C completed with

`DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_FOUND_EXP072C`

and found one unique nondominated ACT×unWISE support rectangle under the already-frozen 5% positive-operator leakage rule:

- `z_min = 0.0087345857837422`;
- `z_max = 2.33`;
- `k_min = 0.000704833374744468 Mpc^-1`;
- `k_max = 4.818261097432861 Mpc^-1`.

At that rectangle the minimum geometrically retained route contains exactly 15/26 coordinates.

This rectangle is planning geometry only. It is not C3 or C5 provider certification.

Before attempting any very large C3/C5 extension, Exp073A asks a more basic question:

> Does the unique Exp072C rectangle retain the frozen minimum ACT×unWISE route after cells that are already non-perturbative in the pinned GR linear matter reference are treated as physically ineligible for the current linear/no-CLEFT route?

Exp073A is a necessary perturbativity screen for the current linear/no-CLEFT observational path. It is not a nonlinear dark-sector calculation and does not validate a provider extension.

## 2. Immutable Exp072C parent binding

Bind exactly the completed Exp072C record:

- implementation merge `b442cddd6ba032d1261a0994bc1c4f5cf899a9f7`;
- workflow run `33031427090`;
- workflow job `98384598473`;
- artifact `9630407069`;
- artifact digest `sha256:0e726d9f12b2b8951a4d2598b3723d54db1a14c09070d8e8770d5256773f2a71`;
- extracted JSON SHA256 `d0d8e6a19177f4a7b94d2f0b95d6fee3b5cd85078e8eadee06e7f0faaf5864c0`;
- classification `DIAGNOSTIC_JOINT_LOWZ_HIGHK_FRONTIER_FOUND_EXP072C`;
- all Exp072C C1–C8 controls PASS;
- Pareto frontier count exactly `1`;
- frontier exactly `(z_min,k_max)=(0.0087345857837422,4.818261097432861 Mpc^-1)`;
- route snapshot exactly 15 retained coordinates with Blue `gg=1,kg=4` and Green `gg=3,kg=7`.

Exp072A remains permanent scientific FAIL and Exp072B remains K-only-target-not-found regardless of Exp073A outcome.

## 3. Frozen external/geometry provenance

Use exactly the same geometry/provenance path as Exp072A/B/C:

- `ACTCollaboration/unWISExLens_lklh@6302c30d9e70f8e4ff2d4a84a9977b4471705179`;
- `cmbant/CAMB@fa3f097343fbbe427cc04b4f5f0041c22c6ec764`;
- official ACT×unWISE archive SHA256 `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`;
- exact released tracer construction;
- exact positive kernels and `1/f_K^2` geometry;
- exact HEALPix pixel window, released transfer functions and absolute released bandwindow weights;
- exact 26-coordinate / 64 coordinate-block ordering;
- exact 96-point Gauss-Legendre redshift projection over `z in [0,3]`;
- `ell=0,...,6143` and exact Limber map `k=(ell+0.5)/f_K(chi)`.

No covariance or downstream fitted quantity enters Exp073A.

## 4. Frozen GR linear matter reference

Use the exact pinned CAMB physical baseline already used by the validated ACT×unWISE forward-geometry path:

- `H0=67 km/s/Mpc`;
- `ombh2=0.0224`;
- `omch2=0.1200`;
- `mnu=0`;
- `nnu=3.046`;
- `TCMB=2.7255 K`;
- `YHe=0.24`;
- `As=2.10e-9`;
- `ns=0.965`;
- flat `w=-1`;
- `tau=0`;
- `WantCls=False`;
- `NonLinear_none`;
- 128 CAMB matter redshift nodes over `z in [0,3]` exactly as in `ci/act_unwise_physical_forward_reproduction_v0_1.py`;
- CAMB internal matter-power `kmax=12 Mpc^-1`;
- physical matter-power interface with `nonlinear=False`, `hubble_units=False`, `k_hunit=False`, `extrap_kmax=None`;
- matter variable pair `delta_nonu × delta_nonu`.

The Exp072C frontier maximum `4.818261097432861 Mpc^-1` must lie strictly inside the available CAMB reference support. No extrapolation is allowed.

This GR reference is used only to determine whether the current linear/no-CLEFT route is already non-perturbative in the baseline cosmology. It is not a substitute for future C3/C5 provider certification.

## 5. Frozen perturbativity statistic

For every exact projection cell inside the Exp072C frontier rectangle, evaluate the pinned linear matter power in physical units and define

`Delta2_m(k,z) = k^3 P_mm^lin(k,z)/(2*pi^2)`.

The primary perturbative-eligibility condition is frozen as

`Delta2_m <= 1`.

`Delta2_m = 1` passes exactly.

Rationale fixed before computation: `Delta2_m` is the dimensionless linear matter variance per logarithmic k interval; order-unity linear variance is a necessary warning boundary for a purely linear/no-CLEFT treatment. This is a necessary screen, not a sufficient proof of perturbative accuracy.

Two non-classifying sensitivity masks must also be recorded:

- conservative diagnostic: `Delta2_m <= 0.5`;
- relaxed diagnostic: `Delta2_m <= 2.0`.

Only the primary `Delta2_m <= 1` mask determines the Exp073A scientific classification.

## 6. Combined physical-support leakage

For each of the same 64 coordinate-block pairs, let `w(z,ell)>=0` be the exact positive Exp072C weight and `D_pair=sum(w)` its unchanged full denominator.

Define the frozen Exp072C geometric-validity mask

`G = (0.0087345857837422 <= z <= 2.33) AND (0.000704833374744468 <= k <= 4.818261097432861)`.

For perturbativity threshold `T`, define

`Q_T = (Delta2_m <= T)`.

The combined valid fraction is

`F_valid,T = sum[w * G * Q_T] / D_pair`.

The combined invalid fraction is

`L_T = 1 - F_valid,T`.

For the primary threshold `T=1`, a coordinate-block pair passes iff

`L_1 <= 0.05`.

Equality passes.

A coordinate passes iff every applicable block passes:

- `gg -> [mm,Wm,WW]`;
- `kg -> [Wm,WW]`.

The route passes iff the unchanged minimum requirements hold:

- retained dimension `>=15`;
- Blue retains at least one `gg` and at least one `kg`;
- Green retains at least one `gg` and at least one `kg`.

Because the perturbativity mask can only remove weight, Exp073A may not admit any coordinate that failed the Exp072C geometric rectangle.

## 7. Required decomposition

For every pair record separately:

- Exp072C geometric leakage `L_geom = 1-sum[w*G]/D_pair`;
- incremental non-perturbative fraction inside the geometric rectangle for `T=1`,
  `N_1 = sum[w*G*(Delta2_m>1)]/D_pair`;
- combined leakage `L_1`;
- the same `N_T` / `L_T` for diagnostic `T={0.5,2}`;
- maximum and positive-weight median `Delta2_m` over geometrically valid cells;
- whether the pair/coordinate survives at each T.

Require the disjoint closure

`|L_1 - (L_geom + N_1)| <= 128*eps(float64)`

and analogously for `T={0.5,2}`.

## 8. Unit/interface control

At frozen probe values

- `z = {0.0087345857837422, 0.295, 1.0}`;
- `k = {0.01, 0.1, 1.0, 4.0} Mpc^-1`,

independently request the same linear `delta_nonu × delta_nonu` matter power in CAMB's `(k/h,(Mpc/h)^3)` convention and convert back using

`k = h*k_h`,

`P_Mpc3 = P_(Mpc/h)^3 / h^3`.

Require maximum relative agreement with the direct physical-unit request `<=2e-8`.

This tolerance is frozen before Exp073A output and reuses the already-established DSIR CAMB unit-roundtrip scale; it is not tuned to the perturbativity result.

## 9. Hard controls

P1. exact Exp072C immutable artifact/classification/frontier binding;

P2. exact upstream/CAMB/archive/source/operator provenance and exact 26-coordinate/64-pair ordering;

P3. reproduce Exp072C per-pair geometric leakage at the unique frontier within absolute `5e-13` and reproduce the exact 15-coordinate Exp072C route snapshot before applying perturbativity;

P4. every CAMB `P_mm^lin` value used by the primary mask is finite and positive, all evaluated frontier cells are inside the non-extrapolated pinned CAMB support, and nonlinear corrections remain disabled;

P5. frozen physical-unit roundtrip maximum relative discrepancy `<=2e-8`;

P6. combined geometric+perturbativity leakage closure for every pair and each `T={0.5,1,2}` within `128*eps(float64)`;

P7. monotonic sensitivity ordering must hold: the retained route at `T=0.5` is a subset of/equal to the route at `T=1`, which is a subset of/equal to the route at `T=2`;

P8. no covariance, Cholesky/whitener, nuisance SVD/rank, G7 relation/null, G8 response, article-selection quantity, C3 provider extension or C5 provider extension is read or executed.

If any P1–P8 control fails after complete numerical evaluation, classify

`FAIL_EXP073A_REPRODUCTION_OR_PROVENANCE`.

Infrastructure failure before complete evaluation is `INCOMPLETE_EXP073A` and is not a scientific classification.

## 10. Scientific classification

If all P1–P8 pass and the primary `T=1` combined mask still satisfies the unchanged route requirements, classify

`ELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`.

This means only that the pinned GR reference does not itself invalidate the current linear/no-CLEFT route under this necessary screen. It does not certify C3/C5 perturbativity or close G7.

If all P1–P8 pass but the primary `T=1` combined mask fails the unchanged route requirements, classify

`INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`.

This is a scientific negative result for the current linear/no-CLEFT ACT×unWISE route under the frozen perturbativity screen. It does not falsify GDM, designer-f(R), dark energy, modified gravity, or DSIR itself.

## 11. Anti-retuning and downstream rule

After the first Exp073A output do not change:

- the Exp072C frontier;
- `Delta2_m` definition;
- the primary threshold `1`;
- diagnostic thresholds `0.5` and `2`;
- the 5% combined-leakage threshold;
- the 15-coordinate/Blue/Green/gg/kg route requirements;
- the CAMB baseline or unit conventions;
- any hard-control tolerance.

If Exp073A returns `INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`, do not blindly extend linear C3/C5 providers to the Exp072C frontier. The next admissible research branch is a separately preregistered solver-neutral nonlinear matter/Weyl feasibility audit; upstream matter-to-Weyl closure may not be assumed for MG/dark-sector models.

If Exp073A returns `ELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A`, a C3+C5 physical-provider extension still requires a separate prospective certification under `docs/PROVIDER_EXTENSION_NATIVE_SUPPORT_BOUNDARY_2026-08-27.md`.

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
