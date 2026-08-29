# Exp073AB — Article 3 DES row-to-operator mapping authority v0.1

**Frozen:** 2026-08-30 while Exp073X run `33277263287` is still in progress, before any complete DES angular authority or Layer-A support fraction exists.

## Purpose

Freeze the exact deterministic mapping from the 1170 immutable DES observation rows inherited by Exp073U to the already-frozen factorized operator coordinates:

- one angular task identity;
- one Exp073Z2 radial-kernel index;
- one exact NaMaster bandpower index and ell interval.

This is a schema/order authority only. It must not read an angular-window value, compute physical k, score support, retain/reject rows or read downstream statistics.

## Exact parents

### Exp073T static inventory

- run `33272691162`;
- head `6efc41b005393deaf6651e90e902e1bf11c64250`;
- artifact `9720563095`;
- artifact digest `sha256:4332ffa9d6b4385a48d3022a8afcedf0bf00a742cee8444fd6ca83842bf1e642`;
- internal `exp073t_cosmotheka_inventory_v0_1.json` SHA256 `55f55d21eedd3779a729af387205ec7db360617c5e026406d21b3b542f355309`;
- token `PASS_EXP073T_PINNED_COSMOTHEKA_INVENTORY_V0_1`.

It freezes:

- Wm 20-pair order = lens-major then source-major;
- WW 10-pair order = `(S0,S0),(S0,S1),(S0,S2),(S0,S3),(S1,S1),(S1,S2),(S1,S3),(S2,S2),(S2,S3),(S3,S3)`;
- 39 bands within each pair;
- Wm coordinate-order SHA256 `dc20ff104c707d006992c1579ce9175295fae426b1c32ff47e56c53d9300603a`;
- WW SHA256 `e0cc92706598a8ac6360d0fd669451e4816091f83c01e8744940e94a2b8593b5`;
- DES Wm+WW SHA256 `736f80a6dd407b1a3891cb34f35262e415a4f0c9bbb200a9f376102b05988ee4`.

### Exp073U immutable observation skeleton

- run `33274852199`;
- artifact `9721184683`;
- digest `sha256:d44e628e9312fb5a919a6681b69d9e06e18418cdd299de641e6465e60dadfd68`;
- internal JSON SHA256 `a6b9eaa697edd63d5b5ca698341c35578d395201ff3e0e0bcffff7f5ba94f534`;
- DES offsets Wm `[0,780)`, WW `[780,1170)`;
- full 1410-row SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`.

### Exp073Z2 stable radial authority

- run `33279208949`;
- artifact `9722468056`;
- digest `sha256:3eb8b025711e8df6d5452a3a57002f36c9d7de2b9116734b71d15d6822dd20be`;
- internal JSON SHA256 `3cb25beed23193a94e10d590296349713d1d83f92771215b72c10ea2e6f82c1a`;
- token `PASS_EXP073Z2_DES_RADIAL_KERNEL_STABLE_DIRECT_V0_2`;
- Wm radial order `L1xS1,L1xS2,...,L5xS4` (20 kernels);
- WW radial order `S1xS1,S1xS2,S1xS3,S1xS4,S2xS2,S2xS3,S2xS4,S3xS3,S3xS4,S4xS4` (10 kernels).

## Mapping rule frozen before output

Parse each exact Exp073T coordinate ID; do not regenerate IDs from local assumptions.

For Wm ID

`Wm|DESgc__L|DESwl__S|TE|component=0|bp=BB|ell=LO:HI`

map to:

- global DES ordinal inherited unchanged from Exp073U, `0..779`;
- angular task `Wm_S{S}`;
- radial index `4*L + S`;
- band index `BB`;
- exact `[LO,HI)` equal to frozen band edges `[BB,BB+1]`.

For WW ID

`WW|DESwl__I|DESwl__J|EE|component=0|bp=BB|ell=LO:HI`

map to:

- global DES ordinal `780..1169`;
- angular task `WW_S{I}_S{J}`;
- radial index equal to the index of `(I,J)` in the frozen 10-pair Exp073T/Exp073Z2 order;
- band index `BB`;
- exact `[LO,HI)` from frozen band edges.

No effective ell is created. `LO:HI` only identifies the released finite bandpower coordinate; the future operator remains the full `[39,12288]` angular window.

## Prospective canonical mapping serialization

For every DES row serialize one UTF-8 tab-separated line:

`global_ordinal<TAB>coordinate_id<TAB>angular_task<TAB>radial_index<TAB>band_index<TAB>ell_lo<TAB>ell_hi\n`

with rows in immutable Exp073U DES order.

Before the hosted Exp073AB execution, an independent implementation using only the already-public non-science parents produced these frozen expected digests:

- all 1170 mapping lines SHA256 `092bb2e83a0ad0d7ad5359110465eccfe2c6096e593c60c459c52c9a2b7e4319`;
- Wm 780 mapping lines SHA256 `4dc85efa2372242d8c612a84a8066dc0bd5774ef8260b5c15b3e5378c8800422`;
- WW 390 mapping lines SHA256 `ffe84463b276030a6248ab289255b472f0d809882d0a577c26fb5e12e34912bf`.

These are order/schema hashes, not science outcomes.

## Cardinality controls

Require exactly:

- 1170 unique DES coordinate IDs;
- 780 Wm + 390 WW;
- every Wm angular task `Wm_S0..Wm_S3` maps 195 observation rows = 5 radial kernels x 39 bands;
- every WW angular task maps 39 rows;
- every one of 20 Wm radial indices maps 39 bands exactly once;
- every one of 10 WW radial indices maps 39 bands exactly once;
- each pair contains band indices exactly `0..38` once;
- no mapping uses BOSS rows.

## Firewall

Forbidden inputs/outputs:

- actual angular-window values or hashes produced by Exp073X/AA;
- radial-kernel numeric values (only frozen names/order and authority hashes may be checked);
- physical k;
- `f_invalid`;
- retained/rejected flags;
- fiducial P;
- covariance/whitening;
- nuisance SVD/rank;
- quotient/relation/null/G8.

## Required token

`PASS_EXP073AB_DES_ROW_OPERATOR_MAPPING_V0_1`

This non-classifying PASS cannot increase strict readiness above **52%** by itself.
