# RECOVERY — Exp073ET formal FAIL; Exp073EU and EV PASS; Exp073EL v0.2 frozen while EN runs

Date: 2026-09-06

## Science authority unchanged
The authoritative `WW_S0_S0` science process remains Exp073EN run `33994398927`, self-hosted job `101382229273`, still `IN_PROGRESS` at the latest reconciliation. No partial numerical output was inspected. Therefore no `WW_S0_S0` authority exists yet and no Article-3 science readiness increase is permitted.

## Exp073ET v0.1 — immutable support FAIL, localized to cross-state serialization
Preregistration:
- `experiments/073et_ww_s0_s1_sequential_alm_spill_direct_lib_exact_v0_1_prereg.md`
- blob `6b6ebdfedd0930a7f450ea50d4334d883fb9ab49`.

Qualifier:
- `ci/exp073et_sequential_alm_spill_direct_lib_exact_v0_1.py`
- blob `d8054ac06a0037278feb84f59d231680738d7233`.

Run evidence:
- run/job `34001003402 / 101399741708`;
- activation head `7d06878f5c8ddad6c0c55e733654cfd3d103222b`;
- artifact `9979490098`;
- artifact ZIP SHA256 from Actions log `90fd16a4f38628f2bfe39dca09ff4f43b86d2077f4ee5ef731f5cb8276fcaa50`;
- token `FAIL_EXP073ET_WW_S0_S1_SEQUENTIAL_ALM_SPILL_DIRECT_LIB_EXACT_V0_1`;
- classification `SEQUENTIAL_ALM_SPILL_DIRECT_LIB_MISMATCH`, accounting `+0/+0`, no authority.

ET MUST remain FAIL because its frozen preregistration required exact equality between direct in-memory BPW and BPW after FITS write/read. Those two cross-state checks differed at `1.1102230246251565e-16`.

However, every low-memory arithmetic equivalence check before serialization passed exactly:
- ALM0 spill/reload: exact, SHA `52cacc8eb9268121ea99754ef4547ed2dc5117df5f4994c354da4a40e5908d1c`;
- ALM1 spill/reload: exact, SHA `07a9357a63c8d769e948eae0601461da92fda385c42659292f14019035a459bb`;
- ordered stock-vs-low mask PCL: exact, SHA `c608409b77a556e835010aff8bbc628e2cb9b29246585e3930d23a44b65565f6`;
- stock-vs-low full unbinned MCM: exact, SHA `e15ffc75b36a7b99e7e8531cedead73afa345c3da3ba94c367edce32973335a0`;
- stock-vs-low in-memory full BPW: exact, SHA `d1f7e792dda86c5346b37624f9440fc54eb0a1a3aa8e425a35445298e2e783ff`;
- stock-vs-low in-memory selected EE: exact, SHA `cf38f15970d3330c81e1ebbfc8935c5f49e6ef5f1933c4fbdd30afbdba19374c`.

The ET low-route fresh reload hashes were:
- full BPW `bf656c5f0493dc44d6c42b31b804f04f6893b7fc4895e92b99cefc356b10b884`;
- selected EE `336a0b57fe734a2f17a4a0844db1a18fc43887abf7556fb63009ee4a3de5f607`.
These exactly equal the older, independently frozen Exp073ER serialized-public hashes. Thus ET localized its failure to the already-known pre-serialization vs post-serialization NaMaster last-bit state difference, not to the sequential low-memory ALM/PCL/MCM route.

## Exp073EU — terminal state-matched exact support PASS
A new prospective qualifier was created after ET terminal failure but before EU execution; its expected serialized-public hashes were frozen from the older Exp073ER PASS, preventing post-hoc selection.

Preregistration:
- `experiments/073eu_ww_s0_s1_sequential_spill_serialized_public_bpw_exact_v0_1_prereg.md`;
- blob `be77fbb5e175775d5e5c0e1370fa4e0bee2ad2d6`.

Qualifier:
- `ci/exp073eu_sequential_spill_serialized_public_bpw_exact_v0_1.py`;
- blob `a6f149180551767e0317f0f57580ad588517870b`.

Run evidence:
- run/job `34001139228 / 101400097453`;
- activation head `c25b882ca459e7c27a1bddee74f464a234f2a333`;
- artifact `9979525491`;
- artifact ZIP SHA256 `5cd9ce3f668b135ee695d51b7dba3e80cfa332c925e71397b2a6e32041ff872c`;
- token `PASS_EXP073EU_WW_S0_S1_SEQUENTIAL_SPILL_SERIALIZED_PUBLIC_BPW_EXACT_V0_1`;
- classification `STATE_MATCHED_SERIALIZED_PUBLIC_BPW_EXACT`, accounting `+0/+0`, no authority.

