# DSIR recovery checkpoint — Exp072B preregistration — 2026-08-27

Current scientific state before Exp072B computation:

- Exp072A is permanent scientific FAIL `FAIL_ACT_UNWISE_ANGULAR_SUPPORT_LEAKAGE_MASK_V0_1`.
- Frozen Exp072A threshold remains 0.05.
- Nominal and tightened retained dimensions are both 0/26.
- No covariance restriction, Cholesky, nuisance SVD/rank, G7 relation/null, or G8 response is authorized.
- G7/G8/G9 remain OPEN.

Exp072B is preregistered before any new support-boundary decomposition output. Its contract is in:

`experiments/072b_exp072a_support_boundary_decomposition_prereg_v0_1.md`.

Key locks:

- same pinned ACT×unWISE/CAMB/archive provenance and same positive operator geometry as Exp072A;
- exact binding to Exp072A run `33029362485`, artifact `9629763833`, artifact digest `sha256:9ecf7d61b4db5e091392a23f508cd5dd3d04dafe32a4a66d1256a70d9947701d`, extracted JSON SHA256 `56b96c096830bf8399ef18df41251a14ded00101a1f206b4419ccb6b5730abe3`;
- exactly 26 coordinates and 64 applicable coordinate-block pairs;
- unit-invariant within-block 3×3 z/k partition;
- exact per-block parent leakage reproduction tolerance `5e-13`;
- only hypothetical support change allowed is upper-k extension;
- same 0.05 threshold and same route requirements: >=15 coordinates plus Blue/Green gg/kg coverage;
- `K_req_pair`, `K_req_coord`, and smallest `K_target_route` are discrete sampled-k quantities with no interpolation;
- result labels are diagnostic only and cannot rescue Exp072A.

If a finite k-only route target is found, the next step is provider certification for both C3 and C5, not an observational mask or covariance run.
