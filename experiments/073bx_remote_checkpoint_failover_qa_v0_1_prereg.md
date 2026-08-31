# Exp073BX — remote checkpoint failover QA v0.1 — preregistration

**Project:** DSIR only. **Classification:** NONCLASSIFYING infrastructure/durability QA. **Accounting:** `+0/+0` for every outcome.

Frozen before the first BX run. Scientific authority state is unchanged: Exp073BJ remains Wm_S1 Track-A PASS; Exp073AQ remains permanent scientific FAIL; Exp073BD remains provisional and forbidden downstream; Exp073BW remains exact streaming-equivalence PASS.

## Purpose

Verify the requested failure-recovery architecture before a full-scale Wm_S2 successor:

1. the self-hosted `DSIR-HOME-PC` creates deterministic completed-band checkpoints;
2. after every completed band it validates canonical `<f8` bytes and SHA256 and pushes the checkpoint tree to a dedicated remote Git branch;
3. a separate GitHub-hosted runner, with no access to the home machine filesystem, restores that branch;
4. the hosted runner validates the checkpoint contract, all completed rows and their SHA256 values and reconstructs the matrix exactly;
5. progress output must include percent complete, completed/total bands, elapsed time, ETA and thread count in ordinary runner logs.

This is infrastructure QA only. It does not establish mixed-host scientific floating-point equivalence for a future Wm_S2 calculation; that property must be separately frozen if a scientific run mixes executors.

## Frozen implementation lineage

- checkpoint utility: `ci/dsir_remote_band_checkpoint_v0_1.py`, creation commit `0b0324afb69acb16cbea97bb924b9be48f303dde`;
- remote Git sync helper: `ci/dsir_checkpoint_git_sync_v0_1.sh`, creation commit `96886916b41dce7f0a40807622928c841ef5fc58`.

Dedicated branch: `checkpoints/exp073bx-v0-1`.

Synthetic QA contract: 3 bands, row length 64, canonical `<f8`; deterministic row `row[j] = band + j/1024`. The home job uses 8 as the displayed thread policy because the independent Wigner benchmark found that setting fastest among 1,2,4,6,8,10. The numerical rows themselves are intentionally trivial: this experiment tests checkpoint durability and cross-runner restoration, not Wigner science.

## Frozen outcomes

- `BX_Q1_REMOTE_CHECKPOINT_FAILOVER_PASS`: all 3 bands are remotely durable and the hosted runner restores and validates all rows and the exact final matrix SHA.
- `BX_Q2_HOME_CHECKPOINT_GENERATION_OR_PUSH_FAIL`: home job cannot create/validate/push all three checkpoints.
- `BX_Q3_HOSTED_RESTORE_OR_SHA_FAIL`: home remote push completed but hosted restore/contract/row/final SHA validation fails.
- `BX_Q4_INFRASTRUCTURE_INCOMPLETE`: no complete evidentiary basis.

No tolerance, ULP, rounding, averaging, preferred executor or rescue. Every outcome is `+0 Verified / +0 Draft-data`.
