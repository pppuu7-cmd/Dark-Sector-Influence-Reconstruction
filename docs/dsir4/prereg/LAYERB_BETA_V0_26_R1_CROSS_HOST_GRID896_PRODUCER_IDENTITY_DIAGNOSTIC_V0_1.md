# Layer-B beta V0.26 R1 — prospective response-blind cross-host GRID896 producer-identity diagnostic V0.1

Status: `PREREGISTERED_DESIGN_ONLY_EXECUTION_CLOSED`  
Date: 2026-09-17  
Scope: DSIR infrastructure/provenance only  
Effect at preregistration: `+0/+0`

## TARGET HYPOTHESIS

The frozen GRID896 byte object can be made host-invariant by replacing per-host floating-point/native-NumPy production with an arithmetic-free, content-addressed reconstruction from the already archived 897 exact IEEE-754 bit patterns. Across the future frozen hosted-runner sample, every admissible lane must reconstruct exactly the same 7176-byte payload with SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`. This is an infrastructure/provenance hypothesis only; it says nothing about Layer-B scientific response.

## DEPENDENCY AND AUTHORIZATION

This design is opened only by terminal implementation qualification `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SUCCESSOR_SENTINEL_V0_2_TERMINAL_IMPLEMENTATION_QUALIFICATION_V0_1.json`, Git blob `fddc6e08d0bdedcb468a18f749e862ae7c813e38`, verdict `INVALID_IMPLEMENTATION`, classification `SUCCESSOR_SENTINEL_V0_2_PER_LANE_NATIVE_GRID896_MATERIALIZATION_NOT_HOST_INVARIANT`, and `authorized_next_stage=AUTHOR_PROSPECTIVE_RESPONSE_BLIND_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_DESIGN_ONLY`.

The latest independent Auditor handoff is `docs/dsir4/handoffs/DSIR_FUNNEL_AUDITOR_HANDOFF_V0_26_R1_SUCCESSOR_SENTINEL_V0_2_TERMINAL_IMPLEMENTATION_V0_1.md`, Git blob `b7994a77cb463c316092ddd7c40e5c63a191a691`, verdict `INVALID_IMPLEMENTATION`.

No diagnostic execution, successor sentinel science, full 107-row replay, or downstream science is authorized by this preregistration.

## EXACT OBJECT

Primary object: the exact frozen GRID896 node payload, not a scientific response and not a surrogate response metric.

Canonical source representation is `docs/dsir4/canonical/LAYERB_BETA_V0_26_R1_GRID896_U64HEX_V0_1.txt`, Git blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6`.

The file must contain exactly 897 lowercase 16-hex-digit unsigned 64-bit words, one per line, in frozen node order, with a final newline. Its exact file SHA256 is `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`.

Canonical binaryization is frozen as: for each line in order, parse the 16 hexadecimal digits as an unsigned 64-bit integer and emit exactly eight bytes in little-endian order (`<Q` semantics); concatenate all 897 outputs. Floating-point arithmetic, `logspace`, `exp`, `log`, geometric-lattice regeneration, NumPy grid generation, and platform-native transcendental computation are forbidden in the canonical producer.

Expected canonical byte length is exactly 7176 and expected SHA256 is exactly `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`.

## FROZEN INPUT ORIGIN AND PROVENANCE

The exact bit patterns predate the v0.2 terminal failure and come from response-blind V0.26 R1 static-identity run `34954905127`, job `104334496210`, artifact `10390997654` (`layerb-beta-v026-r1-static-identity-v0-1`). Frozen artifact ZIP SHA256: `5cd19512bef3d9795957fb8105361e4006123ae59794bc94e2e5ded5722436ff`. Inner `v026_r1_static_identity.json` SHA256: `3a9d8375119068063ddcb4ac37d8f3da92444261b0fad356a228ccaedf6292d7`. Inner hash receipt SHA256: `5c6187a03db04888c4e3bd4f6f98befc1d67ae45a0c362fdbb320fe5dcf70f32`.

