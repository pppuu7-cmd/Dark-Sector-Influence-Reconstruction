# DSIR recovery checkpoint — Exp066B (2026-08-26)

## Immutable prior state

- Exp065B: PASS for the exact upstream-selected ACT DR6 × unWISE Blue/Green `Clgg+Clkg` 26×26 covariance without regularisation.
- Exp066A: PASS for the solver-neutral raw projection basis with independent `P_WW`, `P_Wm`, `P_mm` inputs.
- G7/G8/G9 were OPEN.

## Frozen Exp066B result

Run `32982563070`, job `98222539772` returned:

`FAIL_ACT_UNWISE_SELECTED_BANDPOWER_CLOSURE_V0_1`.

The scientific contract was committed before execution at `ee80305fef9bb56954e4a82d1207ffaf2dab4ca5`.

### B1 — free-CLEFT nuisance algebra: PASS

The DSIR nuisance closure was compared against the exact pinned upstream free-CLEFT private equations on deterministic nonzero synthetic tensors.

- Blue coefficient and final-spectrum maximum differences: exactly 0.
- Green coefficient and final-spectrum maximum differences: exactly 0.
- Turning off only CLEFT raw tensors produced large nonzero changes in both channels, so the equality was not a zero-term accident.

### B2 — released signal bandwindow/transfer operator: PASS

The upstream signal path is

`D(C x)`, with `D=W C^{-1}`,

hence exactly `W x`. A separate small-matrix regression gave maximum difference `3.9968028886505635e-15` under the frozen `5e-13*max(1,max|ref|)` tolerance. Released ACT coupling and bandwindow matrices had the expected `6144×6144` and `59×6144` shapes and finite values.

### B3 — cheap white-noise reduction: FAIL

Upstream adds white noise before decoupling:

`D(C x + N w2 1)`, where `w2=sum(C[0,:])`.

The preregistered cheap reduction would have been valid only if

`C 1 = w2 1`.

For the released ACT `gg` coupling matrix the measured relative residual was

`max|C1-w2 1|/|w2| = 0.3615744168461421`,

far above the frozen `1e-10` threshold. Therefore the shortcut is mathematically false and is permanently forbidden for v0.1.

The `kg` matrix had a descriptive residual `0.342838189662599`; this does not enter the shot-noise gate because white noise is added only to `gg` in the likelihood.

### B4 — selected ordering: PASS

The exact selected order remains 26 entries:

`[Blue gg(6), Blue kg(7), Green gg(6), Green kg(7)]`.

The frozen midpoint sets are reproduced exactly.

## What the failure does and does not mean

Exp066B does **not** invalidate ACT × unWISE as a DSIR observational bridge. It invalidates only the proposed inexpensive constant-template shortcut for the auto-spectrum shot-noise term.

The exact upstream white-noise contribution is instead

`N w2 W C^{-1} 1`,

followed by the released transfer function. Since this template depends only on the fixed survey operator, not on cosmology or dark-sector physics, it can be precomputed once by an exact linear solve and then reused.

A corrective experiment must be separately numbered/preregistered. It may use an exact solve `C y=1` or an exactly equivalent precomputed template. It may not relax Exp066B's threshold, add jitter/shrinkage, change scale cuts, or reinterpret the failed constant-mode identity.

## Next scientifically admissible step

Exp066C should freeze an exact survey-only white-noise template construction and validate it against the literal upstream NaMaster expression on the released ACT matrix. Because a dense 6144×6144 inverse is unnecessary, the preferred implementation is an exact linear solve or a solver whose residual is explicitly bounded and frozen before execution.

Only after the entire selected-bandpower bridge is exact may the project move to a physical Weyl/matter convention bridge and then to a covariance-whitened training-only G7 relation search.

Top-level state remains **G7 OPEN, G8 OPEN, G9 OPEN**.
