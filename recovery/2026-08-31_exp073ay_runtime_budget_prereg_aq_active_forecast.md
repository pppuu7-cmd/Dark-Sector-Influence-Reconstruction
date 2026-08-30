# DSIR recovery checkpoint — Exp073AY runtime policy, AQ active, 52% forecast

**Date:** 2026-08-31  
**Classification:** infrastructure/planning only; no scientific gate change; +0 readiness.

## New prospective infrastructure policy

Created:

`experiments/073ay_article3_controlled_twin_runtime_budget_policy_v0_1_prereg.md`

commit:

`3aeffe02afd44c5474cc15cc53007f9beec2b160`.

It was frozen while Exp073AQ run `33327372191` remained IN_PROGRESS, before any AQ replica artifact or comparator authority existed.

Frozen rule:

- new separately preregistered successor angular replica jobs use `timeout-minutes: 360` on unchanged `ubuntu-24.04` standard GitHub-hosted route;
- all PyMaster/thread/input/comparator/exact-equality rules remain unchanged;
- no partial-output reuse;
- if current AQ finishes with valid comparator PASS/FAIL, no Wm_S1 recovery is needed;
- if current AQ terminates before comparator because of infrastructure timeout/failure, it remains infrastructure-INCOMPLETE and a separately frozen fresh Wm_S1 twin recovery may use 360 minutes;
- if 360 minutes is insufficient, no silent hardware/runner/algorithm rescue is allowed; a separately numbered prospective execution-authority succession is required.

This policy adds 0 readiness.

## Forecast document

Created:

`docs/ARTICLE3_52_PERCENT_BARRIER_FORECAST_2026-08-31.md`

commit:

`3740812af4398ed13b193ff3c9bfcc8bce374725`.

Operational forecast under strict current serial authority order:

- earliest plausible >52%-eligible candidate manifest: `1-2 September 2026`;
- central/realistic target: `2-4 September 2026`;
- infrastructure-risk case: `4-8 September 2026 or later`.

These dates assume active continuation with minimal idle gaps. They are not scientific claims and cannot change readiness.

## Why >52% cannot happen immediately

Individual angular task admissions remain +0 readiness. The minimal path to the next readiness opportunity is:

`Wm_S1`

`-> Wm_S2 -> Wm_S3`

`-> ten WW task admissions`

`-> real Exp073AR 14-window execution-qualified aggregate`

`-> real Exp073AS complete immutable 1410-row pre-support finite-operator candidate manifest`.

Only then is a move above the current 52% plateau eligible under frozen accounting.

## AQ status at this checkpoint

Run:

`33327372191`.

Both jobs remain:

- A `99299799192`: `IN_PROGRESS`, step `Compute exact controlled Wm_S1 replica`;
- B `99299799338`: `IN_PROGRESS`, same step.

No comparator authority exists.

Current AQ workflow replica timeout remains 240 minutes; run started `2026-08-30T18:12:00Z`, so the current workflow budget expires around `2026-08-30T22:12Z` / `2026-08-31 01:12 Europe/Helsinki` if compute does not finish first.

Do not launch Wm_S2 while AQ is active.

## Scientific state unchanged

- Article-3 strict readiness: `52%`;
- Layer A: OPEN;
- Layer B: OPEN;
- covariance/whitening: BLOCKED;
- G7: OPEN;
- G8: OPEN;
- G9: OPEN.
