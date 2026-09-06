# DSIR immutable recovery — Exp073FK S1S1 transformation contract PASS while Exp073FG runs

Date: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Active science ownership preserved

Exp073FG `WW_S0_S3` remains the authoritative science process: run `34034377795`, head `4a02952ee3bcb368a088d87608f61243cd9f7056`, home job `101489679508` on `DSIR-HOME-PC`. At the latest live check the home job remained IN_PROGRESS in the frozen S0->S3 A/B step. No partial numerical output was inspected and no competing self-hosted workload was launched.

## Exp073FK support contract

Preregistration `experiments/073fk_ww_s1_s1_same_field_transformation_contract_v0_1_prereg.md`, blob `f1deff3378f991a9a052b5314ccec1d19629f9b0`, creation commit `e913a49ac914eddf204e17ad9d76814d1fe542e3`.

Hosted workflow `.github/workflows/exp073fk-ww-s1-s1-same-field-transformation-contract-v0-1.yml` was added at commit `df6b4bf33930c075e930b269eca6a5c858758237` and activated by commit `114d99c61c359c93ad462862f33642f196105f6c`.

Workflow/run `34037855604`, job `101499105572`, head `114d99c61c359c93ad462862f33642f196105f6c` completed SUCCESS. Raw job log was consumed and contains exact token `PASS_EXP073FK_WW_S1_S1_SAME_FIELD_TRANSFORMATION_CONTRACT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `ww_s1_s1_authority_created=false`, `self_hosted_science_started=false`.

The audit froze and cross-checked the future auto-pair transformation boundary against Exp073FH, Exp073FJ, the generic Article-3 task runner and the current Exp073FG cross-pair durable source. Required future changes are inseparable: `[0,3]/S0->S3` -> `[1,1]/S1->S1`; two source reconstructions -> exactly one authoritative S1 reconstruction; distinct source payload identities -> one source identity; distinct-field handoff false -> same-field-object handoff true; cross field construction -> one spin-2 field object reused on both coupling sides; dedicated future S1S1 task/token/checkpoint namespaces. No tolerance/allclose/isclose/rounding/smoothing/averaging rescue is authorized.

## Classification and next action

Exp073FK is support `+0/+0` only. It creates no `WW_S1_S1` scientific authority and does not authorize self-hosted S1S1 science while Exp073FG owns the runner. Immediate science gate remains terminal consumption and classification of Exp073FG. If Exp073FG reaches a valid candidate PASS, a separate provenance-admission gate is still mandatory before `WW_S0_S3` authority. Only after runner release and predecessor governance may S1S1 production implementation be prospectively frozen and audited.