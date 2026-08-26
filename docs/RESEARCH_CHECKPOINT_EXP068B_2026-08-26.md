# Research checkpoint — Exp068B — 2026-08-26

## Outcome

`PASS_ACT_UNWISE_LITERAL_PCA_PHYSICAL_FORWARD_V0_1`

This is a separately preregistered corrective experiment after the permanently preserved Exp068A result

`FAIL_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1`.

Exp068A is not reclassified. Exp068B froze the literal pinned-upstream PCA convention before the first Exp068B physical output and then passed every frozen hard test B1–B6.

## Chronology / provenance

- Exp068B preregistration commit: `0fa3cfdbde0e6baea2aab53a4545bd668c61cd4f`.
- Code/workflow head used to trigger the prospective run: `342b53e1fd686df4aed57b26b360ae5b7ef45f15`.
- GitHub Actions run: `33007727478`.
- Scientific artifact ID: `9621695396`.
- Artifact SHA256: `6f6cd856d6ea9f2f728fb56908f589c9e25006f3e98243776c796fcd05431d40`.
- Pinned ACT×unWISE source: `6302c30d9e70f8e4ff2d4a84a9977b4471705179`.
- Pinned CAMB: `fa3f097343fbbe427cc04b4f5f0041c22c6ec764`.
- Official released data archive SHA256: `1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`.

The 1.51-GB released archive is cached in Actions only as an infrastructure optimization. Every restored/downloaded archive remains hard-verified against the frozen SHA256 before science.

## Literal tracer/PCA result

Pinned upstream uses

\[
p_{\rm PCA}^{final}=(1,1,c_0,c_1,\ldots),
\]

where the first unit coefficient multiplies the fiducial cross-correlation `b dN/dz`, the second fixed unit coefficient multiplies the released mean correction `mean Delta dN/dz`, and only the remaining entries are sampled PCA nuisance coefficients.

Therefore:

- Blue: 3 sampled PCA directions, correction file `[z,mean,PC0,PC1,PC2]`, `n_pcs=4`, expanded raw axis length 5, zero-displacement vector `[1,1,0,0,0]`;
- Green: 5 sampled PCA directions, correction file `[z,mean,PC0,...,PC4]`, `n_pcs=6`, expanded raw axis length 7, zero-displacement vector `[1,1,0,0,0,0,0]`.

The frozen normalization controls are finite/nonzero:

- Blue: `0.9999930073020711`;
- Green: `0.9999195790912987`.

## Physical forward result

All frozen tests pass:

- B1 provenance — PASS;
- B2 literal tracer/PCA binding — PASS;
- B3 physical independent power providers — PASS;
- B4 full raw-component upstream-vs-DSIR equivalence — PASS;
- B5 nontrivial physical signal control — PASS;
- B6 zero-displacement coefficient-vector control — PASS.

The strongest numerical result is that every compared raw Blue/Green forward component on the complete frozen input domain `ell=0..6143` has

\[
\max |X_{DSIR}-X_{upstream}| = 0.0,
\]

within the frozen tolerance factor `5e-13`.

This includes the nontrivial `kg_b`, `kmu`, `gg_bsq`, `gmu_b`, `mumu` blocks and the correct no-CLEFT structural zeros.

Independent physical provider examples retain the signed Weyl–matter cross-power, e.g.

\[
P_{Wm}(z=0.5,k=0.02\,\mathrm{Mpc}^{-1})=-1.3961103973289266\times10^{-3},
\]

rather than replacing it by a Poisson-derived or absolute-valued proxy.

## Scientific interpretation

Exp068B closes the **physical linear/no-CLEFT raw forward-adapter reproduction prerequisite**, not G7 itself.

It establishes that, given solver-neutral independent physical `P_WW`, `P_Wm`, `P_mm` inputs and the literal released tracer basis, the DSIR ACT×unWISE projector reproduces the pinned upstream raw forward calculation exactly on the frozen domain.

It does not establish that linear theory is physically valid over every released ACT bandpower kernel. The already-recorded validity-mask boundary therefore remains mandatory.

## Required next ordering

1. certify C5 designer-`f(R)` physical `P_WW/P_Wm/P_mm` provider bridge;
2. certify C3/GDM gauge-invariant `D_m` read-only provider bridge;
3. freeze and evaluate a model-common physical survey-kernel validity/leakage mask;
4. restrict the released selected covariance to retained bins;
5. recompute the whitener only on that valid subspace;
6. build the no-CLEFT nuisance tangent Jacobian, respecting the structural rank bound `rank <= 14`;
7. freeze the numerical SVD rank rule before inspecting any candidate G7 relation;
8. quotient/relation/null-control work;
9. only after a frozen training relation may a fresh G8 withheld family be generated.

Current top-level state: **G7 OPEN, G8 OPEN, G9 OPEN**.
