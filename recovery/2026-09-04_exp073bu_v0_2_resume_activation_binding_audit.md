# Exp073BU v0.2 prospective resume activation-binding audit

Date: 2026-09-04
Scope: DSIR only; support/governance audit `+0/+0`; no science gate scored.

## Live authority preserved
The only authoritative scientific process remains Exp073BU run/job `33885834557 / 101065302520`, workflow `.github/workflows/exp073bu-wm-s3-fresh-ab-exact-science-v0-3.yml`, frozen activation/science source head `a2f14dfd5a9e54a30fb467f6d0e717bd4f00bd35`, contract fingerprint `a400a7cee61f59c89099ac8b2c5ec67286b8c38002d5855a5f3a150c59838147`. This audit does not modify, restart, inspect partial numerical output from, or compete with that run.

## Finding 1 — DD v0.2 is compatible with the frozen launcher lineage field
`ci/exp073bu_wm_s3_fresh_ab_production_v0_2.py` preserves the legacy receipt key `reconstruction_counts` as immutable cumulative lineage `{lens:1, source:1}` and records invocation-local work separately in `invocation_new_reconstruction_counts`. Therefore the frozen launcher v0.1 check on workspace `reconstruction_counts == {'lens':1,'source':1}` is not itself an incompatibility with the DD repair. A verified resume may have invocation-local `{0,0}` while cumulative lineage remains exact `{1,1}`.

## Finding 2 — silent v0.2 substitution is forbidden by the current orchestration
The active science workflow prospectively binds `SOURCE_HEAD` to `GITHUB_SHA`, binds the v0.1 production-driver blob, and re-checks that exact v0.1 blob on the self-hosted runner. Durable manifests are also fail-closed on `source_head` and `contract_fingerprint`.

Consequently, if the active process is interrupted, a future run cannot simply check out a newer repair commit and substitute v0.2 while pretending that newer implementation commit is the old science source authority. Doing so would either violate the prospective implementation binding or fail checkpoint identity verification.

## Required prospective resume orchestration contract
Before v0.2 may be used after a future interruption, a separate hosted support gate must freeze and machine-check two distinct identities:

1. `FROZEN_SCIENCE_HEAD = a2f14dfd5a9e54a30fb467f6d0e717bd4f00bd35` (the authority embedded in existing Exp073BU checkpoint manifests), and
2. an explicit `RESUME_IMPLEMENTATION_HEAD`/blob set containing the already-audited DD v0.2 provenance repair.

The resume orchestration must pass the frozen science head and original science contract fingerprint to checkpoint validation exactly as stored, while independently verifying the prospective repair implementation blobs. It must not rewrite historical checkpoint manifests, change numerical arithmetic, alter the six stage boundaries, broaden restore ownership, import cross-replica output, or weaken SHA/array equality.

A hosted static/source-binding gate is required before any such repaired self-hosted resume. If the current Exp073BU run completes normally, this prospective resume binding is unnecessary for that terminal classification.

## Frozen science unchanged
No DES/Wm_S3 numerical output was inspected or produced by this audit. Exact 39-band authority, `TE<-TE`, canonical `<f8 [39,12288]`, eight outer workers, nested threading=1, six durable checkpoint stages, exact SHA256 and `numpy.array_equal`, and no-tolerance-rescue policy remain unchanged. Wm_S3 scientific authority remains absent until the active run reaches a validated terminal comparator result.
