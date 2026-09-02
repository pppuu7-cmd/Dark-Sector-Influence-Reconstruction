# Exp073CF actual successor workflow/binding static audit — BLOCKED on activation gate placement

Date: 2026-09-02
Classification: `STATIC_INFRASTRUCTURE_AUDIT_NONCLASSIFYING`, readiness `+0/+0`.

## Objects audited

- actual workflow: `.github/workflows/exp073cf-continuation-successor-v0-1.yml`, workflow commit `93ac80426c877c4769ded24fb16196fcfa2501f5`;
- prospective binding: `experiments/073cf_continuation_successor_v0_1_binding.json`, binding commit `1a9f34f87d4e485b00b073e1a75eafd90b0cbe5c`;
- passed disabled design object: `ci/exp073cf_continuation_successor_v0_1.disabled.yml`;
- continuation wrapper commit `ce818db7ae53376ba6e5f7934c24f4c5acb3c75c`;
- checkpoint transport v0.2 commit `bc468ca73a3c4e281bd2b1ee46d6f7704bb54bb1`.

Repository-wide coordination check immediately before this audit: `queued=0`, `in_progress=0`.

## Preserved PASS portions

The actual workflow/binding preserves the intended scientific/infrastructure contract for:

- A/B `max-parallel=1`;
- exact restore heads A=`5c7ccddb54afe1ad286d08abc6f7372aa5a11103`, B=`ce9189a1ccaabc62708f753897b9cab5f51cb9f4`;
- restore through checkpoint sync v0.2;
- resumed heavy computation only through `ci/exp073cf_continuation_wm_s2_v0_1.py`;
- frozen helper lineage and threads=8 / chunk=4 semantics;
- exact DES size/SHA and hardened HTTP/1.1/retry/resume transport;
- fresh memory-stable PCL, frozen compile/preflight, 60 s heartbeat;
- exact compact/final comparators and no-rescue policy;
- historical payload provenance kept separate from continuation transport provenance.

## Blocking finding

`on: workflow_dispatch` is enabled while the first scientific matrix job is directly:

`runs-on: [self-hosted, Linux, X64]`.

The activation/binding guard is currently the first **step inside that self-hosted job**, after Actions has already scheduled the job to the home runner and checkout has begun.

Therefore a manual dispatch made before the prospective activation file exists could still queue/start DSIR-HOME-PC work before the activation guard fails. That does not satisfy the stronger coordination requirement that the home runner remain untouched until a separate prospective activation/trigger authorization exists.

No such manual dispatch occurred in this audit; current Actions state remains empty.

## Verdict

`BLOCKED_EXP073CF_ACTUAL_SUCCESSOR_ACTIVATION_GATE_PLACEMENT_V0_1`, `+0/+0`.

This is an infrastructure/control-plane blocker only. It does not alter or classify Wm_S2 science.

## Required repair

Before any self-hosted authorization, prospectively revise the workflow so unauthorized dispatch cannot schedule a home-runner job. Acceptable minimal patterns include either:

1. a hosted `ubuntu-24.04` authorization job that validates exact workflow/binding/activation state first, with the self-hosted matrix `needs:` that hosted job and therefore never schedules if authorization fails; or
2. removing `workflow_dispatch` and using a separately created, exact-bound activation-file push as the sole trigger, while preserving a pre-self-hosted coordination gate.

Prefer pattern 1 because it makes accidental/manual dispatch fail on hosted infrastructure and leaves DSIR-HOME-PC untouched.

Any workflow edit changes the workflow commit and therefore invalidates binding commit `1a9f34f87d4e485b00b073e1a75eafd90b0cbe5c`; after repair, create a new prospective binding to the repaired exact workflow commit. Do not reuse the old binding as authority.

## Authority/readiness

Exp073CF attempt2 remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT2`, `+0/+0`.

Durable checkpoint authority remains A 32/39 and B 28/39. Article-3 readiness remains **Verified 52.0% | Draft/data 53.7%**.
