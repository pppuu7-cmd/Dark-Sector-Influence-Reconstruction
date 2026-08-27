# Exp073J BOSS component checkpoint — 2026-08-27

## Verified state

Implementation merge: `1bd022ffca543361d265a72b782ef96fe069d2ce`.

Workflow run `33042052616`, job `98417620281`, completed `success`. Immutable artifact `9634226231`, digest `sha256:239b198c1adfc21333779ef1efb597885710bddd593b380a67ac6dd1399daa65`.

The prospectively frozen non-classifying BOSS component of Exp073J used `C=W@M`, `h_fid=0.676`, the unchanged common physical rectangle, and `abs(C)` positive envelopes. No covariance, nuisance rank/SVD, relation/null, G8, fiducial P(k) weighting or post-hoc support cut was used.

Result: `54/240` BOSS component coordinates satisfy the unchanged `f_invalid<=0.05` criterion. Each cap retains `27/120`, with `9/40` retained in each observed P0, P2 and P4 block.

This is not a PASS/FAIL classification for Exp073J. Covariance restriction remains unauthorized. G7/G8/G9 remain OPEN.

## Exact next admissible work

Continue only with the KiDS-BNT part already frozen by `experiments/073j_kids_bnt_boss_finite_matrix_common_support_prereg_v0_1.md` and `experiments/073g_kids_boss_bnt_operator_binding_v0_1.md`.

1. Re-bind `KiDS-WL/Cat_to_Obs_K1000_P1@36676da44471979dacb779155d7e6e7212ae1f4f` and verify the stored SHA256 identities for all five source n(z), lens-bin-2 n(z), `src/bandpowers/xi2bandpow.c`, and `Calc_2pt_Stats/doall_calc2pt.sh`.
2. Reconstruct the public BNT matrix using `pltaylor16/x-cut@fcab1439c896ff4bff0fa21300366eef8107578c`; use only transformed rows `[2,3,4]`, nulling tolerance `1e-10`, repeatability tolerance `1e-12`.
3. Reproduce exact KiDS angular bandpower filter semantics from the pinned C code/arguments; do not substitute top-hat or effective-ell approximations.
4. In the frozen Exp068B R0 geometry, integrate non-negative full support envelopes for lens-bin-2 x BNT-source `Wm` and BNT-source-pair `WW`, with Limber `k=(ell+1/2)/chi(z)` and the unchanged `z,k` rectangle.
5. Apply `f_invalid<=0.05` to every required Wm/WW block. Preserve signed physical `P_Wm` semantics in the later forward model; the support envelope itself remains non-negative.
6. Combine the resulting KiDS-BNT mask with the immutable BOSS component result. Only then calculate the full Exp073J retained coordinate inventory and apply the preregistered minimum retained dimension `>=15`.
7. Only a full `PASS_COMMON_KIDS_BNT_BOSS_PHYSICAL_SUPPORT_EXP073J` may authorize covariance restriction/whitening. A full support FAIL is a scientific FAIL and must be preserved.

Do not read covariance, nuisance SVD/rank, relation residuals, held-out families or G8 before Exp073J is fully classified.
