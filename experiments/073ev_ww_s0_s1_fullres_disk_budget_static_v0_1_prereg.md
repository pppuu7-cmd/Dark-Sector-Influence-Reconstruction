# Exp073EV — WW_S0_S1 full-resolution staged disk-budget static qualifier v0.1

Prospectively preregistered 2026-09-06 while Exp073EN remains unresolved. Hosted/static support only, accounting `+0/+0`; no science authority.

## Purpose
Verify that the Exp073EL v0.2 minimum-free-space floor of 50 GiB is quantitatively consistent with the frozen full-resolution staged storage architecture, including a conservative case where both spilled mask ALM files remain present during workspace serialization.

## Frozen exact dimensions
- NSIDE=4096; NPIX=`201,326,592`.
- lmax=12287; nl=12288.
- spin2 x spin2 => ncls=4; unbinned MCM rows=`49,152`.
- float64 unbinned MCM bytes=`49,152^2*8 = 19,327,352,832` = exactly 18 GiB.
- HEALPix mask ALM count=`(12288*12289)/2 = 75,503,616` complex values.
- one complex128 ALM bytes=`1,208,057,856`.
- two ALM spills bytes=`2,416,115,712`.
- selected EE bytes=`39*12288*8 = 3,833,856`.
- full BPW bytes=`4*39*4*12288*8 = 61,341,696`.

## Conservative peak model
During `write_to`, one 18-GiB construction mmap backing file and the serialized FITS WSP_PRIMARY of the same unbinned matrix may coexist. Treat the FITS unbinned payload conservatively as at least another full MCM and add both ALM spill files even though the preferred stage ordering can prune them after a hash-bound PCL receipt.

Conservative modeled large-payload peak:
`2*MCM_BYTES + 2*ALM_BYTES + FULL_BPW_BYTES + SELECTED_BYTES`.

FITS headers, binned MCM, permutations, bin tables, beams, PCL-mask arrays, receipts and logs are not assumed to be zero; instead the admission test requires at least 10 GiB additional margin beyond the modeled large-payload peak.

## PASS
`PASS_EXP073EV_WW_S0_S1_FULLRES_DISK_BUDGET_STATIC_V0_1` requires:
- all exact dimension identities above;
- `50 GiB = 53,687,091,200` bytes;
- 50-GiB floor minus conservative modeled large-payload peak is at least 10 GiB;
- preferred cleanup ordering can only increase the margin;
- no science gate scored.

A failure is resource-model support FAIL `+0/+0`, not a dark-sector science failure.
