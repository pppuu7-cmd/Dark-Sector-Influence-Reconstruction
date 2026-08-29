# Exp073P v0.3 authority ready before Exp073R1 v0.7 attempt-2 output

Date: 2026-08-29
Repository: `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`
Scope: DSIR only; RTK was not read, changed or used.

## Recovery headline

The only active heavy candidate remains Exp073R1 v0.7 run `33240490287`, run
attempt `2`, job `99080934021`.  At `2026-08-29T10:30:49Z` the job was still
`queued` and the run artifact list was empty.  No heavy duplicate was launched
and no R1 result or downstream physical quantity was inspected.

Before that future output existed, PR #166 gained a new immutable Exp073P v0.3
authority and executable route:

- preregistration commit
  `940fbca20e64e906b4fd61d1d40f340b7db1175e`;
- implementation commit
  `6f463758a3b943060cfbb9cd8180091beee56ff8`;
- branch `automation/exp073r1-v07-artifact-firewall-20260829`;
- PR `https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/pull/166`.

This closes an execution-integrity gap only.  It is not an R1 reproduction
result and not an Exp073P physical-support result.  At this checkpoint
`support_executor_authorized=false`; G7/G8/G9 remain OPEN.

## Why v0.3 was required

Aggregate join v0.1 is permanently bound to the PEP-668-failed v0.6 job.
Aggregate join v0.2 is permanently bound to v0.6 run `33222848695`, job
`99020389131`, which failed by remote EOF; that run also has two same-name
inadmissible artifacts.  Neither historical route may be repointed.

The active v0.7 workflow uses one SHA-only `if: always()` upload.  Attempt 1
lost the runner and produced no artifact, so the risk has not materialized.
Attempt 2 can still be consumed safely only if a new prospective join binds
the exact attempt/job and rejects every partial, duplicate or later-attempt
upload.  v0.3 implements that boundary without modifying the active heavy run.

## Frozen v0.3 R1 authority

Only the following execution can cross v0.3:

- run `33240490287`, `run_attempt=2`;
- job `99080934021`, `transport-stabilized-replay`;
- head `9a4606fb37d5aaa071aa57322ebb7c05eca905d7`;
- workflow
  `.github/workflows/exp073r1-desy1-transport-stabilized-replay-v0-7.yml`;
- workflow blob `99ce26540f15620c9c6a7acd9198b9d5fe81ecb6`;
- workflow SHA256
  `8ef3fb2305fe2789e6198547f5095969cfc107df1f0e17853b20a7aa5c601328`;
