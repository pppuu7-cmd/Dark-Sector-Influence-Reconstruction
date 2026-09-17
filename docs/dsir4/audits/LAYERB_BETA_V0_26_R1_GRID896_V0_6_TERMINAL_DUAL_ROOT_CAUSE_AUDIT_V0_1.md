# Layer-B beta v0.26 R1 GRID896 V0.6 terminal dual-root-cause audit v0.1

Date: 2026-09-17  
Effect: `+0/+0`  
Scope: infrastructure/provenance only. No CLASS response, covariance, statistical/model validity, or physical dark-sector inference is evaluated here.

## Terminal object

The one-shot canonical V0.6 diagnostic is run `35251121404`, run number `1`, attempt `1`, head `c6526f940a559140eaa7928d97164524e462cecf`, workflow ID `360576929`, exact canonical workflow path `.github/workflows/layerb-beta-v026-r1-cross-host-grid896-producer-identity-diagnostic-v0-6.yml`.

The run is historical and closed. It MUST NOT be rerun. GitHub's wrapper conclusion is `failure`; the frozen diagnostic decision is `INVALID_DIAGNOSTIC_PROVENANCE`.

Decision artifact `10510805424` (`grid896-cross-host-decision-v0-6`) has outer SHA256 `fe664cd5ef1c5adf959d40f7c179550074b380ccd0c3805dc361661bf97bc574`. Independent download reproduced this digest. Its sole `decision.json` member has SHA256 `e57bcb39736bf80dac16900cb124ec66429e00bc1e20c31df0b05ea5f2a86325` and records `HTTPError: HTTP Error 415: Unsupported Media Type`. It also records 32 lane artifacts, no missing lane IDs, but no accepted artifact provenance because aggregation failed during artifact retrieval.

## Root cause A — canonical source serialization binding

The frozen semantic canonical source was derived from 897 lowercase 16-hex IEEE-754 words. The pre-existing static identity probe defined the line serialization hash using `("\n".join(words) + "\n").encode("ascii")`, yielding SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`.

The committed canonical file has Git blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6` and the same 897 words, but it does not end in a final LF. Reconstructing the two serializations gives:

- actual raw repository file: 15248 bytes, no final LF, SHA256 `e9b5a3093223f13291993ea4339398cc5274c0047540740dd73978529c2689a0`;
- normalized semantic line serialization with exactly one final LF: 15249 bytes, SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`.

V0.6 `canonical_source_and_payload()` applies the normalized `e4f8...` digest directly to `Path.read_bytes()` and separately requires raw bytes to end in LF. Therefore the V0.6 lane cannot reach payload reconstruction for the actual committed canonical object even though the Git blob and 897 semantic tokens are the intended frozen object.

This is a confirmed one-byte raw-vs-normalized serialization binding defect. It is not evidence of a host-dependent payload mismatch and it is not a scientific result.

Independent lane artifacts confirm the defect on different hosted runners:

- R01 artifact `10508904186`, GitHub digest `sha256:b8897d2b5ff336be7f472bca740f1bc4b82e301b7b6ca0381127627a71050ffd`;
- R03 artifact `10509692685`, GitHub digest `sha256:9ddc2e41d3cd2f351aed65fea8ec5ccaff5668074a2d543e925087d8932b4b26`;
- R17 artifact `10509529109`, GitHub digest `sha256:1180a473d2e68a99cf6ba833a4e69bfe297a36e6c8f19e5725c652ee4a1cd86d`.

All three independently extracted receipts report `BLOCKED_MISSING_OR_UNBOUND_CANONICAL_OBJECT` with `RuntimeError: canonical source SHA256 mismatch`; all keep `class_solver_invoked=false` and `scientific_response_read=false`.

## Root cause B — decision artifact-download transport

V0.6 aggregation enumerated all 32 lane artifacts successfully. When retrieving each artifact ZIP it calls `/actions/artifacts/{artifact_id}/zip` using `Accept: application/octet-stream`. The aggregate terminated with HTTP 415 before any lane artifact could enter `artifact_provenance`.

Current GitHub REST documentation for the GitHub Actions `Download an artifact` endpoint documents a `302` response and recommends `Accept: application/vnd.github+json`. The observed V0.6 call uses a different media type. Therefore the transport defect is localized to the frozen artifact-download request path/media-type behavior. The causal ceiling is deliberately narrow: HTTP 415 is observed; the frozen media type differs from the current documented recommendation; a repaired request must be prospectively qualified before any new diagnostic execution.

This transport defect is distinct from root cause A. Even if root cause A were absent, the V0.6 aggregate could not validate artifact provenance under the observed request behavior. Conversely, fixing only the aggregate downloader would not make the V0.6 lanes valid because they stop earlier on the canonical-source serialization binding.

## Admissible successor repair

V0.6 is immutable and must not be patched or rerun. Any execution successor must have a new experiment/implementation identity, designated V0.7 or later.

The narrow admissible V0.7 implementation change set is:

1. Preserve canonical Git blob `24fa61685ab45e42e3ab0d453f5cb223c247ced6` as the repository-object identity.
2. Bind raw file bytes separately to SHA256 `e9b5a3093223f13291993ea4339398cc5274c0047540740dd73978529c2689a0` and 15248 bytes.
3. Parse semantic tokens without requiring a raw final LF, require exactly 897 lowercase 16-hex words, and separately reproduce the normalized semantic serialization SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`.
4. Keep the packed little-endian payload object unchanged: 7176 bytes, SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`.
5. Keep the one-bit negative-control digest unchanged: `e94e2e05fc0cc1fcbc9bd710a24b8ef231fab350cd6247ea3039b913adfba800`.
6. Repair only the Actions artifact-download transport to a prospectively qualified request compatible with the current documented endpoint behavior; preserve digest verification against GitHub's artifact `digest` field.
7. Keep 32 frozen lanes, exact receipt/job/run/head bindings, PASS/FAIL/BLOCKED/INVALID classifier semantics, consumer roundtrip, and response-blind scope unchanged.
8. CLASS, scientific response, covariance, nuisance, whitening, relation-null, `Wm_S3`, global65537, successor sentinel science, full107, and downstream science remain forbidden.

Before V0.7 promotion or execution, its exact bytes must pass independent static review and a response-blind qualification that exercises both repaired source parsing and repaired artifact retrieval against pre-existing non-scientific evidence. No V0.7 launch authority is created by this audit.
