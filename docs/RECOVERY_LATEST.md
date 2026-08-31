# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-08-31  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable hosted artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical-QA work gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-08-31_exp073bu_q5_exp073bv_source_lineage_active.md`
2. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
3. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
4. `experiments/073bv_article3_namaster27_exact_source_lineage_v0_1_prereg.md`
5. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Scientific authority state

**Exp073BJ remains terminal Track-A exact authority PASS.** Hosted run `33379013167`; final authority artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`. Exact final A/B equality remains frozen and authoritative.

Exp073AQ remains the permanent historical hosted exact-repeatability scientific FAIL. Exp073BA remains infrastructure/execution incomplete. Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`. Exp073BI remains execution-feasibility QA only.

## Source-linkage / source-lineage state

### Exp073BU terminal Q5

Run `33420089328`, job `99580060141`, artifact `9768579019`, digest `sha256:4f181aef054b8447503a94459d66f70fa0b2f9c75bee16572118a5426597f9dc`, head `557881b008aded44cb3895650c575ea289c47dce`.

Immutable frozen outcome: `BU_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE`.

Receipt evidence:

- `pymaster_version=2.7`;
- bounded installed-text search completed and found no `drc3jj` reference inside the frozen installed conda-prefix text scope;
- `pymaster._nmtlib` import failed because that module path does not exist;
- therefore the preregistered BR/BU scheme correctly remains Q5 rather than inferring Q4.

### Official NaMaster v2.7 source topology established prospectively after BU

Official `LSSTDESC/NaMaster` tag `v2.7` resolves to immutable commit `24365fa59a38c15732f4f37e8b29265b75c442d5`.

At that exact snapshot, source inspection shows:

- `pymaster/field.py`: `from pymaster import nmtlib as lib`;
- `pymaster/nmtlib.py`: top-level `import _nmtlib`;
- `setup.py`: builds `Extension("_nmtlib", ...)` and links `./_deps/lib/libnmt.a`;
- `Makefile.am`: includes `src/utils.c` in `libnmt_la_SOURCES`;
- `src/utils.c`: defines `int drc3jj(...)`.

This explains the BU path mismatch but does not retroactively change BU Q5.

### Exp073BV active

Purpose: bind the hosted-successful BJ conda-forge NaMaster-2.7 runtime layout to exact official v2.7 source topology before any extracted/streaming numerical-equivalence QA.

Frozen provenance:

- preregistration commit `d71f8715c9b680c2cf80226853366b9803853a7e`;
- diagnostic implementation commit `89b0790ff82610da6635dd91731dd185d5e74ffd`;
- workflow creation commit `a36450aef353f6a21a28b79797ae198e3822af76`;
- trigger/head commit `6010f094782a277017cbf0bb2a9af63331bb3282`;
- hosted run `33420824723`, job `99582473539`.

At the latest checkpoint BV had passed hosted setup, DSIR full-history checkout and prospective-freeze enforcement and was checking out exact upstream NaMaster commit `24365fa59a38c15732f4f37e8b29265b75c442d5`. **Do not start a duplicate BV run while `33420824723` is active.**

Frozen labels: `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`, `BV_Q2_SOURCE_TOPOLOGY_CONFIRMED_WRAPPER_BYTES_DIFFER`, `BV_Q3_RUNTIME_LAYOUT_INCOMPLETE`, `BV_Q4_UPSTREAM_TOPOLOGY_MISMATCH`, `BV_Q5_DIAGNOSTIC_INCOMPLETE`. Every BV outcome is nonclassifying provenance/source-lineage evidence and `+0/+0`.

## Frozen Article-3 boundaries and G7 order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order remains: `validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`. No G8 jump.

## Exact next gate

Consume terminal Exp073BV run `33420824723`, job `99582473539`, logs and immutable artifact. Apply exactly one frozen BV Q1–Q5 label. If and only if Q1 confirms exact source lineage, prospectively preregister a separate numerical-equivalence QA for the identified `drc3jj` implementation before any low-memory/streaming Wm_S2 Track-A successor is allowed.

- ✅ Exp073BJ exact Track-A authority PASS preserved.
- ✅ Exp073BU terminalized exactly as Q5; no retroactive rescue.
- 🟡 Exp073BV exact source-lineage diagnostic active, `+0/+0`.
- ❌ Exp073AQ permanent historical scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Verified: 52.0% | Draft/data: 53.7%**
