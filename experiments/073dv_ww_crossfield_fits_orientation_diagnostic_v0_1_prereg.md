# Exp073DV — WW distinct-field FITS/MCM orientation diagnostic v0.1

Status: preregistered diagnostic-only gate. Accounting `+0/+0`; no science authority may be created.

## Trigger

Exp073DU v0.1 produced a fail-closed qualifier FAIL for `WW_S0_S1`: the distinct-field workspace was demonstrably different from both auto workspaces, but the production adapter output was not bitwise equal to direct PyMaster 2.7 bandpower windows. Exp073DP had previously shown exact equivalence only for auto-field workspaces `compute_coupling_matrix(f,f,b)`.

## Purpose

Determine whether the DU mismatch is caused by:

1. FITS image orientation/layout when streaming `WSP_PRIMARY` through Astropy;
2. the downstream reconstruction arithmetic itself; or
3. another unresolved interface difference.

This diagnostic explicitly permits materializing the tiny `NSIDE=16` coupling matrix with `get_coupling_matrix()` because it is support-only and cannot be used as a production numerical route.

## Frozen geometry

- PyMaster/NaMaster 2.7;
- synthetic deterministic distinct masks identical in definition to Exp073DU;
- `NSIDE=16`, `nl=48`, spin-2 × spin-2;
- edges `[0,6,12,18,24,30,36,42,48]`;
- `ncls=4`, full shape `[4,8,4,48]`, selected semantics `EE<-EE`;
- no tolerance/rounding/smoothing/averaging rescue.

## Required comparisons

For ordered cross workspace `W01 = workspace(S0,S1)`:

- direct MCM = `w01.get_coupling_matrix()`;
- FITS image = Astropy `hdul['WSP_PRIMARY'].data` after `w01.write_to()`;
- compare FITS-as-is and FITS-transpose against direct MCM exactly;
- reconstruct windows from three canonical MCM payloads using the frozen downstream:
  - direct MCM;
  - FITS-as-is;
  - FITS-transpose;
- compare each reconstructed full window and selected `EE<-EE` against direct `w01.get_bandpower_windows()` using exact `numpy.array_equal`, SHA256 and max absolute difference for diagnostics.

## Classification

Diagnostic tokens are descriptive, not science PASS tokens:

- `DIAG_EXP073DV_FITS_AS_IS_EXACT` if FITS-as-is equals direct MCM and its downstream is exact;
- `DIAG_EXP073DV_FITS_TRANSPOSE_REQUIRED` if FITS transpose equals direct MCM and transpose downstream is exact while as-is is not;
- `DIAG_EXP073DV_DOWNSTREAM_ARITHMETIC_MISMATCH` if direct-MCM downstream itself is not exact;
- `DIAG_EXP073DV_UNRESOLVED_INTERFACE_MISMATCH` otherwise.

All classifications remain `science_gate_scored=false`, `ww_authority_created=false`, accounting `+0/+0`.

## Execution boundary

GitHub-hosted only. Exp073DT retains exclusive ownership of `DSIR-HOME-PC`; this diagnostic must not dispatch, cancel, rerun, or modify any self-hosted science job.