Exact scored comparisons all passed with `numpy.array_equal=true`, canonical SHA equality and max absolute difference `0.0`:
1. ALM0 spill/reload;
2. ALM1 spill/reload;
3. stock-vs-low ordered mask PCL;
4. stock-vs-low in-memory MCM;
5. stock-vs-low in-memory full BPW;
6. stock-vs-low in-memory selected EE;
7. stock-reload-vs-low-reload MCM;
8. stock-reload-vs-low-reload full public BPW;
9. stock-reload-vs-low-reload selected EE.

Both stock and low fresh-reload hashes exactly matched the pre-existing Exp073ER expected serialized-public hashes:
- full `bf656c5f0493dc44d6c42b31b804f04f6893b7fc4895e92b99cefc356b10b884`;
- selected EE `336a0b57fe734a2f17a4a0844db1a18fc43887abf7556fb63009ee4a3de5f607`.

The known in-memory-vs-reload diagnostic difference remains `1.1102230246251565e-16` for both stock and low routes and was explicitly not scored. No tolerance was used anywhere.

Conclusion: the sequential source-mask -> exact ALM spill -> ordered `healpy.alm2cl` -> exact PyMaster-2.7 `nmtlib.comp_coupling_matrix` argument path is bitwise-equivalent to stock in the same numerical state and lands in exactly the same serialized-public state after reload.

## Exp073EV — terminal static disk-budget PASS
Preregistration:
- `experiments/073ev_ww_s0_s1_fullres_disk_budget_static_v0_1_prereg.md`;
- blob `0dbffbfa5fbf4cc7e8baff8a5c8affae1f020f8c`.

Calculator:
- `ci/exp073ev_fullres_disk_budget_static_v0_1.py`;
- blob `e4535b156eec3728c93c934d626c8a0658349538`.

Run evidence:
- run/job `34001215421 / 101400305564`;
- activation head `c0c06d6aa6c63157c000002f0d7a8d5905246dca`;
- artifact `9979535369`;
- artifact ZIP SHA256 `03fc1935292d17d30e236089a17e68e93cd209e3dbd96bb385b6d5bf03663247`;
- token `PASS_EXP073EV_WW_S0_S1_FULLRES_DISK_BUDGET_STATIC_V0_1`;
- classification `STATIC_RESOURCE_BUDGET_PASS`, accounting `+0/+0`.

Conservative staged model:
`2*MCM + 2*ALM + FULL_BPW + SELECTED`.

Exact values:
- one full MCM = `19,327,352,832` bytes = exactly 18 GiB;
- two ALM spills = `2,416,115,712` bytes;
- full BPW = `61,341,696` bytes;
- selected = `3,833,856` bytes;
- conservative peak = `41,135,996,928` bytes;
- 50-GiB floor = `53,687,091,200` bytes;
- residual margin = `12,551,094,272` bytes = `11.689117431640625 GiB`.

Therefore the EL 50-GiB floor still leaves >10 GiB extra margin even in the deliberately conservative case where two ALM spill files remain during MCM/FITS overlap. Preferred cleanup ordering increases the margin.

## Exp073EL v0.2 — prospective superseding resource contract
The never-activated v0.1 prereg remains immutable historical evidence. Because it required the now-impossible ET-v0.1 PASS token, a separate prospective v0.2 was created before EU terminal result:

`experiments/073el_ww_s0_s1_full_resolution_resource_path_v0_2_prereg.md`

Creation commit `dae08a9716b34f98c62083c171b7b7d55a960908`.

V0.2 requires:
- real Exp073EO PASS before activation;
- exact existing Article-3 source reconstruction `ci/exp073aa_article3_des_angular_task_runner_v0_1.py`, blob `050ed7dd3387c4fb031f877825e6b3f4d4ce3ef2`, specifically sequential calls to its `source_count_map(root, bin_index)` for S0 then S1;
- Exp073EM, EK, EP, ER and EU support PASS identities;
- sequential ALM spill and release before MCM construction;
- file-backed 18-GiB MCM construction and fresh serialized-public file-backed reload;
- 50-GiB free-disk floor;
- no competing heavy DSIR job;
- no tolerance or resolution/physics shortcuts.

Only a future `PASS_EXP073EL_WW_S0_S1_FULLRES_RESOURCE_PATH_V0_2` makes the later `WW_S0_S1` science A/B run executable. It does not itself score science.

## Current next support test
Exp073EW has been preregistered and activated hosted-only to test whether the ER-qualified v0.2 patch can serve as one unified PyMaster build for both construction and FITS-read, with independent mmap proof and exact state-matched stock comparison at both stages. This is an operational simplification only and remains `+0/+0`.
