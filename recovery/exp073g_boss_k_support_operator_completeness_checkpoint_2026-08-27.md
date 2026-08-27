# Recovery checkpoint — Exp073G BOSS k-support operator completeness — 2026-08-27

## Current scientific state

- Exp073F remains `PERTURBATIVE_OBSERVATIONAL_ROUTE_CANDIDATE_FOUND_EXP073F`.
- Exp073G remains governed by `experiments/073g_kids_boss_bnt_exact_physical_support_prereg_v0_1.md`.
- Frozen support rectangle: `z=[0.295,2.33]`, `k=[0.000704833374744468,0.06664762008318016] Mpc^-1`.
- Frozen maximum positive invalid-support fraction: `0.05`.
- Frozen dimensional floor: at least 15 retained coordinates with mm, signed Wm and WW represented.
- Pre-output KiDS/BOSS/BNT binding is immutable in `data/derived/g7/exp073g_kids_boss_bnt_operator_binding_v0_1.json`.

## New pre-output finding

The frozen BOSS `mm` coordinate is a configuration-space `xi_wed` observable. Its release window acts on a discrete radial/configuration-space representation. A P-independent Fourier–Bessel response has kernel proportional to `k^2 j_l(k s)`. Taking a positive envelope, as Exp073G requires to forbid cancellation, removes conditional oscillatory convergence; the absolute all-k operator is not release-normalizable without an additional theory weight or k cutoff.

No such theory weight/cutoff was frozen before support output. It must not be introduced post hoc.

## Execution path

Workflow:

`.github/workflows/exp073g-boss-k-support-operator-completeness-v0-1.yml`

Implementation:

`ci/exp073g_boss_k_support_operator_completeness_v0_1.py`

Expected trustworthy classification if exact pinned source/hash/contract checks pass:

`FAIL_EXP073G_REPRODUCTION_OR_PROVENANCE`

This is an operator/reproduction result, not `FAIL_KIDS_BOSS_BNT_PHYSICAL_SUPPORT_EXP073G`; no support fraction or retained dimension is evaluated.

## What must happen next

1. Run and preserve the immutable operator-completeness result.
2. If source/hash checks fail, repair only infrastructure/provenance reproduction and rerun the same frozen audit; do not change the physical criteria.
3. If the trustworthy provenance classification is confirmed, preserve it permanently.
4. Then preregister a separate observational-operator branch using a public mm-sensitive observable with a finite, immutable k-space window/support measure (preferred: Fourier-space BOSS/eBOSS power-spectrum wedges/multipoles with released k bins/windows), while retaining the same C3+C5 rectangle and 5% rule unless a new scientific branch explicitly asks a different question.
5. Do not read covariance, nuisance rank, relation residuals or G8 until a later physical-support PASS authorizes covariance restriction.

## Gate state

G7 OPEN.  
G8 OPEN.  
G9 OPEN.
