# V0.26 R1 hosted contract/code/input/provenance audit evidence

Status: **AUDIT EVIDENCE CANDIDATE — NOT TERMINAL AUTHORITY**  
Date: 2026-09-15  
Effect: `+0/+0`.

This record preserves the response-blind hosted audit of the consolidated V0.26 R1 candidate. It is intentionally not a funnel authority and does not authorize a sentinel executor, sentinel workflow, sentinel science execution, full 107-row replay, or downstream science. The next action remains independent funnel review.

## R1 objects audited

- Branch: `research/v026-r1-freeze`.
- Base main at branch creation: `b489eb58f598915db52476b740eb76de67e42d5f`.
- R1 preregistration: `prereg/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.md`.
- R1 prereg creation commit: `c74828209901d9486f8a778d30084f567807654d`.
- R1 prereg git blob: `545e5be589e0f8029d23db2edb4e2faad116c3a0`.
- R1 machine contract: `docs/dsir4/contracts/LAYERB_BETA_FORCED_BASELINE_EXACT_TARGET_UNION_FULL_LAYERB_NUMERICAL_REPLAY_V0_26_R1.json`.
- R1 contract creation commit: `ad1f7cd07b7d0da27a8c551c7bc44704e50a1f0d`.
- R1 contract git blob: `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

The R1 contract directly consolidates the old split candidate, alpha route hardening, route-specific tolerance correction, hosted NumPy-1.26.4 static identity, corrected `25063` mixed parser maximum, parser byte convention, solver accounting, sentinel preregistration, full replay gates, and firewalls. The historical split candidate is not mutated.

## Hosted static identity precursor

The exact response-blind GRID896/payload identity was captured before the R1 contract:

- probe: `ci/layerb_beta_v026_r1_static_identity_probe_v0_1.py`, git blob `5fffa2fd926eaf3d775213959039577b20b312bd`;
- workflow: `.github/workflows/layerb-beta-v026-r1-static-identity-probe-v0-1.yml`, git blob `0a2f42f70c3d4e8cbe2776f26dc9c5fb3a68bc23`;
- run `34954905127`, run number 2, attempt 1, head `5dc6150191638f48442671395ce4da9e676579b4`, conclusion `success`;
- job `104334496210`, `static-identity`, conclusion `success`;
- artifact `10390997654`, `layerb-beta-v026-r1-static-identity-v0-1`;
- artifact ZIP SHA256 `5cd19512bef3d9795957fb8105361e4006123ae59794bc94e2e5ded5722436ff`;
- `v026_r1_static_identity.json`: 140697 bytes, SHA256 `3a9d8375119068063ddcb4ac37d8f3da92444261b0fad356a228ccaedf6292d7`;
- `v026_r1_static_identity.sha256`: 104 bytes, SHA256 `5c6187a03db04888c4e3bd4f6f98befc1d67ae45a0c362fdbb320fe5dcf70f32`.

Frozen identity from that hosted NumPy `1.26.4` run:

- GRID896 binary64 payload SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`;
- GRID896 u64hex-lines SHA256 `e4f8d7174696d98edc34df25e8be699d641dd4c4f276de4681d933af97fd50b4`;
- mixed target plan SHA256 `59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85`;
- mixed payload manifest SHA256 `6b0f08b196f6afa2086a4275ec364d527c50786921ef0ca1d77a30edbed91ce6`;
- mixed maximum `M013 = 25063` C-string bytes;
- direct target plan SHA256 `1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864`;
- direct payload manifest SHA256 `99a6e4c48d353b05bea5000fc27417731d1c347071254232ed807554ee569da6`;
- direct maximum `D20 = 24262` C-string bytes.

No CLASS solver or scientific response was used in this precursor.

## Independent R1 audit implementation

The R1 contract audit does not import the static identity probe. It independently reconstructs the request geometry, GRID896 binary64 object, mixed/direct batching and payload manifests from the frozen source plan, then checks route-specific tolerances, alpha method authorities, solver accounting, sharding, sentinel identities, and execution firewalls.

- auditor: `ci/layerb_beta_v026_r1_contract_audit_v0_1.py`, git blob `9109f2e2bcc6146fa62e423e145ad09a67b70b0c`;
- workflow: `.github/workflows/layerb-beta-v026-r1-contract-audit-v0-1.yml`, git blob `626c56d86d778453468a6b422b9b780548e041a4`;
- workflow pins Python `3.12.3` and NumPy `1.26.4`;
- frozen source plan artifact `10298655751`, ZIP SHA256 `9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7`, inner `plan.json` 3953984 bytes, SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`.

## Hosted R1 audit result

- Actions run `34955509439`, run number 1, attempt 1, event `push`;
- exact execution head `6d1e8f9a8f4940390b5618bbbdf8be4c91945beb`;
- run conclusion `success`;
- job `104336497954`, `independent-r1-audit`, conclusion `success`;
- all eight substantive/preparation steps completed successfully;
- artifact `10390734361`, `layerb-beta-v026-r1-contract-audit-v0-1`;
- GitHub artifact ZIP digest and independently downloaded ZIP SHA256 both `6309cc724061d66d881157e0c7b49807a6a111d55b76b0ca091fdf6efb43e664`;
- `r1_contract_audit.json`: 1675 bytes, SHA256 `304d14217933d5852b9e9783a127cb6486344adddf228ae70e2a455d298e483f`;
- `r1_contract_audit.sha256`: 104 bytes, SHA256 `758f2382e8616f8c33175e62359ddc99efdade7f8e6cbe60cfa624c2891d546d`.

Receipt token:
`PASS_LAYERB_BETA_V0_26_R1_CONTRACT_AUDIT_PLUS_0_PLUS_0`.

Independently reproduced audit values include:

- source plan SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`;
- 64,658 DES unique targets;
- GRID896 binary64 SHA256 `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`;
- mixed batches = 301;
- mixed target-plan SHA256 `59abce49f6338c30b93d11fa462e1ff8642615d6100d23feca4b36505a5cef85`;
- mixed payload-manifest SHA256 `6b0f08b196f6afa2086a4275ec364d527c50786921ef0ca1d77a30edbed91ce6`;
- mixed maximum `M013 = 25063` bytes;
- direct batches = 59;
- direct target-plan SHA256 `1c98927960e81d7fb55ebc687ef36059d964b233001551dba2aa9a01652c8864`;
- direct payload-manifest SHA256 `99a6e4c48d353b05bea5000fc27417731d1c347071254232ed807554ee569da6`;
- direct maximum `D20 = 24262` bytes;
- alpha `tol_perturb_integration = 3e-10`;
- beta `tol_perturb_integration = 1e-12`;
- full replay solver accounting = 738 CLASS constructions.

The receipt explicitly records `class_solver_invoked=false`, `scientific_response_read=false`, `covariance_read=false`, `sentinel_execution_authorized=false`, and `full_107_row_execution_authorized=false`.

## Interpretation

This hosted audit closes the known split-candidate static-identity blocker and supplies internally consistent response-blind R1 contract evidence. It is not a scientific-response reproducibility result and is not sufficient to self-authorize the sentinel.

The required next gate is an **independent funnel review of the R1 preregistration, contract, audit code/workflow and immutable audit artifacts**. Only a separate explicit authority from that review may permit construction of the 32-lane sentinel executor/workflow. Until then, no sentinel or full replay may be authored or launched, and all downstream scientific firewalls remain closed.
