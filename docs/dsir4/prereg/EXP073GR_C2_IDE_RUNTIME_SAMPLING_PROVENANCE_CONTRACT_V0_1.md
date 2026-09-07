# Exp073GR — C2 IDE runtime sampling + provenance contract v0.1

Status: PROSPECTIVELY FROZEN after validated Exp073GQ hook-to-recorder adapter support PASS. Scope: DSIR only. Scientific contribution ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Exp073GQ established an exact observation-only transfer into the eight-binary64 recorder ABI. Exp073GR freezes the runtime sampling/provenance boundary that must be satisfied before any cosmological extraction may be interpreted as a C2 prediction input. This gate is intentionally non-numerical and must not run the cosmological solver.

## Frozen upstream identities

- solver lineage: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- recorder source: `scripts/dsir4/fixtures/dsir_c2_recorder_v0_1.h`;
- recorder Git blob identity: `c6144598b9f75908ee27a517d31eda509f7947f6`;
- record ABI: exactly eight binary64 fields in this order: `tau,k,a,H,delta_m,theta_m,rho_idm_iv,rho_iv`;
- hook/adapter semantics are inherited prospectively from validated Exp073GQ and may not be altered by this contract.

Any source-head, blob, field-order, field-count, or record-width mismatch is fail-closed and invalid for science.

## Frozen requested sampling domain

The only requested C2 sampling nodes are:

- z, in exact order: `[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`;
- k, in exact order and units Mpc^-1: `[0.00067, 0.00201, 0.0067, 0.0201]`.

The Cartesian request ordering is **z-major then k-minor**: for each z in the frozen z list, traverse all four k values in the frozen k list. The contract therefore contains exactly 28 requested `(z,k)` pairs.

No effective z, effective k, interpolation, extrapolation, smoothing, averaging, bin-centre substitution, tolerance-based matching, nearest-neighbour rescue, rounding rescue, or fiducial-P shortcut is permitted.

The global DSIR science support remains `0.295 <= z <= 2.33` and `0 < k <= 0.06664762008318016 Mpc^-1`; all 28 requested nodes must lie strictly inside that frozen support as written. The historical rounded `0.067 Mpc^-1` value remains forbidden.

## Runtime provenance payload

A future extractor may be authorized only if it emits, before scientific consumption, a deterministic provenance manifest containing at least:

1. exact solver repository and 40-hex source head;
2. exact recorder blob SHA1 identity and recorder schema/version;
3. exact ordered z list and exact ordered k list;
4. ordering declaration `z_major_k_minor`;
5. units declaration `k_Mpc^-1`;
6. exact expected request count `28`;
7. exact raw record width `64` bytes and field count `8`;
8. flags `interpolation=false`, `smoothing=false`, `averaging=false`, `tolerance_matching=false`, `effective_coordinate_substitution=false`;
9. a deterministic SHA256 fingerprint over the canonical UTF-8 contract representation used by the extractor;
10. fail-closed rejection if any runtime request or emitted provenance disagrees with this frozen contract.

This gate does not freeze a result-dependent numerical acceptance threshold. It freezes only deterministic sampling coordinates, serialization/provenance identity and prohibited transformations.

## Hosted static audit

A hosted-only audit must validate the committed machine-readable contract and emit exactly:

`PASS_EXP073GR_C2_IDE_RUNTIME_SAMPLING_PROVENANCE_CONTRACT_V0_1`

The audit must prove all 28 Cartesian pairs are unique and in frozen order, every node lies inside the preserved DSIR z/k support, the recorder blob identity matches the committed file, record size/count are exactly 64/8, and all prohibited transformation flags are false.

## Classification and authority ceiling

PASS is only `SUPPORT_PLUS_0_PLUS_0` with:

- `cosmological_run_started=false`;
- `self_hosted_science_started=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any static/spec/provenance mismatch is implementation/infrastructure `+0/+0`, never a scientific model FAIL. A validated PASS may authorize a separately prospectively frozen runtime request-emission implementation/audit. It does **not** authorize scientific interpretation or model authority.
