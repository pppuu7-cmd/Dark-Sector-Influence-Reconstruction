# Exp073JR — Article III fine-4097 model-operand exact-equivalence v0.2

Date frozen: 2026-09-11. Scope: DSIR Article III process/support only. Effect `+0/+0`.

Status: PROSPECTIVELY FROZEN AFTER independently verified coarse-2049 JR v0.1 exact PASS and AFTER the fine-4097 JR v0.1 job was externally shut down before producing any numerical receipt. Frozen BEFORE any v0.2 numerical output.

## Bound history

Exp073JR v0.1 run `34533562950` proved the coarse lattice exact: coarse job `103059792169`, artifact `10174738651`, independently verified ZIP SHA256 `22f88a9559ace2bf2701c22c93595851ae1112362ffea0f80b18465e804f1b91`, result JSON SHA256 `f7e9e6eabbc7bb7668c313962fb0ecf0db048ebf51d94a09ca2662b57bdbd5f5`. Durable partial receipt: `docs/dsir4/authority/EXP073JR_COARSE_2049_SEQUENTIAL_EXACT_EQUIVALENCE_RECEIPT_V0_1.json`.

The fine v0.1 job `103059792478` passed identity/stack/build checks, entered the exact preflight at `2026-09-10T21:42:32Z`, then at `21:48:05Z` the hosted runner received a shutdown signal. No equality verdict or numerical result artifact existed. The aggregate therefore correctly classified v0.1 `INVALID_INFRA_PLUS_0_PLUS_0`; no scientific/numerical negative was created.

`docs/dsir4/methods/LAYERB_JR_MODEL_OPERAND_EQUIVALENCE_DECOMPOSITION_V0_1.md` was frozen response-blind and proves that exact equality of all four model target-vector operands between the original four-live context and single-live context implies exact equality of the final response produced by the unchanged NumPy formula.

## Frozen science/process identities

- fine lattice: base N=4096 plus exactly one upper guard = 4097 requested nodes;
- same guarded-lattice construction from Exp073JJ/JL;
- pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`;
- `_MAX_NUMBER_OF_K_FILES_=4608`, `_ARGUMENT_LENGTH_MAX_=131072` infrastructure capacities only;
- native `k_per_decade_for_pk=20`;
- finite-difference model roles exactly and in this order: reference `(0,0)`, alpha-minus `(-1e-4,0)`, beta-plus `(0,+1e-4)`, beta-minus `(0,-1e-4)`;
- `h=1e-4`; `REL_TOL=1e-3` retained only as lineage metadata and not used in the exact-equivalence decision;
- centered-cubic interpolation in `ln(k)` using unchanged requested-node recovery and stencil `{j-2,j-1,j,j+1}`;
- requested-node coordinate mismatch ceiling `1e-12`;
- frozen requests exactly JR v0.1 A and B, in order A then B:
  - A: `z=float.fromhex('0x1.3851eb851eb85p-1')`, targets `[0.0013,0.0047,0.013,0.041]`;
  - B: `z=float.fromhex('0x1.1c28f5c28f5c3p+0')`, targets `[0.0019,0.0073,0.021,0.057]`.
- OMP/OpenBLAS/MKL/NUMEXPR threads fixed to 1.

## Resource-safe exact control

Run four independent hosted jobs, one per frozen model role. Each job performs exactly:

1. Build the 4097-node lattice and verify exact identity/count/guards.
2. Construct **all four CLASS instances** in the original fixed model order, retaining all four live as in the original response-engine context.
3. After all four instances are live, query only the matrix-selected model at request A then request B using the exact requested-node recovery and centered-cubic interpolation. Serialize each selected target vector as contiguous `<f8`.
4. Destroy all four reference-context instances.
5. Construct only the same selected model as one live candidate instance; query A then B identically and serialize as contiguous `<f8`; destroy it.
6. Compare selected reference-context vs single-live target vectors exactly.

Thus each job uses five CLASS constructions rather than the eight used by v0.1 while preserving the actual four-live coexistence context for the selected reference operand.

## Per-model decision

A model receipt is `FINE4097_MODEL_OPERAND_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0` only if for both A and B:

- node identity/count and provenance are correct;
- unsupported target count is zero;
- maximum requested-node coordinate mismatch <= `1e-12` in both contexts;
- finite masks are exactly equal;
- positive masks are exactly equal;
- `np.array_equal(reference_context_vector, single_live_vector)` is true;
- contiguous `<f8` payload SHA256 values are identical.

Any valid numerical inequality is `FINE4097_MODEL_OPERAND_NOT_EXACT_PLUS_0_PLUS_0`. Identity/build/grid/parser/provenance/runtime failure without a valid numerical receipt is `INVALID_INFRA_PLUS_0_PLUS_0`. No tolerance, ULP allowance, rounding, averaging or majority vote is permitted.

## Aggregate / combined JR decision

Aggregate requires the durable independently verified coarse v0.1 PASS receipt and four valid v0.2 fine model receipts with the exact same frozen identities.

- 4/4 fine model PASS -> by the frozen operand-equivalence decomposition, combined classification `SAME_RUN_SEQUENTIAL_RESPONSE_ENGINE_EXACT_EQUIVALENCE_PASS_PLUS_0_PLUS_0` for both 2049 and 4097 lattices.
- any valid fine model NOT_EXACT -> combined `SAME_RUN_SEQUENTIAL_RESPONSE_ENGINE_NOT_EXACT_PLUS_0_PLUS_0`.
- any missing/invalid fine receipt -> combined `INVALID_INFRA_PLUS_0_PLUS_0`.

No raw operands from different jobs are combined to form a scientific response. Aggregate uses only exact per-model equality verdicts/hashes plus the already independently verified coarse receipt.

## Interpretation ceiling

Combined exact PASS permits only prospective registration of a full fixed-chunk same-run execution of the unchanged Exp073JL 2049->4097 convergence gate under the frozen atomic topology and associative-reduction rules. It does not itself create Layer-B science authority, authorize covariance restriction, open Wm_S3, or change readiness.

Combined NOT_EXACT forbids the sequential engine. Infrastructure failure permits only minimal infrastructure repair. Global frozen DSIR science boundaries remain unchanged.