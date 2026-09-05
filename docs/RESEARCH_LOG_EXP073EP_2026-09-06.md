# Exp073EP research log — 2026-09-06

## Result

Exp073EP (`WW` ordered cross `S0 -> S1` file-backed storage + serialized public-BPW composition qualifier) completed successfully on GitHub-hosted infrastructure.

- workflow run: `33994782890`
- job: `101383307890`
- activation head: `b1eca498cbda49efc396d1657c3cd1bdcd20b6dc`
- artifact ID: `9977735941`
- artifact digest: `sha256:4007fa89e678f4585cd73641ff26054a9c939c3f0e679581202cdf2154a39ed5`
- terminal token: `PASS_EXP073EP_FILEBACKED_CROSS_PUBLIC_BPW_COMPOSITION_EXACT_V0_1`
- classification: `COMPOSED_STORAGE_PUBLIC_BPW_EXACT`
- accounting: `+0/+0`
- `science_gate_scored=false`
- `ww_authority_created=false`

## Exact checks observed in the immutable artifact

All frozen boolean checks passed:

- distinct ordered masks `S0 != S1`;
- frozen geometry equality;
- PyMaster/NaMaster 2.7 identity;
- real regular-file mmap proof valid;
- expected mapped MCM byte size valid;
- mapped backing cleanup complete;
- all reload operations used public `NmtWorkspace.read_from -> get_bandpower_windows`;
- no tolerance rescue.

All 11 frozen exact array comparisons passed with:

- `numpy.array_equal == true`;
- canonical SHA256 equality;
- shape equality;
- `max_abs_difference == 0.0`.

This includes stock-vs-file-backed construction WSP/full-BPW/selected `EE<-EE`, stock reload A-vs-B, patched reload A-vs-B, and stock-vs-patched fresh reload comparisons.

## Interpretation

Exp073EP closes the *composition support risk* between Exp073EM file-backed MCM storage and Exp073EK serialized distinct-field public-BPW semantics. It therefore strengthens the future `WW_S0_S1` execution route after the ordered frontier is legally/scientifically advanced.

It does **not** advance the Article-3 science frontier and does not change readiness percentages. The frontier remains at `WW_S0_S0` while Exp073EN is in progress. Only a terminal Exp073EN exact A/B candidate PASS followed by the prospectively frozen Exp073EO provenance-authority admission may create `WW_S0_S0` authority and advance to `WW_S0_S1`.
