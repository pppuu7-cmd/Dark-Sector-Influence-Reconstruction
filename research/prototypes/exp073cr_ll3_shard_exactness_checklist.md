# Exp073CR research prototype — ll3 shard exactness checklist

Status: NON-AUTHORITATIVE RESEARCH ONLY. No preregistration, no execution authority, +0/+0.

Historical/frozen Exp073CQ is untouched. This checklist is usable only for a new successor after CQ terminal outcome consumption.

## Frozen reference implementation

Reference arithmetic is `ci/exp073ca_stream_general_coupling_range_v0_1.c` compiled with the established FP restrictions and executed in the frozen NaMaster 2.7 environment.

Prototype source: `research/prototypes/exp073cr_stream_band_ll3_range_v0_0.c`.

## Code-identity obligations per retained output ll3

For one complete frozen band `ib` and each output `ll3 >= lstart`, a valid shard implementation must preserve exactly:

1. full frozen band bounds `lo=edges[ib]`, `hi=edges[ib+1]`;
2. outer `ll2` iteration `lo,lo+1,...,hi-1`;
3. skip rule `if(ll2<lstart) continue`;
4. `lmin_here=abs(ll2-ll3)` and `lmax_here=ll2+ll3`;
5. first call `drc3jj(ll2,ll3,n1,-s1,...)`;
6. second call `drc3jj(ll2,ll3,n2,-s2,...)` when `same_sn` is false, with identical same-sn reuse otherwise;
7. ascending `l1=lmin_here..lmax_here` and identical `if(l1<=lmax)` clipping;
8. identical Wigner indices and zero-for-negative-index rule;
9. identical recurrence `xi += wl_mask[l1]*wsn1*wsn2`;
10. identical `xi *= (2*ll3+1.0)`;
11. identical one-at-a-time `acc[ll3] += xi` sequence as ll2 increases;
12. exactly one final division by the FULL band width `(hi-lo)` after all ll2 contributions.

No shard may partition the ll2 dimension and later add partial accumulators. That would alter floating-point grouping.

## Independence obligation

Disjoint ll3 shards must write disjoint output elements. Assembly may only copy/place canonical `<f8` slices into their frozen output positions. No sum, mean, reduction, interpolation, smoothing, or tolerance-based reconciliation is permitted.

NaMaster `drc3jj` source at public commit `479864f7425cfb8d3a6e9ccedb0649ae833a928c` uses local scalar state plus caller-provided `thrcof` for the normal valid-input computational path. This supports independent ll3 calls but is not a substitute for executable bitwise regression.

## Compiler/runtime obligations

Future exact-regression must use the same compiler flags as the frozen helper unless a newly preregistered equivalence gate explicitly freezes otherwise:

`gcc -O2 -shared -fPIC -fno-fast-math -fno-associative-math -ffp-contract=off -fno-tree-vectorize`

If OpenMP linkage is retained for environment parity it must not introduce numerical parallelism inside a shard. Prototype v0.0 requires `nthreads==1` and uses process-level parallelism only.

Runtime must bind the same NaMaster 2.7 `_nmtlib` used by the frozen reference and the same immutable PCL SHA256 `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`.

## Required hosted/local exact-regression before any future home launch

At minimum, before a future successor can be authorized:

- compile frozen reference helper and prototype helper under identical flags/environment;
- use an already-authoritative immutable PCL;
- choose completed historical bands spanning low, middle and high cost; preferred candidates include 0, 7, 15, 24, 28 where practical;
- compute a full frozen reference row;
- compute the same row as disjoint ll3 shards covering `[lstart,L)`;
- explicitly fill the same frozen zeros below `lstart`;
- assemble by placement only;
- require `np.array_equal(reference,assembled)`;
- require exact canonical SHA256 equality;
- require finite values;
- report first differing index and bit pattern on any mismatch; no tolerance/ULP rescue;
- repeat after at least one different shard partition to ensure boundaries do not influence output bits.

Only after that exact-regression PASS may a prospective resource successor freeze shard boundaries, checkpoint contracts and an eight-worker home workflow.

## Checkpoint obligations

Each future `(band,ll3_lo,ll3_hi)` complete shard must carry canonical payload, SHA256, exact interval, band identity, PCL/helper/compiler/runtime provenance and successor contract fingerprint. Durable remote checkpoint must occur at complete shard boundaries only. Whole-band completion receipt is allowed only after all frozen shards for that band validate exactly and have been assembled by placement.

No authority is created by this checklist.
