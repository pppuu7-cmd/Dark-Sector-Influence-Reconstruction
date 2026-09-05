# Exp073EP — WW cross file-backed + public-BPW composition exact qualifier v0.1

Prospectively preregistered 2026-09-06 while Exp073EN full-resolution WW_S0_S0 remains in progress. Support-only qualifier; accounting `+0/+0`; no WW science authority may be created by this experiment.

## Purpose
Close the composition risk between two already separate support results before the ordered `WW_S0_S1` science frontier is activated:

1. Exp073EM: stock NaMaster/PyMaster 2.7 and the DSIR regular-file `mmap(MAP_SHARED)` storage-only patch are bit-for-bit exact for small spin-2 auto and ordered cross construction, including WSP and public BPW.
2. Exp073EK: for a serialized distinct-field `S0 -> S1` workspace, two independent public `NmtWorkspace.read_from()` + `get_bandpower_windows()` reloads are bit-for-bit repeatable.

Exp073EP must prove these operations compose: a distinct-field workspace built with the EM file-backed backend must serialize into a workspace whose public BPW reload semantics are exactly the same as stock construction/serialization under the frozen small geometry.

## Frozen identities and geometry
- NaMaster tag `v2.7`; exact source commit expected from the EM authority: `24365fa59a38c15732f4f37e8b29265b75c442d5`.
- Storage patch: `patches/namaster-v2.7-dsir-filebacked-mcm-v0.1.patch`, SHA256 `9a80a756960afa8b4ddf61b5fbba7fba6ad5ed9ac919e093bb1365a636c789f0`.
- `NSIDE=16`, `lmax=47`, `nl=48`.
- ordered distinct spin-2 fields `S0 -> S1` using the deterministic masks and bin edges frozen by Exp073EK: edges `[0,6,12,18,24,30,36,42,48]`, 8 bands.
- expected unbinned MCM geometry: `(4*48) x (4*48)` float64 = `294912` bytes.
- full public BPW shape `[4,8,4,48]`; selected block `EE<-EE = wins[0,:,0,:]`, shape `[8,48]`.
- canonical arrays are contiguous little-endian float64.

## Execution contract
Build two isolated PyMaster 2.7 runtimes from the same exact source tree: stock and patched. Only the patched build may set `DSIR_NMT_FILEBACKED_MCM=1` and `DSIR_NMT_MMAP_DIR`.

For both stock and patched builds:
- construct the frozen ordered `S0 -> S1` workspace;
- capture canonical in-memory `WSP_PRIMARY` after serialization and in-memory public BPW/selected EE;
- write the workspace to FITS;
- for patched construction, prove while the workspace is alive that exactly one regular mapped backing file exists, appears in `/proc/self/maps`, and has exactly `294912` bytes; prove it is deleted after workspace destruction.

Then, using the stock PyMaster 2.7 runtime, execute four separate fresh Python processes:
- stock FITS reload A;
- stock FITS reload B;
- patched FITS reload A;
- patched FITS reload B.

Each reload may use only public `NmtWorkspace.read_from()` followed by public `get_bandpower_windows()` for the tested BPW operation.

## Exact acceptance
Terminal `PASS_EXP073EP_FILEBACKED_CROSS_PUBLIC_BPW_COMPOSITION_EXACT_V0_1` requires all of:
- stock vs patched construction WSP exact shape, canonical SHA256 equality, `numpy.array_equal=true`, max absolute difference `0.0`;
- stock vs patched in-memory public full BPW and selected EE exact by the same criteria;
- stock reload A vs stock reload B exact for full BPW and selected EE;
- patched reload A vs patched reload B exact for full BPW and selected EE;
- stock reload A vs patched reload A exact for full BPW and selected EE;
- stock reload B vs patched reload B exact for full BPW and selected EE;
- all tested arrays finite and frozen shapes correct;
- patched regular-file mmap proof valid and backing file cleanup complete;
- PyMaster version is 2.7 in build and reload runtimes;
- no tolerance, `allclose`, rounding, smoothing, averaging, or rescue.

A known possible difference between an original in-memory cross workspace and a serialized/reloaded public BPW, previously localized by Exp073DY, is not itself a failure here. The future cross authority semantics are the Exp073EK-qualified serialized-workspace reload + public BPW operation. Therefore the mandatory construction equality is stock-vs-patched at the same stage, and the mandatory reload equality is stock-vs-patched/repeatability at the same serialized-reload stage; no requirement is imposed that in-memory BPW equal reloaded BPW bit-for-bit.

## Classification
PASS classification: `COMPOSED_STORAGE_PUBLIC_BPW_EXACT`, support-only `+0/+0`, `science_gate_scored=false`, `ww_authority_created=false`.

Any exactness mismatch is `COMPOSITION_QUALIFIER_FAIL +0/+0`, not a dark-sector science FAIL. Build/network/toolchain/resource failures are `BLOCKED +0/+0`.
