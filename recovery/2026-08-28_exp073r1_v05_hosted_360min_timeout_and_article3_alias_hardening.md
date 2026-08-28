# DSIR checkpoint — Exp073R1 v0.5 hosted-run timeout + Article-3 anti-leakage alias hardening

Date: 2026-08-28
Branch: `main`

## Exp073R1 v0.5 authoritative run

Authoritative run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/33175886694

Observed terminal state: `completed / cancelled`.

The cancellation is classified as **infrastructure/runtime-limit**, not scientific FAIL.

Evidence from the authoritative `metacal-map` job:

- `source-index`: PASS.
- immutable Exp073R0 parent binding: PASS.
- mapper started at 2026-08-28 14:08:25 UTC.
- progress reached row `54,525,952 / 136,930,995` with selected counts `[1,984,085, 2,072,589, 2,214,036, 1,140,871]`.
- GitHub cancelled the operation at 2026-08-28 20:08:19 UTC, i.e. essentially the configured `timeout-minutes: 360` boundary.
- the final Exp073R1 PASS assertion never executed.
- reconstruction artifact upload never executed.

Therefore:

- `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1` is **not** established;
- no scientific FAIL is established;
- G7/G8/G9 remain OPEN;
- Exp073P physical support-validity scoring remains unauthorized;
- covariance restriction/whitening, nuisance tangent SVD/rank, quotient/relation/null control, and fresh G8 remain blocked.

A blind re-run of the same hosted v0.5 job is not launched because the same 360-minute hard ceiling would reproduce the infrastructure failure without adding scientific information. Recovery must preserve the frozen no-Range / whole-object identity and parent-binding semantics while moving the full stream computation onto an execution path that can actually finish (e.g. a sufficiently long-lived runner or an equivalently strong preregistered streaming architecture). Frozen acceptance criteria are not to be weakened to fit hosted-run limits.

## Article-3 anti-leakage execution hardening

The previously recorded lexeme alias gap is addressed independently without changing any frozen scientific acceptance criterion.

Added:

- `ci/article3_antileakage_alias_hardening_v0_2.py`
- `.github/workflows/article3-antileakage-alias-hardening-v0-2.yml`

The hardening canonicalizes key names by lowercasing and removing non-alphanumeric separators before forbidden downstream-token matching. Synthetic tests explicitly cover aliases including `p_value`, `p-value`, `P VALUE`, `chi_squared`, `chi-squared`, `inverse_covariance`, `inverse-covariance`, nested nuisance/whitening/relation keys, and G7/G8 aliases, while clean physical-support payloads remain accepted.

This CI is strictly `SYNTHETIC_ONLY_EXECUTION_HARDENING`; it cannot score the real science gate or authorize covariance restriction. Initial workflow run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/33207505723

## Required order remains frozen

1. validated physical forward/power-input bridges;
2. genuine Exp073R1 physical reconstruction PASS;
3. preregistered physical support-validity mask;
4. covariance restriction/whitening;
5. nuisance tangent rank/SVD;
6. quotient/relation/null control;
7. only then fresh G8 withheld family.
