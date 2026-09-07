# Exp073GK — C2 IDE Delta_m generator implementation/static audit v0.1

Date: 2026-09-07
Scope: DSIR only; hypothesis `C2_IDE_LOCAL_TANGENT_CONE`.
Classification: `SUPPORT_PLUS_0_PLUS_0` only. This gate cannot create `prediction_ready`, `G_DOMAIN_MAPPING=PASS`, angular authority, or a scientific model verdict.

## Prospective purpose

Implement the deterministic arithmetic/serialization layer frozen by Exp073GJ while the independent WW heavy frontier runs. This gate deliberately does **not** run new C2 numerical science. It only provides a fail-closed generator that can consume explicitly source-bound same-solver arrays after those arrays are separately produced from pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

Inherited immutable interface: `experiments/073gj_c2_ide_delta_m_generation_freeze_v0_1_prereg.md`.

## Frozen implementation boundary

The generator must accept only a manifest containing all four exact points:

- reference `(alpha,beta)=(0,0)`;
- alpha-left `(-1e-4,0)`;
- beta-plus `(0,+1e-4)`;
- beta-minus `(0,-1e-4)`.

Every point must carry exact arrays over

- `z=[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`;
- `k_Mpc^-1=[0.00067,0.00201,0.0067,0.0201]`;
- source-bound `delta_m`, `theta_m`, `w_m`, `Hconf`;
- explicit solver commit and native source-variable identity strings;
- physical branch status proving `rho_idm>0` and `rho_iv>=0` over the required history.

Shape is prospectively fixed as `[7,4]` for `delta_m`, `theta_m`, `w_m` and generated `Delta_m`; `Hconf` may be `[7]` only and is broadcast across k. Missing, extra, repeated, non-finite, mismatched-coordinate, ambiguous-source, wrong-commit or branch-invalid input fails closed.

The exact arithmetic remains

`Delta_m = delta_m + 3*(1+w_m)*Hconf*theta_m/k^2`.

For this implementation boundary the matched response is computed directly from same-mode amplitudes as

`r_Delta = ln((Delta_m_model*Delta_m_model)/(Delta_m_ref*Delta_m_ref))`

at each exact coordinate. This is valid only for matched runs with the same primordial normalization/phase convention recorded by the source manifest. The generator must fail closed if that equality of normalization/phase provenance is not explicit. It must not use raw CLASS `mPk` as a substitute.

No interpolation, extrapolation, rounding, smoothing, effective coordinates, quasi-static replacement, fiducial-P shortcut or tolerance-based acceptance is permitted.

## Deterministic serialization

The implementation must canonicalize JSON with sorted keys and compact separators. Payload SHA256 is computed over canonical payload bytes with the `payload_sha256` field absent, then inserted; reserialization after removing that field must reproduce the same digest exactly. Arrays must be finite binary64 values represented by Python JSON numbers without deliberate rounding.

The generator may set `prediction_ready=true` only when all exact points and coordinates exist once, source identities are non-empty and unambiguous, solver commit is exact, physical branch masks pass, matched primordial normalization/phase is explicitly identical, all arrays are finite, and canonical SHA self-verification passes. Static audit itself never creates that state because it runs only synthetic arithmetic fixtures.

## Hosted static-audit requirements

The hosted audit must:

1. syntax-compile the generator;
2. inspect implementation text for the exact solver commit, coordinate grids, required keys and forbidden rescue operations;
3. run a deterministic synthetic fixture through the generator twice and require byte-identical output and SHA;
4. independently recompute one fixture cell using the frozen equation and require exact binary64 equality;
5. mutate solver commit, k grid, source identity, branch mask and primordial-match flag one at a time and require fail-closed rejection;
6. confirm `self_hosted_science_started=false` and `scientific_model_authority_created=false`.

Exact support token:

`PASS_EXP073GK_C2_IDE_DELTA_M_GENERATOR_STATIC_AUDIT_V0_1`

## Non-interference

This gate is fixed without reading partial Exp073FS numerical output and without using any C2 observational result. Frozen DSIR thresholds and WW science are unchanged. A later numerical source-extraction/provenance gate is still mandatory before any real C2 payload can be admitted.