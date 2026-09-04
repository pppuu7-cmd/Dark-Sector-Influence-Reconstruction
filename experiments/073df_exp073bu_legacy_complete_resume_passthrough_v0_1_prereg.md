# Exp073DF — legacy-complete checkpoint passthrough for Exp073BU resume v0.1

Date: 2026-09-04. DSIR only. Support/infrastructure `+0/+0`; no science authority.

## Motivation
Exp073DE v0.1 proved the split frozen-science/resume-implementation binding. Before self-hosted resume, source audit found a stricter edge case: `exp073bu_wm_s3_fresh_ab_production_v0_2.py` intentionally rejects an already complete legacy v0.1 final receipt because it lacks explicit v0.2 lineage fields. In a fresh interrupted Exp073BU run, a replica that completed before runner loss can already possess a valid v0.1 receipt with workspace `reconstruction_counts={'lens':1,'source':1}`. Rewriting that historical receipt or recomputing that verified replica is forbidden.

## Prospective minimal repair
Create v0.3 lineage resume semantics that:
- accepts an already complete legacy receipt read-only only when its frozen checkpoint chain validates, its receipt `reconstruction_counts` is exactly `{lens:1, source:1}`, and the workspace checkpoint independently contains exactly the same cumulative lineage;
- returns that legacy receipt without changing any manifest or payload;
- preserves v0.2 behavior for explicit lineage receipts and for incomplete replicas;
- keeps missing/malformed/mismatched provenance fail-closed;
- never treats `{0,0}` legacy final lineage as valid cumulative provenance.

No science arithmetic, DES input, masks, 39-band edges, TE selection, adapter arithmetic, checkpoint boundaries, exact comparator or tolerances may change.

## Gate
Hosted regression/static PASS requires tests for: valid legacy `{1,1}` passthrough with no write; invalid legacy `{0,0}` rejection; explicit v0.2/v0.3 cumulative lineage acceptance; malformed/missing workspace rejection; and no tolerance/migration helper. The 8-core wrapper must remain a thin wiring layer over the exact certified omp8 adapter.

PASS token: `PASS_EXP073DF_LEGACY_COMPLETE_RESUME_PASSTHROUGH_V0_1`.
Only validated PASS may permit construction/activation of the checkpoint-preserving self-hosted resume workflow.
