# DSIR recovery checkpoint — Exp073B implementation — 2026-08-27

Exp073B preregistration is already merged to `main` before this implementation.

The implementation binds the exact Exp073A immutable negative result and clones the exact pinned C3, C5 and ACT×unWISE source commits. It performs a source/provenance capability audit only.

Frozen distinctions preserved:

- the DSIR/ACT projector can consume three independent `P_mm`, signed `P_Wm`, `P_WW` blocks;
- upstream CLEFT capability is not automatically a nonlinear MG Weyl provider, especially where an explicit `matter2weyl_factor` is used;
- the current certified C3 provider is linear (`pk_lin` + linear `phi/psi` transfer construction);
- the current certified C5 q=3 provider explicitly sets `nonlinear=False` / `NonLinear_none`;
- generic nonlinear matter implementations do not count as physically justified independent nonlinear Weyl auto/cross providers for GDM or designer-f(R);
- no covariance, whitening, nuisance SVD, G7 relation/null, G8 output or new numerical provider extension is read/run.

If the audit is trustworthy but either C3 or C5 lacks complete independent nonlinear matter/Weyl capability, the frozen outcome is `GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B`.

G7/G8/G9 remain OPEN. Repository-sync policy remains active.
