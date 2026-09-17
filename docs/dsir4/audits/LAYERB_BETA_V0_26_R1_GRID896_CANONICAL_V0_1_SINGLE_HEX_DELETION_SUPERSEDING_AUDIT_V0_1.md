# Layer-B beta v0.26 R1 GRID896 canonical V0.1 single-hex-deletion superseding audit v0.1

Date: 2026-09-17  
Effect: `+0/+0`  
Scope: infrastructure/provenance only.

## Superseded interpretation

The historical audit `docs/dsir4/audits/LAYERB_BETA_V0_26_R1_GRID896_V0_6_TERMINAL_DUAL_ROOT_CAUSE_AUDIT_V0_1.md` (blob `43045a929e5cfb87aaa32c3158fc8839ede88df5`) correctly preserved the V0.6 terminal classification `INVALID_DIAGNOSTIC_PROVENANCE` and correctly localized the independent aggregate HTTP-415 transport defect. Its source-root-cause interpretation that the committed canonical file lacked a final LF is **superseded by stronger byte-level evidence**. The historical file is not rewritten; this audit records the correction explicitly.

## Definitive hosted byte capture

One-shot provenance capture run `35253892736`, run #1 / attempt #1, head `aaf6b44dd46b32010256bb0690a8b07f8ae104a3`, workflow ID `360739640`, completed success. Artifact `10511577132` has outer SHA256 `55268b6f8302b269583e6546d61a8504c82bc644ed04d8ddb87765fd6122cf24`; its sole result member has SHA256 `2d6d5d5cd5fc0cefc5f9ab53b64379a4a1e722638188d5734f3e6c051ccca9c7`.

The capture measured three independent repository byte paths on the Ubuntu hosted checkout:

- Python working-tree `read_bytes()`;
- `git show HEAD:<canonical_path>`;
- `git cat-file blob 24fa61685ab45e42e3ab0d453f5cb223c247ced6`.

All three were byte-identical. `git hash-object` of the working-tree file was exactly `24fa61685ab45e42e3ab0d453f5cb223c247ced6`. No `.gitattributes`, `core.autocrlf`, or `core.eol` transformation was observed.

Exact V0.1 byte metrics:

- byte length: `15248`;
- SHA256: `f84d6fa7cf9e5b8014176fd480062b27aaf97947d4a5211c7fbb5c69f93634ba`;
- final LF: **present**;
- LF byte count: `897`;
- CRLF pairs: `0`;
- split-line count: `897`;
- all lines lowercase 16-hex: **false**.

Therefore the V0.6 source SHA mismatch was not caused by checkout transformation or missing final LF.

## Exact comparison with pre-existing origin

The pre-v0.2 static identity origin is run `34954905127`, artifact `10390997654`. Its archived `v026_r1_static_identity.json` contains the frozen `grid896.node_u64hex` sequence before any V0.6/V0.7 outcome was known.

Re-serializing those 897 archived words as `"\n".join(words) + "\n"` gives:

- 897 lowercase 16-hex words;
- byte length `15249`;
- SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`;
- Git blob SHA1 `ded43b233a71a631809111514c9dd35d0419af2d`;
- packed little-endian payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`.

The committed V0.1 canonical object is obtained from that exact pre-existing origin serialization by deleting **one ASCII byte `e`**:

- zero-based byte offset: `13182`;
- line: `776` (1-based);
- column: `8` (1-based within the intended 16-hex token);
- origin/correct token: `3f9c8a9eeea3c9c8`;
- committed malformed token: `3f9c8a9eea3c9c8`.

Applying only that single-byte deletion to the origin bytes yields exactly:

- byte length `15248`;
- SHA256 `f84d6fa7cf9e5b8014176fd480062b27aaf97947d4a5211c7fbb5c69f93634ba`;
- Git blob SHA1 `24fa61685ab45e42e3ab0d453f5cb223c247ced6`.

This is an exact content-addressed reconstruction, not a similarity inference.

## Corrected root-cause classification

`CANONICAL_V0_1_SINGLE_HEX_DELETION_CONFIRMED_AND_PRIOR_FINAL_LF_INTERPRETATION_SUPERSEDED`.

V0.6's canonical source guard correctly rejected the malformed committed V0.1 object before payload reconstruction. Therefore the V0.6 lane-side blocker is a frozen-object publication/canonicalization defect, not a defect in the guard and not evidence of host-specific content-addressed reconstruction failure.

The V0.6 aggregate HTTP 415 remains a separate independently observed transport defect and is **not** superseded by this audit.

## Consequences for successor identity

- V0.6 remains historical `INVALID_DIAGNOSTIC_PROVENANCE`; no rerun.
- First V0.7 static qualification run `35253515074` remains historical `INVALID_STATIC_QUALIFICATION`; no rerun. Its raw-SHA premise was based on the now-superseded final-LF interpretation.
- The V0.7 implementation identity is closed and must not be silently mutated.
- Any successor must use a new identity, V0.8 or later.
- The corrupt V0.1 canonical Git object must remain immutable as historical evidence.
- A successor may reconstruct a corrected canonical V0.2 object only from the pre-existing origin plus the exact one-byte repair, and must bind its expected SHA256/Git blob before execution.
- The corrected semantic object must have Git blob `ded43b233a71a631809111514c9dd35d0419af2d`, byte length `15249`, SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`, 897 valid lowercase 16-hex words, and payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`.
- The separate artifact-download transport repair still requires response-blind runtime qualification before any new 32-lane diagnostic execution.

No V0.8 promotion/execution, successor sentinel science, full107, or downstream science is authorized by this audit.
