# Exp073BY v0.1 — M1 exact mmap full-component equivalence

Date: 2026-09-04
Scope: DSIR only.

## Authority
- prereg commit: `f51c738e4074b2a547f9ebc27388d7534eeb584b`
- activation/head: `5e243ee67f47b74a5a2c92f47fad079f5deeddd0`
- run/job: `33823950570` / `100872477739`
- artifact: `9919271393`
- artifact ZIP SHA256: `62a11bd69439eb60e07f25a321c077faa756c82163f530f3901b6a2268337b59`

## Raw result
Artifact status: `M1_EXACT_MMAP_FULL_COMPONENT_EQUIVALENCE`.

All three prospectively frozen NSIDE=16/lmax=47 synthetic cases matched stock NaMaster 2.7 exactly for the complete canonical `<f8 [2,8,2,48]` tensor under both canonical SHA256 and `numpy.array_equal`; `max_abs_difference=0.0` for every case. Selected TE slices also matched exactly. Runtime lineage was PyMaster 2.7 + GSL 2.7. No DES or historical numerical data were read and no tolerance/closeness rule was used.

Memory contract satisfied: downstream emulator reads the serialized complete unbinned MCM using read-only POSIX `mmap` and does not allocate/read a second full-MCM heap copy before source-order full ncls=2 binning, GSL LU inversion, GSL BLAS dgemm and stock raw ordering.

## Classification
Support/resource architecture PASS `+0/+0`, NON-SCIENTIFIC and NON-AUTHORIZING. This does not create Wm_S3 authority and does not activate Exp073BU.

## Consequence
The duplicate downstream MCM-residency bottleneck is closed: exact stock downstream arithmetic can consume a durable file-backed full MCM without a second full resident MCM copy. The next unresolved memory question is upstream construction/retention/persistence of the stock full MCM itself at DES scale. A new prospective source/lifecycle audit must identify whether NaMaster 2.7 can persist the full MCM directly from its workspace representation without materializing another complete ncls*lmax^2 buffer, or whether a new exact construction/persistence architecture is required.
