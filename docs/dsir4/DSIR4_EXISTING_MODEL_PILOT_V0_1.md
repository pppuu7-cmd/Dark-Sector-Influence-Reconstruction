# DSIR-4 existing-model pilot funnel v0.1

Frozen: 2026-09-07. Scope: DSIR only.

## Purpose

Migrate already-computed existing-model/control evidence from the legacy DSIR theory atlas into the prospectively frozen DSIR-4 Model Funnel Matrix without retroactively converting theory-space separability into observational PASS/FAIL.

This pilot does **not** create full model authority. The current overall status of every hypothesis remains `NOT_YET_TESTABLE` until all mandatory DSIR-4 gates have admissible authority.

## Frozen pilot hypotheses

The pilot reuses only hypotheses/equivalence objects already represented in `docs/GATES.md`:

1. `C0_LCDM_REFERENCE` — LambdaCDM/GR reference origin and exact solver-specific zero limits.
2. `C1_SMOOTH_W_LOCAL_EPS1E4` — smooth non-phantom DE local ray, `epsilon_w=1+w=1e-4` as the smallest frozen finite-difference step.
3. `C2_IDE_LOCAL_TANGENT_CONE` — interacting-dark-sector local tangent cone: physically allowed left-sided alpha ray plus two-sided beta tangent.
4. `C3_GDM_CS2_CV2_LOCAL_PAIR` — GDM local `cs2/cv2` tangent pair.
5. `C4_WDM_3KEV` — thermal WDM 3 keV control.
6. `C5_FR_B0_1E5` — H-EFTCAMB designer-f(R), `B0=1e-5`.
7. `C5_FR_B0_1E4` — H-EFTCAMB designer-f(R), `B0=1e-4`.
8. `C6_DCDM_DR_GAMMA_H0_1` — withheld DCDM->DR representative with `Gamma/H0=1`.

No new parameter point has been selected after looking at future observational gates.

## Legacy evidence retained, not upgraded

- C0 is the reference origin/control.
- C1 has a converged one-sided smooth-w ray.
- C2 has a non-collinear alpha/beta structure angle `58.9338 deg` in the frozen theory setup.
- C3 has near-collinear low-k matter-power rays (`0.322616 deg`) but a strong metric-slip separator (`137.9432 deg`; equalized Weyl+slip `56.9632 deg`).
- C4 3 keV is intentionally nearly blind at low k (`r_T(0.1)=-3.46e-6`) while becoming strong at high k (`r_T(10)=-0.10375`), so lack of discrimination in the current low-k DSIR domain is not a model PASS.
- C5 is represented by official H-EFTCAMB designer-f(R) production points; theory-space scale similarity with GDM is broken by time/sign structure in the frozen comparison.
- C6 supplied genuine withheld-family mechanism support; it did not close G7/G8.

These are legacy theory/control facts. None is observational model acceptance or rejection.

## Migration rule to DSIR-4

The new DSIR-4 mapping contract requires an explicit six-component residual mapping, frozen `T_known` convention, certified domain, prediction artifact identity/hash, and per-gate authority provenance. Legacy theory-atlas evidence by itself is insufficient to silently declare `G_DOMAIN_MAPPING=PASS`.

Therefore this pilot records, for each hypothesis:

- legacy theory evidence and exact provenance anchor;
- whether the hypothesis has response evidence inside the frozen DSIR domain;
- whether a distinct high-k block is required;
- mapping-conversion readiness;
- all current DSIR-4 gate statuses.

Until a dedicated model-mapping artifact is frozen and admitted, `G_DOMAIN_MAPPING` remains `NOT_YET_TESTABLE`. All later mandatory gates also remain `NOT_YET_TESTABLE`.

## Scientific interpretation

The existing repo already establishes that the candidate model families do **not** occupy one trivial identical theory manifold: IDE, GDM, WDM, designer-f(R), smooth-w, LambdaCDM and DCDM exhibit different response geometries/mechanisms. However, the repository also explicitly forbids treating raw theory-space separators as observational distinguishability before survey kernels and covariance whitening.

Thus the correct pilot conclusion is:

- existing models are sufficiently mature to enter a prospectively audited DSIR-4 mapping/conversion program;
- no tested family currently has a complete `DSIR PASS`;
- no family may be scientifically rejected from the complete DSIR funnel on this pilot alone;
- some parameter/mechanism directions are already known to be weakly identifiable or structurally degenerate in specific blocks, which will be useful when the observational gates open.
