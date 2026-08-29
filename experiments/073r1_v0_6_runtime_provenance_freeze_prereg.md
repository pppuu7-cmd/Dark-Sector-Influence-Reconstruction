# Exp073R1 v0.6 runtime-provenance freeze preregistration

Date: 2026-08-29
Scope: reproducibility hardening only. This document does **not** alter any frozen Exp073R1 scientific acceptance criterion, mapper logic, source/metacal identity, transport contract, selection, HEALPix mapping, parent lineage, or G7 ordering.

## Motivation

The authoritative Exp073R1 v0.6 Stage-B workflow creates an isolated venv but currently installs `numpy` and `healpy` without explicit version pins. The running job prints the resolved versions, so its scientific computation is still auditable, but future reruns must not silently drift to a different numerical runtime.

## Frozen post-run provenance contract

After the current authoritative run reaches a terminal state, record from the job log (or an equivalent immutable execution record):

- Python implementation and exact version;
- `numpy.__version__`;
- `healpy.__version__`;
- pip version;
- runner OS/architecture metadata sufficient to identify Linux/X64 execution;
- authoritative workflow run id and head SHA;
- evaluator Git blob SHA1 `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- source and metacal frozen SHA256 identities already specified by Exp073R1;
- whether the run reached `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.

No package version may be inferred from a later install. Only the versions actually resolved inside the authoritative run are admissible.

## Future-rerun rule

Any future Exp073R1 rerun intended to reproduce or supersede the current authoritative result must use an environment pinned to the recorded Python/numpy/healpy versions, or else be explicitly labelled a runtime-variation replication and kept distinct from exact reproduction authority.

A runtime mismatch is a **reproducibility/infrastructure deviation**, not by itself a scientific FAIL. A scientific FAIL may only arise from the frozen scientific evaluator after all preregistered input and execution contracts are satisfied.

## Gate-order firewall

This provenance freeze does not authorize any downstream quantity. Until genuine Exp073R1 PASS exists, the following remain forbidden: physical support-validity scoring, `f_invalid`, covariance restriction/whitening, nuisance tangent SVD/rank, quotient/relation/null control, and fresh G8 withheld-family evaluation.

Frozen sequence remains:

validated physical forward/power-input bridges -> preregistered physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family.
