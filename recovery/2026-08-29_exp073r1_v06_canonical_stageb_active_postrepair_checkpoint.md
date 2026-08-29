# DSIR recovery checkpoint — canonical Exp073R1 v0.6 Stage-B active after runtime repair

Date: 2026-08-29
Branch: `main`

## Canonical authority

The single authoritative heavy run is GitHub Actions run `33222848695`, job `99020389131`, workflow `Exp073R1 DESY1 self-hosted long-run Stage-B v0.6`, head SHA `98c4b8783a95932949947d9e214706c4ec7eaf8c`.

At this checkpoint the job is `in_progress` on the canonical step:

`Sequentially stream authoritative 84GB metacal object and execute unchanged frozen mapper`

All prerequisite execution/provenance steps before the mapper are complete with `success`:

1. checkout;
2. unchanged-evaluator / execution-firewall assertion;
3. immutable Stage-A and Exp073R0 Actions-metadata binding;
4. isolated self-hosted mapper runtime installation;
5. Stage-A artifact download;
6. Exp073R0 artifact download;
7. downloaded-parent internal-contract re-binding.

The terminal genuine Exp073R1 PASS assertion has not yet executed and remains pending.

## Frozen evaluator and identities

Frozen evaluator remains `ci/exp073r1_sequential_wholestream_v0_5.py`, blob `46fe1271d97ddd9e2164d24e7d79cf27bfda805d`.

Frozen source authority:

- whole-object SHA256 `491f623d9370d3e5657db67d410e7cfd0e89475827046e6cd82ef6b3dd88c7a5`;
- rows `136930995`;
- source-index bytes `273861990`;
- source-index SHA256 `dbb362b10c68825e775e7398b18eb77d37fe725ce80cfd5c07faec5cb5755628`.

Frozen metacal authority:

- bytes `84075649920`;
- SHA256 `39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8`;
- rows `136930995`.

Transport contract remains one ordinary whole-object GET, no Range requests, `Accept-Encoding: identity`, exact byte count and exact full-object SHA256.

## Scientific classification

Current status is **Exp073R1 reproduction INCOMPLETE**. There is no scientific FAIL. The prior PEP-668 event was infrastructure/runtime only and is already repaired by the isolated venv execution path.

No duplicate heavy run is authorized while `33222848695` remains active.

## Gate ordering

Frozen order remains unchanged:

1. genuine Exp073R1 PASS;
2. already-preregistered Exp073P physical support-validity join/mask;
3. covariance restriction / whitening;
4. nuisance tangent rank / SVD;
5. quotient / relation / null control;
6. only then fresh G8 withheld family.

Until step 1 finishes with genuine PASS, no real Exp073P support statistic, covariance, whitening, nuisance-rank, quotient/relation/null or G8 result is authorized.
