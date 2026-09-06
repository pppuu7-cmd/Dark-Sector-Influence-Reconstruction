# DSIR20 — G_DOMAIN_MAPPING re-audit for IDE, GDM, and designer-f(R)

Date: 2026-09-07
Status: **CLOSED — THREE FAMILY MAPPINGS RE-ADMITTED FROM EXISTING HARD EVIDENCE**

## Purpose

Reconstruct the actual Gate-1/domain-mapping status of three already implemented known-model families without changing the frozen DSIR response contract and without treating infrastructure failures or downstream missing angular authority as model failures.

This note is a provenance re-audit of existing hard solver/manifold evidence. It is **not** a new observational ranking and it does not rerun or reinterpret partial Exp073FM outputs.

## Frozen common response contract

Authority basis: `config/response_basis_v0_1_1.json`, status `frozen-pass`.

Required first-six-family common coordinates:

- relative expansion `r_E` on the frozen redshift nodes;
- comoving total-matter response
  `r_Delta = ln[P_Delta_model/P_Delta_ref_same_solver]`
  on the common linear grid
  `k = {0.001,0.003,0.01,0.03,0.1} h/Mpc`.

Same-solver reference quotients, explicit matter-component provenance, fixed primordial parameters, model-specific solver/domain masks, and no zero-imputation are mandatory.

## C2 — interacting vacuum / IDE

Pinned upstream:
`kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Pinned interaction:

`Q = H (alpha rho_idm + beta rho_iv)`.

Source audit (`experiments/016_interacting_vacuum_perturbation_source_audit.md`) establishes the synchronous-gauge zero-coupling closure. The production family uses the physical composition `f_idm_iv=1`, `f_iv=1`, with explicit positivity checks on the interacting densities.

`experiments/030_comparison_readiness_gate.md` admits both a physical negative-alpha ray and a two-sided beta tangent line into the frozen 35-cell low-k block. The hard comparison-readiness run returned no failures and measured an alpha/beta structure angle of `58.933798 deg`.

**Reconstructed G_DOMAIN_MAPPING verdict: PASS.**

Scope: PASS means a valid, provenance-controlled mapping into the frozen DSIR response domain. It is not an observational preference for IDE.

## C3 — generalized dark matter / GDM

Pinned upstream:
`s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

Source-level zero-closure regression (`experiments/014_gdm_zero_limit_source_regression.py`) verifies the CDM limit at background, perturbation-equation, shear, and leading adiabatic-IC level, with the documented finite-start IC caveat.

`experiments/025_gdm_cs2_manifold.md` establishes a nonzero sound-speed response manifold on the frozen response grid. The frozen response-basis contract explicitly keeps `k<0.001 h/Mpc` outside the core for the pinned GDM implementation because of finite-start IC sensitivity.

`experiments/030_comparison_readiness_gate.md` admits both positive `cs2` and `cv2` rays into the 35-cell common block; the hard run returns no failures and reproduces their orientation angle `0.322616 deg`.

**Reconstructed G_DOMAIN_MAPPING verdict: PASS.**

Scope: this does not resolve the strong internal cs2/cv2 low-k degeneracy; that requires later discriminant channels.

## C5 — designer f(R)

Pinned official upstream:
`EFTCAMB/EFTCAMB@16d9c4e9f85751e30efd0a53b177941713078904`.

`experiments/021_eftcamb_designer_fr_gr_limit.md` closes MG-S0 with pre-frozen hard conditions. The fresh hard rerun obtained

`max |r_Delta(B0=0)| = 1.0926960404022163e-6 < 2e-6`,

`|B0_found| = 2.221e-17 < 1e-12`,

and theory stability passed.

The nonzero production direction uses same-solver GR quotients. `experiments/030_comparison_readiness_gate.md` admits the minimum resolved production ray `B0=1e-6` after exact-zero-floor subtraction. The comparison-readiness hard run returns no failures.

**Reconstructed G_DOMAIN_MAPPING verdict: PASS.**

Scope: this is domain admissibility and a controlled GR limit, not evidence that f(R) is preferred by observations.

## Cross-family hard evidence

`experiments/030_comparison_readiness_gate.md`:

- status: `PASS_READY_FOR_BLOCK_AWARE_MODEL_COMPARISON`;
- exactly six nonzero low-k response objects required and admitted;
- failures: `[]`;
- IDE, GDM, and designer-f(R) all present in the admitted aggregate.

`experiments/031_first_model_comparison.md` then performed the first actual cross-family comparison in the same 35-cell response space. It found, among other diagnostics:

- GDM cs2 vs cv2: `0.3226 deg`;
- IDE negative-alpha vs GDM cs2: `24.9345 deg`;
- GDM cs2 vs designer-f(R): oriented ray angle `154.8182 deg`;
- nearly identical leading low-k scale shapes for GDM cs2/cv2 and designer-f(R), while their time/sign behavior differs.

This is raw theory-response geometry, not an observational likelihood or Bayes-factor ranking.

## DSIR20 verdict table

| Family | G_DOMAIN_MAPPING | Evidence status | Downstream status |
|---|---|---|---|
| IDE | **PASS** | pinned source + zero-coupling source audit + admitted alpha/beta hard response | observational/angular gates remain downstream |
| GDM | **PASS** | pinned source + CDM zero closure + admitted cs2/cv2 hard response | extra channel needed to break internal low-k degeneracy |
| designer-f(R) | **PASS** | pinned H-EFTCAMB + hard GR limit + admitted B0=1e-6 response | observational/angular gates remain downstream |

## Authority boundary

The current missing `G_ANGULAR_AUTHORITY` is downstream of this domain-mapping result. Its absence must **not** erase these Gate-1 passes, and the failed Exp073FM terminal consumer must **not** be converted into a scientific model failure.

Therefore DSIR20 should no longer describe IDE, GDM, or designer-f(R) as waiting for `G_DOMAIN_MAPPING`. Gate-1 is already supported by repository hard evidence. The next scientifically new task is to carry these already-admitted families through the next common observational/discriminant gates under the same frozen no-tuning rules.
