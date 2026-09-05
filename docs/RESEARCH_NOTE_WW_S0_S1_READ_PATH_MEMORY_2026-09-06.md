# WW_S0_S1 serialized public-BPW read-path memory audit — 2026-09-06

## Finding

The already-qualified NaMaster 2.7 DSIR file-backed MCM patch v0.1 solves the unbinned-MCM backing allocation used by `nmt_workspace_new()` during workspace construction, but does not intercept the FITS workspace read path.

Exact NaMaster source authority: `24365fa59a38c15732f4f37e8b29265b75c442d5`.

In exact `src/nmt_io.c`, `nmt_workspace_info_fromhdus()` with `w_unbinned=true` allocates `coupling_matrix_unbinned` independently:

- allocates the row-pointer array with `my_malloc`;
- loops over all `n_el = ncls*(lmax+1)` rows;
- allocates every row with `my_malloc(n_el*sizeof(flouble))`;
- fills each row via `fits_read_pix`.

Therefore v0.1 construction-only mmap storage does not reduce memory on serialized `read_from()`.

Exact PyMaster 2.7 `NmtWorkspace.get_bandpower_windows()` calls `self.check_unbinned()` before `lib.get_bandpower_windows(...)`. Consequently `read_from(..., read_unbinned_MCM=False)` is not an admissible workaround for the Exp073EK-qualified serialized-workspace public-BPW semantics.

## Full-resolution consequence

For spin-2 WW with `nl=12288`, `ncls=4`:

- unbinned MCM rows = `4*12288 = 49152`;
- unbinned matrix = `49152 x 49152` float64;
- exact payload = `49152^2*8 = 19,327,352,832` bytes (~18 GiB).

Thus a future full-resolution `WW_S0_S1` route that simply serializes a file-backed-built workspace and then uses stock PyMaster `read_from(..., read_unbinned_MCM=True)` would reintroduce the same structural RAM problem on read.

## Remedy under qualification

A new additive storage-only v0.2 patch is being qualified by Exp073ER. It does not modify the active Exp073EN v0.1 science identity. The proposed change shares one unbinned-MCM allocator/cleanup registry between construction and FITS read:

- flag disabled: preserve stock `calloc` construction and `malloc` FITS-read semantics;
- flag enabled: use one regular-file `MAP_SHARED` backing matrix for either path;
- retain row-pointer indexing, FITS read order, arithmetic, binning, LU/GSL state, public API and serialized semantics;
- require exact-size regular-file mmap proof and cleanup.

Exp073ER is support-only `+0/+0`. Only exact stock-vs-patched public-BPW equality can qualify this remedy; it cannot advance the Article-3 science frontier by itself.
