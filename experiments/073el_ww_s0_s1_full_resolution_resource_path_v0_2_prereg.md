# Exp073EL — WW_S0_S1 full-resolution ordered distinct-field resource-path admission v0.2

**Prospectively preregistered:** 2026-09-06 after Exp073ET v0.1 terminal support FAIL and before Exp073EU terminal result, while Exp073EN `WW_S0_S0` remains unresolved/in progress.

**Status:** `PREREGISTERED_NOT_ACTIVATED`.

**Accounting:** support/resource `+0/+0`; cannot create science authority.

## Supersession
This v0.2 prospectively supersedes the never-activated Exp073EL v0.1 preregistration. V0.1 remains immutable historical evidence. Its dependency on a terminal `Exp073ET PASS` became unsatisfiable because ET v0.1 correctly remained FAIL under an over-strong cross-state condition (in-memory BPW == post-FITS-reload BPW), despite exact success of its ALM/PCL/MCM/in-memory-route checks.

V0.2 does not reclassify ET and does not introduce a tolerance. Instead it requires a new independently preregistered state-matched Exp073EU PASS, where stock and low-memory routes are compared exactly in the same pre-serialization state and again exactly in the same serialized-public-reload state.

## Frontier lock
EL v0.2 MUST NOT activate until real Exp073EO emits:
`PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

EL PASS is resource readiness only; `WW_S0_S1` remains a later separately frozen science A/B gate.

## Frozen source reconstruction
Future low-memory execution MUST import and use the existing Article-3 task runner source reconstruction rather than creating a new source-mask algorithm:
- file `ci/exp073aa_article3_des_angular_task_runner_v0_1.py`;
- frozen blob `050ed7dd3387c4fb031f877825e6b3f4d4ce3ef2`;
- function `source_count_map(root, bin_index)`;
- R1 artifact `9720335366`;
- R1 digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

For each source bin the function validates exact pixel-record bytes/SHA, NSIDE pixel range, selected-row total, unique pixels and occupancy SHA before returning the dense float64 count map. It must be called sequentially for bin 0 and bin 1; the current task-runner main-path behavior that stores both maps simultaneously MUST NOT be used for this low-memory route.

## Resource rationale
At NSIDE=4096 / lmax=12287:
- one dense float64 source mask = `1,610,612,736` bytes = `1.500 GiB`;
- one complex128 mask ALM = `75,503,616 * 16 = 1,208,057,856` bytes = `1.125091552734375 GiB`;
- public simultaneous distinct-field preparation can retain about `5.25018 GiB` in just two masks plus two ALMs before SHT/Healpy/Python/GSL/NaMaster working buffers.

Therefore S0 and S1 must be reconstructed/transformed/spilled one at a time. Two exact ALM files may then be read-only mmap inputs to ordered `healpy.alm2cl`; after `pcl_mask` is produced, the ALM mappings must be released before MCM construction.

## Frozen numerical route
- exact NaMaster/PyMaster source commit `24365fa59a38c15732f4f37e8b29265b75c442d5`;
- spin-2 ordered `S0 -> S1`;
- lmax=lmax_mask=12287, 39 frozen Article-3 bands;
- MASTER normalization; unit beams; no purification; `is_teb=False`; no Toeplitz approximation;
- low-memory PCL preparation and the exact same `pymaster.nmtlib.comp_coupling_matrix` argument order as PyMaster 2.7;
- construction unbinned MCM uses the Exp073EM-qualified regular-file file-backed semantics, exact geometry `49152 x 49152`, `19,327,352,832` bytes;
- serialize through ordinary NaMaster FITS writer;
- terminate construction workspace/process and prove construction mmap cleanup before reload;
- fresh serialized-public reload uses Exp073ER-qualified file-backed read semantics with the same exact `19,327,352,832`-byte mapping;
- call public `get_bandpower_windows()` only after fresh reload;
- selected output exactly `wins[0,:,0,:] = EE<-EE`, canonical `<f8 [39,12288]`.

The post-serialization public state is the future authority-candidate numerical state. Pre-serialization BPW may be retained only as a support diagnostic and must not be compared cross-state under an exact-equality gate.

## Mandatory support prerequisites
Before EL v0.2 may PASS it must bind immutable evidence for:
1. Exp073EM construction-storage exact PASS;
2. Exp073EK serialized distinct-field public-BPW repeatability PASS;
3. Exp073EP file-backed-cross/public-BPW composition exact PASS;
4. Exp073ER file-backed FITS-read/public-BPW exact PASS;
5. `PASS_EXP073EU_WW_S0_S1_SEQUENTIAL_SPILL_SERIALIZED_PUBLIC_BPW_EXACT_V0_1`.

ET v0.1 remains historical support FAIL `+0/+0` and is not a prerequisite.

## Host resource admission
Immediately before future `WW_S0_S1` science dispatch, EL v0.2 must verify:
- exact intended self-hosted runner identity/labels;
- no competing heavy DSIR self-hosted job;
- WSL configuration no weaker than the proven EN environment (`memory=6GB`, `processors=8`); no unsafe memory increase is required;
- at least **50 GiB free** on the filesystem used for science root, ALM spill and file-backed MCM;
- regular-file create/ftruncate/mmap/cleanup support;
- sufficient file-descriptor and path permissions;
- stage ordering that permits at most the necessary ~18-GiB backing + ~18-GiB serialized workspace overlap, plus ~2.25-GiB ALM spill files/checkpoints/headroom, and removes obsolete large intermediates only after hash-bound receipts exist.

Resource failure is `RESOURCE_BLOCKED +0/+0`, not science FAIL.

## Exact admission token
Only a future implementation conforming to this v0.2 preregistration may emit:
`PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2`.

No tolerance, allclose, rounding, smoothing, averaging, effective-ell substitution, altered binning, reduced resolution or other numerical rescue is allowed.
