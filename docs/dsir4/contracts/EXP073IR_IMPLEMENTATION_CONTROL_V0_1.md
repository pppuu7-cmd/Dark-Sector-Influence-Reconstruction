# Exp073IR implementation-control freeze v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 / Exp073IR only.

Status: PROSPECTIVE IMPLEMENTATION CONTROL FROZEN AFTER `EXP073IR_ARTICLE3_REAL_LAYERB_COMMON_RESPONSE_V0_1.md` AND BEFORE ANY Exp073IR real response value or classification is produced.

This document changes no scientific acceptance criterion. It only removes implementation ambiguities needed to execute the already-frozen Exp073IR contract on the inherited 107-row `S_op`.

## 1. Immutable science remains unchanged

The immutable parent is `EXP073IQ_ARTICLE3_REAL_LAYERA_SUPPORT_PASS_V0_1.json` and its exact 107 retained coordinates. The two response components, `h=1e-4`, pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`, direct gauge-invariant public `d_m` route, physical domain, strict finite/nonzero rule, `f_B<=0.05`, minimum retained dimension 15, and downstream covariance firewall are unchanged.

No effective `ell`, `z`, or `k` is introduced.

## 2. CLASS native-k convergence control

The production transfer calculation uses the pinned solver's native precision setting

`k_per_decade_for_pk = 10`

which is the upstream default at the pinned commit.

The prospectively denser control uses exactly

`k_per_decade_for_pk = 20`.

Every other frozen physical and p8 precision parameter is identical between the two calculations. The dense calculation is a numerical convergence control only and cannot create a PASS that the production calculation does not have.

For both calculations, requested survey atom `k` values are evaluated only by piecewise-linear interpolation in `ln(k)` between bracketing solver-native samples. Extrapolation is forbidden. Any active atom lacking brackets in either calculation makes Exp073IR `NUMERICALLY_UNRESOLVED_EXP073IR`.

The frozen Exp073IR convergence requirements remain:
- identical finite/nonzero state for every compared response cell;
- identical Layer-B row labels;
- maximum relative component difference <= `1e-3` over cells finite and strictly positive in both runs.

No epsilon enters the scientific finite/nonzero classification.

## 3. DES atom execution

DES uses exactly the factorized broad support already admitted by Exp073IM/Exp073IQ:
`abs(W_q[band,ell]) * B_q(z)` on the exact 2001-node Exp073Z2 fine radial representation.

For Layer B, a DES atom is active exactly when:
- the inherited angular absolute support is strictly positive;
- the inherited radial support value is strictly positive;
- its literal radial node satisfies `0.295<=z<=2.33`;
- `k=(ell+0.5)/chi(z)` satisfies `0<k<=0.06664762008318016 Mpc^-1`.

The response field may be evaluated/checked in a streamed factorized form. Materializing row-duplicated Cartesian arrays is not required for classification and would not change the atom set.

## 4. BOSS z3 support execution without effective-z substitution

Exp073W froze the BOSS z3 survey support as the open interval `(0.5,0.75)` and explicitly forbade effective-z substitution. Exp073IR therefore does not use `z_eff`, midpoint, mean, or any scalar proxy.

The deterministic production quadrature representation of that inherited open support is fixed prospectively to a 64-node Gauss-Legendre rule on `(0.5,0.75)`. All Gauss-Legendre weights are strictly positive; Layer B uses only the positive-support atom predicate, not their amplitudes.

A stricter numerical support control is fixed prospectively to a 128-node Gauss-Legendre rule on the same open interval. It is a one-way fail-closed control:
- if production and dense-z certification disagree on a row's finite/nonzero status, classify the experiment `NUMERICALLY_UNRESOLVED_EXP073IR`;
- the dense-z control cannot rescue any production-invalid row.

For each BOSS redshift node, the k support is exactly the inherited Exp073W `C=W@M` true-k cells with positive absolute row weight and the frozen physical k cut. No effective k is used.

## 5. Transport and build compatibility

The pinned CLASS-IV equations/source are not altered. The already-audited Exp073HB exact modern-toolchain compatibility shim may be applied. If the legacy Python wrapper requires removal of the obsolete simultaneous `-liomp5` link flag while retaining GNU OpenMP `-lgomp`, this is a build-only compatibility edit to `python/setup.py`; it changes no solver equation, precision parameter, source variable, transfer value, or scientific rule.

Failure to build/import the pinned wrapper, missing exact artifacts, hash/provenance mismatch, or solver/runtime failure is `INVALID_FOR_SCIENCE_ARTICLE3_SUPPORT` (or infrastructure failure), never scientific FAIL.

## 6. Output/accounting

The classifying JSON must record:
- exact parent authority/run/job/artifact;
- ordered component names;
- production/dense native-k settings;
- native transfer k-key/unit route;
- per-row active atom count, strict finite/nonzero label and component minima;
- convergence maxima/disagreement flags;
- invalid-row count, `f_B`, retained dimension;
- anti-leakage flags and covariance authorization.

Scientific readiness earns credit only for a valid real `PASS_PHYSICAL_SUPPORT_ARTICLE3`. Implementation, workflow construction, synthetic checks, INVALID, or NUMERICALLY_UNRESOLVED outcomes earn no readiness increase.
