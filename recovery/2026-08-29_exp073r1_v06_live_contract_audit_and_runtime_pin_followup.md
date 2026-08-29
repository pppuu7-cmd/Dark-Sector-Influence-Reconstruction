# DSIR recovery checkpoint — Exp073R1 v0.6 live contract audit and runtime reproducibility follow-up

Date: 2026-08-29 (MSK)
Authority branch: `main`

## Live authoritative run

Canonical Stage-B run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/33222848695

At this checkpoint the sole job `metacal-map-longrun` is `in_progress`.
Steps 1–8 are completed `success`; step 9 (`Sequentially stream authoritative 84GB metacal object and execute unchanged frozen mapper`) is `in_progress`; terminal Exp073R1 PASS assertion and artifact upload remain pending.

Therefore the only valid classification is **Exp073R1 reproduction INCOMPLETE**. This is not a scientific FAIL and does not authorize downstream physical-support or covariance work.

No duplicate heavy run was started in this iteration.

## Independent frozen-contract audit

The active Stage-B workflow still enforces the frozen Exp073R1 v0.6 preregistration and the unchanged v0.5 evaluator.

Verified bindings present in the active workflow:

- evaluator path: `ci/exp073r1_sequential_wholestream_v0_5.py`;
- evaluator Git blob SHA-1 required by workflow: `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`;
- Stage-A source run: `33175886694`;
- Stage-A source head: `2926f1866fed4f0767ce3d1ec797f6e6ed4f4f2c`;
- Stage-A artifact ID: `9688707039`;
- authoritative source whole SHA256: `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- source-index SHA256: `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`;
- Exp073R0 run: `33103083736`;
- Exp073R0 head: `94b05d307295d5e9263646983ece9514f9fa2e88`;
- frozen metacal bytes: `84075649920`;
- frozen metacal SHA256: `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- row count: `136930995`;
- frozen selection: `zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`;
- frozen mapper: NSIDE 4096, RING, celestial `C`, `lonlat=True`;
- transport remains whole-object GET with no Range semantics;
- terminal assertion still requires `science_gate_scored=false`, `f_invalid_computed=false`, `covariance_read=false`, `G8_read=false`, and `G7/G8/G9=OPEN`.

The active job has already passed the workflow's evaluator-blob assertion, immutable parent metadata binding, downloaded-parent internal contract binding, and runtime installation steps. No scientific acceptance criterion was changed in the execution repair.

## New reproducibility hardening observation

The current Stage-B workflow installs `numpy` and `healpy` into an isolated venv but does not pin their package versions in the workflow source. This is **not a scientific failure and does not invalidate the currently running candidate**, because the active run uses one concrete installed environment and the frozen evaluator/inputs/terminal assertions remain bound. However, it is a future rerun reproducibility risk: a later package release could alter numerical or serialization behavior even when the evaluator source is unchanged.

Do not modify the currently executing authority retroactively. After the active run terminates, capture the exact `numpy` and `healpy` versions reported by that run and freeze them (preferably with hashes or an environment lock) for any future rerun/reproduction path. This is infrastructure/reproducibility hardening only and must not be used to change frozen science criteria.

If the current run reaches the genuine terminal PASS, its result remains the authority for Exp073R1 and no rerun is required merely to obtain package pins. Package pinning is for future reproduction durability.

## Gate discipline

Frozen order remains:

1. genuine Exp073R1 PASS;
2. preregistered real physical support-validity mask (Exp073P);
3. covariance restriction / whitening;
4. nuisance tangent rank / SVD;
5. quotient / relation / null control;
6. only then fresh G8 withheld family.

Until step 1 is genuinely terminal PASS, no downstream numerical science quantity is authorized.
