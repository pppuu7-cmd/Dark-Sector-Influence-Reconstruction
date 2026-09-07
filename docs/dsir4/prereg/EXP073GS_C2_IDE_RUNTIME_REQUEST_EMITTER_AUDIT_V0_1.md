# Exp073GS — C2 IDE deterministic runtime request-emitter audit v0.1

Status: PROSPECTIVELY FROZEN after independently raw-validated Exp073GR support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Authority inherited from Exp073GR

The only admitted input contract is `scripts/dsir4/fixtures/dsir_c2_runtime_sampling_provenance_contract_v0_1.json`, whose canonical JSON SHA256 from Exp073GR run `34130804754`, job `101770188173`, is:

`6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`.

The frozen solver lineage remains `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`; recorder blob remains `c6144598b9f75908ee27a517d31eda509f7947f6`.

## Purpose

Exp073GS may implement only a deterministic request enumerator and provenance-manifest constructor over the already frozen GR contract. It must not clone, build or execute CLASS and must not create any scientific prediction.

## Frozen emitter semantics

1. Load the exact GR JSON contract.
2. Canonicalize using UTF-8 JSON with `sort_keys=true` and separators `(',', ':')`.
3. Require SHA256 exactly `6a14470157e0677ee10d65d24e759907b9a5df5fe1fd9d80e940787224dbfe9b`; any mismatch must fail closed before emitting requests.
4. Emit exactly 28 requests in z-major/k-minor order with ordinals `0..27`.
5. Each request contains only the literal frozen `z` and `k_Mpc^-1` values; no arithmetic coordinate transform is allowed.
6. Build a deterministic provenance manifest containing the GR contract fingerprint, solver repository/head, recorder blob, ordering, units, request count, record width/count and all prohibited-transformation flags.
7. The emitted manifest must itself be canonicalizable and SHA256-addressable.
8. No interpolation, extrapolation, smoothing, averaging, tolerance matching, nearest-neighbour selection, rounding rescue, effective-coordinate substitution or fiducial-P shortcut may appear in the emitter logic.

## Hosted audit

A hosted-only audit must:

- import the exact committed emitter fixture;
- verify all 28 outputs against a separately constructed expected Cartesian product;
- verify ordinals and exact floating values;
- verify a one-byte/one-value mutation of a temporary contract fails closed before any request is returned;
- verify the provenance manifest retains the frozen identities and all prohibited flags false;
- static-scan the emitter for prohibited numerical rescue operations and any CLASS execution/build invocation;
- emit exact token `PASS_EXP073GS_C2_IDE_RUNTIME_REQUEST_EMITTER_AUDIT_V0_1`.

## Classification

PASS is only `SUPPORT_PLUS_0_PLUS_0` with `cosmological_run_started=false`, `self_hosted_science_started=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, and `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any implementation/static/provenance mismatch is `+0/+0`, never a scientific model FAIL. A PASS may authorize a separately frozen dry-run record-envelope assembly gate, but not a real cosmological extraction or scientific interpretation.
