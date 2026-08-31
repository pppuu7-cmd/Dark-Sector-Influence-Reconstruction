# Article-3 streaming general-coupling successor design — 2026-08-31

**Project:** DSIR only.  
**Status:** design / nonclassifying QA.  
**Scientific readiness increment:** `+0`.  
**Draft/data readiness increment:** `+0`.

This design is prepared while Exp073BJ remains active. It must not modify, reinterpret, accelerate by changing mathematics, or otherwise affect the already-triggered BJ classifying run.

## 1. Quantified bottleneck

Frozen full scale is `L=12288`, 39 output bands.

The current low-memory implementation calls

`G = nmt.get_general_coupling_matrix(...)`

before applying deterministic compression to `A`.

Thus the implementation is low-memory only after the general-coupling call has returned; it is not a true streaming construction of the compact object.

At frozen shape:

- dense `G`: `12288^2 = 150,994,944` float64 entries;
- dense `G` payload alone: `1,207,959,552` bytes = `1.125 GiB`;
- compact `A`: `39*12288 = 479,232` float64 entries;
- compact `A`: `3,833,856` bytes = `3.65625 MiB`;
- output-size reduction `G/A`: about `315.08x`.

The deterministic compression touches each dense matrix element once, about `150,994,944` float64 additions, whereas construction of `K=AQ` needs only `479,232` band additions and the final 39x39 solve with 12288 RHS is negligible compared with the multi-hour general-coupling stage.

Independent local conditioning diagnostics on provisional real DES-derived Wm_S2 already found `cond_2(K)=2.1928888836909883` and `||KW-A||/||A||=3.2380349152387473e-16`, further arguing that the small finalizer is not the observed BA/BH execution bottleneck.

## 2. Public API limitation relevant to streaming

The Python `get_general_coupling_matrix` interface returns a complete dense `[nl,nl]` matrix. The current DSIR implementation therefore cannot request only a row band or block through that public interface.

A true streaming/checkpointable successor would require either:

1. a C-level NaMaster extension/wrapper able to emit rows or row blocks in canonical ascending-ell order; or
2. an independently implemented mathematically equivalent general-coupling row generator, prospectively validated against NaMaster before any classifying use.

Simply changing Python slicing after `get_general_coupling_matrix` cannot remove the dense construction bottleneck because the dense array has already been formed.

## 3. Exact accumulation equivalence demonstrated locally

A deterministic synthetic coupling matrix was generated and compressed by the current frozen fixed-order algorithm. The same rows were then fed to a streaming accumulator in identical ascending-ell order.

Tested block sizes:

`1, 3, 17, 64, 127, 256, 1024` rows.

Every streaming result was exactly `numpy.array_equal` to the full-matrix reference, had the same canonical float64 SHA256, and had maximum absolute difference `0.0`.

The accumulator was also serialized to `.npy` and reloaded repeatedly during a band, with checkpoint intervals:

`1, 2, 7, 31, 100, 257` rows.

Again every result was bit-for-bit identical to the no-checkpoint full reference.

Frozen QA implementation:

`ci/article3_streaming_compression_equivalence_qa_v0_1.py`

commit `12a9c86331df0cd7954f440c94f518d0c157ff42`.

This proves only the accumulation/checkpoint arithmetic statement: if a future generator emits exactly the same float64 rows in exactly the same ell order, block boundaries and exact float64 checkpoint/reload do not themselves change compact `A`.

It does **not** prove that a future C-level/blockwise general-coupling row generator will emit the same row values as the current NaMaster call. That row-generation equivalence must be tested prospectively.

## 4. Candidate future successor architecture

Only after BJ has terminal classification, and only in a separately frozen experiment if needed:

1. bind the same immutable canonical mask PCL and all existing physical/angular criteria;
2. generate general-coupling rows in ascending output ell without materializing all `[12288,12288]` rows simultaneously;
3. maintain one float64 accumulator vector of length 12288 for the current frozen band;
4. divide exactly once by the frozen band width when that band closes;
5. append the completed row of `A` and checkpoint exact float64 state plus next ell;
6. include PCL SHA, implementation commit, dependency lineage, thread policy, completed-band hashes, current accumulator hash and next-ell index in every checkpoint receipt;
7. after all 39 bands exist, emit canonical `<f8 [39,12288]` compact `A`;
8. require two independent full replicas and exact comparator equality before finalization, exactly as the authority chain requires.

A checkpoint resume must restore the exact stored float64 accumulator and continue at the next unprocessed ell. It must never recompute a partial band with a different summation grouping and then merge partial sums, because regrouping additions can change floating-point bits.

## 5. Why this matters even if BJ succeeds

BJ tests Wm_S1 only. Article-3 angular authority ultimately requires the remaining Wm/WW task family as separately authorized successors. A checkpointable compact generator could therefore remove the six-hour hosted-run fragility from later tasks without changing scientific definitions, provided its row-generation equivalence is prospectively demonstrated.

If BJ itself times out, this design becomes a candidate execution successor rather than a reason to weaken the frozen BJ gate.

If BJ passes, BJ remains the Wm_S1 authority and this design may be evaluated only for later separately preregistered tasks.

## 6. Firewalls

- Exp073AQ remains permanent scientific repeatability FAIL.
- no tolerance, ULP, rounding, averaging, preferred replica or majority vote is introduced.
- this design is not authority and gives `+0/+0`.
- no Layer-A/B support, covariance, whitening, nuisance, relation/null or G8 information is used.
- G7 ordering remains unchanged and G8 remains forbidden before actual G7 authorization.
