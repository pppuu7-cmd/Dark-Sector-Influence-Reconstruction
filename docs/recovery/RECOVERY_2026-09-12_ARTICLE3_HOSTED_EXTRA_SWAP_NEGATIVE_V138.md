# DSIR Article III recovery V138 — hosted extra-swap route tested negative

Date: 2026-09-12. Scope: **DSIR only**. V137 and all earlier recovery notes remain immutable history.

## Scientific frontier — unchanged
Canonical 8193->16385 remains independently verified `COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`.

Frozen science is unchanged: `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, same physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0, lookup mismatch `<=1e-12`.

No 16385->32769 scientific execution has occurred. `HIGH_MEMORY_RESOURCE_LIFECYCLE_PREFLIGHT_PASS=FALSE`; no real durable resource authority, actual live-guard PASS or current-run authorization exists. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Why V138 was opened
V137 saturated parser-corrected hosted static/control-plane preparation and left a physical higher-memory runner as the active resource blocker. V138 prospectively tested one remaining non-biasing hosted alternative: whether standard GitHub-hosted Ubuntu could complete the exact parser-corrected canonical 32769 resource computation after adding swap, without reading scientific transfer values.

This is a resource/infrastructure experiment only (`+0/+0`). It does not alter the scientific engine, tolerance, step size, grid, domain, masks, interpolation, estimator, accounting, or stopping rule.

## Probe and prospective repair
Parser-corrected single-role probe:
- `ci/layerb_32769_parser_1mib_single_role_candidate_probe_v0_2.py`
- creation commit `e8bc32b152307828dcde8138f8ea7d82a3b0783b`
- Git blob `f8776ae1e9e0c325f1a3f5f01b4388e1c93ef7e2`.

An initial workflow run `34659804885` proved that standard hosted VMs accept added `swapon`, but the experiment then failed a cross-runner ELF SHA assertion after the exact source build completed. This was classified as infrastructure reproducibility, not resource/science failure. Before rerunning, the repair was frozen in `docs/dsir4/contracts/LAYERB_32769_HOSTED_EXTRA_SWAP_RESOURCE_FEASIBILITY_REPAIR_CONTRACT_V0_2.json`, creation commit `c5dcb067406073dbbbe851cd679cee3dc4387e5a`, Git blob `8da137f5ee260fc0aede75c22ed292e47d32157b`.

The repair preserves exact CLASS commit, exact point/parser source pre/post hashes, exact DSIR compatibility/public-exposure patches and build-authority V0.2 identity, while recording rather than equating the toolchain-dependent executable bytes. Scientific production binary identity was not changed.

## Parallel hosted extra-swap result
Repaired workflow:
- `.github/workflows/layerb-32769-hosted-extra-swap-resource-feasibility-v0-2.yml`
- creation commit/head `eb1273af37024b839326141b389e002330c2499d`
- Git blob `0c7d2b014464d4bd2c9f993b4d093e5109b59cc0`
- run `34659953959`.

Five independent hosted jobs were run in parallel:
- `103460194789`: `reference`, +8 GiB swap;
- `103460194951`: `alpha_minus`, +8 GiB swap;
- `103460194926`: `beta_plus`, +8 GiB swap;
- `103460194973`: `beta_minus`, +8 GiB swap;
- `103460194914`: independent `reference`, +12 GiB swap.

All five passed checkout, frozen-identity checks, swap activation, and exact parser-corrected source build. All five then terminated during the response-blind `Class.compute(["transfer"])` resource probe before a completed role receipt existed. Available terminal logs for the four +8 GiB roles and the +12 GiB reference show runner shutdown / exit code 143 during the probe. The +12 GiB reference began the probe at approximately `2026-09-11T23:58:34Z` and the runner shutdown was recorded at `2026-09-12T00:05:25Z`.

Because the hosted runner was shut down during compute, the per-lane `always()` upload step could not execute; this is why the finalizer contains no completed role result artifacts. No scientific transfer values were read.

Independent finalizer job `103461606069` completed successfully and classified the source experiment as:
`LAYERB_32769_HOSTED_EXTRA_SWAP_INFRASTRUCTURE_FAIL_PLUS_0_PLUS_0`.

Final artifact:
- artifact ID `10287222231`;
- ZIP SHA256 `4cb9be648cb448215ee5b9e9d0d649dccd8b212d9b45313b9e39c2b093b1ed9b`;
- `all_four_roles_pass_at_extra_swap_8gib=false`;
- `reference_pass_at_extra_swap_12gib=false`.

Durable authority:
- `docs/dsir4/authority/LAYERB_32769_HOSTED_EXTRA_SWAP_RESOURCE_FEASIBILITY_V0_2.json`;
- latest authority content blob `9a46702839bd08de3c7a27a60dcdbf544977bf76`;
- latest authority commit `4b170a6b0bd7575d4a02a771934329560defbefa`.

No exact minimum RAM requirement is inferred from these results and no linear memory extrapolation is authorized.

## Prospective dependent gate proved fail-closed
Before the feasibility result was known, a dependent sequential-lifecycle gate was frozen:
- contract `docs/dsir4/contracts/LAYERB_32769_HOSTED_SWAP_SEQUENTIAL_LIFECYCLE_GATE_V0_1.json`, creation commit `55a0302edd8da352d2baef7d9fb12903c8beca77`, blob `53c26f82d821ecb39f3be97c3942134ec8452150`;
- event workflow `.github/workflows/layerb-32769-hosted-swap-sequential-lifecycle-v0-1.yml`, creation commit `59c65ed75f10e7cf91d0bb36bb1cb3ba6d0ec84b`.

It was authorized to launch exactly one sequential four-role hosted lifecycle only if source run `34659953959` produced exact `LAYERB_32769_HOSTED_EXTRA_SWAP_ALL_FOUR_ROLES_FEASIBLE_PLUS_0_PLUS_0` with all four +8 GiB roles complete.

Event run `34660445579` correctly failed its source-gate job `103461646780` on that unmet assertion. Dependent jobs were skipped:
- sequential lifecycle `103461686830`: `skipped`;
- independent verifier `103461686949`: `skipped`.

Therefore no dependent lifecycle and no science were launched from a failed feasibility result.

## Interpretation
The tested standard GitHub-hosted alternatives are now closed for +8 GiB and +12 GiB added-swap configurations. This is stronger resource evidence than the original default-swap exhaustion, but it remains resource/infrastructure evidence only. It does not establish an exact RAM threshold and does not imply scientific failure.

Further blind escalation of hosted swap size is not justified by current evidence. The efficient frontier returns to the isolated physical higher-memory route already prepared in V137.

## Remaining true blockers
1. Configure/attach a real isolated runner with unique name, `--no-default-labels`, exact custom label `dsir-32769-highmem`, and physical `MemTotal > 16373452 kB`. `32 GiB` remains preferred execution guidance only, not a proven minimum.
2. Dispatch exactly one current V0.3 response-blind measured 32769 lifecycle pilot and obtain real resource PASS.
3. Real artifact must pass independent consumer V0.3 -> candidate packaging V0.2 -> materializer V0.2.
4. Real candidate must pass promotion review V0.2 and exact reviewed bytes must be deliberately copied to durable resource authority.
5. Inside the first production run, immediate one-live guard V0.2 and current-run-only one-run authorization V0.2 must PASS.
6. Only then exactly one canonical 16385->32769 scientific run may execute and be independently terminal-consumed.

Old superseded run `34550495778` / job `103112190909` remains queued on generic `[self-hosted, Linux, X64]` and must not receive the dedicated runner.

## Readiness
`ARTICLE3_REPOSITORY_READINESS: 68%`.

Funnel-freeze/scientific frontier: `67%`.

`WORKING_PLAN_COMPLETION: 88%`.

The operational increase from V137 87% to V138 88% reflects closure of a scientifically admissible hosted-resource alternative and proof that its dependent event chain fails closed. It is not scientific or publication progress; convergence remains open.

## Exact next action
Do not run more arbitrary standard-hosted swap escalations. Attach a qualifying isolated higher-memory runner and dispatch exactly one V0.3 response-blind lifecycle pilot. Production science V0.2 remains forbidden until measured resource authority and live authorization exist.
