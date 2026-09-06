# Exp073FL — WW_S1_S1 driver-generation static audit v0.1

Prepared prospectively while Exp073FG `WW_S0_S3` home science is unresolved. Scope: DSIR only. This gate is GitHub-hosted support/static work only: it must not read partial Exp073FG numerical output, must not construct a NaMaster workspace, must not launch self-hosted science, and cannot create `WW_S1_S1` scientific authority.

## Purpose

Qualify, before any future heavy `WW_S1_S1` run, a deterministic transformation/generation path from the already frozen durable full-resolution architecture into the materially different same-field auto-pair architecture established by Exp073FH/FJ/FK.

## Frozen predecessor support

The audit must bind and cross-check:

- Exp073FH same-field architecture support PASS;
- Exp073FJ semantic-matrix `WW_S1_S1` auto-cell PASS;
- Exp073FK transformation-contract PASS;
- current durable Exp073FG source architecture only as an implementation template, never as a source of numerical results.

## Required generated-driver semantics

A proposed generated `WW_S1_S1` production driver must satisfy all of the following simultaneously and fail closed if any is absent:

1. task identity exactly `WW_S1_S1` and authoritative source indices exactly `[1,1]`;
2. authoritative S1 count map reconstructed exactly once from the frozen R1 S1 record;
3. exactly one spin-2 `NmtField` constructed from that S1 map;
4. the exact same Python field object passed to both sides of the coupling-matrix/workspace construction; equal-but-distinct second fields are forbidden;
5. provenance receipt records `same_field_object_handoff=true`, one source identity, and no second source reconstruction/import;
6. dedicated `exp073fl`/future-S1S1 support namespace and dedicated future `ww-s1-s1` A/B checkpoint namespaces; no stale `S0`, `S2`, `S3`, `[0,3]`, `S0->S3`, or cross-pair handoff semantics may survive in the generated candidate;
7. checkpoint/resume architecture preserves complete-stage fail-closed validation and terminal/prune evidence semantics already hardened for Exp073FG;
8. frozen numerical/storage semantics remain unchanged: DES NSIDE=4096, ell `0..12287`, 39 bands, PyMaster/NaMaster 2.7 lineage, regular-file-backed unbinned MCM exactly `19,327,352,832` bytes with `/proc/self/maps` proof, serialized `read_from(..., read_unbinned_MCM=True)` followed by public `get_bandpower_windows()`, full BPW `[4,39,4,12288]`, selected `wins[0,:,0,:] = EE<-EE`, canonical `<f8 [39,12288]`, exact A/B SHA plus `numpy.array_equal`, all finite;
9. no `allclose`, `isclose`, tolerance, rounding, smoothing, averaging, manual BPW reconstruction, effective-coordinate substitution, fiducial-P shortcut, or result-dependent rescue;
10. generated code must compile and a hosted synthetic/static audit must prove same-object reuse and reject a deliberately mutated equal-but-distinct-field variant.

## Authority boundary

Exp073FL is support only. Its only permitted PASS classification is `SUPPORT_PLUS_0_PLUS_0`; `ww_s1_s1_authority_created=false`; `self_hosted_science_started=false`.

Frozen support token: `PASS_EXP073FL_WW_S1_S1_DRIVER_GENERATION_STATIC_AUDIT_V0_1`.

A PASS may authorize committing/auditing a future exact S1S1 production driver and home envelope only after the current Exp073FG home process is terminal and fully consumed. It never authorizes concurrent heavy use of `DSIR-HOME-PC` and never substitutes for a future S1S1 scientific candidate or provenance-admission gate.
