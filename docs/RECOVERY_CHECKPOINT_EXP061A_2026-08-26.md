# DSIR recovery checkpoint — after Exp061A (2026-08-26)

Current reproducible state after the first withheld C9 response.

Exp059A froze C9 as IDM–baryon with `cross_idm_b={1e-30,1e-29,1e-28,1e-27,1e-26} cm^2`, `n_index_idm_b=0`, source-only before response. Exp060A froze the exact 2D `(ell,q)` operator using only immutable C3/C5/C7/C8 training responses: `ell` is the R^2 localization coordinate; `q` is training-only PC2 with deterministic sign; centering/scaling are training-only; step and intersection tolerances are `1e-10`; seven leave-one-z rebuilds are mandatory.

Exp061A then generated the first C9 matter-power response on pinned official CLASS and evaluated that exact frozen operator. Immutable artifact status: `PASS_IDM_BARYON_MULTICOORDINATE_PROSPECTIVE_V0_1`; failures `[]`; full adjacent standardized step norms `[0.43867499476052313,2.9102332589802873,5.761860689614482,0.04774833503993949]`; no nonadjacent intersections; all seven leave-one-z rebuilds pass.

Scientific ledger: F27 HARD FAIL; F29 HARD PROSPECTIVE FAIL; F30 HARD PROSPECTIVE PASS. G7/G8/G9 remain OPEN. Never rewrite F27/F29 as superseded; F30 is evidence for the frozen 2D representation only, not proof of universal dark-sector reconstruction.

Exact provenance: PR #53; run 32957427686; head `d2f9a91f156de30c4795a8fb053f64132ea75f07`; artifact 9602537353; artifact digest `sha256:560f1fe127bfee1cd6fc14b91c455c11babf211a0854a37f6db30d6e5bbea6ed`; PR merge commit `77f81ccfa42959bf91875723f123a402a467aef0`; result note `docs/GATE_UPDATE_EXP061A_F30_2026-08-26.md`.

Resume protocol: read `docs/GATES.md`, the F27/F29/F30 gate updates, Exp058A/Exp059A/Exp060A/Exp061A experiment records/workflows, then inspect the literal closure requirements of G7/G8/G9. Preregister the next test before seeing its response. Preserve negative results and forbid post-response threshold, mask, redshift, rotation, sign, source-grid, or family selection retuning.
