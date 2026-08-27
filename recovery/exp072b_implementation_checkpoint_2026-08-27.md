# DSIR recovery checkpoint — Exp072B implementation — 2026-08-27

Exp072B was preregistered and merged to `main` before this implementation branch was created.

Implementation scope is diagnostic only:

- bind exact Exp072A run `33029362485`, artifact `9629763833`, digest `sha256:9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d`, and extracted JSON SHA256 `56b96c096830bf8399ef18df41251a14ded00101a1f206b4419ccb6b5730abe3`;
- reconstruct the same pinned ACT×unWISE/CAMB positive operator geometry;
- decompose each of 64 coordinate-block pairs into the frozen 3×3 redshift/k support states;
- reproduce every parent per-block leakage within `5e-13`;
- compute only the preregistered discrete upper-k-only `K_req_pair`, `K_req_coord`, and route target;
- do not read covariance, whitener, nuisance SVD/rank, G7 relation/null, G8 response, or article-selection quantities;
- do not extend either physical provider;
- preserve Exp072A as permanent scientific FAIL regardless of Exp072B outcome.

The workflow is intentionally `push: main` / manual only, so the first Exp072B decomposition output can occur only after the already-frozen preregistration is present in `main`.

Allowed Exp072B outcomes remain exactly:

- `DIAGNOSTIC_K_ONLY_TARGET_FOUND_EXP072B`;
- `DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B`;
- `FAIL_EXP072B_REPRODUCTION_OR_PROVENANCE`;
- infrastructure failure before full diagnostic: `INCOMPLETE_EXP072B` by interpretation, not a scientific result.

G7/G8/G9 remain OPEN.
