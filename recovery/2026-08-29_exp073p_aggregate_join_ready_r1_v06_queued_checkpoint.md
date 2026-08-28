# DSIR checkpoint — Exp073P aggregate join ready; canonical R1 v0.6 queued

**Date:** 2026-08-29 (EEST)
**Scope:** chat-independent recovery after the DSIR 5/6 continuation audit

## Executive state

The repository, rather than an older chat recap, is authoritative.  The active
G7 boundary is still before real Exp073P physical-support evaluation.

- canonical Exp073R1 v0.6 Stage-B run: `33212521957`;
- canonical job: `98988824629`, `metacal-map-longrun`;
- head: `79abf2a9694e57e7a2ba1fbb563a0f6413e891f9`;
- state at this checkpoint: `queued` on the self-hosted Linux runner;
- terminal R1 artifact: absent;
- real Exp073P aggregate join: blocked on terminal genuine R1 PASS;
- Exp073P physical support: blocked on real aggregate-join PASS;
- covariance/whitening and all later stages: blocked.

G7, G8 and G9 remain OPEN.  No support fraction or retained dimension was
computed in this iteration.

## Authority correction after recovery audit

The previous recovery note
`recovery/2026-08-29_exp073r1_v06_selfhosted_longrun_dispatch_checkpoint.md`
temporarily named run `33213021914` as the authority candidate.  Later commits
superseded that route.  It is now cancelled and its workflow is deliberately
fail-closed.

The sole canonical heavy v0.6 route is the Stage-B-only workflow above, already
queued as run `33212521957`.  Protocol-guard run `33215131178` and R1-to-P
interlock run `33215180917` both completed successfully before this checkpoint.

## Obsolete heavy-route cleanup

Old v0.4 microshard run `33160570463` still had one shard executing and many
queued even though v0.5/v0.6 had superseded it.  Commit
`414ec7512ecb193e286feb2cddc9cd62fc320a93` added a fail-safe cancellation that
first binds the exact canonical v0.6 authority and only then cancels listed
superseded runs.

- cancellation workflow run: `33216480776`;
- conclusion: `success`;
- old v0.4 terminal state: `completed/cancelled`;
- canonical v0.6 run `33212521957`: untouched and still queued.

This removes wasted computation and prevents partial v0.4 shards from being
mistaken for R1 authority.

## New Exp073P provenance-join implementation

The already-frozen split-provenance method had no executable aggregate join.
This iteration closed that implementation gap prospectively.

### Chronology

1. Before implementation or synthetic output, commit
   `c947a30cdcc1457c72e2501c6030f003ca9f037d` froze the exact evaluator
   contract and the exact admitted R1 authority.
2. Commit `6d32ce32d16c33d3731031d543776e2045eb8115` implemented
   `ci/exp073p_aggregate_prerequisite_join_v0_1.py` and its synthetic CI.
3. CI run `33217294341`, job `99003665458`, completed `success`.
4. Immutable synthetic receipt artifact:
   - ID `9703832682`;
   - name `exp073p-aggregate-join-synthetic-selftest-6d32ce32d16c33d3731031d543776e2045eb8115`;
   - digest `sha256:6d4779be4a5e9dce1a582ed1e742b3c9f5766c551d7ee487c325f842cc1eddfe`.

Internal synthetic status:

`PASS_EXP073P_AGGREGATE_JOIN_SYNTHETIC_SELFTEST_V0_1`.

That label is intentionally distinct from the real prerequisite PASS and has
`support_executor_authorized=false`.

## What the evaluator now enforces

The join requires all ten immutable parents frozen in
`experiments/073p_aggregate_prerequisite_join_evaluator_prereg_v0_1.md`,
including:

- exact Cosmotheka pin and four source hashes;
- the complete six-object DES byte/SHA256 identity table;
- large source and metacal whole-object artifacts;
- P2 four-object checksum PASS;
- S0 redMaGiC mask plus lens/source n(z) PASS;
- genuine R1 internal PASS through the independent R1 interlock;
- frozen BOSS `54/240`, `27/120` per cap and `9/40` per multipole;
- frozen support-contract, split-join, R1-interlock and v0.6 protocol-guard runs;
- exact local contract hashes;
- all no-downstream-leakage flags.

The mutation suite alters every metadata parent and every substantive record
class.  Expired/missing artifacts, head/path/name drift, wrong SHA256/bytes,
legacy preflight READY resurrection, R1 mapper/selection/leakage drift, S0 hash
drift and BOSS count/leakage drift all fail closed.

## Real-parent compatibility audit

The evaluator was also applied separately to the real already-existing records
without pretending that R1 exists.  It accepted:

- committed preflight SHA256
  `e3429fff6786437aef68d2c5930341fd2b1752c193fd99f1c917e636859636f1`;
- actual source artifact `9650284556`;
- actual metacal artifact `9650627630`;
- actual P2 artifact `9652278804` with four records;
- committed S0 key-metrics SHA256
  `abc41cfb16daece655e61b2fb8c592b2a09c9384943184272d59d63703eaef49`;
- committed BOSS key-metrics SHA256
  `dfe8861cd62e82297d9ce733d79585f7c5eca93d9bdbcef445b9f578105b2029`;
- all five frozen local contract-file hashes.

Machine-readable record:
`data/derived/g7/exp073p_aggregate_join_parent_compatibility_audit_v0_1.json`.

Repository regression result: `44 passed`; Python compile audit also passed.

This compatibility PASS is non-science and keeps
`support_executor_authorized=false`.  It establishes that the join will not be
blocked later merely by an untested historical parent schema.

## Frozen scientific contract — unchanged

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- classifying `nside=4096`;
- exact Limber support bookkeeping;
- positive absolute support envelope while production Wm remains signed;
- no crop-before-normalization, effective ell, model/P weighting or post-hoc cut;
- no covariance, nuisance SVD/rank, quotient/relation/null, held-out or G8 read.

## Exact continuation order

1. Bring the configured self-hosted Linux runner online and let run
   `33212521957` execute without changing or duplicating it.
2. On terminal completion, verify Actions success is accompanied by the exact
   internal `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`, exact bytes,
   SHA256 values, row counts, four nonempty bins, repeatability, mask hashes and
   no-leakage flags.
3. If interrupted, record only `INCOMPLETE_EXP073R1`.  Do not reuse a partial
   mask and do not relabel infrastructure failure as support FAIL.
4. If genuine PASS, freeze the returned R1 artifact ID/digest in the actual
   aggregate-join workflow before running that workflow.
5. Require real `PASS_EXP073P_PREREQUISITE_BINDING_V0_1` before starting the
   separately preregistered Exp073P physical-support executor.
6. Only real
   `PASS_COSMOTHEKA_DESY1_BOSS_COMMON_PHYSICAL_SUPPORT_EXP073P` may open
   covariance restriction/whitening.
7. Then, and only then: nuisance tangent SVD/rank -> quotient/relation/null ->
   fresh G8 withheld family.

## Recovery read order

1. `docs/RECOVERY_MANUAL.md`
2. `docs/RECOVERY_LATEST.md`
3. this checkpoint
4. `experiments/073r1_v0_6_selfhosted_longrun_stageb_prereg.md`
5. `experiments/073p_aggregate_prerequisite_join_evaluator_prereg_v0_1.md`
6. `ci/exp073p_aggregate_prerequisite_join_v0_1.py`
7. `recovery/2026-08-28_exp073r1_to_exp073p_execution_integrity_matrix.md`
8. `experiments/073p_cosmotheka_desy1_boss_exact_common_physical_support_prereg_v0_1.md`
