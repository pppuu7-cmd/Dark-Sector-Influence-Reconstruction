# Exp073JO Article III JL slot20 canonical-node sharded recovery V0.5

Date frozen: 2026-09-10. Scope: DSIR Article III support/process recovery only.

Status: PROSPECTIVELY FROZEN AFTER JO V0.4 TERMINAL INFRASTRUCTURE BLOCK AND BEFORE ANY V0.5 GRID-FREEZE OR RESPONSE OUTPUT. SUPPORT-ONLY `+0/+0`.

## Trigger and valid interpretation of V0.4

JO v0.4 repaired the hosted-runner lifetime problem by executing the four frozen CLASS models independently. Repaired run `34529375485` completed static equivalence and all eight model shards, but aggregate job `103047043452` stopped before response reconstruction/equality on `cross-shard identity mismatch node_sha256`.

The eight receipts revealed two independently generated 4097-node lattice identities from the same frozen `np.geomspace` construction, with `grid_ratio_binary64` differing by one ULP. Because the aggregate failed before `np.array_equal(after_history,fresh_tail)`, V0.4 is infrastructure/provenance BLOCKED, not a valid history-control negative result. No response value from V0.4 may be used to choose a preferred lattice realization.

## Frozen scientific/numerical contract retained exactly

Preserve without modification:
- `KMIN=1e-4`, `KMAX=0.06664762008318016 Mpc^-1`;
- base fine architecture `F4096 = np.geomspace(KMIN,KMAX,4096,dtype=float64)`;
- response-blind guard counts exactly `(lower,upper)=(0,1)`, total requested nodes exactly `4097`;
- native CLASS `k_per_decade_for_pk=20`;
- pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c` and unchanged build/source patches;
- capacity `4608`, parser capacity `131072`;
- centered-cubic interpolation in `ln(k)` with the frozen JJ stencil;
- finite-difference models `(0,0),(-1e-4,0),(0,+1e-4),(0,-1e-4)`, `h=1e-4`;
- `REL_TOL=1e-3`, lookup tolerance `1e-12`;
- exact frozen `pre_z`, `tail_z`, pre/tail target vectors and history semantics from V0.4;
- all DSIR domain/mask/traversal/anti-rescue boundaries.

No tolerance, estimator, density, support, mask, smoothing, averaging, effective-coordinate, fiducial-P, interpolation rule or physical-domain change is permitted.

## Prospective canonical-node selection rule

The canonical 4097-node payload SHALL be the exact little-endian float64 output of the **first successful V0.5 response-blind grid-freeze job** satisfying all frozen guards below. This rule is frozen before that job is executed. The payload is accepted regardless of whether its SHA256 equals either V0.4 candidate and regardless of any V0.4 response values.

The grid-freeze job:
1. runs on GitHub-hosted `ubuntu-24.04` with `numpy==1.26.4`;
2. imports the exact frozen JJ implementation `ci/exp073jj_article3_layerb_common_grid_resolution_refinement_convergence_v0_1.py` and sets only `jj.CAPACITY=4608`;
3. calls exactly `jj.guarded_lattice(4096)` once;
4. verifies `(lower_guard,upper_guard,node_count)==(0,1,4097)`, finite/positive/strictly-increasing nodes, unchanged endpoints/support semantics, and complete centered-cubic support for the frozen JI target extrema;
5. writes exact `<f8` node bytes, one exact `float.hex()` literal per node, ratio binary64/hex, node SHA256 and provenance;
6. MUST NOT import/build/run CLASS, read any observational artifact, read any JO v0.4 tail payload, or evaluate any physical response.

Only the first successful production grid-freeze artifact under this prereg may define V0.5 canonical nodes. A failed/invalid grid-freeze attempt creates no candidate authority; after a successful artifact exists no later generation may replace it.

After independent ZIP/payload/hash verification, the exact node payload must be committed durably and all later V0.5 response shards must load that payload rather than regenerating `np.geomspace` locally. Each shard must prove its loaded node SHA equals the canonical authority SHA before CLASS construction.

## V0.5 response recovery

All eight response shards MUST be recomputed under the canonical payload; no V0.4 response shard may be reused, even if its historical `node_sha256` happens to match the new canonical payload. This prevents post-hoc selection/reuse.

Execution topology and algebra remain exactly V0.4:
- phases: `slot20_after_history`, `slot20_fresh_tail`;
- models: reference, alpha-minus, beta-plus, beta-minus;
- after-history performs frozen `pre_z` evaluation then frozen `tail_z` evaluation on the same model instance;
- fresh-tail performs only frozen `tail_z` evaluation;
- each model receipt emits four exact little-endian float64 tail interpolants and immutable provenance;
- aggregate requires exactly eight unique receipts, one common canonical node SHA, exact phase/model identities and payload hashes;
- reconstruct alpha and beta response columns exactly by the frozen JJ/V0.4 algebra;
- require exact `np.array_equal`, identical finite masks and identical positive masks between reconstructed after-history and fresh-tail response arrays.

Only after all provenance guards pass may exact history equality be interpreted. A valid exact inequality is a valid JO support-only negative. Missing/mismatched provenance is `INVALID_INFRA_PLUS_0_PLUS_0`, never a scientific/history result.

## Authority ceiling and downstream rule

PASS remains support-only `+0/+0`; it creates no scientific model authority, no covariance authority and does not open Wm_S3. Only an independently verified V0.5 aggregate exact PASS may unlock exactly one checkpointed JL recovery with unchanged science-source/topology guards. JL CONVERGED may activate only its predeclared scientific Layer-B successor; JL NOT_CONVERGED may activate only the next sequential refinement; infrastructure invalidity activates neither.

Readiness telemetry is management-only: V0.5 process repair by itself does not increase Article III or funnel readiness percentages.