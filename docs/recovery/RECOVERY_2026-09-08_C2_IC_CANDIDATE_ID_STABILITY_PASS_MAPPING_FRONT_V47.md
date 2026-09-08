# DSIR Recovery V47 — Exp073IC candidate PASS; Exp073ID exact stability PASS; C2 mapping front

Date: 2026-09-08 UTC. Scope DSIR only; RTK/RQIR excluded.

## Preserved authority
All prior DSIR scientific authority is unchanged, including admitted `WW_S3_S3` from run `34218457380 / 102035691774`, GA artifact `10051382493`, SHA256 `a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. C2 still creates no prediction/model scientific authority.

The C2 reference chain HT/HU/HV/HW and tangent HZ/IA/IB-v0.2 chain remain preserved exactly as recorded in V46. Historical IB v0.1 remains `IMPLEMENTATION_PROVENANCE_FAIL_PLUS_0_PLUS_0`, not scientific FAIL.

## Exp073IC deterministic tangent response candidate PASS
- prereg creation commit: `7d94f9f9bfaa3b320250c7b046d2a6c7a37309b5`
- prereg blob: `9e1235a48a4288bb2083d69084f1cae7d79847bb`
- workflow/head: `f3475f5d409a50c31fb1eda3870837542797e091`
- run/job: `34249380208 / 102139612475`
- artifact: `10065344213`
- GitHub ZIP SHA256: `e48b0fd4f7d80717231df60a5065d9f1eac37a13193951f17d01ee34761ff7dc`
- canonical response JSONL SHA256: `e97ef98a5b137081df5937454f02576d30e726266e9c50733bf399a9be2b1907`
- raw token: `PASS_EXP073IC_C2_TANGENT_FINITE_DIFFERENCE_RESPONSE_CANDIDATE_V0_1`
- classification: `TANGENT_RESPONSE_CANDIDATE_PLUS_0_PLUS_0`.

IC used only the prospectively frozen HX definitions: one-sided negative alpha and symmetric beta finite differences at `h=1e-4,1e-3,1e-2`, with `1e-4` base and larger scales controls. It did not select a scale, impose a convergence threshold, extrapolate, smooth, fit, predict or create scientific authority. Its artifact was independently verified for exact ZIP digest, exact 28-row request order, canonical SHA and finite binary64 fields.

## Exp073ID prospective no-tolerance numerical stability admission PASS
Critically, the ID rule was prospectively frozen **before inspecting IC inter-scale numerical relationships**.

- prereg creation commit: `538c2839cf7eff40cafe0561bbdf745c9a98f446`
- prereg blob: `92454c05e19b95ba04574d9c077c5ccba6d38920`
- workflow/head: `9e6ba30de55a2fa3f63a6d47d22015aa6cfa2265`
- run/job: `34249671091 / 102140579398`
- artifact: `10065453571`
- GitHub ZIP SHA256: `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`
- raw token: `PASS_EXP073ID_C2_TANGENT_RESPONSE_MONOTONE_SCALE_STABILITY_ADMISSION_V0_1`
- classification: `TANGENT_RESPONSE_NUMERICALLY_ADMITTED_PLUS_0_PLUS_0`.

Frozen exact rule for every one of 28 coordinates and both alpha/beta directions: `e_small=abs(D(1e-4)-D(1e-3))`, `e_large=abs(D(1e-3)-D(1e-2))`, exact binary64 PASS iff `e_small <= e_large`, no tolerance. Raw result: `stability_check_count=56`, `stability_fail_count=0`. Independently downloaded artifact verifies 56/56 `pass=true`, exact digest and authority receipt.

Therefore the C2 numerical boundary advances to:
- `mapped_reference_coordinate=true`
- `mapped_tangent_coordinate=true`
- `response_candidate_created=true`
- `tangent_response_ready=true`
- `admitted_base_step=1e-4`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

This is numerical tangent-response admission only. It is not full C2 model admission.

## DSIR-4 mapping requirement now controls the frontier
The frozen DSIR-4 mapping contract requires a dedicated versioned six-component residual mapping under the common convention `X_munu=M0^2 G_munu - T_known_munu`, with explicit sector partition, gauge/velocity convention, certified domain, source/code provenance and later separate prediction artifact. For interacting dark sectors, the authoritative common source is the **total** dark-sector residual; internal transfer bookkeeping must not create false differences.

C2 may therefore not advance directly from ID to a prediction or observational gate. The exact next research front is a prospective C2 six-component residual mapping/source audit, binding the pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` implementation to the DSIR-4 common interface and identifying any still-unmapped components without silently treating them as zero.

## Current process / ownership
At V47 creation live Actions state is `0 in_progress / 0 queued`. Home/self-hosted runner has no owner and remains free. No competing heavy run exists.

## Exact next transition
Prospectively freeze and run a hosted-only `Exp073IE` C2 six-component residual mapping source/readiness audit. It must inspect the exact pinned background and perturbation implementation and classify each required component (`rho_X,p_X,delta_rho_X,q_X,delta_p_X,pi_X`) as source-derived/structural-zero/not-yet-mapped/outside-domain with explicit evidence. It must not create `G_DOMAIN_MAPPING=PASS` merely from tangent-response readiness. If one or more components lack a proved source mapping, record the support result and launch only the smallest prospective extractor/derivation gate needed next.

Global frozen DSIR boundaries remain unchanged.