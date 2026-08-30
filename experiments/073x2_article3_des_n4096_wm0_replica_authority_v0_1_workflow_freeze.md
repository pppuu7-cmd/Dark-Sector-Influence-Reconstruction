# Exp073X2 workflow freeze — exact DES nside4096 Wm0 replica authority v0.1

Date: 2026-08-30
Status: FROZEN BEFORE HOSTED OUTPUT.

This document freezes the executable prospective chain for Exp073X2 after workflow QA and before the trigger-only commit.

## Frozen chain

- preregistration: `experiments/073x2_article3_des_n4096_wm0_replica_authority_v0_1_prereg.md`
- preregistration_last_modifying_commit: `29740bea67bb02e7e8f4ae80d8e6ebc633754cf5`
- implementation: `ci/exp073x2_des_n4096_wm0_replica_authority_v0_1.py`
- implementation_last_modifying_commit: `09e9cdb5b9e50531ca3e6ecb8bdda48a520161d8`
- workflow: `.github/workflows/exp073x2-article3-des-n4096-wm0-replica-authority-v0-1.yml`
- workflow_last_modifying_commit: `c8deb4f4489f13416a613aa96711ee35207fa84f`

An earlier workflow-creation commit `9e0d410b2db3f43f553ce3b1e42a08ba62cf1bcb` contained a duplicate YAML `env` mapping in the heavy compute step. It was caught during prospective workflow audit before this freeze and before any trigger. Commit `c8deb4f4489f13416a613aa96711ee35207fa84f` removes that ambiguity without modifying the preregistered science/operator contract or implementation.

## Frozen hosted execution structure

- matrix replicas: `a`, `b`
- runner: `ubuntu-24.04`
- each replica timeout: `360` minutes
- each replica constructs exactly one frozen `NSIDE=4096` Wm source-bin-0 spin0xspin2 NaMaster workspace and immediately uploads its compact `[39,12288]` TE<-TE response array plus provenance metadata
- `fail-fast: false` so one infrastructure failure does not cancel the other replica
- aggregator depends on both replicas and performs no NaMaster workspace construction
- aggregator requires canonical hash equality, exact `numpy.array_equal`, equality of provenance-critical metadata, and the full non-classifying science firewall
- only the aggregator may emit `PASS_EXP073X2_DES_N4096_WM0_REPLICA_AUTHORITY_V0_1`

## Trigger integrity

The push-trigger path is exactly:

`ci/exp073x2_des_n4096_wm0_replica_authority_v0_1.trigger`

For a push-triggered hosted run, the workflow requires the trigger commit to modify that file and no other path. The trigger commit must not modify preregistration, implementation, workflow, or this freeze record.

## Scientific interpretation

Exp073X2 remains non-classifying angular-operator authority work. PASS does not evaluate physical support, does not close G7/G8/G9, and does not increase strict Article-3 readiness above **52%**. Infrastructure cancellation/resource failure before aggregation is INCOMPLETE, not scientific FAIL.
