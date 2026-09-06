# DSIR immutable recovery — Exp073FF admitted WW_S0_S2

Date: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Exp073FA terminal candidate
Exp073FA producer run `34020756634`, hosted envelope job `101452788638`, home science job `101452805620`, head `894885b2c2b811954d1724c2733d2a810a486d70` is terminal SUCCESS. Raw candidate artifact `9988291781` (`exp073fa-ww-s0-s2-filebacked-ab-v0-1`) has GitHub digest and independently recomputed downloaded-ZIP SHA256 `70fd7e9ff320ba0dee9d0036c9777963b530ef605919c964484ea6cc3cb841a6`.

The compact artifact independently validates both complete six-stage checkpoint chains under namespaces `checkpoints/exp073fa-ww-s0-s2-a-v0-1` and `checkpoints/exp073fa-ww-s0-s2-b-v0-1`; frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; ordered pair `S0->S2`, indices `[0,2]`; distinct-field handoff; exact file-backed MCM `19327352832` bytes with `/proc/self/maps` proof; serialized `read_from(..., read_unbinned_MCM=True)` followed by public `get_bandpower_windows()`; full BPW SHA256 `bb8d3c2c647ca62b341008acfa4f523b0af1c66a3779baafc9ffa26ee3c83a89`; workspace FITS SHA256 `74831fe9aa7d7d85c2d91f5e9c0fc53e3c2ae9d5709f866034b8825b010005a4`; canonical selected `<f8 [39,12288]` `EE<-EE` A/B SHA256 `f7c02a13e746008c7b2099c2900787fb58ff39c2cc4cb0903ef11cb32fc9f07e`; `numpy.array_equal=true`, all finite, no tolerance rescue. Candidate token is `PASS_EXP073FA_WW_S0_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`, classification `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION`; candidate alone created no authority.

Exp073FF base prereg blob `c6f1fd11c4a0dc68bb17669a58854979fe84869e`; terminal-binding erratum blob `eb67fd9506f82b315edc178c4e456c5d4a4560e4`, creation commit `d30235175a477db9969a220e66d940eab8ed05bb`.

## Exp073FF infrastructure history
First activation run `34032269670` failed before creating a job because Python heredoc text was not indented inside the YAML block scalar. Classification: `INFRASTRUCTURE_YAML_TRANSPORT_FAIL +0/+0`; no science was evaluated. Minimal repair changed only YAML indentation, commit `f41e37522a73e694fba2ce84e70e5446f90924df`.

Second run `34032324879 / 101484002796` passed repository identity freeze but failed in support-log transport because `grep -Fqx` incorrectly required an unprefixed whole line while GitHub decoded job logs carry timestamps. Classification: `INFRASTRUCTURE_LOG_FORMAT_TRANSPORT_FAIL +0/+0`; no candidate admission step ran. Minimal repair changed only literal token search to timestamp-safe substring matching, commit `b7f2ec628560678982ac083c110a004f5b91587d`.

## Exp073FF scientific authority
Repaired Exp073FF run/job `34032384956 / 101484177968`, head `b7f2ec628560678982ac083c110a004f5b91587d`, completed SUCCESS. Raw job log independently contains:
- `PASS_EXP073FF_WW_S0_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`
- `classification=SCIENTIFIC_AUTHORITY_ADMITTED`
- `science_gate_scored=true`
- `ww_s0_s2_authority_created=true`

The hosted gate downloaded the exact Exp073FA artifact itself, rechecked metadata and ZIP SHA256, prior Exp073EZ/FC/FE support tokens, frozen repository blobs, both six-stage chains, exact selected binary SHA/shape/dtype/finiteness, exact A/B array equality, distinct S0/S2 source/field provenance, file-backed public-BPW receipts and post-receipt pruning evidence. Therefore `WW_S0_S2` is now admitted scientific authority.

Preserve all prior admitted authority and all historical negative/infrastructure results. No frozen global science boundary changed.

## Next frontier
Live Actions must be reconciled before dispatch. With `WW_S0_S2` admitted, the next ordered S0-row source pair permitted by authoritative R1's four source bins is `WW_S0_S3` (indices `[0,3]`), subject to its own prospective preregistration and hosted prerequisite/static qualification before any self-hosted heavy computation. Never import S0/S0, S0/S1 or S0/S2 numerical payloads into the new pair.
