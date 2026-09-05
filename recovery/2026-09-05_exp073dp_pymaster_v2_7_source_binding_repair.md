# DSIR immutable recovery — Exp073DP PyMaster v2.7 source-binding repair

Date: 2026-09-05. Scope: DSIR only.

Preserve all admitted Wm authority and the closed Exp073DL/DM/DN/DO support results. No scientific arithmetic or WW acceptance criterion is changed by this note.

## Exp073DP attempt 1 — infrastructure/dependency FAIL `+0/+0`

The prospectively frozen hosted small-NSIDE exact-equivalence workflow was activated at head `b1b7ed2246f6e44153fe99d9807349911871cb30`.

Run/job `33938315128 / 101230515264` ended FAILURE before the downstream compile and before any stock-vs-adapter numerical comparator ran. Native apt dependencies succeeded. The first causal failure in decoded logs was the command requesting `pymaster==2.7.0` from PyPI: pip reported `Could not find a version that satisfies the requirement pymaster==2.7.0` and listed releases through 2.6 followed by 3.0. Therefore this is an infrastructure/dependency-source error `+0/+0`, not a WW implementation equivalence failure and not a scientific result. No Exp073DP artifact/comparator was produced.

## Prospective smallest repair

Repository/external source verification establishes that the required NaMaster/PyMaster lineage is the official LSSTDESC/NaMaster source tag `v2.7`, whose advertised commit prefix is `24365fa`. The repair changes only dependency provenance in the workflow; `experiments/073dp_ww_exact_adapter_smallnside_equivalence_v0_1_prereg.md` and `ci/exp073dp_ww_exact_adapter_smallnside_equivalence_v0_1.py` remain unchanged.

Repair commit/head: `b2dc8a395991963885d47a964d44c50c3ef2927e`.

The repaired workflow now:
1. installs only general Python dependencies from PyPI;
2. shallow-clones official `https://github.com/LSSTDESC/NaMaster.git` at exact tag `v2.7`;
3. requires `git describe --tags --exact-match == v2.7`;
4. records the source commit and fail-closes unless its first seven hex characters equal `24365fa`;
5. installs PyMaster from that source tree;
6. fail-closes unless installed package metadata is `2.7` or `2.7.*`;
7. preserves the exact same three synthetic cases, stock PyMaster reference, 8-worker deterministic downstream, full/selected SHA equality, `numpy.array_equal`, and zero max-absolute-difference comparator.

No fallback to PyMaster 2.6 or 3.0 is authorized.

## Current process

Repaired Exp073DP run/job `33938446310 / 101230897808` is `IN_PROGRESS` at latest reconciliation. It is GitHub-hosted only; checkpoint namespace `N/A`; no full-resolution DES data are read; no WW scientific authority can be created by this gate. `DSIR-HOME-PC` remains FREE.

Expected token remains `PASS_EXP073DP_WW_EXACT_ADAPTER_SMALLNSIDE_EQUIVALENCE_V0_1`.

On SUCCESS: inspect raw artifact/digest and source-provenance receipt before classifying support PASS. Only a validated exact PASS permits prospective implementation/audit of the full-resolution durable A/B `WW_S0_S0` driver. On FAIL: diagnose the first new infrastructure/implementation cause; do not weaken arithmetic or switch lineage.
