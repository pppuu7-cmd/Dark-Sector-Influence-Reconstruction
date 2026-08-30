# Article-3 52% barrier forecast — 2026-08-31

**Status:** planning/operations forecast only. Not a scientific gate, not authority, and not a readiness increment.

## Current state at forecast freeze

- strict Article-3 scientific readiness: `52%`;
- Exp073AQ run `33327372191` is still IN_PROGRESS;
- both Wm_S1 replicas are still in the exact controlled compute step;
- AQ started `2026-08-30T18:12:00Z` (`2026-08-30 21:12` Europe/Helsinki);
- current AQ replica timeout: 240 minutes;
- no AQ replica artifact or comparator authority exists at forecast freeze;
- Exp073AY runtime-budget policy was prospectively frozen before any AQ output, allowing 360-minute replica budgets for future separately preregistered tasks while changing no scientific/numerical criterion.

## What actually has to happen before >52% is even eligible

Individual exact angular admissions earn `+0` readiness.

The currently authorized minimal chain to the next scientific-readiness opportunity is:

1. valid exact Wm_S1 admission;
2. Wm_S2 exact twin admission;
3. Wm_S3 exact twin admission;
4. ten WW exact twin admissions in the already frozen order;
5. real execution-qualified 14-window aggregate under Exp073AR;
6. real complete Exp073AS 1410-row pre-support finite-operator candidate manifest.

Only after this chain exists can the project legitimately consider increasing the strict Article-3 readiness above 52%. Later Layer-A/Layer-B/covariance/G7 steps are still required for much higher readiness, but they are not required merely to leave the 52% plateau if the real candidate-manifest gate is successfully established under the frozen accounting.

## Runtime observations

Wm_S1 has already consumed roughly three wall-clock hours with two replicas running in parallel. The wall-clock cost of a task is therefore approximately the duration of one replica rather than the sum of both replicas.

The remaining angular tasks are serial at the **authority-admission level** under the current frozen order. They may not be treated as one unfrozen batch. WW spin-2 x spin-2 coupling is expected to be at least as expensive as Wm spin-0 x spin-2 and may be materially more expensive; therefore extrapolating three hours per every future task is an optimistic lower bound, not the central estimate.

## Forecast scenarios

All scenarios assume active continuation with no idle gaps between completed gate inspection, prospective freeze of the next task, and launch.

### Optimistic

Assumptions:

- AQ completes before its 240-minute timeout;
- remaining Wm tasks average ~3 hours each;
- WW tasks average ~3-4 hours each;
- no exact-twin mismatches;
- no infrastructure failures;
- aggregate/join are lightweight relative to angular production.

Estimated time to the first >52%-eligible real candidate manifest:

**~40-50 wall-clock hours from the current point.**

Calendar estimate: approximately **1-2 September 2026** Europe/Helsinki.

### Central / realistic

Assumptions:

- one or more angular tasks use 4-5.5 hours of the 6-hour standard hosted budget;
- WW tasks are slower than Wm tasks;
- small preregistration/workflow/authority-inspection overhead exists between tasks;
- no major repeatability failure.

Estimated time:

**~60-90 wall-clock hours of active serial progression.**

Calendar estimate: approximately **2-4 September 2026**.

### Conservative infrastructure case

Assumptions:

- AQ reaches its 240-minute infrastructure timeout and requires a fresh 360-minute recovery;
- one or more later tasks hit infrastructure failures or the standard hosted six-hour ceiling;
- no scientific repeatability FAIL, but prospective execution-route repair is required.

Estimated time:

**~4-8 days or longer**, depending on whether a >6-hour task forces a separately qualified execution-authority succession.

Calendar estimate: approximately **4-8 September 2026**, with a longer tail if a new route must be qualified.

## Most important forecast risk

The dominant risk is no longer missing schema/governance preparation. AR through AX have already removed many downstream procedural ambiguities.

The dominant near-term risk is **high-resolution NSIDE=4096 angular runtime under exact controlled execution**. Current AQ has already demonstrated that a 240-minute task budget has little headroom. Exp073AY reduces avoidable timeout risk for future tasks to the standard-hosted 360-minute ceiling, but it cannot make a computation faster and does not authorize hardware/route changes.

A second risk is exact computational repeatability: any task-specific A/B mismatch is a real computational repeatability FAIL under the frozen comparator and blocks progression rather than being averaged or tolerance-rescued.

## Forecast conclusion

If the present controlled route behaves normally, the best current forecast for leaving the 52% plateau is:

**central target: 2-4 September 2026.**

**earliest plausible: 1-2 September 2026.**

**infrastructure-risk case: 4-8 September 2026 or later.**

These are operational estimates only. The readiness number changes only after real hosted authority exists; elapsed time or successful synthetic/infrastructure QA never changes readiness by itself.
