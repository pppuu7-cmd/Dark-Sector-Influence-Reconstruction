# Exp073ER — NaMaster 2.7 file-backed FITS-read + public-BPW exact qualifier v0.1

Prospectively preregistered on 2026-09-06 while Exp073EN `WW_S0_S0` remains in progress. Hosted-only support qualifier; accounting `+0/+0`; it cannot create Article-3 science authority.

## Motivation
The already-qualified v0.1 storage patch only changes `nmt_workspace_new()` construction storage. Exact NaMaster 2.7 `src/nmt_io.c::nmt_workspace_info_fromhdus()` independently allocates `coupling_matrix_unbinned` row-by-row with `my_malloc` when a serialized workspace is read with `w_unbinned=true`. Exact PyMaster 2.7 `NmtWorkspace.get_bandpower_windows()` calls `check_unbinned()`, so `read_unbinned_MCM=False` cannot implement the Exp073EK-qualified serialized-workspace public-BPW semantics.

At full spin-2 resolution this read path would therefore reintroduce a `49152 x 49152` float64 allocation (`19,327,352,832` bytes) into RAM. Before the ordered frontier can activate full-resolution `WW_S0_S1`, the FITS-read storage path must be made file-backed without changing numerical semantics.

## Frozen source and operation
- NaMaster/PyMaster 2.7 exact source commit: `24365fa59a38c15732f4f37e8b29265b75c442d5`.
- New patch file: `patches/namaster-v2.7-dsir-filebacked-mcm-read-v0.2.patch`.
- The active Exp073EN v0.1 patch is immutable and must not be modified.
- Test geometry is the already-qualified ordered cross geometry used by Exp073EK/EP: `NSIDE=16`, `lmax=47`, `nl=48`, spin-2 distinct `S0 -> S1`, edges `[0,6,12,18,24,30,36,42,48]`, 8 bands.
- Expected unbinned MCM: `(4*48)^2*8 = 294,912` bytes.
- Public BPW operation: serialized workspace -> fresh `NmtWorkspace.read_from()` with unbinned MCM -> `get_bandpower_windows()`.
- Full BPW shape `[4,8,4,48]`; selected `EE<-EE` shape `[8,48]`.

## Patch scope
The v0.2 patch may change storage allocation/cleanup only:
1. construction allocation preserves the v0.1 regular-file mmap semantics when `DSIR_NMT_FILEBACKED_MCM=1`;
2. FITS read allocation uses the same regular-file mmap registry when the environment flag is enabled;
3. with the flag disabled, stock allocation semantics remain `calloc` for construction and `malloc` for FITS read;
4. FITS read order, `fits_read_pix`, MCM arithmetic, binning, GSL state, serialization, and PyMaster public API are unchanged;
5. all backing files must be regular files, exact-sized, visible in `/proc/self/maps` while the workspace is alive, and removed on workspace destruction.

## Exact acceptance
`PASS_EXP073ER_FILEBACKED_FITS_READ_PUBLIC_BPW_EXACT_V0_1` requires:
- stock and patched builds from the exact same source commit;
- one stock-constructed serialized ordered `S0 -> S1` workspace used as the common immutable FITS input;
- stock fresh reload A/B and patched file-backed fresh reload A/B all use public `read_from()` + `get_bandpower_windows()`;
- patched reload A/B each independently prove a regular mapped backing file of exactly `294,912` bytes while the workspace is alive, and complete cleanup after destruction;
- stock A == stock B, patched A == patched B, stock A == patched A, stock B == patched B for full BPW and selected `EE<-EE`, with exact shape, canonical little-endian float64 SHA256 equality, `numpy.array_equal=true`, and max absolute difference `0.0`;
- all arrays finite;
- no tolerance, `allclose`, rounding, smoothing, averaging, or rescue.

A mismatch is a storage/read support qualifier failure `+0/+0`, not a dark-sector science failure.

## Frontier effect
Even a PASS remains support-only. It only demonstrates that the already-qualified serialized public-BPW cross semantics can be executed at full resolution without restoring the 18-GiB RAM allocation. `WW_S0_S1` may not be activated until `WW_S0_S0` authority is independently admitted by Exp073EO.
