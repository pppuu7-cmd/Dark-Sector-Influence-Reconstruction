# Exp073P aggregate prerequisite join — superseding R1 authority preregistration v0.2

**Frozen:** 2026-08-29, while the replacement Exp073R1 mapper step was still
`in_progress`, before its terminal assertion and before any result artifact
existed.

## Scope

This preregistration supersedes only the failed Exp073R1 parent binding used by
aggregate prerequisite join v0.1.  It does not alter any physical-support
coordinate, threshold, parent dataset, evaluator rule, classification boundary
or downstream gate order.

The v0.1 aggregate evaluator and actual route remain immutable historical
records.  They are bound to failed run `33212521957`, job `98988824629`, and
must remain fail-closed.  They may not be repointed post hoc.

## Why a superseding authority is required

Run `33212521957`, job `98988824629`, passed the unchanged-evaluator firewall
and immutable-parent metadata checks but failed before artifact download on
pip's PEP 668 `externally-managed-environment` guard.  The 84 GB metacal GET
never started, zero metacal rows were read and no R1 artifact was created.  Its
classification is only `INCOMPLETE_EXP073R1`.

Runtime repair commit `5f773b3600defd5c5a2e94b8ef9489bb9ba32787`
replaced the disallowed user-site installation with a clean virtual environment
under `RUNNER_TEMP`.  It changed only dependency installation and PATH
selection.  The evaluator, inputs, transport, row semantics, selection,
HEALPix mapping, serialization, repeatability tests and terminal criteria did
not change.

## Sole admitted replacement R1 authority

Aggregate join v0.2 may admit only:

- repository `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`;
- run `33222848695`, attempt `1`;
- job `99020389131`, `metacal-map-longrun`;
- head `98c4b8783a95932949947d9e214706c4ec7eaf8c`;
- workflow path
  `.github/workflows/exp073r1-desy1-selfhosted-longrun-stageb-v0-6.yml`;
- workflow name `Exp073R1 DESY1 self-hosted long-run Stage-B v0.6`;
- artifact name
  `exp073r1-v06-selfhosted-longrun-98c4b8783a95932949947d9e214706c4ec7eaf8c`;
- workflow Git blob `2cdcb0c60f464c0c65c3bafdde23daec7732215e`;
- workflow SHA256
  `02010ab372ae6225996a44c8e768573549b78269fa0ee08f7213409eedbac162`;
- unchanged evaluator Git blob
  `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- unchanged evaluator SHA256
  `5d4fcd8eebe0ae3a45b173a9f5ad261f014586ec81c5587e8720f3290254483e`.

At freeze time, workflow steps through downloaded-parent internal re-binding
were `completed/success`.  The whole-object metacal mapper was `in_progress`;
the terminal R1 assertion was pending; the Actions artifact list was empty.
No terminal summary, selected-row count, mask hash or downstream science value
was available or used to define this contract.

## Required R1 terminal evidence

Actions `success` alone is insufficient.  The unique future artifact must be
non-expired, independently ID/digest-bound to the run above, and contain the
exact internal status

`PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.

The unchanged R1 admissibility interlock must require every already-frozen
control, including:

- exact 84,075,649,920 metacal bytes and SHA256
  `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- exact source identity, index bytes/hash and row count `136930995`;
- one ordinary HTTP 200 whole-object GET with `Accept-Encoding: identity` and
  no Range/resume requests;
- exact selection, parent order, four nonempty bins and finite coordinates;
- `nside=4096`, RING, celestial `C`, `lonlat=True`;
- zero out-of-range pixels and all independent mask repeatability controls;
- every Exp073R0 parent check;
- no support scoring, `f_invalid`, covariance, whitening, nuisance SVD,
  relation/null, held-out or G8 read;
- `gate_state={G7: OPEN, G8: OPEN, G9: OPEN}`.

Missing, interrupted, unsuccessful, duplicate, expired or internally rejected
evidence must fail closed.  No partial pixel records or masks are authority.

## Unchanged remaining parent registry

All nine non-R1 parents, artifact identities, byte hashes and semantic checks
remain exactly those frozen by:

- `experiments/073p_aggregate_prerequisite_join_evaluator_prereg_v0_1.md`,
  SHA256
  `5e4a64ac47204f82261b9aa9f1a46250f5cc86bf654f001ee4f8db4a80603c4f`;
- `ci/exp073p_aggregate_prerequisite_join_v0_1.py`, SHA256
  `9dc0b5a0ea82b8fb69d82e06b566b08d61c1982bd5e13ecd8db6752253bc0e46`.

Implementation v0.2 must reuse those checks without weakening them and change
only the exact R1 run/job/head/workflow/artifact binding listed above.

## Required implementation and taxonomy

Implementation must use new v0.2 files; v0.1 files remain byte-immutable.  It
must collect live Actions metadata with complete pagination, independently
validate the future supplied artifact ID/digest, download the exact R1 artifact
by frozen run/name, and execute the same aggregate semantic and byte checks.

The only real receipt states are:

- `PASS_EXP073P_PREREQUISITE_BINDING_V0_2`;
- `REJECTED_EXP073P_PREREQUISITE_BINDING_V0_2`;
- `INCOMPLETE_EXP073P_PREREQUISITE_BINDING_V0_2`.

Only the genuine real v0.2 PASS may set
`support_executor_authorized=true`.  It authorizes only the separately frozen
Exp073P physical-support executor; covariance remains closed.

Synthetic validation must use a distinct synthetic PASS label, include a
mutation proving v0.1's failed R1 authority is rejected, and always retain
`support_executor_authorized=false`.

## Runtime-provenance follow-up

The active venv resolved one concrete Python/numpy/healpy environment before
the mapper began.  Under
`experiments/073r1_v0_6_runtime_provenance_freeze_prereg.md`, its exact versions
must be copied only from immutable execution logs after termination and pinned
for any future exact rerun.  Version capture may not change or reinterpret the
active result.

## Frozen scientific firewall

No v0.2 join implementation may change or inspect downstream values used to
define the support decision.  The following remain frozen:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- positive absolute final-response support envelope while production Wm stays
  signed;
- invalid radial tails outside the rectangle;
- no crop-before-normalization, effective ell, fiducial-P/model weighting or
  post-hoc cuts;
- order: prerequisite join -> physical support -> covariance/whitening ->
  nuisance SVD/rank -> quotient/relation/null -> fresh G8 withheld family.

At freeze time `support_executor_authorized=false`; G7, G8 and G9 are OPEN.
