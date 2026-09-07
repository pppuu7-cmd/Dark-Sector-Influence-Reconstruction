# DSIR research log — 2026-09-07 — autoguard check and C2 source-site advance

## Heavy-chain status

Active heavy workflow: Exp073FU WW_S1_S3 autonomous audited home science v0.1.

- run id: `34089383137`;
- head SHA: `11b62ebd73fe8bed03f31c559593756149c7fbc0`;
- hosted-launch-audit job `101639612389`: `SUCCESS`;
- home-science job `101639652148`: `IN_PROGRESS`;
- active compute step: `Run frozen WW_S1_S3 A/B gate with durable checkpoints`;
- evidence collection/upload steps remain pending because no terminal scientific artifact exists yet.

Repository-wide Actions query at this check found exactly one `in_progress` run, the heavy run above. No duplicate heavy-run was launched.

The newest failure remains the already-repaired Exp073GL first attempt run `34093447421`; its repaired successor run `34093619964` completed successfully. No newer unresolved failed workflow was found in this check.

Classification: current heavy chain = **RUNNING / no terminal science classification yet**. The prior GL failure remains **infrastructure/static-matcher failure +0/+0**, not scientific FAIL.

## Safe DSIR4 advance while heavy computation runs

Created `docs/dsir4/mappings/C2_IDE_OBSERVATION_HOOK_SOURCE_SITE_AUDIT_V0_1.md`.

Pinned source audit establishes an exact observation-only runtime site in `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`:

- `perturb_einstein` receives native `tau` and `k`;
- native `a,H` are already present in the current background workspace;
- `perturb_total_stress_energy` returns with pre-transform `ppw->delta_m` and `ppw->theta_m` assigned;
- the native CLASS gauge-independent correction occurs later;
- therefore all required bridge inputs can be read before transformation without a second background calculation or solver-state mutation.

A convention boundary is explicitly frozen: this `Delta_m` coordinate is the pinned pressureless total-matter observable partition and must not be silently identified with the full residual source `X=T_idm+T_iv`.

Source-site audit commit: `449bec72a3f3579f4cc6b39a2aa17e22eead56f6`.

## Scientific state

- C2 mapping_ready = `true`;
- C2 source_site_ready = `true`;
- actual diagnostic patch/build equivalence audit = absent;
- C2 prediction_ready = `false`;
- C2 `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- no new scientific PASS or FAIL;
- contribution this iteration = `+0/+0`.

Next permitted C2 action: commit an actual diagnostic-only patch and hosted static/build no-mutation equivalence audit. Numerical C2 prediction generation remains forbidden until that implementation audit passes.
