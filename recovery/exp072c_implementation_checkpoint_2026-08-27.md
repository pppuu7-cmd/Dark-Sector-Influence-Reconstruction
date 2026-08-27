# DSIR recovery checkpoint — Exp072C implementation — 2026-08-27

Exp072C preregistration is already merged to `main` before any Exp072C computation.

The implementation is diagnostic only and must:

- bind exact Exp072A and Exp072B immutable artifacts;
- reconstruct the same pinned ACT×unWISE/CAMB positive operator geometry;
- vary only the lower-z and upper-k support boundaries on exact sampled projection values;
- keep `z_max=2.33`, `k_min=0.000704833374744468 Mpc^-1`, threshold `0.05`, 26 coordinates and 64 block pairs fixed;
- reproduce the Exp072B current-boundary result before accepting a frontier;
- compute only unit-invariant within-block leakage and the frozen discrete Pareto frontier;
- never read covariance, whitening, nuisance rank/SVD, G7 relation/null, G8 response or article-selection quantities;
- never execute or extend C3/C5 physical providers.

A frontier is planning geometry only. Any selected provider-extension target remains blocked by `docs/PROVIDER_EXTENSION_NATIVE_SUPPORT_BOUNDARY_2026-08-27.md` until both providers independently pass a new prospective certification.

Exp072A remains permanent scientific FAIL and Exp072B remains `DIAGNOSTIC_K_ONLY_TARGET_NOT_FOUND_EXP072B` under every Exp072C outcome.

G7/G8/G9 remain OPEN.
