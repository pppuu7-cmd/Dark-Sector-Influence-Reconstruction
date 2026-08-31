# DSIR Article-3 checkpoint — Exp073BD terminal P3 incomplete; Exp073BA active

**Date:** 2026-08-31  
**Scope:** DSIR only. RTK/RQIR excluded.  
**Scientific authority readiness:** **52.0%**  
**Draft/data readiness:** **53.714285714285715%** (display **53.7%**)

Repository state and immutable hosted artifacts outrank chat wording. This checkpoint applies the prospectively frozen Exp073BG terminal-outcome policy; it does not alter any frozen acceptance criterion.

## Authority preserved

- Exp073AQ remains permanent hosted exact-repeatability `SCIENTIFIC_REPEATABILITY_FAIL`; numerical closeness does not rescue it.
- Synthetic/infrastructure/provenance QA remains `+0` scientific authority readiness.
- Track-P provisional objects never become Track-A authority retroactively.
- G7 ordering and the anti-leakage firewall remain unchanged; G8 remains forbidden before actual G7 authorization.

## Exp073BD — terminal hosted outcome

Workflow run: `33342265114`  
Workflow: `Exp073BD Article3 provisional Wm_S2 data v0.1`  
Frozen source head: `2990c51ec1ec263eb883398b21356770401ee83a`  
Run conclusion: `cancelled`  
Run created: `2026-08-31T02:30:56Z`  
Run terminal update: `2026-08-31T05:33:05Z`

### Branch A

Job `99339920252` (`Wm_S2 provisional branch A`) was cancelled while in `Compute independent Wm_S2 provisional branch` after setup, NaMaster 2.7 install, frozen Track-P enforcement, and DES mask-cache compression had succeeded.

The upload step preserved only a PCL precompute artifact, not a complete Wm_S2 object:

- artifact id: `9746718704`;
- artifact name: `exp073bd_wm_s2_branch_a_provisional_pcl_v0_1`;
- artifact digest: `sha256:e7ab0b3859070441532d8778f51faf9c3d7e7a0d6afe8af2546995067b5e15e5`;
- NPY shape/dtype: `<f8 [12288]`;
- NPY SHA256: `16e00d60e8298f94ab6e5d223db823231b84df3b7b588a017acbb208a1dbdb64`;
- metadata class: `provisional_observed_pcl_precompute`;
- metadata stage: `PCL`;
- metadata explicitly says `provisional_only=true`, `science_use=FORBIDDEN`, `readiness_increment=0.0`.

This is a valid preserved intermediate diagnostic payload but **not** the required complete Track-P angular object `<f8 [39,12288]`.

### Branch B

Job `99339920262` (`Wm_S2 provisional branch B`) completed successfully and uploaded a complete provisional object:

- artifact id: `9746250767`;
- artifact name: `exp073bd_wm_s2_branch_b_provisional_v0_1`;
- artifact digest: `sha256:3bd4850d9f768fd36cad34788394b913507d71ec828dee7a68544b44ce6f7481`;
- NPY shape/dtype: `<f8 [39,12288]`;
- NPY SHA256: `10d12a10965b49c9dbba4638c91bd81c0b40cc35bd0d464c8ca837b5231dcb26`;
- metadata class: `provisional_track_p_data`;
- metadata explicitly says `provisional_only=true` and `science_use=FORBIDDEN`.

Branch B is retained as provenance/diagnostic evidence only. It is **not** selected as a preferred branch and cannot receive standalone Wm_S2 draft/data credit under the frozen pair requirement.

### Pair diagnostic

Job `99339920344` (`Wm_S2 provisional pair diagnostic`) was `skipped` because both complete branch inputs were not available. No A/B pair classification exists.

## Frozen classification

Exp073BG was preregistered while BA and BD were still active. Its BD decision rule states that an incomplete/missing branch maps to:

`P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`

Therefore Exp073BD is terminally classified:

**`P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`**

This is **not a scientific FAIL**. It is a terminal incomplete provisional outcome. The completed branch B does not authorize downstream sensitivity propagation, preferred-replica selection, manuscript claim credit, Layer A/B, covariance/whitening, or G7/G8 work.

Readiness delta:

- Verified scientific authority: `+0`;
- Draft/data: `+0`;
- totals remain `Verified 52.0% | Draft/data 53.714285714285715%`.

## Independent provenance defect preserved

Both inspected Exp073BD A/B JSON payloads contain the field:

`"experiment": "Exp073AZ"`

while their `contract_version` is `exp073bd_v0_1` and their artifact/job lineage is Exp073BD. This is recorded as a **metadata/provenance defect** only. It is not asserted as the cause of branch-A cancellation and it does not alter the P3 classification or readiness.

No post-hoc metadata repair may convert this historical BD run into a complete pair.

## Exp073BA status at this checkpoint

Clean rerun `33345968620` remains active. Both A/B compact Wm_S1 jobs have successfully passed frozen enforcement, NaMaster 2.7 installation, immutable Exp073AZ artifact download, and exact AZ->BA PCL binding; both remain inside `Compute low-memory compact Wm_S1 replica`.

No BA comparator authority exists at this checkpoint. Therefore no BA scientific PASS/FAIL is declared and no duplicate heavy workflow is launched.

## G7 / anti-leakage state

Required order remains exactly:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`

No covariance/whitening/nuisance/G7/G8 information may leak into upstream support selection. G8 remains unopened.

## Exact next gate

1. Inspect terminal state of Exp073BA `33345968620`.
2. If both complete compact replicas reach the frozen comparator, consume only the frozen exact comparator result.
3. Exact compact PASS is required before the two frozen finalizers; then final exact PASS plus immutable hosted authority is required for BA scientific authority.
4. Timeout/OOM/runner/harness/resource termination before two complete comparator inputs remains infrastructure/resource failure, not scientific FAIL.
5. Do not relaunch or salvage Exp073BD as the same historical gate; any future Wm_S2 attempt must be a separately prospectively frozen successor after the required upstream authorization.

## Chronology

- `2026-08-31T02:30:56Z` — Exp073BD run `33342265114` created.
- `2026-08-31T02:31:07Z` — branch A job started.
- `2026-08-31T02:31:08Z` — branch B job started.
- `2026-08-31T04:38:54Z` — branch B completed successfully with full `<f8 [39,12288]` artifact.
- `2026-08-31T05:32:55Z` — branch A terminated cancelled during Wm_S2 compute; only PCL `<f8 [12288]` intermediate was preserved.
- `2026-08-31T05:33:05Z` — pair diagnostic skipped and workflow reached terminal `cancelled` state.
- Post-terminal artifact inspection confirmed branch-A incompleteness and branch-B completeness; Exp073BG frozen rule was then applied without modifying its criterion.
