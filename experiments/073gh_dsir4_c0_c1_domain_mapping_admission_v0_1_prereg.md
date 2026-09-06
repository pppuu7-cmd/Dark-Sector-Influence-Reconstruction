# Exp073GH — DSIR-4 C0/C1 G_DOMAIN_MAPPING admission v0.1

Frozen: 2026-09-07 after support-only Exp073GG mapping audit and before any domain-mapping authority is created.

Scope: admit **only** `G_DOMAIN_MAPPING` for two frozen hypotheses:
- `C0_LCDM_REFERENCE`;
- `C1_SMOOTH_W_LOCAL_EPS1E4` (`epsilon_w=1e-4`, `w=-0.9999`, smooth-DE control).

Required evidence:
- common residual convention blob `9ab68fe254891a076e24757de724e32e2190bfb6`;
- analytic mapping note blob `f080b8cec3197d8852a68e7de7e2183d2c7c6b50`;
- C0 mapping blob `46e9a402a57aee7baa4649784e868013ea6a07bb`;
- C1 mapping blob `cec09e097aa8650f488276ed21e949f34e4f4ac1`;
- validator blob `de0bce5e3e96d20e7a56e546cecfb846289b2f5c`;
- Exp073GG repaired support run/job `34060810001 / 101560878127` must be completed SUCCESS and contain `PASS_EXP073GG_DSIR4_C0_C1_MAPPING_STATIC_AUDIT_V0_1`.

Admission criteria:
1. same shared `T_known` and fixed `M0` convention;
2. all six residual components explicitly mapped with provenance;
3. exact full frozen domain `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`;
4. no quasi-static/sub-horizon rescue is required;
5. C1 is explicitly the phenomenological smooth-DE control and is not generalized to clustered quintessence;
6. prediction readiness and all observational gates remain separate and unavailable;
7. overall model status remains `NOT_YET_TESTABLE`.

PASS tokens:
- `PASS_EXP073GH_C0_LCDM_G_DOMAIN_MAPPING_ADMISSION_V0_1`;
- `PASS_EXP073GH_C1_SMOOTH_W_G_DOMAIN_MAPPING_ADMISSION_V0_1`.

PASS classification: `SCIENTIFIC_GATE_AUTHORITY_ADMITTED` for `G_DOMAIN_MAPPING` only. `scientific_model_authority_created=false` and `full_dsir_model_pass=false` are mandatory.