R1 science contract remains Git blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`; R1 preregistration remains Git blob `545e5be589e0f8029d23db2edb4e2faad116c3a0`. The contract already freezes the same GRID896 payload SHA256, byte length, node count, u64hex-lines SHA256, and node ordering. No science threshold or response object changes here.

## FUTURE DIAGNOSTIC POPULATION

If and only if a later independent pre-execution audit and separate execution authority permit one run, the diagnostic population is prospectively fixed at 32 independent `ubuntu-24.04` GitHub-hosted jobs, labels `R01` through `R32`, with no post-hoc lane selection or replacement. One launch, run attempt 1 only. Missing/failed lanes remain missing/failed and may not be rerun or substituted within the experiment identity.

The implementation/runtime fingerprints must be recorded for provenance, but CPU feature class, hosted-runner identity, native NumPy dispatch class, or timing may not be used to select lanes or alter PASS/FAIL after execution.

## REQUIRED FUTURE LANE OPERATIONS

Each lane, before any CLASS import or science response access, must:

1. bind the exact preregistration, machine contract, canonical u64hex Git blob, and future audited executor/workflow identities;
2. verify canonical source line count = 897 and source SHA256 = `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`;
3. reconstruct bytes only by unsigned-64 hex parse plus little-endian packing;
4. verify byte length = 7176 and SHA256 = `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`;
5. perform a consumer round-trip: interpret the exact bytes as contiguous little-endian IEEE-754 binary64 without arithmetic, immediately reserialize to contiguous little-endian binary64, and require byte-for-byte identity and the same SHA256;
6. run the frozen negative control described below and require the exact-hash guard to reject it;
7. emit a response-blind receipt containing source, output, round-trip, negative-control, runtime-fingerprint, code/workflow, run/job/attempt, and artifact hashes.

A descriptive native-generator control may be included only if prospectively implemented and independently audited before execution. It is non-gating for the canonical shared-payload PASS. If included, its exact native hash must be reported without reading any CLASS/scientific response. A mismatch to the frozen hash classifies the native producer as not host-invariant on that lane; 32/32 matches would only mean variance was not observed in this sample, never proof of global invariance.

## POSITIVE CONTROL

The canonical source itself is the positive control: the exact 897 u64 words must reconstruct the already frozen 7176-byte payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d` on every admissible lane.

## NEGATIVE CONTROL

Before execution, the implementation must hard-code this exact corruption: copy the canonical byte payload, flip bit 0 of byte offset 0 (`corrupted[0] ^= 0x01`), and pass the corrupted copy through the same exact length/hash acceptance guard. The guard must reject it because its SHA256 differs from the frozen canonical hash. No alternative corruption may be substituted post hoc.

## PASS

`PASS_SHARED_GRID896_CONTENT_ADDRESSING_CROSS_HOST` requires all of the following in the single authorized future run: exactly 32 unique lane receipts `R01..R32`; every lane binds the same frozen canonical source and audited code/workflow identities; every lane validates source count/hash; every lane reconstructs exactly 7176 bytes with canonical SHA256 `8499...`; every consumer round-trip is byte-identical with the same SHA256; every frozen negative control is rejected; all receipts/artifacts and inner hashes are present and bind run #1 / attempt #1; no prohibited science object is read or computed.

PASS is infrastructure/provenance only. PASS does not authorize a successor sentinel science run. A separate terminal authority and then a separately prospectively frozen launch authority would still be required.

## FAIL

`FAIL_SHARED_GRID896_CONTENT_ADDRESSING_CROSS_HOST` if at least one otherwise valid completed lane, with correct canonical source hash and correct audited implementation identity, reconstructs a different canonical payload hash/length, fails exact consumer byte round-trip, or accepts the frozen negative-control corruption. This is an implementation/serialization/endianness failure only.

## BLOCKED / INVALID

`BLOCKED_MISSING_OR_UNBOUND_CANONICAL_OBJECT` if the canonical u64hex source or required binding is absent/unverifiable before execution.

`INVALID_DIAGNOSTIC_PROVENANCE` if the run is duplicated/rerun, attempt != 1, lanes are selected/replaced post hoc, exact audited code/workflow identities differ, artifacts/inner hashes are incomplete, or any CLASS/scientific response/covariance/whitening/nuisance/relation-null/Wm_S3/global-65537 object is accessed.

`BLOCKED_HOSTED_INFRASTRUCTURE_INCOMPLETE` if fewer than 32 lane receipts are available for infrastructure reasons without an implementation-level FAIL predicate being established. No same-identity retry is automatically authorized.

## INTERPRETATION CEILING

Maximum interpretation: exact producer/content-addressing infrastructure and provenance for the frozen GRID896 bytes across the sampled hosted-runner population. Numerical reproducibility of Layer-B responses, exact-vs-direct science criterion, statistical/model validity, nuisance identifiability, and physical dark-sector inference remain `NOT_EVALUATED`.

## FORBIDDEN

Forbidden under this design: CLASS solve; reading or computing scientific response values; reading the response-blind plan beyond identity if not needed for binding; changing 897-word source; changing packing endianness; regenerating canonical payload via floating arithmetic; changing corruption control after outcome; filtering/replacing lanes; rerun selection; threshold tuning; successor sentinel science; full 107 rows; covariance; whitening; nuisance marginalization; relation-null; `Wm_S3`; global 65537; any physical inference.

## NEXT STAGE AFTER THIS PREREGISTRATION

`INDEPENDENT_PREEXECUTION_AUDIT_OF_FROZEN_CROSS_HOST_GRID896_PRODUCER_IDENTITY_DIAGNOSTIC_DESIGN_ONLY`.

That audit must verify exact canonical input provenance, blob/hash equivalence, decision logic, source/code boundaries, and no-science guards. Only a later separate terminal audit authority may authorize construction/launch of one diagnostic execution. Scientific effect remains `+0/+0`.
