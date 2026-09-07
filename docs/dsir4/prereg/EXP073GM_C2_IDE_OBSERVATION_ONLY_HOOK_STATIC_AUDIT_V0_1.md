# Exp073GM — C2 IDE observation-only pretransform hook static audit v0.1

Status: PROSPECTIVELY FROZEN BEFORE ANY C2 NUMERICAL GENERATION.
Scope: DSIR only. Scientific contribution ceiling: support +0/+0.

Pinned upstream source is exactly `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`; target is only `source/perturbations.c`. Predecessor authority is Exp073GL hosted PASS plus `C2_IDE_OBSERVATION_HOOK_SOURCE_SITE_AUDIT_V0_1.md`.

The committed transformer `scripts/dsir4/apply_exp073gm_c2_pretransform_hook.py` is the patch identity. It must fail closed unless it finds exactly one `class_call(perturb_total_stress_energy(...))` in `perturb_einstein`. It inserts the diagnostic call **after that helper returns and before the first native gauge/metric transformation** of `ppw->delta_m` or `ppw->theta_m`.

The hook receives only read-only scalar inputs already present at that runtime site: `tau`, physical solver `k`, native `a`, native `H`, pre-transform `ppw->delta_m`, pre-transform `ppw->theta_m`, native `rho_idm_iv`, and native `rho_iv`. It must not call a second background/cosmology calculation, read downstream `index_tp_delta_m`, or apply a second gauge correction.

The patch contains only two diagnostics-only additions: a conditional header include guarded by `DSIR_C2_PRETRANSFORM_HOOK`, and a guarded `dsir_c2_pretransform_observe(...)` call. It may not mutate `ppw`, `y`, `pvecback`, `pvecmetric`, approximation flags, derivatives, precision/tolerance state, species sums, integration state, branches, or evolution equations.

The hosted static auditor must prove: pinned commit identity; deterministic single-anchor insertion; hook ordering after helper return and before native correction; exact read-only argument identity; absence of mutation/downstream-export/second-background tokens; and byte-for-byte recovery of the original pinned source after removing the two exact diagnostic regions.

A PASS is only `SUPPORT_PLUS_0_PLUS_0`; `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, no model/scientific authority. Any failure is implementation/static `+0/+0` or invalid-for-science, never scientific model FAIL. Exact PASS token: `PASS_EXP073GM_C2_IDE_OBSERVATION_ONLY_HOOK_STATIC_AUDIT_V0_1`.

Even a GM PASS authorizes only a separately frozen hook implementation/build-equivalence stage. Numerical C2 generation remains forbidden until that later stage passes.
