# Exp073BB — Article-3 provisional dual-track evidence policy v0.1

**Date frozen:** 2026-08-31  
**Project:** Dark-Sector Influence Reconstruction (DSIR) only. RTK/RQIR excluded.  
**Purpose:** permit exploratory/provisional continuation and manuscript drafting from numerically non-identical but complete computational replicas without changing any scientific authority, PASS/FAIL state, frozen threshold, anti-leakage rule, or readiness accounting.

## 1. Two tracks are mandatory

### Track A — scientific authority

Track A is unchanged.

- Existing frozen exact PASS/FAIL criteria remain binding.
- Exp073AQ remains permanently `SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`.
- A later approximate/provisional result may never reclassify, erase, average away, or rescue an authority FAIL.
- Article-3 scientific readiness remains 52% until a separately authorized real scientific gate changes it.
- Synthetic, infrastructure, provisional, numerical-diagnostic and manuscript-planning work always adds +0 readiness.

### Track P — provisional research/manuscript track

Track P may continue downstream for navigation, sensitivity analysis, prioritization and working-manuscript construction even when Track A is blocked by exact nonidentity, provided all rules below are satisfied.

Every Track-P object must state:

- `authority=false`;
- `provisional=true`;
- `scientific_pass_claimed=false`;
- `readiness_increment=0`;
- `article3_scientific_readiness_percent=52` unless Track A has independently changed later;
- `recompute_before_final_submission=true` unless a later Track-A authority explicitly supersedes the provisional object.

## 2. No preferred replica

When two or more complete replicas exist but are not exactly identical, Track P must propagate **all complete admissible replicas**. It is forbidden to select the replica that is closer to a historical result, prettier, smoother, more convenient, more supportive of a desired claim, or better aligned with downstream data.

Allowed representations are:

1. independent branch propagation (`A`, `B`, ...), or
2. an explicitly derived componentwise envelope/range computed from all branches.

A midpoint/average may be reported only as a descriptive summary together with the full branch range; it may not replace branch propagation for classification or claim-stability tests.

## 3. Provisional claim-stability rules

A provisional qualitative claim is `PROVISIONAL_BRANCH_ROBUST` only if **every complete propagated branch gives the same qualitative conclusion** under the already-frozen downstream rule.

Examples:

- sign claim: every branch has the same nonzero sign;
- threshold/gate claim: every branch lies strictly on the same side of the already-frozen threshold;
- ordering claim: every branch preserves the same strict ordering;
- retained/rejected classification: every branch produces the same classification and no branch lands exactly on an unresolved numerical boundary;
- topology/intersection claim: every branch gives the same discrete topology/intersection outcome under the frozen algorithm.

If branches disagree in sign, ordering, retained set, gate class, topology, or any scientific interpretation, status is `PROVISIONAL_NUMERICALLY_SENSITIVE_RECOMPUTE_PRIORITY` and that claim is not eligible as a positive manuscript result.

Exact equality to a frozen threshold remains `numerically_unresolved`; Track P may not round it.

## 4. Numerical reporting

For non-authoritative numeric quantities the working manuscript must report either:

- branch values explicitly, or
- a branch envelope `[min,max]`, optionally with a descriptive center.

A single replica value may not be presented as if uniquely determined.

Any table/figure derived from Track P must carry provenance sufficient to reproduce the branches and must be tagged `PROVISIONAL_NONAUTHORITATIVE` in its source manifest.

## 5. Article-use classes

### P1 — `PROVISIONAL_BRANCH_ROBUST_MANUSCRIPT_ELIGIBLE`

May be used to organize and draft Article-3 text, figures and discussion when all propagated branches support the same stated conclusion. Required wording in the working manuscript must identify the calculation as provisional/pending final reproducibility certification.

P1 does **not** authorize a scientific PASS or readiness increase.

### P2 — `PROVISIONAL_NUMERICALLY_SENSITIVE_RECOMPUTE_PRIORITY`

Branches change the scientific conclusion or cross a frozen decision boundary. Not eligible as a positive article claim. Must be placed high in the exact-recompute backlog.

### P3 — `PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`

Partial/incomplete outputs, missing branches, failed pre-classification jobs or malformed provenance. Cannot be propagated downstream.

## 6. Manuscript boundary

Track P is explicitly intended to avoid stopping scientific exploration while exact numerical reproducibility is being engineered.

It may be used for:

- working Article-3 structure;
- provisional figures/tables;
- ranking promising relations/tests;
- identifying which exact computations are worth prioritizing;
- estimating whether conclusions are robust to the observed numerical branch spread.

Before a final submission-ready manuscript, every central quantitative claim depending on Track P must either:

1. be replaced by a later Track-A authoritative result, or
2. remain explicitly labeled provisional/non-authoritative in the manuscript with the reproducibility limitation disclosed.

No provisional result may be silently promoted to authoritative wording.

## 7. Anti-leakage remains unchanged

Track P does not relax stage ordering. In particular:

- support selection may not read covariance/whitening/nuisance/relation/null/G8 information;
- no effective ell/z/k shortcut;
- no fiducial-P weighting;
- G8/withheld information may not select or tune a G7 relation;
- exact-threshold ambiguity remains unresolved rather than rounded.

Track-P downstream calculations must preserve the same upstream/downstream information firewall as Track A.

## 8. Current Wm_S1 provisional status

The already-immutable Exp073AQ A/B selected windows may be used as the first Track-P branch pair without changing the AQ authority FAIL.

Observed input-level diagnostics from the two complete `<f8 [39,12288]` arrays:

- maximum absolute difference: `2.0816681711721685e-17`;
- global maximum absolute window magnitude: `0.04906169081530385`;
- `max|delta| / max|W| = 4.2429605188470844e-16`;
- RMS branch difference / RMS(A) = `2.193471255136272e-16`;
- sign-bit mismatches: `0`;
- zero/nonzero mismatches: `0`;
- maximum relative difference of per-band `sum(abs(W))`: `4.130423023448714e-16`.

This supports only the input-level statement that the two complete Wm_S1 branches are extremely close and sign-pattern identical. It does not pre-award any downstream support/gate classification; downstream Track-P calculations must still be run independently on both branches.

Initial Track-P label:

`PROVISIONAL_WM_S1_BRANCH_PAIR_ELIGIBLE_FOR_DOWNSTREAM_SENSITIVITY_PROPAGATION`

## 9. Recompute ledger

Every Track-P object used in Article-3 drafting must appear in a durable recomputation ledger with:

- source experiment/run/artifact/digest(s);
- provisional class P1/P2/P3;
- manuscript claims/figures depending on it;
- exact-recompute priority;
- later authoritative supersession, if any.

Nothing may be deleted from the ledger merely because a later precise calculation agrees.

## 10. Effect on current route

Exp073AZ/BA low-memory authority-succession work continues unchanged in Track A.

Track P may proceed in parallel from complete branch pairs to explore later support/geometry/statistics, but Track-P outputs may not satisfy Exp073AR/AS/AT/AU/AV/AW/AX authority prerequisites.

The two tracks may inform engineering priorities, but only Track A changes scientific readiness.