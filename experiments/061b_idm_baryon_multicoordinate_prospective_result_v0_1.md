# Experiment 061B — Exp061A prospective C9 result v0.1

Date: 2026-08-26
Status: PROSPECTIVE PASS RECORDED; no post-response recalibration performed.

## Frozen lineage

- Candidate preregistration: `experiments/058a_multicoordinate_source_response_prereg_v0_1.md`.
- C9 source-only freeze: Exp059A, IDM–baryon `cross_idm_b = {1e-30,1e-29,1e-28,1e-27,1e-26} cm^2`, `n_index_idm_b=0`.
- Exact operator freeze: Exp060A, training only on immutable C3/C5/C7/C8 responses.
- Solver: official CLASS pinned at `e85808324f51fc694d12e3ed7439552a3c3f9540`.
- First C9 response run: GitHub Actions `32957427686`, completed successfully 2026-08-26.
- Artifact digest: `sha256:560f1fe127bfee1cd6fc14b91c455c11babf211a0854a37f6db30d6e5bbea6ed`.

## Prospective result

The immutable result JSON reports `PASS_IDM_BARYON_MULTICOORDINATE_PROSPECTIVE_V0_1` with an empty failure list.

Full frozen standardized `(ell,q)` path adjacent step norms:

`[0.43867499476052313, 2.9102332589802873, 5.761860689614482, 0.04774833503993949]`.

All four are strictly above the preregistered `1e-10` threshold. There are no non-adjacent polyline intersections. The full path therefore passes.

Every one of the seven leave-one-redshift operator rebuilds also passes and agrees with the full-path status. No source point, redshift, k node, tolerance, PC sign, axis rotation, source interval, or response threshold was changed after C9 response generation.

## Interpretation boundary

This is positive prospective evidence for the preregistered two-coordinate localization+shape organizing relation on the genuinely withheld C9 IDM–baryon family. It does not erase or weaken prior negative results: F27 remains HARD FAIL and F29 remains HARD PROSPECTIVE FAIL; F28 remains retrospective only.

Gate closure is deliberately not changed in this result-record commit. A separate gate audit must map the successful prospective result to the pre-existing G7/G8/G9 definitions without redefining those gates after seeing C9.

## Provenance note

The Exp061A JSON metadata names `experiments/058a_multicoordinate_source_response_law_v0_1.md`, while the actual preregistration file is `experiments/058a_multicoordinate_source_response_prereg_v0_1.md`. This is a metadata-path typo only: the scientific operator and criteria were frozen in Exp058A/Exp060A before C9 response and were executed unchanged.