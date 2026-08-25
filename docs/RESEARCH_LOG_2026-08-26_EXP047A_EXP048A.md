# DSIR research log — 2026-08-26 — Exp047A / Exp048A

## 00:xx EEST — close Exp047B

PR #26 completed all current-head regressions and was merged to `main` as

`d10cdbdd6ac189ac4ef0cb83d6574105a912ab59`.

Hard result retained as F17: interaction-tier ordering survives all 12 single-node deletions; GDM/f(R) pairwise interaction localization remains `eta_I~0.55-0.655`; smooth-w absolute `chi_I` is low-k-node sensitive.

## Exp047A — finite-amplitude response geometry

Created branch `research/finite-amplitude-interaction-curvature-v0-1`, PR #27.

Reused exact immutable C1/C2/C3/C5 solver artifacts already admitted to the atlas. No new cosmological evolution equation or solver parameter was introduced.

First successful reproducible target:

- run `32900174734`;
- science head `efdd85847d4244285716824f960329fa24cbf852`;
- artifact `9582737965`;
- SHA256 `95d6ce81bc208443ca2377c6f1c4b9523393e2620a2876a2fb53c36a8beabb37`.

Operator controls pass to much better than `1e-12`.

Sampled finite-amplitude `chi_I` envelopes remain non-overlapping:

`IDE < smooth-w < GDM < designer f(R)`.

Ranges:

- IDE `1.4351e-11..5.4945e-11`;
- smooth-w `0.00108051..0.00108806`;
- GDM `0.0130105..0.0454103`;
- f(R) `0.173327..0.313326`.

No scientific classification threshold was post-frozen because these finite products had already been inspected. Result is hard descriptive geometry, not a universal-law PASS.

### New finite-trajectory result

The response ray need not remain straight at finite amplitude.

- smooth-w: max full turn `0.155 deg`;
- IDE alpha: `0.251 deg`;
- IDE beta central: `0.00414 deg`;
- GDM cs2: `0.0279 deg`;
- GDM cv2: `7.1765 deg`, interaction turn `12.1916 deg`;
- f(R): `12.1367 deg`, interaction turn `12.9969 deg`.

Hard methodological consequence: a one-parameter microscopic family can generate several significant global response modes because a one-dimensional manifold is curved. Therefore keep separate `N_micro`, `N_manifold`, `N_repr`, `N_disc`.

Added standalone F18, updated BuyanovGPT atlas, STATUS, RECOVERY_LATEST, and recovery appendix.

## Preliminary localization clue found after Exp047A

For interaction residual `I`, inspected normalized squared-energy marginals

`q_k(k)=sum_z I^2/||I||^2`,

`q_z(z)=sum_k I^2/||I||^2`.

At smallest reliable GDM/f(R) amplitudes the k-localization profiles appeared almost identical (`~0.04 deg` profile angle), while redshift-localization differed by `~20-21 deg`. This was inspected before protocol freeze and was **not** promoted to a finding.

## Exp048A — interaction localization geometry

Created stacked branch `research/interaction-localization-geometry-v0-1`, PR #28.

Pre-frozen only algebraic controls:

- decomposition reconstruction;
- core/I orthogonality;
- zero-mean component constraints;
- `q_k`, `q_z` normalization.

No post-hoc threshold for GDM/f(R) similarity or redshift separation.

Reported descriptors:

- `q_k`, `q_z`;
- profile cosine angles;
- Hellinger distances;
- geometric k centroid;
- redshift energy centroid;
- interaction-energy peak cell.

C4 remains absent by domain contract and is never imputed as zero.

## Continuation

1. Complete Exp048A target and record exact numbers if operator controls pass.
2. Stress localization geometry across finite amplitudes (candidate Exp048B).
3. Test whether GDM cv2/f(R) trajectory bending is accompanied by a systematic transition-scale flow through the low-k window.
4. Build C4 WDM high-k time-dependent atlas before family-complete nonseparability/localization claims.
5. Keep G7/G8 open.
