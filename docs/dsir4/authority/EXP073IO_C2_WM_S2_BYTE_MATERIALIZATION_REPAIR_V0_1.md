# Exp073IO — C2 Wm_S2 exact byte-materialization repair v0.1

Date frozen: 2026-09-10. Scope: DSIR Article 3 / Exp073IM transport only.

Status: PROSPECTIVE IMPLEMENTATION-REPAIR PROTOCOL AFTER AN INVALID-FOR-SCIENCE TRANSPORT RUN AND BEFORE ANY VALID EXP073IM RADIAL OUTPUT.

## 1. Trigger and scientific boundary

Exp073IM v0.2 run `34413917978`, job `102674368422`, successfully downloaded and SHA256-verified every frozen GitHub artifact ZIP, then stopped before any radial scientific classification because the executor could not find the canonical Wm_S2 logical array inside artifact `9853165664`.

The run emitted `INVALID_FOR_SCIENCE_EXP073IM`, not a scientific radial FAIL. No physical-support fraction, covariance, nuisance, relation/null or downstream result was evaluated.

Inspection establishes that artifact `9853165664` is the Exp073CI finalizer *receipt* (758-byte JSON payload), containing the already-frozen expected `W` SHA but not the 39x12288 `W` byte array itself. The earlier Exp073IM materialization audit therefore over-described that receipt as a directly machine-consumable Wm_S2 array carrier.

This protocol repairs only byte materialization. It does not change Wm_S2 authority, algorithm, numerical target, radial criterion, physical-support threshold, or any downstream gate.

## 2. Existing authority remains unchanged

The admitted Article-3 authority remains the previously frozen composite:

`Exp073CF compact exact PASS -> Exp073CI v0.2 deterministic fixed-Nehalem exact finalizer PASS`.

Frozen logical identities remain exactly:

- compact `A`: canonical `<f8 [39,12288]`, SHA256 `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`;
- `K = k_from_a(A)`: canonical SHA256 `c24456b19e7248cc7ad68502fc78d6f75b885665641d662b1d9c789cf473f795`;
- final `W = np.linalg.solve(K,A)`: canonical `<f8 [39,12288]`, SHA256 `96248e7699a5a12945854db2c9af150affcfe13f4f9dc0bfcbb87b99f92ff087`;
- no tolerance, ULP, rounding, averaging or preferred-numerical-result rescue.

The Exp073CI authority receipt remains artifact `9853165664`, digest `sha256:fcfccb6768948ffe34d28e9ed32da64d3b1d071704028fe6f312c1ab8b440f57`.

## 3. Exact compact byte source

The historical Exp073CF comparator downloaded two immutable compact-array lanes and proved them exactly array-equal and SHA-equal before Exp073CI existed.

For byte materialization only, select lane A by a prospective non-numerical rule: **fixed lexical lane order A before B**. No downstream value is consulted.

Bind exactly:

- source run `33601943300`;
- lane-A artifact ID `9841348367`;
- artifact ZIP digest `sha256:d6703819745b22eadc9c6557c4d89d926ed9675c09bd41cb19e79d4050ef399b`;
- NPZ logical array key `A`;
- required canonical array identity `963dfd79bd49119d2c3124de3507330b3c47637b41dcbd7b9536f617186ef7bd`.

Lane B (`9848067175`, digest `sha256:7e655144c07959f4ba7c6c6d82db0685b58e425958fa308e6b9e698ad6e30737`) remains a preserved exact replica and is not selected based on a numerical result.

## 4. Exact reconstruction environment

Materialize Wm_S2 using the already-frozen Exp073CI v0.2 finalizer semantics only:

- Python 3.11 hosted Linux route;
- NumPy exactly `2.1.3`;
- `OPENBLAS_CORETYPE=Nehalem`;
- `OPENBLAS_NUM_THREADS=1`;
- `OMP_NUM_THREADS=1`;
- `MKL_NUM_THREADS=1`;
- `NUMEXPR_NUM_THREADS=1`;
- `BLIS_NUM_THREADS=1`;
- `OMP_DYNAMIC=FALSE`;
- exact `k_from_a` algebra and band edges inherited from `ci/exp073az_article3_low_memory_general_coupling_v0_1.py`;
- exact `W=np.linalg.solve(K,A)`;
- canonical little-endian float64 before hashing.

The materializer must verify all three frozen logical SHA values (`A`, `K`, `W`) and must fail closed if any differs.

## 5. Durable byte object

On exact success the repair workflow may serialize the already-authoritative logical `W` as a transport file (`.npy` or raw little-endian float64) and upload it as a new *materialization carrier*.

This new carrier does not create a new Wm_S2 scientific authority. Its admissibility is conditional on exact equality to the pre-existing Exp073CI W SHA. The new artifact ID/digest and internal canonical W SHA must be recorded before the next Exp073IM real execution consumes it.

## 6. Invalid-run preservation

Run `34413917978` remains permanently recorded as:

`INVALID_FOR_SCIENCE_EXP073IM__WM_S2_RECEIPT_NOT_BYTE_CARRIER`.

It is not reclassified and earns no Article-3 gate credit.

## 7. Downstream firewall

This repair may not read or evaluate:

- radial support classification;
- physical-support domain or 5% thresholds;
- covariance/whitening;
- nuisance/SVD/rank;
- relation/null;
- G7/G8 or article selection.

Only after a new carrier is produced with exact pre-existing W SHA may Exp073IM be rerun under the already-frozen v0.2 radial criteria.