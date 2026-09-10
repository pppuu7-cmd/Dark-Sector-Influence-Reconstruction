# Exp073JE infrastructure repair v0.2 — parser argument capacity

Date frozen: 2026-09-10. Scope: DSIR Article 3 / C2 only.

Status: PROSPECTIVELY FROZEN AFTER terminal infrastructure failure of Exp073JE run `34474514433 / 102861967751` and before repaired-run numerical output.

## First causal failure
The original JE run completed frozen lineage, dependency installation and pinned CLASS-IV build, then aborted at the first diagnostic execution with `malloc(): corrupted top size` / exit 134 before producing an artifact. This is an infrastructure/software failure, not a scientific result.

The JE design enlarged `_MAX_NUMBER_OF_K_FILES_` from 30 to 512 but left CLASS-IV parser `FileArg` / `_ARGUMENT_LENGTH_MAX_` at 1024 bytes. JE supplies 64, 128 and 256 float64 physical-k nodes as one comma-separated `k_output_values` argument. The 256-node serialization is longer than the original 1024-byte parser argument capacity, so increasing only the destination k-array capacity is not a sufficient safe infrastructure change.

## Frozen minimal repair
Retain the original JE science contract and exact node grids unchanged. In addition to the already preregistered one-line perturbation capacity patch `30 -> 512`, apply exactly one parser-capacity replacement in pinned CLASS-IV `include/parser.h`:

`#define _ARGUMENT_LENGTH_MAX_ 1024` -> `#define _ARGUMENT_LENGTH_MAX_ 32768`.

This changes only input-string storage capacity. It MUST NOT alter equations, transfer/source definitions, cosmological parameters, physical k nodes, interpolation rule, finite-difference operator, `h=1e-4`, `REL_TOL=1e-3`, acceptance logic, public gauge-invariant `d_m`, or any DSIR scientific boundary.

Before build/execution, fail closed unless each source replacement count is exactly one and the pre/post SHA256 values are recorded. Add a static regression check that the exact JE serialization of every frozen shared grid N in `{64,128,256}` fits strictly inside 32768 bytes and that the N=256 serialization exceeds 1023 bytes, confirming the original capacity defect is exercised by the test rather than guessed away.

## Provenance correction binding
The repaired JE run must bind to corrected Exp073JD provenance authority `EXP073JD_ARTICLE3_LAYERB_EXACT_K_INJECTION_ORIGINAL_PAIR_AUTHORITY_V0_2`, while preserving the same validated JD numerical observations and raw token. No JD science is changed by this provenance correction.

## Classification
A repaired JE numerical outcome remains support-only `+0/+0` under the original preregistration. Any further malformed-memory/parser/build/interface failure is `INVALID_INFRA_PLUS_0_PLUS_0`; it cannot be interpreted as scientific PASS/FAIL.
