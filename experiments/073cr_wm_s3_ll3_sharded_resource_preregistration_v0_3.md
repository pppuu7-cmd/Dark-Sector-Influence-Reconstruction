# Exp073CR v0.3 preregistration — static-audit control repair

Date: 2026-09-03
Scope: Wm_S3 resource/performance/control only; scientific credit `+0/+0`.

## Historical predecessor

Exp073CR v0.2 was created prospectively to repair the candidate-file SHA256 binding before any home Exp073CR execution. Its hosted run `33768408220`, job `100692073818`, passed the corrected geometry / authoritative bitwise-regression step and passed durable v0.2 seed creation. It then failed in the final static-audit step because the workflow searched for the literal text `durability-before-refill`, while the frozen driver represents the invariant as `durability_before_refill` and implements the actual order as `store_shard -> checkpoint sync -> refill submit`.

This is a **pre-self-hosted static-control defect +0/+0**. No Exp073CR v0.2 home numerical task was authorized or executed. v0.2 is preserved and is not edited or rescued.

## v0.3 repair boundary

Exp073CR v0.3 changes only the static-audit mechanism and the version/checkpoint namespace required for a prospective successor. It replaces the brittle literal grep with an explicit source-order audit that requires the unique compute-loop operations to appear in this frozen order:

1. `store_shard(root,got,a,tel)`;
2. durable `sync(root,branch,script,...)` for that completed shard;
3. only then `ex.submit(worker,nxt)` to refill the freed worker slot.

The audit also continues to require exactly 8 outer process workers, nested numerical threads=1, the exact helper ABI, the corrected candidate byte SHA and frozen heavy-first queue SHA.

## Unchanged numerical/resource contract

Everything else is inherited unchanged from Exp073CR v0.2:
- task: Wm_S3 compact general-coupling `A`, not final `W`;
- source bin 3; signature `(0,2,0,2)`; `L=12288`; `lmax=12287`; Wm `TE <- TE`;
- immutable PCL SHA256 `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`;
- candidate creation commit `d27deaec49f175ac17267fce94bfe2214a02ab6d`;
- corrected candidate byte SHA256 `d48e46197b48a6fcdf7d3eb3b0817973a2eadb25bbb617e7b8060c8c17209462`;
- 64 frozen ll3 shards over bands 29..38 with allocation `3,3,4,5,6,7,8,9,9,10` and the same boundaries;
- manifest creation commit `9fa7566f82ff61ba24e9f94b24d22f1264f0a8a5`;
- heavy-first queue SHA256 `3ba315d9bc24883ef746d92e785e0a040f9b13e751f59dda9a93e825a6390db4`;
- helper creation commit `bb856b8c49eea804fea73807c3eef53cc20ff3fa`, symbol `exp073cr_stream_compress_band_ll3_range_v0_1`;
- exactly 8 persistent outer workers, at most 8 numerical shards in flight;
- all nested numerical thread variables fixed to 1; `OMP_DYNAMIC=FALSE`;
- durability-before-refill;
- placement-only shard reassembly; no arithmetic reduction across shards;
- exact canonical `<f8 [12288]` equality and SHA equality for every reconstructed band 29..38 against hosted-seeded immutable Exp073CQ v0.2 terminal references;
- CPU fraction threshold remains `>=0.90`;
- positive swap increase remains 0 KiB;
- no tolerance, ULP, rounding, smoothing, averaging, regularization or post-hoc rescue;
- any resource/control/infrastructure outcome remains `+0/+0`.

Historical CQ parent remains terminal head `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`, contract fingerprint `87b58bf120510bec50b21851d7ff21269689db6dcdd906cb3a14102e4a4f5f97`, token `FAIL_EXP073CQ_V0_2_WM_S3_CPU_TARGET`.

## v0.3 prospective execution bindings

- version: `v0.3`;
- dedicated checkpoint namespace: `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3`;
- new v0.3 wrapper, static-audit helper, hosted workflow, self-hosted workflow and binding commits must all be frozen before activation;
- a fresh hosted seed + authoritative bitwise/static audit is mandatory;
- only a real explicit hosted PASS token plus exact v0.3 seed head/fingerprint may authorize one home run.

No Exp073CR result creates Wm_S3 scientific authority. A resource PASS only permits later preregistration of the separate fresh-independent-PCL A/B scientific successor and deterministic finalizer.
