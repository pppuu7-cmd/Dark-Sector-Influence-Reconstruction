# DSIR recovery — Exp073GJ C2 Delta_m freeze closed support-only; Exp073FS attempt 2 running

Date: 2026-09-07. Scope: DSIR only; never mix RTK/RQIR.

## Heavy process authority

Authoritative heavy workflow remains Exp073FS `34067352681`, attempt `2`, head `f3e49041a5b869ddf22be8ca7a612901ec9f9458`.

- home job `101592579318` remains the sole in-progress DSIR heavy job;
- runner ownership remains `DSIR-HOME-PC-2` / runner id `22` exclusively for job `101592579318`;
- active frozen step remains `Run frozen WW_S1_S2 A/B gate with durable checkpoints`;
- hosted launch audit `101592593435` is SUCCESS support `+0/+0`;
- evidence collection/upload have not started;
- no partial numerical output/checkpoint was inspected;
- no competing self-hosted/heavy workflow was launched.

Attempt 1 remains historical `INFRASTRUCTURE_RUNNER_ORCHESTRATION_FAIL_PLUS_0_PLUS_0` and created no science authority.

## New independent C2 IDE freeze

Exp073GJ prereg was prospectively created in commit `668031cade3455e795e299056c9d98334b4ad0e3` at `experiments/073gj_c2_ide_delta_m_generation_freeze_v0_1_prereg.md` before any new C2 numerical generation.

Frozen interface:

- solver lineage `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- common same-solver bridge `Delta_m = delta_m + 3*(1+w_m)*Hconf*theta_m/k^2` and matched model/reference `r_Delta`;
- parameter points `(0,0)`, `(-1e-4,0)`, `(0,+1e-4)`, `(0,-1e-4)`;
- z nodes `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`;
- exact in-domain legacy-node intersection `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`;
- legacy `0.067 Mpc^-1` remains excluded because it exceeds frozen `k_max=0.06664762008318016`;
- raw legacy `mPk`, raw `delta_idm_iv`, Newtonian-gauge IDE, interpolation/rounding/effective-coordinate/fiducial shortcuts remain forbidden;
- branch masks `rho_idm>0`, `rho_iv>=0`, deterministic canonical JSON and payload SHA256 are mandatory.

## Static-audit failure/repair history

Exp073GJ hosted static audit did not start self-hosted science in any attempt.

- `34081553496 / 101617650342`: implementation/static FAIL `+0/+0` from an audit-harness literal mismatch;
- `34081596871 / 101617772642`: diagnostic FAIL `+0/+0` isolated the missing `r_Delta` literal;
- `34081626964 / 101617857129`: harness repair attempt still checked `ln[` and failed `+0/+0`;
- first causal defect: audit harness expected square-bracket `ln[...]` while the immutable prereg froze parenthesized `ln(...)`;
- minimal repair commit `1b977af76a7ca2de438156a7ceb88c4e1a29844c` changed only the support audit literal; no scientific formula, parameter, domain, threshold or solver lineage changed;
- repaired `34081658093 / 101617944759`: raw token `PASS_EXP073GJ_C2_IDE_DELTA_M_GENERATION_FREEZE_STATIC_AUDIT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `self_hosted_science_started=false`, `scientific_model_authority_created=false`.

Exp073GJ therefore closes only the generation-interface freeze/static-audit prerequisite. C2 remains `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific contribution `+0/+0`.

## Exact next actions

Priority remains terminal consumption of Exp073FS attempt 2. On terminal success verify raw log/artifact digest, checkpoint restore/new provenance, ordered S1->S2 distinct-field semantics, frozen identities, exact `19,327,352,832`-byte mmap proof, finiteness and exact A/B equality; only validated candidate PASS permits Exp073FT admission.

While FS remains active, the independent C2 next step is implementation/static audit of the pinned-lineage generator under the already-frozen Exp073GJ interface, without inspecting partial FS output or using downstream C2 results.