# Exp073DT runner-shutdown reconciliation and resume authority

Date: 2026-09-05
Scope: DSIR only.

## Terminal classification
Exp073DT run `33940588308`, hosted preflight job `101237102962`, self-hosted science job `101237118421`.

The self-hosted job terminated as infrastructure `+0/+0`, not a scientific result. The first causal failure in the decoded job log is GitHub runner shutdown at `2026-09-05T03:56:42Z`: `The runner has received a shutdown signal`, followed by operation cancellation. The frozen science step was therefore cancelled; terminal evidence upload was skipped; no terminal comparator artifact exists and `WW_S0_S0` authority was not created.

Before shutdown the same continuous-flock science step had already passed live exclusivity, PyMaster 2.7 validation and the exact runtime OpenMP-team=8 certification. The frozen DQ driver writes durable complete-stage manifests and validates source head, contract fingerprint, checkpoint namespace and payload hashes on restore. Its fixed durable root remains `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`, so a rerun of the same frozen job is permitted to restore only verified complete stages and recompute only the interrupted/incomplete stage.

No scientific arithmetic, threshold, tolerance, domain, source head, contract fingerprint, component blob or checkpoint namespace is changed. No fresh competing control plane or duplicate heavy job is authorized.

## Resume decision
Diagnosed cause is external runner shutdown, not a reproducible code/science defect. Therefore no code repair is justified. Resume is authorized by rerunning only failed self-hosted job `101237118421` of run `33940588308`, preserving the same durable root and frozen workflow/head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`.

On resume, fail-closed checkpoint validation governs reuse. Missing, malformed or identity/hash-mismatched durable state must fail as infrastructure/BLOCKED; it must never be silently accepted. Exact terminal A/B inequality remains scientific repeatability FAIL. Only the frozen raw token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1` plus independent terminal reread can create `WW_S0_S0` authority.
