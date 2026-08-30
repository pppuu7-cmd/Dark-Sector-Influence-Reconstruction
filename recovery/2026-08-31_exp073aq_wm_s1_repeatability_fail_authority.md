# DSIR recovery checkpoint — Exp073AQ Wm_S1 hosted repeatability FAIL

**UTC authority completion:** 2026-08-30T22:08:45Z  
**Local +03:00:** 2026-08-31 01:08:45  
**Repository:** `pppuu7-cmd/Dark-Sector-Influence-Reconstruction`  
**Scope:** DSIR only. RTK/RQIR are excluded.

## Authority event

Frozen workflow run:

`33327372191`

Workflow:

`Exp073AQ Article3 controlled twin Wm_S1 production v0.1`

Frozen source head:

`fe89b6c64ee0cee5dbc40080973ec2af2ae683e0`

All three jobs completed successfully at the workflow/infrastructure level:

- replica A job `99299799192` — completed/success;
- replica B job `99299799338` — completed/success;
- exact comparator job `99329163628` — completed/success.

Replica artifacts:

- A artifact `9739721339`, artifact digest `sha256:ec6ab1e6a602bd37f7a781a5e8030b09171905e5800b0cfeeba6fabe06e195a1`;
- B artifact `9739045909`, artifact digest `sha256:4069f4deb3c608f6fb2c1fa686181746901befbe945cc07374c7d32346778e2f`.

Hosted comparator authority artifact:

- artifact `9739725913`;
- name `exp073aq-wm-s1-controlled-twin-authority-fe89b6c64ee0cee5dbc40080973ec2af2ae683e0`;
- digest `sha256:5184bb3034bd2c1bd497ad30db3dbd4e1550d09a0c25af328cdee553385fef03`.

## Frozen comparator result

Terminal status:

`SCIENTIFIC_REPEATABILITY_FAIL_EXP073AQ_WM_S1_CONTROLLED_TWIN_EXACT_V0_1`

Exact contract results:

- `canonical_sha256_identical = false`;
- `numpy.array_equal = false`;
- frozen metadata identical = true;
- single-thread controls verified = true;
- differing bands = `39 / 39`;
- differing entries = `472997 / 479232`;
- maximum absolute difference = `2.0816681711721685e-17`;
- mean absolute difference = `2.5248672723363528e-20`.

Selected-window canonical SHA256:

- replica A: `979c61faea99cf60146078ccdd5a9c75547dcc5a689ee48c4c5f309cf6a10b69`;
- replica B: `5b02a691607dd21ede7601f081767ac3713e300abd5a9e358e4593a6ec486225`.

The magnitude of the difference is irrelevant to classification. The prospectively frozen controlled exact authority contract requires exact canonical SHA equality and `numpy.array_equal == True`. No tolerance, rounding, ULP, majority-vote, preferred-replica, nearest-historical-result, or other rescue exists.

Therefore this is a genuine hosted scientific-computational repeatability FAIL, not an infrastructure-INCOMPLETE state and not a scientific PASS.

## Scientific accounting and firewall

- `Wm_S1` is **not admitted** to the future 14-window authority.
- `Wm_S2` and all successor angular tasks are **blocked** under the current controlled-route contract.
- Exp073AR aggregate cannot be built from this failed route.
- Exp073AS 1410-row candidate manifest cannot be built.
- Layer A remains OPEN.
- Layer B remains OPEN.
- covariance/whitening remains BLOCKED.
- G7/G8/G9 remain OPEN.
- strict Article-3 scientific readiness remains **52%**.
- readiness increment from this event is `+0`.

No covariance, nuisance geometry, support selection, relation/null, G7 or G8 information was used by the comparator. Anti-leakage remains intact.

## Diagnostic-only post-authority inspection

After the hosted comparator had already frozen the FAIL, the two immutable replica artifacts were inspected for root-cause triage only. This inspection cannot reclassify the gate.

Observed numerical distribution over the selected `<f8 [39,12288]` window:

- nonidentical entry fraction `472997 / 479232 = 0.9869896000...`;
- median absolute difference among differing entries `4.486627642487622e-21`;
- 90th percentile `2.604626312806133e-20`;
- 99th percentile `4.336808689942018e-19`;
- 99.9th percentile `3.469446951953614e-18`;
- maximum `2.0816681711721685e-17`.

The replica environment receipts show different hosted CPU models while the frozen software lineage and thread controls match:

- A: AMD EPYC 7763 64-Core Processor;
- B: AMD EPYC 9V74 80-Core Processor.

This is only an observed environment difference and a candidate source of floating-point nondeterminism. It is **not** a causal diagnosis and cannot rescue the exact repeatability gate.

## Next admissible work

The current successor chain is blocked by the negative authority. Do **not** launch Wm_S2.

Only a separately numbered, prospectively frozen authority-succession/root-cause protocol may investigate whether a more tightly pinned execution environment or different deterministic implementation can establish a new authority class. Such work must:

1. preserve Exp073AQ permanently as FAIL;
2. make no post-hoc tolerance change;
3. use no failed-replica payload as a preferred numerical target;
4. remain `+0` readiness until a separately authorized scientific chain reaches the previously frozen readiness gate;
5. preserve all Article-3 support thresholds and anti-leakage firewalls.
