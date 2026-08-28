# DSIR Article 2 — final figure/table specification v0.1

**Date:** 2026-08-28

Purpose: convert the terminal Article-2 evidence chain into a compact draft-ready visual plan without introducing new scientific claims.

Canonical claim source:

`docs/ARTICLE2_CLAIM_MATRIX_CURRENT.md`

## Figure 1 — From static similarity to nuisance geometry

### Panel A — static response ambiguity

Show K2 bar1 against GDM `cs2/cv2` in the frozen static comparisons:

- matter-only: `19.2231° / 19.0371°`;
- equalized `(r_P,r_W,Delta_slip)`: `19.0749° / 50.1667°`.

Message: adding correlated static channels does not automatically create generic specificity.

### Panel B — oriented temporal/velocity rays

Positive K2 ray:

- finite-bin temporal: `138.1006° / 137.0973°`;
- raw `t_tot`: `165.9455° / 164.7113°`;
- `t_tot` shape after per-z constant-in-k quotient: `166.4387° / 164.9271°`.

Message: a selected oriented deformation can differ strongly in independent evolution/velocity channels.

### Panel C — ray versus nuisance line

Show the same positive K2 shape direction together with fresh negative K2:

- positive-oriented ray: `166.4387° / 164.9271°`;
- K2 line angles predicted from sign freedom: `13.5613° / 15.0729°`;
- fresh negative K2: `13.5503° / 15.0709°`;
- plus/minus K2 mutual angle: `179.9078°`.

Message: an oriented ray and an interior two-sided nuisance line are different comparison objects.

## Figure 2 — Representation kernel and recovery

### Panel A — K1 transfer-only null

Primordial tilt K1:

- reference `n_s=0.965`;
- plus `0.970`;
- minus `0.960`;
- exact transfer-only response: `max |ln(t_tot/t_tot_ref)| = 0.0` for both signs.

Label Exp071M:

`INVALID_FOR_SCIENCE_EXP071M` because the frozen response vector is zero.

Message: absence of response in a representation is not absence of physical effect.

### Panel B — velocity-power representation

Use

`Delta ln P_R(k) + 2 Delta ln |t_tot|`.

K1 line versus GDM rays:

- cs2: `36.0622°`;
- cv2: `37.8458°`;
- frozen separator: `45°`.

Classification:

`K1_TWO_SIDED_VELOCITY_POWER_SHAPE_OVERLAPS_GDM_EXP071N`.

Retained projected norms:

- K1: `0.6255`;
- GDM cs2: `0.8272`;
- GDM cv2: `0.8372`.

Message: making a nuisance resolvable does not guarantee mechanism specificity.

## Figure 3 — Support and observational boundary

Three-stage schematic:

1. common physical-provider domain: Exp071A `495/495` provider cells;
2. first ACT×unWISE support route: retained observational dimension `0` under frozen 5% leakage rule;
3. finite-operator inventory: BOSS finite true-k matrix produces non-empty component (`54/240` rows), while examined KiDS finite-theta absolute route is non-normalizable under its frozen criterion.

Message: theory-space distinguishability and observational admissibility are separate gates.

Do not present these finite-operator results as likelihood preference or G7 closure.

## Figure 4 — DSIR comparison hierarchy schematic

Final conceptual diagram:

`representation A`
→ `resolvability / ker(A)`
→ `channel block`
→ `ray / line / nuisance subspace`
→ `metric M`
→ `physical support`
→ `finite observation operator`
→ `covariance whitening`
→ `nuisance quotient`
→ `G7 relation or null`.

Article 2 stops before covariance whitening.

## Table 1 — terminal comparison matrix

| Control | Representation | Comparison object | cs2 angle | cv2 angle | Frozen result |
|---|---|---|---:|---:|---|
| K2 static matter | `r_P` | + ray | 19.2231° | 19.0371° | overlap |
| K2 static 3-channel | `r_P+r_W+slip` | + ray | 19.0749° | 50.1667° | overlap at cs2 |
| K2 temporal | finite-bin `r_P` derivative | + ray | 138.1006° | 137.0973° | oriented separation |
| K2 total velocity | `t_tot` | + ray | 165.9455° | 164.7113° | oriented separation |
| K2 velocity shape | projected `t_tot` | + ray | 166.4387° | 164.9271° | oriented separation |
| K2 velocity shape | projected `t_tot` | two-sided line | 13.55–13.56° | 15.07° | line overlap |
| K1 transfer-only | `t_tot` | two-sided line | undefined | undefined | representation null |
| K1 velocity-power shape | `Delta ln P_R + 2Delta ln|t_tot|` | two-sided line | 36.0622° | 37.8458° | line overlap |

## Table 2 — evidence/provenance compact ledger

Minimum rows:

- Exp071E — static joint falsification;
- Exp071F — 3-channel non-cure;
- Exp071H — temporal oriented separation;
- Exp071I — source-audited total velocity;
- Exp071J — amplitude-mode quotient;
- Exp071K — 24 support ablations;
- Exp071L — two-sided K2 falsification;
- Exp071M — K1 transfer-null boundary;
- Exp071N — K1 velocity-power nuisance overlap;
- Exp071A / Exp072A-C / Exp073A-L — physical/finite observational applicability chain.

Columns:

`experiment | prereg commit | immutable run | artifact | classification | article claim ID | non-claim boundary`.

## Caption rules

Every angle caption must identify:

- the response representation;
- whether the object is an oriented ray or a two-sided line/subspace;
- the metric/normalization used;
- whether the result is theory-space or observational;
- the frozen threshold only when it is part of a preregistered classification.

Never use “fingerprint”, “detection”, “RSD measurement”, “observational preference”, or “unique identification” for these Article-2 figures.
