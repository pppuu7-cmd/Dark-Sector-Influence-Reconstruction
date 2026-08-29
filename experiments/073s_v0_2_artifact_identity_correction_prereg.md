# Exp073S v0.2 — artifact-identity correction — preregistration

**Frozen:** 2026-08-29 after v0.1 terminated before any artifact download or reconstruction, and before any v0.2 execution output.

## Why v0.2 exists

Exp073S v0.1 run `33272451503` launched four independent bin jobs. In all four jobs the authority-freeze step passed, but the next metadata-binding step failed before `actions/download-artifact`, before NumPy installation, and before the reconstruction evaluator executed. Therefore v0.1 produced no count-mask result and is classified as infrastructure/authority-metadata INCOMPLETE, not a scientific or reconstruction FAIL.

The v0.1 preregistration had frozen stale GitHub artifact ID/digest metadata. A fresh authoritative Actions API query for R1 run `33270843577` returns exactly one non-expired artifact with the already-frozen expected name:

- artifact ID: `9720335366`;
- artifact name: `exp073r1-v08-hosted-wholestream-ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- size: `66138507` bytes;
- digest: `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- workflow run: `33270843577`;
- head: `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- expired: `false`.

The already-successful hosted prerequisite join run `33271876425` currently has its exact receipt artifact:

- ID `9720339539`;
- digest `sha256:dc63797a8bfe12a91c264eb5204182164e15d9f6441886ef79ab25f55b3040fc`;
- expired `false`.

## Frozen correction scope

v0.2 changes **only** the R1 artifact ID/digest/size binding used by the delivery preflight. It reuses the unchanged evaluator:

`ci/exp073s_desy1_source_countmask_reconstruction_v0_1.py`

git blob:

`4d22d596b39f07f0bcb3af390e99ead607c517f5`.

All scientific/representation semantics from `073s_desy1_source_countmask_reconstruction_v0_1_prereg.md` remain unchanged:

- bins `0,1,2,3` independently;
- NSIDE 4096, RING;
- exact little-endian uint32 pixel records;
- exact count semantics from multiplicities;
- binary occupancy reconstruction/hash comparison;
- sparse `(pixel,count)` fingerprint;
- no support/covariance/nuisance/G7/G8/G9 evaluation.

No count-mask output from v0.1 exists and therefore no v0.2 choice was informed by reconstruction results.

## v0.2 PASS rule

All four independent jobs must pass the unchanged evaluator under the corrected exact artifact identity. No majority vote, retry selection by scientific output, or cross-bin substitution is allowed.

Positive token remains:

`PASS_EXP073S_DESY1_SOURCE_COUNTMASK_RECONSTRUCTION_V0_1`

because the evaluator/representation semantics are unchanged; the workflow lineage is v0.2.

G7/G8/G9 remain OPEN and covariance remains unauthorized by Exp073S itself.
