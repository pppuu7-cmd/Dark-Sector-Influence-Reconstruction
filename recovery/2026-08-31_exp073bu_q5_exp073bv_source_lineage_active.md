# DSIR recovery — Exp073BU Q5 terminal; Exp073BV exact source-lineage active

**Date:** 2026-08-31  
**Scope:** DSIR only.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

## Preserved authority and firewalls

- Exp073BJ run `33379013167` remains terminal Track-A exact authority PASS; final authority artifact `9758841785` remains authoritative.
- Exp073AQ remains the permanent hosted exact-repeatability scientific FAIL.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and cannot be preferred or used downstream.
- All source-linkage/source-lineage diagnostics here are nonclassifying `+0/+0`.
- Required G7 order and all frozen Article-3 support boundaries remain unchanged. No G8 jump.

## Exp073BU terminal exact outcome

Hosted run: `33420089328`  
Job: `99580060141`  
Artifact: `9768579019`  
Artifact digest: `sha256:4f181aef054b8447503a94459d66f70fa0b2f9c75bee16572118a5426597f9dc`  
Head: `557881b008aded44cb3895650c575ea289c47dce`

Immutable receipt:

`data/derived/g7/exp073bu_wigner_linkage_yaml_successor_result_v0_1.json`

Frozen terminal label:

`BU_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`

Exact evidence recorded by the immutable receipt:

- `pymaster_version = 2.7`;
- installed-text search completed (`ok=true`, return code `0`) and returned no `drc3jj` text hit within the frozen conda prefix search scope;
- import of `pymaster._nmtlib` failed with `ModuleNotFoundError("No module named 'pymaster._nmtlib'")`;
- because the extension import/path was unresolved, the frozen BR/BU scheme correctly remains Q5 rather than inferring Q4.

No Q1–Q4 source-linkage claim is extracted from BU post hoc.

## New upstream source observation made after BU and before BV execution

Official `LSSTDESC/NaMaster` tag `v2.7` resolves to immutable commit:

`24365fa59a38c15732f4f37e8b29265b75c442d5`.

At that exact source snapshot:

- `pymaster/field.py` imports `from pymaster import nmtlib as lib`;
- `pymaster/nmtlib.py` imports the low-level extension as top-level `import _nmtlib`;
- `setup.py` builds `Extension("_nmtlib", ...)` and links `./_deps/lib/libnmt.a`;
- `Makefile.am` includes `src/utils.c` in `libnmt_la_SOURCES`;
- `src/utils.c` defines `int drc3jj(...)`.

This provides a prospective hypothesis explaining BU's incorrect extension-path assumption, but it is not retroactively used to change BU Q5.

## Exp073BV active

Purpose: prospectively bind the hosted-successful Exp073BJ conda-forge NaMaster-2.7 runtime layout to the exact official v2.7 source topology and identify the precise implementation source for a later separately preregistered numerical-equivalence QA.

Preregistration:

- `experiments/073bv_article3_namaster27_exact_source_lineage_v0_1_prereg.md`
- commit `d71f8715c9b680c2cf80226853366b9803853a7e`

Frozen diagnostic implementation:

- `ci/exp073bv_namaster27_exact_source_lineage_v0_1.py`
- commit `89b0790ff82610da6635dd91731dd185d5e74ffd`

Workflow:

- `.github/workflows/exp073bv-article3-namaster27-exact-source-lineage-v0-1.yml`
- creation commit `a36450aef353f6a21a28b79797ae198e3822af76`

Trigger/head:

- `experiments/073bv_hosted_trigger_v0_1.md`
- commit `6010f094782a277017cbf0bb2a9af63331bb3282`

Hosted run:

- run `33420824723`
- job `99582473539`

At this checkpoint, setup, DSIR full-history checkout, and prospective-freeze enforcement had passed. The job had entered checkout of exact upstream NaMaster commit `24365fa59a38c15732f4f37e8b29265b75c442d5`.

Do not start a duplicate BV run while `33420824723` is active.

## Frozen BV terminal labels

- `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`
- `BV_Q2_SOURCE_TOPOLOGY_CONFIRMED_WRAPPER_BYTES_DIFFER`
- `BV_Q3_RUNTIME_LAYOUT_INCOMPLETE`
- `BV_Q4_UPSTREAM_TOPOLOGY_MISMATCH`
- `BV_Q5_DIAGNOSTIC_INCOMPLETE`

Every outcome is nonclassifying source-lineage/provenance evidence with `+0/+0`.

## Exact next action

Consume terminal BV run `33420824723`, job `99582473539`, and its immutable artifact. Apply exactly one preregistered BV Q1–Q5 label. If and only if Q1 establishes exact source lineage, the next permissible step is a separately prospectively preregistered **numerical-equivalence QA** for the identified `drc3jj` implementation / proposed low-memory or streaming use. Source lineage alone cannot authorize Wm_S2, WW, Layer A/B, covariance/whitening, G7, or G8.
