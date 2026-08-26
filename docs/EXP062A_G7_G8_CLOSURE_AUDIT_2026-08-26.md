# Exp062A — literal G7/G8 closure audit after F30 (2026-08-26)

## Purpose

Audit whether the immutable Exp061A/F30 prospective PASS is sufficient to close G7 or G8, without changing any previously frozen criterion and without using C9 to redesign the tested operator.

## Immutable evidence entering this audit

- F27: HARD FAIL.
- F29: HARD PROSPECTIVE FAIL on C8 IDM–photon.
- F30: HARD PROSPECTIVE PASS on withheld C9 IDM–baryon for the pre-frozen two-coordinate `(ell,q)` representation, including all seven leave-one-redshift rebuilds.
- G7 definition: first nontrivial residual **cross-channel relation** after quotienting known identities/measurement degeneracies.
- G8 definition: that relation survives withheld prediction.
- Existing G7 note explicitly requires observational kernel/covariance whitening before a law claim.

## Audit result

**G7 remains OPEN. G8 remains OPEN.**

F30 is not itself a G7 relation. Its two coordinates are constructed from the same matter-response block: `ell` is an R^2 localization coordinate and `q` is a training-only PC2 shape/orientation coordinate. The F30 gate establishes a stable, injective/non-self-intersecting 2D response path for C9 under a frozen operator. It does not establish an equation linking independent observable channels after quotienting identities and measurement degeneracies.

Therefore G8 also cannot close from F30: a withheld-family PASS of a representation is not logically equivalent to withheld survival of a previously established G7 cross-channel law.

This is a boundary result, not a downgrade of F30. F30 remains positive out-of-family evidence for the 2D representation.

## Smallest scientifically admissible next gate

Before selecting another withheld family, construct and freeze a genuine **cross-channel law candidate** on training families only. The next candidate must satisfy all of the following before any new withheld response is inspected:

1. use at least two independently meaningful response/observable blocks (not two summaries of one matter-power block);
2. explicitly quotient exact Bianchi/conservation identities and known measurement-degeneracy directions;
3. map theory responses through a stated observational response/kernel when available and whiten with a frozen covariance convention; if a required kernel is unavailable, mark that channel/theory cell masked rather than zero-impute it;
4. state one mathematical relation and a numerical acceptance statistic/tolerance frozen from training/control information only;
5. demonstrate nontriviality against a null/permutation or covariance-coordinate control;
6. only after items 1–5 are frozen, select a fresh withheld family/mechanism for the G8 prospective test.

The most economical route is to reuse existing matter/growth plus metric/Weyl/slip or geometry information where the repository already has validated channel provenance, rather than inventing a new scalar localization proxy. Exp032 already shows that slip can separate a matter-power degeneracy, but that separator is raw theory-space evidence; it must not be promoted to observational distinguishability without the kernel/covariance step.

## Anti-retuning contract

No post-F30 reinterpretation of F27/F29 is allowed. No future G7/G8 candidate may choose its channel set, mask, whitening convention, tolerance, rotation/sign convention, redshift subset, k-range, or withheld family after seeing the withheld response. Negative results remain first-class scientific results.

## Decision

Exp062A is a **hard logical closure audit**, not a numerical discovery experiment. It deliberately prevents a false-positive promotion of F30 and fixes the next research target: a preregistered, covariance-aware, genuinely cross-channel residual relation, followed by a fresh withheld-family test.