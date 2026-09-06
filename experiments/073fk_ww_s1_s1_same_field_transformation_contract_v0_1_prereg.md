# Exp073FK — WW_S1_S1 same-field transformation contract v0.1

Prepared prospectively while Exp073FG `WW_S0_S3` home science is unresolved. Scope: DSIR only. This is GitHub-hosted support/static work only: no self-hosted computation, no partial Exp073FG numerical reads, no workspace construction, no science-gate scoring, and no `WW_S1_S1` authority creation.

## Purpose

Freeze the exact semantic edits required before any future durable `WW_S1_S1` production implementation may be generated from the current cross-pair architecture.

## Frozen target

- task: `WW_S1_S1`;
- authoritative source index pair: `[1,1]`;
- reconstruct authoritative S1 once;
- construct exactly one spin-2 `NmtField` from that map;
- call the coupling matrix with the same Python field object on both sides;
- `same_field_object_handoff=true` in future provenance receipts;
- ordered duplicate/cross semantics are forbidden;
- future checkpoint namespaces must be dedicated to `ww-s1-s1` A/B replicas;
- future numerical/storage semantics remain NSIDE=4096, ell `0..12287`, 39 bands, public file-backed serialized workspace BPW route, selected `wins[0,:,0,:] = EE<-EE`, canonical `<f8 [39,12288]`, exact A/B SHA and `numpy.array_equal`, all finite, no tolerance/rescue.

S1 authority remains selected `7,851,711`, record bytes `31,406,844`, record SHA256 `752f585125e413c7bd40cc5174cf7ef98e95f970022a351c5d91206f371d2241`, unique `4,339,193`, occupancy SHA256 `fed1ffdf2ef7a7ae88e42615bd08e207e039239c44fa20b7994258f147a739f1`; R1 run/job/artifact/digest remain `33270843577 / 99148916507 / 9720335366 / sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`.

## Required transformation boundary

A future S1S1 driver derived from current cross-pair durable architecture must prospectively replace all of the following concepts together, never partially:

1. cross source pair `[0,3]` / `S0->S3` -> auto pair `[1,1]` / `S1->S1`;
2. two source-map reconstruction calls -> exactly one S1 reconstruction;
3. two distinct source payload identities -> one source payload identity referenced consistently;
4. distinct-field handoff false -> same-field-object handoff true;
5. cross-pair field construction -> one field object reused on both coupling sides;
6. Exp073FG task/token/checkpoint namespace -> dedicated future S1S1 identities.

The audit must reject any proposed plan that keeps stale S0/S3 source semantics, constructs a second equal-but-distinct field, uses `(S1,S1)` as two independent source reconstructions, introduces tolerance/allclose/isclose/rounding/smoothing/averaging, or claims numerical/scientific authority.

Candidate support token: `PASS_EXP073FK_WW_S1_S1_SAME_FIELD_TRANSFORMATION_CONTRACT_V0_1`. Classification: `SUPPORT_PLUS_0_PLUS_0`; `ww_s1_s1_authority_created=false`.
