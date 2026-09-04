# Exp073DH — mask-to-workspace cumulative-lineage resume v0.1

Date: 2026-09-04. Scope: DSIR only. Support/infrastructure `+0/+0`; no Wm_S3 science authority.

## Trigger
Exp073DG closed the verified full-window -> selected-TE boundary without recomputing a verified expensive stage. A complete boundary audit then found one remaining earlier-stage resume case: when `fresh_masks_complete` is valid but `fresh_workspace_mcm_complete` is absent, the inherited v0.1 code restores the masks (invocation-local reconstruction counts `{lens:0,source:0}`) and would write those invocation-local counts into the newly computed workspace manifest. The cumulative scientific lineage of those restored masks is still exactly `{lens:1,source:1}` and must remain so.

## Prospective minimal repair
The resume implementation may normalize only the newly-created `fresh_workspace_mcm_complete` manifest's `reconstruction_counts` to immutable cumulative `{lens:1,source:1}`, but only after independently validating the existing `fresh_masks_complete` manifest and its exact mask payload SHA identities. It must not change a pre-existing valid workspace manifest.

Requirements:
- fresh first execution still records exact cumulative `{1,1}`;
- resume from verified masks only records workspace cumulative `{1,1}` while invocation-local work remains separately knowable as `{0,0}` at the later receipt layer;
- any stored masks/workspace cumulative value other than exact integer `{1,1}` is fail-closed;
- existing manifests are read-only and never migrated/re-written;
- all later boundary-safe behavior from Exp073DG remains preserved;
- scientific arithmetic, masks, data, band edges, TE selection, OpenMP-8 adapter, six checkpoint boundaries, SHA checks and exact comparator remain unchanged.

PASS token: `PASS_EXP073DH_MASK_WORKSPACE_LINEAGE_RESUME_V0_1`.
Only a raw hosted PASS allows construction/activation of the self-hosted checkpoint resume process.
