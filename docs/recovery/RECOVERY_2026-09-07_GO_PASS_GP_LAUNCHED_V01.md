# DSIR recovery — Exp073GO support PASS and Exp073GP launched

Date: 2026-09-07. Scope: DSIR only. Never mix RTK or RQIR.

## Heavy authority preserved

Authoritative heavy process remains Exp073FU run `34103803637`, hosted launch audit job `101684090730` SUCCESS, home-science job `101684145754` IN_PROGRESS in the frozen `WW_S1_S3 A/B gate`. No competing self-hosted run was launched and no partial numerical output was inspected.

`WW_S1_S3` remains NOT ADMITTED. Only validated terminal FU candidate evidence followed by Exp073FV admission may create authority.

## Reconciled C2 support result — Exp073GO

Prospective gate commit: `4990506b70f77b288a4815a31de6f3a5c23563c9`.

Authoritative hosted run: `34098916677`, job `101668625499`, SUCCESS.

Raw log verified:

- pinned source commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- baseline `perturbations.o` SHA256 `c7bc0378e5d251f0419c6757790d986c0fc7828bd2736681f0f26c137a9ab0c8`;
- instrumented `perturbations.o` SHA256 `d308b6a663fa6f2db6ee7c51d91963f8540e9ea62ecc08bb89c161da98be184f`;
- `base_perturbations_tu_compiled=true`;
- `instrumented_perturbations_tu_compiled=true`;
- `full_executable_link_attempted=false`;
- `cosmological_run_started=false`;
- `self_hosted_science_started=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`;
- exact token `PASS_EXP073GO_C2_IDE_PERTURBATIONS_TU_ABI_EQUIVALENCE_V0_1`.

Classification: `SUPPORT_PLUS_0_PLUS_0`. This is not a C2 scientific PASS and creates no model authority.

Historical Exp073GN baseline full-build remains `BLOCKED_UPSTREAM_BASELINE_BUILD_PLUS_0_PLUS_0`; GO does not rewrite it.

## Newly frozen next support gate — Exp073GP

Prereg commit `d75191bb34b0aac5c03b015ecdf493d16da11ac7` freezes an eight-binary64 recorder ABI with exact field order `tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`, finite-only acceptance, append-only external serialization, exact round-trip requirement, and no solver-state mutation.

Fixture commit `c0b00d5abfab2098c5578685325e358c80ce5d46`.

Hosted workflow commit `a2f1711ad553e9be9e3e98ae0713fba34f59af11` launched Exp073GP run `34114027439`, job `101716542107`, queued at last reconciliation.

Expected token: `PASS_EXP073GP_C2_IDE_RECORDER_ABI_STATIC_AUDIT_V0_1`.

PASS ceiling remains `SUPPORT_PLUS_0_PLUS_0`; `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`. No numerical C2 generation is authorized merely by GP.

## Exact next actions

1. If FU becomes terminal, consume its raw logs/artifact first and classify under the frozen contract before any heavy successor.
2. If GP becomes terminal, inspect the raw log. PASS may authorize a separately prospectively frozen hosted integration/runtime extraction contract; implementation failure must be diagnosed and minimally repaired without changing C2 science.
3. Never duplicate the active FU home job.