- evaluator blob `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- evaluator SHA256
  `5d4fcd8eebe0ae3a45b173a9f5ad261f014586ec81c5587e8720f3290254483e`;
- artifact name
  `exp073r1-v07-transport-stabilized-9a4606fb37d5aaa071aa57322ebb7c05eca905d7`.

Attempt-1 job `99068879596`, every later run attempt, every replacement job,
every other head/workflow and every v0.6 artifact are rejected.  If another
attempt creates a second artifact under the same frozen name, v0.3 rejects
artifact multiplicity instead of choosing an output post hoc.

## New executable files and byte identities

- `ci/exp073p_aggregate_prerequisite_join_v0_3.py`, SHA256
  `d5953f447ea1b189599bf26a3f7ffe0c9b879439b5af2ffa1b702b83f27e8d41`;
- `ci/exp073p_actions_metadata_bundle_v0_3.py`, SHA256
  `fc74c64c096528eac5179202f32ad1de275416b754b76ed19ba5d7be9da8bb43`;
- `ci/exp073p_v07_r1_payload_bundle_v0_3.py`, SHA256
  `a1825a45c9683797e0faf5f232eafad2f81cf12b69bd758f0a2c8768c0b28a3c`;
- `.github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-3.yml`,
  SHA256
  `4afd3b990f4741156e3dda853c704d62e7cc6224dbe51f514b7eaf60de369a87`;
- `.github/workflows/exp073p-aggregate-prerequisite-join-v0-3-selftest.yml`,
  SHA256
  `478490ee0d064a16dc1ce6cd377766ac0871502536c60e2a48345c7d01a73289`;
- preregistration file SHA256
  `f33b4d761173e43809b209d4bc1f2059ba022f9d4dc71e8b21b84b40fe4a6a25`.

The evaluator privately loads and byte-freezes v0.1; v0.1 and v0.2 files were
not edited.  All nine non-R1 parent identities and semantic checks therefore
remain unchanged.

## Fail-closed interlocks

### Actions identity

The live collector requires complete first-page pagination (`total_count`
equals returned rows), exact repository/run/head/workflow, `run_attempt=2`,
the attempt-specific jobs endpoint, exact job ID/name and completed/success
states.  It also requires exactly one non-expired frozen-name artifact and
cross-checks the user-supplied artifact ID/digest against live metadata.

### Acquisition provenance

The semantic evaluator requires all remote attempts to start at byte zero,
send no Range header and receive no Content-Range.  Every nonterminal attempt
must be only `INFRASTRUCTURE_TRANSPORT_FAILURE`.  The last attempt must be HTTP
200 and `PASS_EXACT_OBJECT_IDENTITY` with exactly `84,075,649,920` bytes and
SHA256
`39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`.
Final acquisition bytes/hash are cross-bound to the R1 summary.

### Complete artifact payload

The payload validator rejects duplicate basenames, missing/extra bin
identities, empty files and byte/hash disagreement.  A complete candidate must
contain exactly one summary, acquisition record and runtime record, plus four
pixel records and four masks.  Record bytes must equal `selected_rows*4`;
each RING `nside=4096` mask must be exactly `25,165,824` bytes.  Every actual
SHA256 is compared with the terminal summary before byte-preserving
normalization.

### Scientific no-leakage

The v0.1 R1 interlock remains authoritative for the exact internal PASS,
source/metacal identities, `136930995` rows, selection, HEALPix mapper,
nonempty bins, repeatability and Exp073R0 controls.  The v0.3 join additionally
requires all acquisition/payload no-leakage flags false.  It reads no support,
covariance, whitening, nuisance, relation/null, held-out or G8 value.

Synthetic PASS labels cannot authorize the physical-support executor.  Only a
future genuine real receipt `PASS_EXP073P_PREREQUISITE_BINDING_V0_3` may set
`support_executor_authorized=true`.

## Verification record

Local checks:

- inherited v0.1 aggregate mutation suite: PASS;
- 19 new v0.3 evaluator mutations: rejected;
- 10 inherited plus 5 new live-metadata mutations: rejected;
- four complete-payload file/multiplicity mutations: rejected;
- both new workflows parsed with `yaml.BaseLoader`;
- `compileall`, all repository JSON parsing and `git diff --check`: PASS;
- repository tests: `44 passed`.

Hosted PR self-test:

- run `33248034308`, job `99088793819`: `completed/success`;
- all lineage, evaluator, metadata, payload and synthetic-receipt steps:
  `success`;
- artifact `9713466820`, digest
  `sha256:d53b87eec234c3533fd9d167bfdae7433db27e4aa106a614c2dd5812a9f6019e`;
- internal synthetic receipts retain
  `support_executor_authorized=false`.

No real aggregate workflow was dispatched.

## Exact recovery and continuation procedure

1. Read `docs/RECOVERY_MANUAL.md`, `docs/RECOVERY_LATEST.md`, then this file.
2. Fetch `main` and PR #166 before any edit.  Do not create another v0.7 heavy
   run while `33240490287` attempt 2 exists.
3. Verify the v0.3 byte identities listed above.  Reproduce local checks with:

   ```text
   python3 ci/exp073p_aggregate_prerequisite_join_v0_3.py --selftest --out /tmp/join-v03.json
   python3 ci/exp073p_actions_metadata_bundle_v0_3.py --selftest --workflow .github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-3.yml --out /tmp/route-v03.json
   python3 ci/exp073p_v07_r1_payload_bundle_v0_3.py --selftest --manifest-out /tmp/payload-v03.json
   uv run --with pytest pytest -q
   ```

4. Re-read run `33240490287`, attempt-2 job `99080934021` and all run
   artifacts.  Record the exact terminal step boundary before classification.
5. If the job is runner/transport/infrastructure failed, preserve provenance,
   keep science unscored and do not dispatch the aggregate join.
6. If Actions is success, still require the unique artifact, exact ID/digest,
   complete 11-file payload, acquisition identity PASS and internal
   `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`.
7. PR #166 must be merged before a real v0.3 dispatch; the production workflow
   deliberately requires `refs/heads/main`.  Dispatch it manually with the
   independently copied exact artifact ID and digest.  Never run v0.1/v0.2.
8. If attempt number, job, head, workflow or artifact multiplicity differs,
   v0.3 must remain rejected.  Freeze a new version before any later candidate;
   never edit v0.3 post hoc.
9. Only after genuine aggregate PASS run the separately frozen physical-support
   executor.  Then preserve the fixed order: covariance/whitening -> nuisance
   SVD/rank -> quotient/relation/null -> fresh G8.

## Frozen scientific boundaries

Do not change:

- `0.295 <= z <= 2.33`;
- `k <= 0.06664762008318016 Mpc^-1`;
- `f_invalid <= 0.05` inclusive;
- minimum retained full-coordinate dimension `15`;
- `nside=4096`, RING, celestial C, `lonlat=True`;
- positive absolute final-response support envelope; production Wm signed;
- radial tails outside the rectangle invalid;
- no crop-before-normalization, effective ell, fiducial-P/model weighting or
  post-hoc cuts;
- no downstream leakage into prerequisite/support selection.

At this checkpoint no physical result is claimed.  G7/G8/G9 are OPEN.
