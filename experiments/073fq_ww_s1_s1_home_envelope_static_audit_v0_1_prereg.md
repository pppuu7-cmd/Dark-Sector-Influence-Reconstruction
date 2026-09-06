# Exp073FQ — WW_S1_S1 fail-closed home-envelope static audit v0.1

Date: 2026-09-06. Scope: DSIR only.

Purpose: hosted-only final launch-qualification gate for Exp073FM. No self-hosted science and no WW authority may be created here.

Frozen inputs are the already Exp073FP-audited Exp073FM v0.1/v0.2 drivers plus `ci/exp073fm_verify_and_prune_replica_v0_1.py`, `ci/exp073fm_compare_terminal_receipts_v0_1.py`, and `ci/exp073fm_home_filebacked_fullres_v0_1.sh`.

PASS requires: exact committed blob identities; shell/Python syntax; dedicated Exp073FM A/B checkpoints; live fail-closed no-competing-self-hosted guard inherited from the canonical FA envelope; exact 8-CPU affinity and nested BLAS/OpenMP pins; >=50 GiB WSL and Windows free-space gate; exact R1 artifact validation; frozen NaMaster head and file-backed patch; local storage exact-activation qualifier; one-at-a-time A then B replica execution; complete six-stage verification before pruning; exact MCM `19327352832` byte and `/proc/self/maps` evidence; terminal comparison from bound prune receipts without restoring replicas; exact SHA + `numpy.array_equal` + finiteness only; candidate creates no authority; no tolerance/rescue.

PASS token:
`PASS_EXP073FQ_WW_S1_S1_HOME_ENVELOPE_STATIC_AUDIT_V0_1`

Classification `SUPPORT_PLUS_0_PLUS_0`, `ww_s1_s1_authority_created=false`, `self_hosted_science_started=false`.

Only after PASS may exactly one Exp073FM home-science workflow be launched.