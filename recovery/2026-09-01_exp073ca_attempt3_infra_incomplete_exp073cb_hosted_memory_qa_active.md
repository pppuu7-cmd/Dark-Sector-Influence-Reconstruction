# 2026-09-01 — Exp073CA attempt3 infrastructure incomplete; Exp073CB hosted memory-lifetime QA active

## Authority state

- Exp073BJ remains terminal Track-A exact Wm_S1 authority PASS.
- Exp073AQ remains permanent historical exact-repeatability scientific FAIL.
- Exp073BD remains provisional/incomplete and forbidden downstream.
- Exp073BV exact source-lineage PASS, Exp073BW exact streaming-equivalence PASS, and Exp073BZ checkpoint/failover PASS remain preserved.
- Article-3 readiness remains Verified 52.0% | Draft/data 53.7%.

## Exp073CA attempt3

Run `33448843621` remains queued only because self-hosted replica B job `99673921530` is queued. Replica A job `99673921219` is terminal failure during fresh Wm_S2 PCL; compile, checkpoint preflight/restore, heavy 39-band streaming, compact comparator and finalizer never ran. Frozen classification remains:

`INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`

This is +0/+0 and not a scientific mismatch. Overnight home-runner hard lock remains in force; queued replica B must not be revived or caused to run.

## Memory-structure finding motivating hosted QA

At DES NSIDE=4096, NPIX=201,326,592, one float64 real-space map occupies 1.500 GiB. A mask alm through ell=12287 contains 75,503,616 complex128 values, about 1.12509 GiB. The current Exp073AZ Wm PCL path constructs both input maps and both NmtField objects before obtaining both mask alms. NaMaster 2.7 stores a float64-converted mask in each field, so the deterministic persistent residency of maps/field-owned copies plus two alms is already about 8.25 GiB before SHT workspace and process overhead. Therefore a 6 GiB WSL cap is structurally unsafe for the simultaneous-lifetime PCL path.

A lifetime-only sequential construction can release the first real-space map/field before creating the second field while preserving the same transforms and hp.alm2cl call. This is an infrastructure hypothesis only until exact byte-equivalence is demonstrated.

## Exp073CB prospectively frozen hosted-only QA

Purpose: exact simultaneous-vs-sequential PCL equivalence plus independent-process peak RSS on synthetic HEALPix masks. It is NONCLASSIFYING and cannot close any real-survey/scientific gate.

Frozen lineage:
- prereg commit `5b63330f5273fc9186bc9921f5d4702aaecb7c3a`;
- helper commit `c6d792f7b57fa38ca9017e6335046919bb33d94f`;
- workflow commit `7deadbeeafac479a059708efbfaa69e70f356470`;
- binding commit `1bb95adc8205aa74c78b91c46a5765f811effbaa`;
- trigger/head `07242a550fc856a6bd4621ba887866d735b96334`.

Hosted run `33464547851`, job `99721585397`, ubuntu-24.04 only. At last inspection checkout and prospective freeze/binding passed; environment installation was in progress. Frozen cases nside 64/128/256, one thread. Exact comparator requires np.array_equal plus canonical contiguous little-endian <f8 SHA-256 equality for every case. No tolerance/ULP/rounding/averaging/smoothing/majority/preferred-replica rescue. `/usr/bin/time -v` records Maximum resident set size separately for each mode. RSS is diagnostic only.

Frozen branches:
- `CB_Q1_EXACT_EQUIVALENCE_PASS` if every complete case is exact array+SHA equal;
- `CB_Q2_COMPLETE_EXACT_MISMATCH_FAIL` if complete valid comparator inputs differ exactly;
- `CB_Q3_INFRASTRUCTURE_INCOMPLETE` if complete valid comparator inputs do not exist for all frozen cases.

Every branch is +0/+0. Only CB_Q1 may justify prospective design of a memory-lifetime-only Exp073CA infrastructure successor after the home runner is explicitly re-enabled.

## Exact next gate

Monitor Exp073CB to terminal and preserve exactly one frozen CB_Q1/Q2/Q3 classification plus immutable artifact provenance. Do not touch Exp073CA queued replica B overnight. No G7/G8 advance.
