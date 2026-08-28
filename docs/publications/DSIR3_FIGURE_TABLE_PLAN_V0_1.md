# DSIR Article 3 — figure and table plan v0.1

**Date:** 2026-08-29  
**Status:** manuscript planning; no real G7 result implied.

The Article-3 visual package should explain the observational quotient as a sequence of immutable transformations rather than present a single favorable significance plot. Figures 1–2 can be prepared before real G7 closure; Figures 3–5 and result tables require terminal scientific artifacts.

## Figure 1 — fail-closed observational reconstruction pipeline

**Status:** READY TO DRAW FROM FROZEN ARCHITECTURE.

A left-to-right flow diagram:

`solver-validated physical response`
→ `finite observation operator`
→ `physical-support mask`
→ `frozen retained coordinate sequence S`
→ `covariance binding C_S`
→ `Cholesky whitening L^{-1}`
→ `signed nuisance responses +/-`
→ `thin SVD nuisance span`
→ `quotient (I-P_N)y`
→ `G7 relation/null`
→ `future G8 withheld family`.

Every transition should show its possible terminal alternatives: PASS, scientific FAIL/NULL, and INVALID/blocked where applicable. The visual message is that downstream quantities do not exist scientifically until their parent gate passes.

**Caption claim boundary:** methodology/ordering only; no survey PASS claim.

## Figure 2 — geometry of ray, line, subspace and quotient

**Status:** READY TO DRAW SCHEMATICALLY.

Panel A: demonstrate why a selected positive nuisance ray is not the same as an interior two-sided line.

Panel B: show several resolved whitened nuisance tangents spanning `col(N_w)`.

Panel C: decompose target response

`y = P_N y + (I-P_N)y`

and label

`eta_N = ||(I-P_N)y|| / ||y||`.

Panel D: distinguish `N_exo`, `N_med`, and `N_unknown` and visually warn that geometric projection is not equivalent to causal non-dark-sector attribution.

**Caption claim boundary:** conceptual geometry motivated by earlier validated ray/line corrections and the frozen Article-3 contracts; no measured Article-3 angle or survival fraction.

## Figure 3 — physical-support retention map

**Status:** BLOCKED UNTIL REAL SUPPORT TERMINALITY.

Recommended representation after support execution:

- x-axis: `k [Mpc^-1]`;
- y-axis: `z`;
- candidate coordinates shown by immutable coordinate identity/ordinal;
- outside-domain coordinates visually distinct from geometrically eligible coordinates;
- geometrically eligible but envelope-invalid coordinates marked separately;
- retained coordinates highlighted;
- frozen exact boundaries `z=0.295`, `z=2.33`, `k=0.06664762008318016 Mpc^-1` drawn explicitly.

Inset or annotation:

`N_candidate`, `N_geom`, `N_invalid`, `N_retained`, `f_invalid`, support classification, retained-sequence SHA256.

Do not encode covariance weight, nuisance overlap, or G7 statistic into this plot.

## Figure 4 — covariance and nuisance spectrum diagnostics

**Status:** BLOCKED UNTIL COVARIANCE AND NUISANCE GATES PASS.

Possible two-panel layout:

Panel A: covariance numerical diagnostics after valid coordinate binding, including eigenvalue spectrum for diagnostics, condition number, `rho_sym`, `rho_chol`, and `rho_white`. Avoid interpreting covariance eigenmodes as selected science modes.

Panel B: singular values of `N_w` with the prospectively frozen numerical-rank threshold and retained rank `r`. Mark unresolved/null nuisance columns in accompanying text rather than deleting them from provenance.

A small validation box should report basis/sign/permutation invariance errors and projector idempotence/orthogonality errors.

## Figure 5 — quotient survival by target/channel

**Status:** BLOCKED UNTIL QUOTIENT EXECUTION.

For each preregistered target/channel, display a decomposition of whitened norm into

- nuisance-span component `||P_N y||`;
- surviving quotient component `||y_perp||`;
- `eta_all`;
- where causally justified, `eta_exo`;
- mediated/unknown overlap diagnostics separately.

The plot must not turn `eta_N` into a Gaussian significance. If a G7 statistic is defined separately, show it in a separate panel or table with its own frozen null semantics.

## Optional Figure 6 — G7 terminal relation/null result

**Status:** BLOCKED UNTIL G7.

Only create if the final G7 result benefits from visualization. A positive result should show the preregistered relation and its frozen test without adding a post-hoc fit family. A null result should show the same preregistered statistic and why the criterion was not met. An INVALID state should not be visualized as a scientific data point.

## Table 1 — gate and provenance ledger

**Status:** FRAME READY; RESULT CELLS BLOCKED.

Columns:

| Stage | Parent identity | Prereg/freeze commit | Run/job/artifact | Digest | Terminal classification | Authorizes |
|---|---|---|---|---|---|---|
| upstream reconstruction | TBD terminal replacement | frozen lineage | TBD | TBD | TBD | real support only if PASS |
| physical support | upstream PASS | frozen support contract | TBD | TBD | TBD | covariance only if PASS |
| covariance/whitening | support PASS | frozen covariance contract | TBD | TBD | TBD | nuisance execution only if PASS |
| signed nuisance SVD | covariance PASS | frozen nuisance contract | TBD | TBD | TBD | quotient only if valid |
| quotient | nuisance PASS | same immutable support/metric | TBD | TBD | TBD | G7 only if valid |
| G7 | quotient terminal | frozen G7 protocol | TBD | TBD | TBD | future G8 framework |

This table should become the main reproducibility ledger in the final paper.

## Table 2 — support and covariance numerical audit

**Status:** BLOCKED.

Rows should include exact coordinate counts, `f_invalid`, retained coordinate dimension, symmetry/Cholesky/whitening residuals, covariance condition diagnostics, and all corresponding frozen thresholds. Values should be read directly from terminal machine-readable artifacts.

## Table 3 — nuisance family and causal-status inventory

**Status:** FRAME READY; SCIENTIFIC VALUES BLOCKED.

Columns:

`family | parameter | +/- step | representation-resolved? | epsilon_anti | +/- angle | singular-value contribution / rank note | causal status (exo/med/unknown) | provenance`.

Causal status must be frozen independently of the target quotient and cannot be inferred from overlap.

## Table 4 — quotient and G7 terminal matrix

**Status:** BLOCKED.

For each preregistered target/channel:

`||y|| | ||P_N y|| | ||y_perp|| | eta_all | theta_all | eta_exo if justified | mediated/unknown overlap | G7 statistic | terminal classification`.

No cells should be filled from exploratory, synthetic, or non-parent-bound runs.

## Visual integrity rules

1. Never plot downstream quantities for a coordinate rejected at the physical-support gate.
2. Never show a covariance-weighted quantity before exact coordinate binding is demonstrated.
3. Never show a normalized nuisance angle for an unresolved final-representation nuisance direction.
4. Never replace a two-sided nuisance line with one favorable sign in a scientific panel.
5. Never color or order support coordinates by future G7 outcome.
6. Preserve null and negative terminal outcomes visually; do not omit them from comparison matrices.
7. Label synthetic-only QA figures explicitly if any are included in an appendix; they must not resemble real survey results.
