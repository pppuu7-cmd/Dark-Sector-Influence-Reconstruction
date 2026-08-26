# Gate update — Exp061A / F30 (2026-08-26)

## Immutable prospective result

Exp061A evaluated the pre-frozen Exp058A/Exp060A two-coordinate response operator on the first withheld C9 IDM–baryon matter-power response. No C9-dependent retuning was permitted.

**Verdict: HARD PROSPECTIVE PASS for F30 / multicoordinate path gate v0.1.**

The GitHub Actions workflow completed successfully and the immutable artifact reports `PASS_IDM_BARYON_MULTICOORDINATE_PROSPECTIVE_V0_1` with no failures.

Full standardized adjacent `(ell,q)` step norms were:

`[0.43867499476052313, 2.9102332589802873, 5.761860689614482, 0.04774833503993949]`

All four are strictly above the preregistered `1e-10` floor. The C9 polyline has no nonadjacent intersections. All seven leave-one-redshift operator rebuilds also pass the same frozen gate.

## Interpretation

This is positive out-of-family evidence that the 2D localization+shape/orientation representation survives a genuinely withheld source family where the prior scalar localization law F29 failed on C8. It does **not** erase or reinterpret F27/F29: those negative results remain frozen. It also does not by itself close G7/G8/G9; those gates require their own stated evidence.

## Provenance

- PR preregistration/implementation: #53
- prospective workflow run: `32957427686`
- workflow head SHA: `d2f9a91f156de30c4795a8fb053f64132ea75f07`
- artifact id: `9602537353`
- artifact digest: `sha256:560f1fe127bfee1cd6fc14b91c455c11babf211a0854a37f6db30d6e5bbea6ed`
- merged PR merge commit: `77f81ccfa42959bf91875723f123a402a467aef0`

## Frozen state after Exp061A

- F27: HARD FAIL (unchanged)
- F29: HARD PROSPECTIVE FAIL (unchanged)
- F30: HARD PROSPECTIVE PASS
- G7: OPEN
- G8: OPEN
- G9: OPEN

Next step: audit what additional independent evidence is required by G7/G8/G9 and preregister the smallest non-retuned test that can actually close one of them; do not promote F30 into a broader universality claim without that evidence.
