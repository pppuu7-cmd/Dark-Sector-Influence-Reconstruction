# DSIR recovery — Exp073FE restore hardening preregistered while Exp073FA runs

Date: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Preserved authority

All prior admitted authority remains unchanged. `WW_S0_S0` and `WW_S0_S1` remain admitted. `WW_S0_S2` is not yet admitted.

## Live authoritative science process

Exp073FD/Exp073FA run `34020756634`, home job `101452805620`, head `894885b2c2b811954d1724c2733d2a810a486d70`, remains the sole self-hosted DSIR owner and is still in the frozen S0-to-S2 A/B step. Checkpoint namespaces remain `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `checkpoints/exp073fa-ww-s0-s2-b-v0-1`. Partial numerical output was not inspected; durable stage remains `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`.

## Prospectively discovered checkpoint/restore implementation issue

While the science run remained in progress, a result-independent static audit compared the frozen Exp073FA preregistration with the committed driver and home wrapper. The preregistration requires that every complete stage restored from checkpoint be restored only after exact identity and payload verification.

The home wrapper currently executes replica A, prunes superseded large payloads after `replica_receipt_complete`, executes replica B, prunes likewise, then invokes the driver again with `--replica AB`. In the v0.1 driver, `validated_finished()` recognizes a terminal replica by validating the terminal receipt and selected EE payload only; it does not revalidate the full six-stage chain and all prior stage payloads before returning the completed replica. Thus the final AB invocation uses a terminal-restore shortcut that is not strong enough to satisfy the frozen checkpoint restore wording.

This finding was made before terminal numerical output was inspected and therefore cannot be result-dependent. It does not change `(S0,S2)`, `[0,2]`, source head, contract fingerprint, NSIDE/ell/bands, NaMaster arithmetic, BPW route, `EE<-EE`, exact thresholds, or scientific acceptance.

## Exp073FE prospective support repair

Preregistered `experiments/073fe_exp073fa_terminal_compare_checkpoint_restore_hardening_v0_1_prereg.md`, Git blob `43ff6dfe8d1eb682202b142e6ed2408a4beb00f7`.

Added `ci/exp073fe_compare_exp073fa_terminal_receipts_v0_1.py`, Git blob `14841dc412d3989e6f86294072479424f26cec93`. The comparator consumes only terminal A/B receipts and selected EE payloads; it never calls `run_replica()` and never restores a completed replica merely to compare A and B. It fail-closes source/contract/pair/namespaces/public-route/no-cross-read/no-historical-import identities, selected payload SHA and exact `<f8 [39,12288]` size, exact SHA equality, `numpy.array_equal`, and finiteness; no tolerance rescue exists.

Hosted static audit Exp073FE run `34023253707`, job `101459598645`, was launched while Exp073FA remained running. This support audit is hosted-only and does not compete for `DSIR-HOME-PC`. Its frozen support token is `PASS_EXP073FE_EXP073FA_TERMINAL_COMPARE_RESTORE_HARDENING_V0_1`; it can never create WW authority.

## Terminal handling rule now frozen prospectively

The running Exp073FA result must still be consumed exactly. Workflow SUCCESS or its candidate token alone is not authority. If the artifact shows exact A/B mismatch, that remains scientific FAIL. If arrays match but the frozen checkpoint/provenance contract cannot be proven, classification is provenance/infrastructure `+0/+0`; preserve valid completed evidence and apply the smallest prospective repair without weakening science or unnecessarily recomputing verified expensive stages.

A later authority-writing provenance admission must explicitly inspect the raw artifact's complete ordered six-stage manifests and the exact terminal A/B evidence before `WW_S0_S2` authority can exist.