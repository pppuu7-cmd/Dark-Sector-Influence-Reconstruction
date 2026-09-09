# Exp073IN — C2 Wm_S0 authority-succession/materialization protocol v0.1

Date frozen: 2026-09-09. Scope: DSIR Article 3 only.

Status: PROSPECTIVELY FROZEN SUPPORT PROTOCOL. This protocol is frozen before any Exp073IM real radial output is inspected or produced for scientific scoring. It may inspect only already-preserved pre-radial Wm_S0 provenance and immutable identities. It must not inspect downstream radial, physical-support, covariance, nuisance, relation/null, or model-comparison information.

## 1. Purpose

Resolve the sole 14-slot materialization ambiguity identified by `docs/dsir4/audits/EXP073IM_ANGULAR_BYTE_AUTHORITY_MATERIALIZATION_AUDIT_V0_1.md`: `Wm_S0` has two preserved exact-route identities, while Exp073IM requires one exact machine-consumable byte authority.

The protocol must select an already-existing object from provenance alone or remain fail-closed. It cannot create scientific authority by numerical preference.

## 2. Authority is historical state, not a function of bytes alone

Let `O(H)` denote the recovery-visible numerical object/state produced by admissible history `H`, and let `A(H)` denote the production authority legitimately inherited under that history.

If two admissible histories `H1,H2` can satisfy `O(H1)=O(H2)` while `A(H1) != A(H2)`, then no deterministic selector `f(O)` using only the recovered numerical object can satisfy `f(O(H))=A(H)` for every admissible history. Therefore production authority is not identifiable from numerical state alone; a causally preserved provenance/succession witness is required.

Consequence for DSIR: digest value, numerical closeness, exact reproducibility, lexical hash order, artifact size, or a later downstream fit must never be used to infer an authority transfer.

## 3. Frozen succession rule

For one logical slot with an existing admitted production authority `P` and one or more later exact-route candidates:

1. **Continuity.** The last explicitly admitted production authority remains current unless an admissible prospective supersession event exists.
2. **No implicit transfer by exactness.** Determinism, internal exact replay, exact equality on one route, or successful recomputation does not itself transfer production authority.
3. **Explicit supersession only.** A successor may replace the current authority only if a preserved pre-downstream record explicitly authorizes the succession and binds the successor's exact immutable identity.
4. **Ambiguous succession fails closed.** If multiple same-precedence supersession records conflict, if the current authority cannot be materialized, or if the historical record does not establish whether a supersession occurred, classify `BLOCKED_AUTHORITY_SUCCESSION`; do not choose numerically.
5. **No retrospective rescue.** A later protocol may formalize inheritance of an already-existing authority, but it may not rewrite an earlier classification that explicitly declined to select a new canonical production authority.

The rule is evaluated on provenance precedence only. It is invariant to the numerical values of Exp073IM and all later gates.

## 4. Frozen Wm_S0 candidate inventory

The input audit preserves exactly two relevant immutable canonical identities:

- historical primary-P Wm_S0 canonical SHA256: `6ec29f6dbbcf0c29d7af9d6eb98d271bcd06e00d28cebe658b5e266f7ef18d0f`;
- controlled single-thread Exp073AI/AM canonical SHA256: `8ac59fc060195addcc5cd8b6d75e32fbc6dbfeea8456f4c83e8bf0cf034b9220`.

The preserved Exp073AN classification is `DETERMINISTIC_SINGLE_THREAD_ROUTE_BUT_EXACT_AUTHORITY_SHIFT_FROM_PRIMARY_P`, and the recovery record explicitly states that no new canonical production authority was selected at that stage.

No other Wm_S0 candidate may enter Exp073IN v0.1.

## 5. Mechanical decision procedure

Evaluate in this order:

- Was historical primary-P an admitted production authority? If no: `BLOCKED_AUTHORITY_SUCCESSION`.
- Is there a preserved pre-Exp073IM supersession record that explicitly transfers canonical production authority away from primary-P and binds a successor byte identity? If yes: select that bound successor.
- If no such transfer exists: retain primary-P by continuity.
- If the selected authority's exact byte object cannot be materialized from preserved run/artifact/checkpoint provenance: `BLOCKED_AUTHORITY_MATERIALIZATION`.

The procedure must not compare candidate array values except to verify the already-preserved identities and must not use tolerance/ULP/rounding rescue.

## 6. Expected classification tokens

- `PASS_EXP073IN_C2_WM_S0_AUTHORITY_SUCCESSION_V0_1` only when exactly one authority is selected by the frozen provenance rule and its existing immutable object is materializable.
- `BLOCKED_AUTHORITY_SUCCESSION_EXP073IN` when provenance cannot uniquely establish succession.
- `BLOCKED_AUTHORITY_MATERIALIZATION_EXP073IN` when succession is unique but the selected existing bytes cannot be recovered exactly.
- `INVALID_FOR_SCIENCE_EXP073IN` for parent/provenance mutation, candidate substitution, downstream-data leakage, numerical-ranking selection, or any alteration of the frozen decision order.

## 7. Downstream boundary

A PASS authorizes only replacement of the `Wm_S0` 13/14 materialization blocker with one exact inherited byte identity, making the angular input inventory 14/14 materializable. It does not itself score `G_RADIAL_SUPPORT`, does not change `G_ORDERED_JOIN=PASS`, and does not create final model authority.
