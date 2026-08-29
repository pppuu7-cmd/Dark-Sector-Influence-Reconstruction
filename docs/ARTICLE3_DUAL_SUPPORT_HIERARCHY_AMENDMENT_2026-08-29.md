# Article 3 dual physical-support hierarchy amendment

**Frozen:** 2026-08-29, before any real hosted Exp073R1 terminal result, before any real operator-support result, before any real Article-3 coordinate-support result, and before covariance inspection.

## Why this amendment is necessary

A pre-execution audit identified that two previously preregistered support quantities answer different physical questions and neither safely substitutes for the other.

### Layer A — broad finite-operator support leakage

The legacy Exp073P methodology in

`experiments/073p_cosmotheka_desy1_boss_exact_common_physical_support_prereg_v0_1.md`

propagates the **positive absolute bandpower/window response envelope** through the physical `(k,z)` support. For a finite observation row it evaluates a weighted leakage fraction

`operator_f_invalid = positive operator-envelope weight outside the frozen physical domain / total positive operator-envelope weight`.

This is necessary for DES pseudo-C_ell observables because a single measured bandpower is not localized at one physical `(k,z)` point. The pinned Cosmotheka implementation explicitly constructs a NaMaster mode-coupling workspace and bandpower windows via `w.get_bandpower_windows()`; the preregistered Wm/WW support audit propagates those broad windows through lens/source kernels.

### Layer B — final-coordinate/common-response validity

The later contract

`docs/ARTICLE3_PHYSICAL_SUPPORT_GATE_CONTRACT_2026-08-28.md`

checks a different quantity:

`article3_coordinate_f_invalid = N(geometrically eligible coordinates with invalid common final-response envelope) / N(geometrically eligible coordinates)`.

It also enforces unique inherited coordinate identity/order, finite strictly positive physical k, and finite strictly positive `final_response_abs_values` for every preregistered response component.

This is a final-coordinate numerical/common-response validity test. It does not integrate a broad survey window and therefore cannot by itself certify that a pseudo-C_ell/BOSS row has negligible support outside the allowed physical domain.

## Scientific conclusion of the audit

The two tests are **not alternative definitions of the same f_invalid**. They are sequential necessary conditions:

1. the observation row must be sufficiently localized inside the frozen physical domain under its full positive operator envelope;
2. the surviving row must then have a valid common final-response representation under the later Article-3 coordinate contract.

Using only Layer B would permit an effective `(z,k)` label to conceal broad out-of-domain support. Using only Layer A would not enforce the later common-response/coordinate-integrity conditions. Requiring both reuses already-preregistered criteria and introduces no outcome-conditioned threshold.

## Frozen current order

The current Article-3 support chain is therefore:

`genuine hosted reproduction authority`

`-> full pre-support finite observation operator and immutable candidate ordering`

`-> Layer A: broad operator-support leakage audit on Wm, WW and the already-frozen BOSS mm component`

`-> freeze operator-support-retained set S_op in inherited ordinal order`

`-> Layer B: Article-3 coordinate/common-response envelope audit on S_op using the later coordinate contract`

`-> freeze final retained set S`

`-> restrict the already-built finite operator to S`

`-> covariance coordinate binding/restriction`

`-> covariance validation + Cholesky whitening`

`-> signed nuisance subspace / quotient`

`-> relation/null and later falsification gates`.

No covariance or downstream quantity may participate in either support layer.

## Layer-A criteria — no change from preregistered operator support

The current implementation must preserve the legacy scientific content rather than silently reinterpret it:

- pinned Cosmotheka DES-Y1 Wm/WW finite harmonic operator source and exact public-data provenance;
- classifying DES route `nside=4096`;
- exact frozen bandpower edges;
- positive absolute response/window envelope for support bookkeeping while the measured Wm observable remains signed;
- physical support bookkeeping through the exact preregistered lens/source kernels;
- no fiducial P(k), nonlinear boost, covariance, nuisance, relation/null or G8 weighting in numerator or denominator;
- coordinate acceptance only for `operator_f_invalid <= 0.05`;
- Wm and WW block-local masks evaluated before composition;
- frozen BOSS mm support component retained as its immutable previously audited mask/provenance;
- complete retained observation-coordinate dimension at least 15;
- reproduction/numerical incompleteness distinct from scientific support-dimension FAIL.

Because the old Exp073P label has subsequently also been used for prerequisite-authority joins, the new hosted implementation must use an unambiguous Article-3 operator-support receipt name rather than overload the join label.

Prospective positive label:

`PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`

Prospective scientific negative label:

`FAIL_ARTICLE3_OPERATOR_SUPPORT_V0_1`

Execution/provenance invalidity must be reported separately as

`INVALID_FOR_SCIENCE_ARTICLE3_OPERATOR_SUPPORT_V0_1`.

These are new unambiguous receipt labels around the already-frozen scientific criteria, not new thresholds.

## Layer-B criteria — no change from later Article-3 coordinate contract

Layer B preserves exactly:

- inherited unique `coordinate_id` and `ordinal`;
- canonical finite float64 z and k;
- `0.295 <= z <= 2.33`;
- finite strictly positive `k_Mpc^-1` and `k <= 0.06664762008318016`;
- all preregistered `final_response_abs_values` finite and strictly positive;
- `article3_coordinate_f_invalid <= 0.05` using its frozen coordinate-count denominator;
- at least 15 final retained coordinates;
- anti-leakage metadata and PASS / scientific FAIL / INVALID_FOR_SCIENCE semantics unchanged.

Layer B receives only the Layer-A-retained candidate rows, preserving their original full-operator ordinals. Within Layer B, `FULL_PRE_SUPPORT_COORDINATE_SET` means the full immutable `S_op` set presented to Layer B before its own geometry/envelope filtering; it does not permit renormalizing or regenerating Layer-A operator windows.

## Covariance authorization

Covariance restriction is authorized only after **both**:

- `PASS_ARTICLE3_OPERATOR_SUPPORT_V0_1`, and
- `PASS_PHYSICAL_SUPPORT_ARTICLE3`.

A PASS of either layer alone is insufficient.

A genuine scientific FAIL in either layer is retained as a negative result under the frozen criterion. Thresholds may not be loosened, support windows may not be narrowed after seeing the result, and a failed coordinate may not be removed because of covariance/nuisance/G7 geometry.

## Relation to earlier architecture-resolution note

`docs/ARTICLE3_EXP073P_SUPPORT_ARCHITECTURE_RESOLUTION_2026-08-29.md` correctly established that the two `f_invalid` definitions must not be aliased and stated that legacy operator support would become an additional current requirement only if a new prospective contract explicitly reintroduced it before real output.

This document is that prospective contract. It is motivated by the pre-output realization that real finite survey coordinates have broad response kernels, so a point-coordinate validity test cannot replace a window-leakage test.

## Readiness consequence

This correction does not reduce the value of completed work and does not represent a science FAIL, but it exposes one additional real implementation milestone before covariance. Article-3 headline scientific readiness remains **44%** until genuine hosted reproduction/prerequisite authority closes; future readiness progression must count both real support layers before declaring the physical-support stage complete.