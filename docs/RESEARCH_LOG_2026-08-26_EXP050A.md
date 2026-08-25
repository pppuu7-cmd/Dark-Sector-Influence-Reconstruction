

<!-- DSIR_EXP050A_DOC_SYNC_2026_08_26 -->
# Research log — 2026-08-26 — Exp050A

Exp050A first hard run `32908751625` passed. Artifact `9585845292`, SHA256 `5d02bdce07da95c2bb9eab01acb2641f110b6b16e4ecf29ac2e8b1619d053139`.

C4 thermal-WDM is now represented by a solver-native high-k `(k,z)` atlas rather than only the legacy static transfer fit. The strongest new descriptive result is that large free-streaming suppression is nearly time-separable over the frozen linear domain: `chi_I~2e-10` for all three masses.

This closes the *time-domain missing-data issue* for the current C4 block, but not any universal-law or observation-space gate. Next step is a block-aware atlas/discriminant recomputation and an independent withheld WDM free-streaming validation.
