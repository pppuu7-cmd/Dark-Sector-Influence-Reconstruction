# DSIR recovery — Exp073EN retry-safe run active; Exp073EO preregistered

Date: 2026-09-06. DSIR only; RTK/RQIR excluded.

## Live reconciliation
Authoritative heavy process is Exp073EN network-retry v0.2 run `33994398927` at activation head `4d1cbd504067a64a94b038292793e5e8bffba911`. Hosted preflight job `101382210840` is SUCCESS. Home science job `101382229273` is IN_PROGRESS. `DSIR-HOME-PC` is exclusively reserved by this job; no competing self-hosted heavy task may launch.

The frozen science identity is unchanged from Exp073EN v0.1: source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, R1 artifact `9720335366` digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`, NSIDE=4096, ell 0..12287, 39 bands, spin-2 S0->S0, selected EE<-EE `<f8 [39,12288]`, exact A/B equality only.

Partial numerical output was not inspected. The current durable stage cannot be inferred safely from live step summaries and must not be guessed.

## Immutable earlier infrastructure outcomes
Exp073EN original run `33993889263` home jobs `101380820499` and `101381512953` failed before science/resource arithmetic because the live-exclusivity API transport encountered SSL EOF/network failures. These remain infrastructure `+0/+0`; no science artifact and no WW authority were produced.

Repair v0.2 changes only the live-exclusivity network transport to retry-safe curl and leaves the frozen science path inherited from v0.1 unchanged.

## Prospectively prepared admission gate
Exp073EO was preregistered while Exp073EN was still running at commit `65c8e8d4f68c6d81c5a139fbb93f5b59467761a9` as `experiments/073eo_ww_s0_s0_filebacked_checkpoint_provenance_admission_v0_1_prereg.md`.

Exp073EO is not activated. It may run only after terminal Exp073EN evidence exists. It must independently verify the compact artifact, frozen identities, file-backed storage proof, and the complete six-stage A/B durable checkpoint chain: `fresh_s0_mask_complete`, `fresh_workspace_mcm_complete`, `mcm_fits_verified`, `full_window_complete`, `selected_ee_complete`, `replica_receipt_complete`. Only EO PASS may admit WW_S0_S0 authority.

## Exact next action
Consume Exp073EN run `33994398927` when terminal. On candidate PASS, independently verify its raw compact artifact and then activate Exp073EO. On infrastructure/resource failure, diagnose the first causal failure and preserve verified durable checkpoints. On qualified exact scientific repeatability FAIL, record the negative result without repair of frozen arithmetic.
