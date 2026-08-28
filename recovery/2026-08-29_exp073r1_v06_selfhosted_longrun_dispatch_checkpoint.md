# DSIR checkpoint — Exp073R1 v0.6 long-run execution recovery

Date: 2026-08-29 (Europe/Helsinki, EEST)

## Scientific state

Exp073R1 remains **reproduction/infrastructure INCOMPLETE**, not scientific FAIL. The authoritative v0.5 workflow run `33175886694` had a successfully completed Stage-A `source-index` job, while its Stage-B `metacal-map` job was cancelled at the GitHub-hosted 360-minute boundary after reaching `54,525,952 / 136,930,995` metacal rows. No frozen acceptance criterion is changed here.

The completed Stage-A product is therefore reusable only as the immutable artifact explicitly frozen by the v0.6 preregistration. The cancelled Stage-B output is not a scientific result and is not reusable as a partial mask.

## Frozen v0.6 protocol authority

Preregistration commit: `7e801ce0352faf3a5b8ac232a0cd6e965d22762a`.

Canonical preregistration file: `experiments/073r1_v0_6_selfhosted_longrun_stageb_prereg.md`.

The preregistration explicitly requires **Do not repeat Stage A**. Reuse only:

- v0.5 workflow run `33175886694`;
- workflow head SHA `2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c`;
- Stage-A artifact ID `9688707039`;
- artifact name `exp073r1-v05-source-index-2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c`;
- artifact ZIP digest `sha256:366aad6468046e6964edc9cd2bfd299960d5dadf1856a30ec608e9ae191c1582`;
- source-index bytes `273861990`;
- source-index SHA256 `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`;
- source whole-object SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`.

## 2026-08-29 protocol audit and correction

A protocol audit found that the first v0.6 execution workflow revisions accidentally rebuilt Stage A before the self-hosted Stage B. That contradicted the already-frozen v0.6 preregistration even though the scientific mapper itself was unchanged.

Those attempts are therefore **non-authoritative** and were cancelled before they may be used as R1 authority:

- run `33212040452`: cancelled;
- run `33212050260`: superseded/non-authoritative;
- run `33212522053`: cancelled.

The actions-write cancellation workflow run `33212981098` completed successfully.

The v0.6 workflow was then corrected so that it contains only the self-hosted `metacal-map` job and downloads/binds the exact immutable v0.5 Stage-A artifact. The corrected workflow execution is:

- **current authority candidate:** run `33213021914`;
- workflow head SHA: `399031473baa6af163f59bbdeea7b1f9c104006b`;
- workflow path: `.github/workflows/exp073r1-desy1-selfhosted-longrun-v0-6.yml`;
- current state at this checkpoint: `queued` on `[self-hosted, Linux, X64]`;
- jobs: exactly one `metacal-map` job; no Stage-A recomputation job.

Do not promote any earlier v0.6 run to authority. Do not merge artifacts across attempts. Only a terminal result from the corrected authority candidate (or a later explicitly superseding prereg-compliant execution of the same frozen workflow semantics) may satisfy Exp073R1.

## Exact execution contract preserved

The corrected workflow deliberately reuses `ci/exp073r1_sequential_wholestream_v0_5.py` unchanged and preserves the exact frozen v0.5/v0.6 identity and science assertions:

- metacal whole-object SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- exact metacal bytes `84075649920`;
- exact source and metacal row count `136930995`;
- one ordinary whole-object GET, identity encoding, no HTTP Range semantics;
- immutable Exp073R0 run `33103083736`, head SHA `94b05d307295d5e9263646983ece9514f9fa2e88`;
- selection `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- HEALPix mapper `nside=4096`, `RING`, celestial `C`, `lonlat=True`;
- final internal status must be exactly `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`;
- zero out-of-range pixels;
- all four tomographic bins non-empty;
- independent repeatability checks true for every bin;
- all parent R0 checks true;
- `science_gate_scored=false`, `f_invalid_computed=false`;
- `covariance_read=false`, `G8_read=false`;
- `gate_state={G7: OPEN, G8: OPEN, G9: OPEN}`.

An Actions job marked `success` without the frozen internal PASS contract is insufficient.

## Gate order remains frozen

`validated physical forward/power-input bridges -> genuine Exp073R1 PASS -> preregistered Exp073P physical support-validity mask -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.

Until genuine R1 PASS:

- Exp073P real physical support: **BLOCKED**;
- covariance/whitening: **BLOCKED**;
- nuisance quotient/relation/null tests: **BLOCKED**;
- G7: **OPEN**;
- G8: **OPEN**;
- G9: **OPEN**.

## Recovery instruction

On a future chat/session, first inspect run `33213021914`. If it is still queued, do not modify science semantics merely to make it run faster. If it completed, verify the internal JSON PASS contract and artifact hashes before authorizing Exp073P. If it was interrupted, classify it only as infrastructure `INCOMPLETE_EXP073R1`; do not call that a scientific FAIL and do not use partial masks.