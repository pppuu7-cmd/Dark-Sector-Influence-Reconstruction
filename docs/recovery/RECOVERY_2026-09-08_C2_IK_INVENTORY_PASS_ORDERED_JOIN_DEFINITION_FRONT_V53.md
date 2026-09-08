# DSIR recovery V53 — Exp073IK inventory PASS; ordered-join definition frontier

Date: 2026-09-08. Scope: **DSIR only**. Never mix RTK/RQIR.

## Preserved scientific authority
All V51 and earlier scientific authority is unchanged. `G_DOMAIN_MAPPING=PASS` and `G_ANGULAR_AUTHORITY=PASS` remain admitted. `G_ORDERED_JOIN=NOT_YET_TESTABLE`; all later C2 gates remain `NOT_YET_TESTABLE`; `scientific_model_authority_created=false`; overall status remains `NOT_YET_TESTABLE`.

## Exp073IK prospective support gate
Preregistration: `docs/dsir4/prereg/EXP073IK_C2_SOURCE_BASIS_OBSERVABLE_ORDER_INVENTORY_V0_1.md`, creation commit `0212a3ab9abcbd8f2644ae6a663e5b84a5307c7a`, blob `ec821b94fb16b2b2e8e66d0fe1d423c7f1d1aed5`.
Frozen inventory blob: `745d0494640c9a89a2a639ad8df2e6eab960e125`.
Workflow blob: `6a0846b1da1a16948f26d4f21572d8d4f4ab4169`.
R1 evaluator blob: `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`.
Angular runner blob: `050ed7dd3387c4fb031f877825e6b3f4d4ce3ef2`.
Angular authority blob: `0037c8944aff5c96935ccb16ec441c89d285319e`.
Classification ceiling: `SUPPORT_PLUS_0_PLUS_0` only.

## Infrastructure history and minimal repairs
The frozen workflow initially had no launch-binding file, so no IK run existed. The missing binding was added in commit `0c3c19c83084fb067960344755b940cf69e636ea`; this launched run `34266137693`, job `102195867755`. Binding verification passed, but the static audit failed before any scientific result because `ast.literal_eval` could not resolve authoritative `MAPPER={'nside': NSIDE,...}`. This is implementation/infrastructure `+0/+0`.

Commit `5196775e65e58ff116e4de5a7c2b20959d96b777` added fail-closed static-name resolution only; rebound commit `73fab4dd4f49b98a63f79075779b608eff2e0597` launched run `34266234477`, job `102196195647`. That attempt exposed the next first causal parser defect: `LMAX_PLUS_ONE = 3 * NSIDE` was a frozen static arithmetic expression not handled by the audit parser. This attempt is also implementation/infrastructure `+0/+0`.

Commit `12ae5db48d6407be82c0bc872602e4bc5b78c269` extended only the static resolver to arithmetic constants; no source evidence, scientific equation, ordering, threshold, domain, or acceptance criterion changed. Final audit blob: `61c8431786aef7ca2dc55cb0329ed48675db1aba`. Rebound binding commit: `6fd55818814741677d2184b2c4ef8e5576f2b0cd`.

## Exp073IK terminal result — support PASS only
Authoritative final run: `34266340535`.
Job: `102196556716`.
Branch/head: `main / 6fd55818814741677d2184b2c4ef8e5576f2b0cd`.
Runner: GitHub-hosted `ubuntu-24.04`; home/self-hosted owner none.

Raw job log was consumed and contains the exact token and state:
- `PASS_EXP073IK_C2_SOURCE_BASIS_OBSERVABLE_ORDER_INVENTORY_V0_1`
- `classification=SUPPORT_PLUS_0_PLUS_0`
- `source_basis_inventory_verified=true`
- `observable_order_inventory_verified=true`
- `prospective_ordered_join_contract_may_be_defined=true`
- `G_DOMAIN_MAPPING=PASS`
- `G_ANGULAR_AUTHORITY=PASS`
- `G_ORDERED_JOIN=NOT_YET_TESTABLE`
- `scientific_model_authority_created=false`
- `overall_status=NOT_YET_TESTABLE`.

Artifact ID: `10068463479`.
Artifact name: `exp073ik-c2-source-basis-observable-order-inventory-audit-v0-1`.
Artifact size: `1855` bytes.
GitHub artifact digest: `sha256:57ee4e1bb04e7511bdc52cb200ce7bdde745a749f5f4f7be0df060e6e5b2c10b`.

The recovered exact inventories are:
- source basis order `[S0,S1,S2,S3]` with `zbin_mcal=[0,1,2,3]`;
- WW pair order `S0_S0,S0_S1,S0_S2,S0_S3,S1_S1,S1_S2,S1_S3,S2_S2,S2_S3,S3_S3`;
- historical 14-task angular order `Wm_S0,Wm_S1,Wm_S2,Wm_S3,WW_S0_S0,WW_S0_S1,WW_S0_S2,WW_S0_S3,WW_S1_S1,WW_S1_S2,WW_S1_S3,WW_S2_S2,WW_S2_S3,WW_S3_S3`;
- Wm semantics `TE<-TE`, WW semantics `EE<-EE`, NSIDE=4096, ell `0..12287`, 39 bands, canonical `<f8 [39,12288]`;
- R1 source selection `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0` and mapper `nside=4096, ordering=RING, coords=C, lonlat=true`.

## Ordered-join firewall and current block
The Exp073IK PASS authorizes only prospective definition work. Its preregistration explicitly forbids inferring future C2 join membership merely from the historical 14-task manifest and forbids inventing redshift-edge values.

After terminal consumption, default-branch repository searches for `G_ORDERED_JOIN`, `ordered_join`, `ordered join`, `mapping operator`, `domain mapping`, `mapping_operator_domain_pair`, `radial kernel`, and related C2 terminology did not recover an already-frozen machine-checkable scientific ordered-join equation/domain membership/redshift-edge contract. `EXP073IL` is not currently occupied, but no new experiment is created solely to fill that label.

Therefore the scientifically correct frontier is **BLOCKED / NOT_YET_TESTABLE on an explicit prospective ordered-join scientific definition**. The repository has sufficient provenance for basis/order, but not sufficient authority to invent what objects are joined, the join equation, or required radial/redshift support. Launching a numeric join now would be post-hoc science and is forbidden.

## Current process ledger
- queued Actions: none;
- in-progress Actions: none;
- home/self-hosted owner: none;
- checkpoint namespace: N/A;
- last durable gate: Exp073IK support-only PASS described above;
- exact next permitted action: locate or prospectively derive from explicit scientific premises an ordered-join contract that fixes membership, operator/equation, domain coordinates and required provenance **before** reading/scoring join outputs. Only then may a separate gate (label collision checked at creation time) be preregistered and launched.

No scientific/resource failure was created in this iteration. The two failed IK attempts remain historical infrastructure `+0/+0` only.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
