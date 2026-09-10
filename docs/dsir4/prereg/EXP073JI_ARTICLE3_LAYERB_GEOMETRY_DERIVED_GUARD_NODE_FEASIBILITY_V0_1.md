# Exp073JI — Article 3 Layer-B geometry-derived guard-node feasibility v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 support only.

Status: PROSPECTIVELY FROZEN AFTER VALIDATED EXP073JH AND BEFORE ANY EXP073JI RESPONSE OUTPUT.

## Bound authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; no covariance restriction is authorized.

Validated Exp073JH run/job `34487047656 / 102903883547`, artifact `10156346630`, independently verified ZIP SHA256 `c89fbebde6e9a635614cdebe7a82b088d3224183d82c6361e8133c8923b04edd`, is support-only `FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_PLUS_0_PLUS_0`.

JH nevertheless established exact kpd10-vs-kpd20 invariance on every inherited atomic target for which its centered-cubic stencil existed: maximum relative component difference `0.0`, no finite/nonzero status change, no row-label change, and no BOSS dense-z disagreement. JH failed feasibility because `3202` target evaluations lacked a complete centered-cubic stencil on the finite 512-node evaluation lattice; those unsupported evaluations propagated NaNs into all 107 retained coordinate rows.

Independent static boundary audit commit `29f081089bd6ce174285446a266dbc59baeed15e` identified this risk before JH terminated. The JH grid has nodes `np.geomspace(1e-4,0.06664762008318016,512)` and a centered-cubic stencil requiring `{j-2,j-1,j,j+1}` with `j=searchsorted(nodes,k)`, so its interpolation support is narrower than the unchanged judged DSIR k-domain near the lattice edges.

## Purpose
Test whether the JH non-feasibility is removed by adding only the minimum **response-blind, geometry-derived guard nodes** required for complete centered-cubic stencil coverage of the inherited Exp073IR atomic support, while preserving:
- every original JG/JH 512 common physical-k node bit-for-bit;
- the exact JH centered-cubic interpolation rule in `ln(k)`;
- the exact Exp073IR atom geometry, masks, physical z/k domain, finite-difference operator, thresholds and row accounting;
- the kpd `{10,20}` cross-check.

No guard count or guard location may be chosen from response values.

## Frozen two-phase execution
Use the exact Exp073IR parent lineage, inputs, 53 DES + 54 BOSS retained coordinate rows and atomic-support construction. No covariance, whitening, nuisance, relation/null, model-selection or withheld-family input may be read.

### Phase A — response-blind geometry scan
Before constructing any new CLASS response:
1. Run the exact Exp073IR atomic traversal with a dummy geometry-only `ResponseSuite` that records every target-k request passed by the inherited code and returns finite positive placeholder arrays only so traversal can complete. The placeholders are not scientific values and MUST be discarded.
2. Record total target evaluations, minimum requested target k, maximum requested target k, minimum/maximum by DES/BOSS when obtainable without changing the inherited traversal, and a SHA256 over a canonical stream of `(kpd,response_call_ordinal,target_index,target_k_binary64)` records.
3. The geometry scan MUST use the unchanged judged domain and masks from Exp073IR; it must not clip or add atoms.

### Guard-node construction
Let the original frozen base lattice be exactly
`base = np.geomspace(1e-4,0.06664762008318016,512,dtype=float64)`
and let the frozen logarithmic ratio be `r = base[1]/base[0]` in binary64.

Construct an extended lattice only by prepending/appending whole same-ratio nodes:
- lower guard nodes are `base[0] / r**m`, integer `m>=1`;
- upper guard nodes are `base[-1] * r**m`, integer `m>=1`.

Choose the **smallest nonnegative integers `(n_lo,n_hi)`** such that every Phase-A target has a complete centered-cubic stencil under the unchanged JH validity rule `j>=2 and j<=len(nodes)-2`, where `j=searchsorted(extended_nodes,target)`.

Requirements:
- all original 512 base nodes must appear unchanged and in the same order inside the extended lattice;
- total node count must be `<=640`; exceeding this bound is `INVALID_INFRA_PLUS_0_PLUS_0` and must not trigger retuning;
- after construction, a geometry-only exhaustive check must prove zero unsupported inherited targets before any scientific response calculation begins;
- exact `(n_lo,n_hi)`, node count, endpoints, ratio and geometry-stream SHA256 must be recorded in the artifact.

### Phase B — full response feasibility
Use pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`, the audited public gauge-invariant `d_m` exposure, exact baseline/precision inputs and the same four models `(alpha,beta)=(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`.

Finite-difference `h=1e-4` and `REL_TOL=1e-3` remain frozen.

For each native-density setting `k_per_decade_for_pk in {10,20}`:
1. inject the exact geometry-derived extended common lattice through `k_output_values` for every model;
2. recover requested node coordinates from public transfer output with relative mismatch `<=1e-12`;
3. interpolate only between requested common nodes, never model-dependent native nodes;
4. use the exact JH centered-cubic Lagrange interpolation in `x=ln(k)` with stencil `{j-2,j-1,j,j+1}`;
5. compute exactly the inherited Exp073IR alpha-left one-sided and beta-symmetric finite-difference responses and absolute component magnitudes;
6. reuse the exact original Exp073IR atomic convergence and Layer-B accounting logic.

Infrastructure patches may only enlarge `_MAX_NUMBER_OF_K_FILES_` sufficiently for the prospectively bounded `<=640` requested nodes and retain the already-audited parser argument capacity `32768`. Exact one-replacement and pre/post SHA256 provenance is mandatory. No equation, transfer definition or scientific threshold may change.

## Frozen feasibility decision
A complete run is `GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0` only if all are true:
- Phase-A guard construction is deterministic and valid, with total nodes `<=640`;
- exhaustive geometry check after guard construction has exactly zero unsupported inherited target evaluations;
- Phase-B response engine reports exactly zero unsupported target evaluations for both kpd values;
- no finite/nonzero-status change, row-label change or BOSS dense-z disagreement occurs between kpd10 and kpd20;
- maximum atomic kpd10-vs-kpd20 relative component difference is `<1e-3`;
- inherited Layer-B invalid-row fraction is `<=0.05` and retained dimension is `>=15`.

Otherwise, a valid numerical run is `GUARD_NODE_FULL_SUPPORT_NOT_FEASIBLE_PLUS_0_PLUS_0`, preserving exact failure diagnostics. Lineage/hash/build/download/parser/capacity/geometry/provenance failures are `INVALID_INFRA_PLUS_0_PLUS_0`.

## Interpretation boundary
Exp073JI is support-only `+0/+0` in every outcome. A feasibility PASS may authorize only the design of a separate prospectively frozen accuracy/calibration or scientific Layer-B convergence rerun. It MUST NOT itself retroactively PASS Exp073IR, authorize covariance restriction, open Wm_S3, or create model/manuscript authority.

No post-hoc clipping, extrapolation, atom removal, row removal, interpolation-rule switching, averaging, tolerance change, physical-domain change or guard-node tuning from response values is allowed.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; finite-difference `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
