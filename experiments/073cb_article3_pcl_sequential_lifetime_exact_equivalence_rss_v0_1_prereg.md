# Exp073CB — Article-3 PCL sequential-lifetime exact-equivalence + RSS QA v0.1 preregistration

Status: PROSPECTIVELY FROZEN BEFORE EXECUTION.

Purpose: NONCLASSIFYING hosted-only infrastructure QA. Test whether changing only the lifetime/order of Python/NmtField objects during mask-PCL construction can reduce peak RSS while preserving the exact PCL bytes. This experiment does not use real-survey Exp073CA Wm_S2 outputs, cannot close any scientific gate, and scores +0 Verified / +0 Draft-data.

Authority preserved: Exp073BJ Track-A exact Wm_S1 PASS; Exp073AQ permanent historical scientific FAIL; Exp073BD forbidden downstream; BV/BW/BZ unchanged. Exp073CA attempt3 remains infrastructure incomplete and its queued self-hosted replica is not touched.

Frozen test geometry and inputs:
- GitHub-hosted ubuntu-24.04 only; no self-hosted labels.
- NaMaster/pymaster 2.7.x; Python 3.11.
- deterministic synthetic HEALPix masks generated analytically, no RNG.
- nside in {64,128,256}; lmax=3*nside-1.
- spin pair matches Wm mask-PCL usage: first field spin=0, second field spin=2.
- simultaneous implementation mirrors current Exp073AZ object lifetime: create a,b,fa,fb then aa,ab then hp.alm2cl.
- sequential implementation changes only lifetime: create a,fa; release a after field construction; obtain aa; release fa; then create b,fb; release b; obtain ab; release fb; then identical hp.alm2cl(aa,ab,lmax).

Frozen exact comparator for every nside:
1. output shapes identical and finite;
2. np.array_equal(simultaneous,sequential) is true;
3. canonical contiguous little-endian <f8 SHA-256 is identical.
No tolerance, ULP, rounding, smoothing, averaging, majority vote or preferred-run rescue is permitted.

RSS measurement:
- run each implementation in a separate process under `/usr/bin/time -v` so Maximum resident set size is not contaminated by prior mode execution;
- report max RSS in KiB and ratio sequential/simultaneous for each nside;
- RSS is diagnostic only and cannot override exact comparator classification.

Frozen branches:
- CB_Q1_EXACT_EQUIVALENCE_PASS: all frozen cases satisfy exact array and SHA equality. RSS may increase or decrease; classification remains exact-equivalence PASS.
- CB_Q2_COMPLETE_EXACT_MISMATCH_FAIL: both valid outputs exist for any frozen case and exact array/SHA differs. Preserve mismatch; no rescue/tuning.
- CB_Q3_INFRASTRUCTURE_INCOMPLETE: setup/execution fails before a complete pair of valid comparator inputs exists for all frozen cases. No scientific classification.

All CB outcomes are NONCLASSIFYING +0/+0. Only CB_Q1 may justify prospectively designing a future memory-lifetime-only Exp073CA infrastructure successor; it cannot authorize Wm_S2/WW authority, Layer A/B, G7 or G8.
