# DSIR research checkpoint — Exp068A (2026-08-26)

## Frozen scientific result

Exp068A remains permanently

`FAIL_ACT_UNWISE_PHYSICAL_FORWARD_REPRODUCTION_V0_1`.

The scientific contract was preregistered before the first physical comparison. No tolerance, cosmology, tracer file, ell range, projector setting, or acceptance criterion was changed after output.

Scientific run:

- GitHub Actions run: `33003973559`;
- job: `98292701587`;
- artifact: `9620309853`;
- artifact ZIP digest: `sha256:ebbaa11a1591762299f905978a9ee0840ee348ea823550ea7a0b6c7037a4ae07`;
- workflow source branch head: `37a1e08c39c4c94fe10b3797fbcacc243f61ee3f`;
- PR synthetic merge SHA used by Actions: `12392994f434aa2b8c231c985c65a9839e55c80e`;
- base entering the PR: `main@502af6dc9789665d373868536ff5282af8d446bf`.

The first run `33001472791` was infrastructure-only: NERSC connectivity failed before the scientific script executed. It is not a scientific Exp068A classification. The scientific run used the official NASA LAMBDA mirror and accepted it only after the same frozen archive digest passed exactly:

`1b2d1563c5eb548ca6488ed8d60c5260d9e110b743a2e3a84620cfe46fbb6570`.

## Subtest outcome

- provenance: PASS;
- pinned source contract: PASS;
- physical CAMB `P_WW/P_Wm/P_mm` sanity: PASS;
- raw upstream↔DSIR component equivalence: PASS;
- nontrivial physical-signal control: PASS;
- tracer/PCA binding: **FAIL**.

Thus the frozen overall classification is FAIL solely because the preregistered tracer test expected the number of correction columns reported by `dNdz.n_pcs` to equal the number of sampled PCA nuisance parameters.

Measured:

- Blue released correction file shape: `500×5`, hence 4 correction columns after z; frozen expectation: 3;
- Green released correction file shape: `500×7`, hence 6 correction columns after z; frozen expectation: 5;
- Blue upstream `bdNdz(z,pcs=True)` shape on 96 projection nodes: `96×5`;
- Green upstream `bdNdz(z,pcs=True)` shape: `96×7`.

## Exact forward equivalence nevertheless passed

For every raw no-CLEFT component, the DSIR adapter and exact pinned upstream algebra had identical shapes, identical finite/nonfinite patterns, and

\[
\max |X_{DSIR}-X_{upstream}|=0
\]

at float64 precision on the full frozen `ell=0..6143` support.

Nonzero physical components included `gg_bsq`, `gmu_b`, `mumu`, `kg_b`, and `kmu` for both Blue and Green, so the equality is not a zero-output accident.

Examples of nontrivial maxima:

- Blue `gg_bsq`: `2.8611973417824423e-06`;
- Blue `kg_b`: `5.941018853189526e-07`;
- Green `gg_bsq`: `5.000267485528644e-07`;
- Green `kg_b`: `2.45381472754403e-07`.

## Post-failure source diagnosis — no reclassification

The pinned source explains the 4/6 versus 3/5 mismatch exactly.

`model_helpers_unWISExLens.py::dNdz` documents the correction object as follows:

> first component = mean `Delta dN/dz`; subsequent components = PCA modes.

`unWISExLensTheory.load_sample_data()` loads **all** released columns after redshift into that correction interpolator:

`delta_dndz_pcs_data[:,1:]`.

The raw projector then prepends the fiducial cross-correlation distribution. Hence its basis dimensions are

- Blue: `1 fiducial + 1 mean correction + 3 sampled PCs = 5`;
- Green: `1 fiducial + 1 mean correction + 5 sampled PCs = 7`.

The likelihood itself independently confirms the coefficient semantics. It samples only 3 Blue and 5 Green nuisance PCA coefficients, while `unWISExkappa_model.evaluate()` constructs

\[
\boxed{p_{PCA}^{final}=(1,1,c_0,c_1,\ldots)}.
\]

The first coefficient fixes the fiducial `bdN/dz`, the second coefficient fixes the released **mean correction**, and only the remaining entries are sampled PCA deviations. The source explicitly asserts

`len(pca_coeff[i]) == n_pcs - 1`.

Therefore Exp068A's tracer-binding hypothesis was wrong: `dNdz.n_pcs` counts the mean-correction column plus sampled PCs, whereas the nuisance prior count includes only sampled PCs.

This diagnosis is made after the frozen FAIL and does **not** turn Exp068A into PASS.

## Exact corrective next step

A separately numbered Exp068B is scientifically admissible. It must be preregistered before its first output and must preserve all physical Exp068A settings. The only corrected scientific statement is the literal upstream tracer contract:

- Blue correction-basis count = 4 = 1 mean + 3 sampled PCs;
- Green correction-basis count = 6 = 1 mean + 5 sampled PCs;
- raw basis widths = 5 and 7 after prepending fiducial `bdN/dz`;
- `p_PCA_final=[1,1,pca...]` must be verified from pinned source and by a deterministic contraction control.

Exp068B may not relax the `5e-13` raw-equivalence tolerance, change the physical cosmology/domain, or erase the Exp068A FAIL.

## Gate state

- G7: OPEN;
- G8: OPEN;
- G9: OPEN.

Even a future Exp068B PASS would close only the physical linear/no-CLEFT ACT×unWISE raw-forward prerequisite. The later validity-mask, covariance-subspace whitening, nuisance-tangent, G7 law/null, and G8 withheld barriers remain separate.
