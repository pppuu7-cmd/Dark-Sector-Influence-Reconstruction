# Exp073Q2 — transport-resilient first-table FITS schema retry v0.2

Date: 2026-08-27
Parent: Exp073Q / Exp073P
Science gates before this retry: G7 OPEN, G8 OPEN, G9 OPEN.

## Why Q1 did not score the schema

Exp073Q run 33084029912 stopped with `TimeoutError: The read operation timed out` while opening a small HTTP Range request to the exact 84,075,649,920-byte Metacalibration object. This is a transport/infrastructure failure, not evidence of schema or row-alignment failure. The Q1 JSON label `FAIL_EXP073Q_SCHEMA_OR_ROW_ALIGNMENT` was therefore overly broad and MUST NOT be interpreted as a physical or schema FAIL.

Q2 splits outcome classes:

- `SCHEMA_ROW_LAYOUT_PASS_EXP073Q2` — preregistered schema/row-layout checks pass;
- `FAIL_EXP073Q2_SCHEMA_OR_ROW_ALIGNMENT` — a deterministic FITS/schema/row-count invariant fails after bytes have been obtained;
- `INCOMPLETE_EXP073Q2_TRANSPORT` — network/range transport prevents evaluation.

Only the first two evaluate the schema. Transport incomplete leaves every science gate OPEN.

## Frozen coordinate provenance

The pinned Cosmotheka test configuration
`cosmotheka/tests/data/desy1_ebossqso_p18cmbk.yml`
at `Cosmotheka/Cosmotheka@7bde066626f66cd7bbe79cc46224d2342840e463`
contains the same DES Y1 weak-lensing and redMaGiC mapper inputs and freezes

- `sphere.nside: 4096`
- `sphere.coords: 'C'`.

Both `MapperDESY1wl` and `MapperDESY1gc` use `_get_rotator('C')`, so for this pinned configuration the DES coordinate rotation is the identity. The coordinate-provenance blocker identified in Q1 is therefore CLOSED.

## First-table rule

Both pinned DES mapper paths use Astropy table/file reads without selecting an alternate table extension for the catalogue. Q2 consequently audits the first reachable FITS `BINTABLE` following the primary HDU and requires the mapper-needed columns there. It does not scan past a massive table payload looking for a second candidate.

## Transport strategy

For each exact byte-bound P2 URL, Q2 requests a single small prefix (default 8 MiB) with `Range: bytes=0-N`, retries transient failures, and accepts either:

1. HTTP 206 with a valid `Content-Range` whose total equals the P2 exact object size; or
2. HTTP 200 with `Content-Length` equal to the P2 exact object size, while reading only the frozen prefix and closing the connection.

No full-object redownload is performed by Q2.

## FITS row-offset correction

Q1 incorrectly treated `P`/`Q` variable-length FITS columns as having unknown row width. In a FITS binary-table row, however, the P/Q descriptors themselves occupy fixed row storage (8/16 bytes per descriptor); only the pointed-to heap payload is variable length. Q2 therefore computes positional offsets across P/Q descriptors correctly while still rejecting a required geometry field if that field itself is a P/Q variable-length payload.

## Frozen checks

Source-bin first BINTABLE must contain:

- `zbin_mcal`
- `zbin_mcal_1p`
- `zbin_mcal_1m`
- `zbin_mcal_2p`
- `zbin_mcal_2m`

Metacalibration first BINTABLE must contain:

- `ra`
- `dec`
- `flags_select`

Q2 records `NAXIS1`, `NAXIS2`, `TFIELDS`, `TTYPE/TFORM`, row storage offsets, and requires equal `NAXIS2` between the two exact files.

A PASS changes no science-gate state. It only permits Exp073R one-pass mask construction.
