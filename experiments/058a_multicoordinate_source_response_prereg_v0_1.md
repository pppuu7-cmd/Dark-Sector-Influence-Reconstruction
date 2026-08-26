# Experiment 058A — multicoordinate source-response law preregistration v0.1

Date: 2026-08-26
Status: PREREGISTERED; no response data from the future test family may be inspected before the family/source selector is frozen.

## Motivation

Exp056B/F29 prospectively falsified the one-coordinate endpoint-half-transition law on C8 IDM-photon. Exp057A showed that this was structural: the C8 response family changes orientation and shape with coupling, with a negative first adjacent cosine and a leading normalized-response mode carrying only 79.10% of variance. Therefore any next candidate must allow more than one response coordinate and must not be fitted on C8 and then called predictive.

## Candidate statement

For a family with a monotone microscopic/source control `s`, define two response coordinates on a frozen observable block:

1. a localization coordinate `ell`, chosen from a predeclared response crossing/centroid operator and held fixed for the whole experiment;
2. a shape/orientation coordinate `q`, defined as the signed projection of the normalized response vector onto a training-only second response mode.

The prospective candidate is not that either coordinate is universally monotone by itself. The candidate is that the ordered response path is locally non-self-intersecting in the 2D coordinate plane `(ell,q)` over the frozen source interval.

For adjacent source points `i -> i+1`, let

`d_i = (ell_{i+1}-ell_i, q_{i+1}-q_i)`.

The hard prospective criterion is:

- every response point is valid on the frozen mask;
- `||d_i||_2 > 0` for every adjacent pair;
- no two non-adjacent line segments in the ordered `(ell,q)` polyline intersect, using exact segment-intersection logic with a numerical tolerance frozen before the withheld response run;
- the same pass/fail outcome must survive every leave-one-redshift recomputation that still leaves at least five redshift nodes.

This is a topology/ordering statement, not a fitted slope law. No post-hoc rotation, threshold change, redshift deletion, sign flip, or source-range trimming is allowed after withheld responses are generated.

## Training-only construction boundary

C3/C5/C7 and the already-seen C8 diagnostic may be used only to choose the operator definitions and to construct the two training response modes. C8 is explicitly contaminated for future validation and cannot be used as the withheld family.

The next withheld family must satisfy all of:

- not used in Exp054A, Exp055A, Exp056A/B, or Exp057A to choose the candidate;
- source-side selector frozen before response generation;
- solver lineage, reference cosmology, redshift grid, k-domain, observable mask and interpolation conventions frozen in the selector record;
- no response-derived amplitude tuning.

## Gate interpretation

A PASS on a new family would be evidence for a preregistered multicoordinate organizing relation, but would not by itself close G8 unless the family is genuinely withheld from construction and all hard criteria pass. A FAIL is preserved as a scientific negative result. G7/G8/G9 remain OPEN at preregistration.
