# Exp073BO — Article-3 native band-projected general-coupling QA v0.1

**Project:** DSIR only.  
**Classification:** nonclassifying source-equivalence / execution-engineering QA.  
**Scientific readiness increment:** `+0`.  
**Draft/data readiness increment:** `+0`.

## Purpose

Test a true low-memory native successor architecture for the frozen Wm general-coupling stage without changing the mathematical cell definition.

The active Exp073BJ Track-A run is immutable and must not be changed, duplicated, rescued or reclassified by this QA.

## Exact source basis

NaMaster tag `v2.7`, `src/nmt_master.c`, function `nmt_compute_general_coupling_matrix` is the source reference.

For a requested channel `(s1,s2,n1,n2)`, the reference implementation:

1. forms `wl_mask[l1] = pcl_mask[l1]*(2*l1+1)/(4*M_PI)`;
2. for each `ll2,ll3`, obtains Wigner arrays through `drc3jj`;
3. accumulates in ascending `l1` order
   `xi += wl_mask[l1]*wsn1*wsn2`;
4. multiplies the completed cell by `(2*ll3+1.0)`.

Exp073BO does **not** independently reimplement Wigner-3j. Its native C prototype receives the address of the exact `drc3jj` symbol from the installed PyMaster/NaMaster 2.7 extension and calls that binary function directly.

## Frozen channel

Only the actual Wm general-coupling channel used by the current Article-3 low-memory implementation:

`get_general_coupling_matrix(pcl, 0, 2, 0, 2)`

thus:

- `s1=0`, `s2=2`;
- `n1=0`, `n2=2`.

No WW channel is qualified by this experiment.

## Frozen deterministic inputs

Three tractable scales are required:

- `lmax=95` (`L=96`);
- `lmax=255` (`L=256`);
- `lmax=511` (`L=512`).

For each integer `ell=0..lmax`, construct the mask PCL in a Python scalar loop as

`pcl[ell] = float(1 + (ell % 11)) / float((ell + 1)*(ell + 2))`.

Canonicalize to contiguous `<f8`. Each replica records the PCL SHA before computation.

Band edges are the frozen Article-3 edges truncated at `L`, with `L` appended if it is not already an edge. Therefore the same low-ell bands and ascending-ell averaging convention are exercised.

## Frozen reference path

For each scale, in a fresh child process using exact PyMaster/NaMaster 2.7:

1. compute full stock `G = pymaster.get_general_coupling_matrix(pcl,0,2,0,2)`;
2. require shape `[L,L]`, finite `<f8`-canonical values;
3. compress with the current frozen Article-3 order: initialize one length-L float64 accumulator per band; for `ell=lo..hi-1`, execute `acc += G[ell]`; divide exactly once by `float(hi-lo)`;
4. emit canonical compact `A_stock` and SHA.

The dense matrix may be discarded after compression.

## Frozen native projected path

The native C prototype must **never allocate an `L x L` matrix**.

For each band in ascending order and each output `ll2` in ascending order:

1. compute every `G[ll2,ll3]`, `ll3=0..L-1`, using the exact source formula and the exact runtime `drc3jj` symbol;
2. add that completed scalar cell to the current length-L band accumulator using `acc[ll3] += cell`;
3. after the band closes, divide every accumulator element exactly once by `float(width)` and write the completed A row.

For `ll2 < max(s1,s2)=2` or `ll3 < 2`, cells remain exact `0.0`, matching the stock source loop bounds.

The native prototype is compiled once per hosted replica with:

`gcc -O2 -std=gnu11 -shared -fPIC ... -lm`

No `-ffast-math`; no explicit FMA/tolerance/rounding controls are introduced.

## Hosted replication

Require four independent `ubuntu-24.04` replicas A-D. Pin the same conda lineage used by the recent NaMaster-2.7 diagnostics:

`python=3.11 namaster=2.7 healpy astropy numpy`.

Set all known thread controls to one. Record CPU model, NumPy runtime CPU features, PyMaster version, PCL SHA, stock A SHA, stream A SHA, exact equality, wall time and maximum RSS for the separate stock and native child processes.

## Prospectively frozen classes

All three scales must complete on all four replicas.

### `BO_Q1_NATIVE_PROJECTED_EXACT_EQUIVALENCE_PASS`

Requires simultaneously:

- `numpy.array_equal(A_stock, A_native)` for every scale in every replica;
- canonical byte SHA equality `SHA(A_stock)==SHA(A_native)` for every scale in every replica;
- one cross-host canonical native-A SHA per scale across A-D;
- no invalid/nonfinite values.

### `BO_Q2_NATIVE_PROJECTED_EXACT_EQUIVALENCE_FAIL`

Any complete within-replica exact mismatch or complete cross-host native-A mismatch.

Numerical closeness cannot rescue this class.

### `BO_Q3_INFRASTRUCTURE_INCOMPLETE`

Fewer than four valid replica receipts / any scale missing before exact comparison.

## Resource diagnostics

Wall time and maximum RSS are descriptive only. No runtime or memory threshold is a PASS criterion in v0.1. A successful exact result qualifies only the source-equivalence concept at these scales; it does not prove full-scale speedup or full-scale Wm authority.

## Firewalls

- Exp073AQ remains permanent scientific exact-repeatability FAIL.
- Exp073BJ remains the sole active full-scale Track-A Wm_S1 authority run.
- no tolerance, ULP acceptance, rounding, averaging, majority vote or preferred replica;
- no support/covariance/whitening/nuisance/relation/null/G8 information;
- `+0/+0` regardless of result;
- a future full-scale streaming Track-A successor requires a separate prospective preregistration after this QA and after respecting the active BJ result.
