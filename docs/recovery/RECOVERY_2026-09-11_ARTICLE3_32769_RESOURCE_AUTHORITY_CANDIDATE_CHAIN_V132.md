# DSIR recovery V132 — resource authority candidate packaging chain

Date: 2026-09-11. Scope: **DSIR only**. V132 extends authoritative V131; all earlier recovery notes remain immutable.

## Scientific frontier — unchanged
Canonical 8193→16385 remains independently `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No scientific 16385→32769 execution occurred. No measured 32769 resource PASS, real one-live PASS or real one-run authorization exists. Covariance restriction remains unauthorized and Wm_S3 remains closed.

## V131 inherited closure
V131 already prospectively closed the dormant scientific engine and dispatch-only production workflow in addition to all earlier 32769 canonical/build/terminal/resource-consumer/materializer/guard/authorizer prerequisites. V132 does not change their science or execution authority.

## Resource-authority candidate provenance packager — closed
Packaging contract:
- `docs/dsir4/contracts/LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_CONTRACT_V0_1.json`;
- creation commit `75acbba1e76fec5f61c1c32ee2e8cd6315dda58b`;
- Git blob `ade2fd2d43ce7e556bf473f93ae8491a694e868f`.

Packager:
- `ci/layerb_32769_resource_authority_candidate_packager_v0_1.py`;
- creation commit `ff5e3ed2659891e80486a95b2a0bfe188a190372`;
- Git blob `c92ffc97c04c27ff6cdbf05b7f84527884848f40`.

The packager requires exact completed source and independent workflow identities; exactly one required job and artifact on each side; SHA256 of both downloaded artifact ZIPs matching GitHub API digest when present; exact source-result classification; exact independent validation classification; source-result SHA matching the independent validation binding; and chain receipt binding to the same source run/head/conclusion and independent-validation SHA. Output is provenance/candidate-only and cannot create a durable repository authority or authorize science.

Synthetic audit run `34637254849`:
- source job `103388059249` — SUCCESS;
- independent verifier `103388098677` — SUCCESS;
- artifact `10278453264`;
- artifact ZIP SHA256 `7c21596f22fd19987aedd0def81cdcf6f8e64fae4359e35569584a4022bde9c3`;
- summary SHA256 `e71946167b9b2b91362e575e357d009248d6f7ad6c221f0acabfa344392a660f`;
- PASS receipt SHA256 `9831cf697adba335f53bee073fff34c2854b9ddfef982f80ef4780569dbb7639`.

Verified fail-closed cases include artifact ZIP digest mismatch, duplicate exact source artifact, chain/source-run mismatch and source-result/independent-validation hash mismatch.

Durable synthetic authority:
`docs/dsir4/authority/LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGER_SYNTHETIC_AUDIT_V0_1.json`, creation commit `e0b2ee3847c998cee065e60fa53c7b37a8f6552b`.

## Real read-only candidate-packaging event chain — closed statically
Workflow:
- `.github/workflows/layerb-32769-resource-authority-candidate-packaging-v0-1.yml`;
- creation commit `5478e7e3976338ee30cd22f4de1beb2ab58ae5c3`;
- Git blob `93dc50385c4b126b91d384e79f6b7079bae283a6`.

It triggers only when the exact independent resource-consumer workflow completes. It checks out the triggering head SHA, queries source/independent GitHub jobs and artifacts, downloads exact ZIPs, invokes the frozen provenance packager, and only after provenance PASS invokes the hardened resource materializer. It uploads a `resource_authority_candidate.json` plus provenance/receipt as an Actions artifact.

Repository permissions are strictly `contents: read` and `actions: read`; there is no commit/push/write path. The candidate receipt explicitly says `candidate_only=true` and `durable_repository_authority_created=false`. A not-ready provenance result fails the workflow closed.

Static audit run `34637435128`:
- source job `103388656014` — SUCCESS;
- independent verifier `103388709957` — SUCCESS;
- artifact `10278693444`;
- artifact ZIP SHA256 `b14abf859ea61bc35dbe04d6fef6b83ab312b3af41e0dbff50b2e3e366c54bbb`;
- result JSON SHA256 `2322299bd4205e22308214ca62340de100132a155c4b1592c93dbf7ab0fbfa68`.

Durable static authority:
`docs/dsir4/authority/LAYERB_32769_RESOURCE_AUTHORITY_CANDIDATE_PACKAGING_STATIC_AUDIT_V0_1.json`, creation commit `ebd12c93dfc6ffccd3bfff27f756805056cd3ffb`.

## Consequence
After a future successful measured high-memory pilot, the chain is now prospectively:
`isolated resource pilot → hosted independent consumer → API-backed provenance packager → hardened materializer → read-only authority candidate artifact`.

The only remaining authority promotion step is deliberate verification and creation of the durable repository file `docs/dsir4/authority/LAYERB_32769_HIGH_MEMORY_RESOURCE_LIFECYCLE_V0_1.json`. This promotion is intentionally not automatic.

## Remaining true blockers
1. Real isolated `dsir-32769-highmem` runner with no default labels and physical `MemTotal > 16372440 kB`.
2. Exactly one measured response-blind V0.2 resource/lifecycle pilot PASS.
3. Successful automatic independent-consumer/candidate-packaging chain, followed by deliberate durable resource-authority promotion.
4. Actual first-production one-live guard PASS.
5. Real current-run-only one-run authorization.
6. Only then exactly one canonical scientific 16385→32769 run and independent terminal consumption.

The current GitHub connector still exposes no physical self-hosted runner administration/enumeration; runner presence/configuration is not inferred.

## Readiness
Frozen publication metrics remain `ARTICLE3_REPOSITORY_READINESS=68%` and funnel-freeze readiness `67%`.

Operational roadmap tracking advances from V131 `80%` to **`WORKING_PLAN_COMPLETION=81%`**. The increment is candidate-provenance/packaging closure only; measured resource and scientific convergence remain open.

## Exact next permitted action
Attach/use a qualifying isolated `dsir-32769-highmem` runner and dispatch exactly one V0.2 response-blind resource/lifecycle pilot. Do not dispatch scientific production before the resulting real resource-authority candidate has been independently checked and deliberately promoted to the durable repository authority path.
