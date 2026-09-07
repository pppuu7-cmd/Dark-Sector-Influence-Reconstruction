# DSIR current-process ledger

Updated: 2026-09-07. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0` Exp073EO, `S0_S1` Exp073EZ, `S0_S2` Exp073FF, `S0_S3` Exp073FN, and `S1_S1` Exp073FR.

Newest immutable recovery note: `docs/recovery/RECOVERY_2026-09-07_EXP073GJ_C2_DELTA_M_FREEZE_FS_ATTEMPT2_RUNNING.md`.

## Exp073FS attempt 1 — historical infrastructure failure +0/+0

Exp073FS run `34067352681`, attempt `1`, head `f3e49041a5b869ddf22be8ca7a612901ec9f9458`: hosted job `101578350681` succeeded support-only; home job `101578366531` failed on runner `DSIR-HOME-PC` / id `21` before evidence collection/upload. Old job log became unavailable after rerun, so no shell/numerical cause is invented. Classification remains `INFRASTRUCTURE_RUNNER_ORCHESTRATION_FAIL_PLUS_0_PLUS_0`; no scientific artifact or authority was created.

## Authoritative current process — Exp073FS attempt 2 / WW_S1_S2

The same workflow run is attempt `2`; this is not a competing heavy run.

- workflow/run: **Exp073FS `34067352681`**, attempt **`2`**;
- branch/head: `main` / **`f3e49041a5b869ddf22be8ca7a612901ec9f9458`**;
- home job: **`101592579318`**;
- runner ownership: **`DSIR-HOME-PC-2` / runner id `22`, exclusively owned by job `101592579318`**;
- created `2026-09-07T01:18:30Z`, started `2026-09-07T01:31:27Z`;
- latest live state: **IN_PROGRESS** in `Run frozen WW_S1_S2 A/B gate with durable checkpoints`;
- latest-attempt hosted-launch audit `101592593435`: SUCCESS, support `+0/+0`;
- latest live Actions reconciliation: one in-progress DSIR heavy run and no competing heavy run observed;
- evidence collection and artifact upload are still pending;
- checkpoint roots: `~/.cache/dsir/exp073fs-ww-s1-s2-filebacked-ab-v0-1/checkpoints/A` and `/B`;
- last durable checkpoint: `UNKNOWN_NOT_INSPECTED_WHILE_RUNNING`;
- science prereg blob: `80c6af017b47d51db3f588221749fb152577b0e5`;
- Exp073FT admission prereg blob: `072bdeae68e86312142e980fe2015f979e7b117f`;
- frozen source/contract: `de83e20a68f79ccf25b89b0d33eb4206e294c757` / `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`;
- expected candidate token: `PASS_EXP073FS_WW_S1_S2_FILEBACKED_AB_EXACT_REPEATABILITY_V0_1`.

Runner transition `21 -> 22` is provenance-relevant. Terminal evidence must prove restored versus newly computed complete stages; shared local checkpoint availability is never assumed from a path string alone.

Frozen pair semantics remain ordered `[1,2] = S1->S2`: reconstruct S1 and S2 once each, build two distinct spin-2 fields, forbid same-object handoff and reversed order; DES NSIDE=4096; ell `0..12287`; 39 bands; public file-backed BPW; full `[4,39,4,12288]`; canonical `<f8 [39,12288] EE<-EE`; exact A/B SHA plus array equality; all finite; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial rescue.

### Exact heavy-chain next actions

Do not duplicate attempt 2 and do not inspect partial numerical output. On terminal SUCCESS, consume raw terminal log and artifact immediately and independently verify artifact digest/ZIP SHA, both complete stage chains before prune, restored-versus-new stage provenance, ordered source/reconstruction counts, distinct field identities, source/contract/implementation/checkpoint identities, exact `19,327,352,832`-byte mmap proof, finiteness and exact canonical A/B equality. Candidate PASS does not itself create authority. Only prospectively frozen Exp073FT may create `WW_S1_S2` authority and dispatch Exp073FU.

On infrastructure/resource failure, diagnose the first causal defect from terminal evidence, preserve every verified complete-stage checkpoint, make the smallest prospective repair, and resume without changing frozen science. Exact numerical mismatch is a scientific FAIL and must never be tolerance-rescued.

Remaining deterministic queue: `FS -> FT -> FU -> FV -> FW -> FX -> FY -> FZ -> GA -> GB -> STOP`; every successor is gated on explicit predecessor scientific authority.

## Independent DSIR-4 work while heavy compute runs — C2 IDE

C2 IDE six-component mapping is frozen and `mapping_ready=true`; numerical prediction authority is still absent.

The validated legacy IDE artifact remains independently recovered in `docs/dsir4/mappings/C2_IDE_PREDICTION_PROVENANCE_RECOVERY_V0_1.md` (creation commit `1e6f48278cb3398c290df4d08c0d239fab032147`). Legacy raw `mPk` response is not a valid replacement for the frozen common `Delta_m` bridge.

### Exp073GJ same-solver Delta_m generation freeze — hosted support PASS +0/+0

Prospective prereg `experiments/073gj_c2_ide_delta_m_generation_freeze_v0_1_prereg.md` was created in commit `668031cade3455e795e299056c9d98334b4ad0e3`, before any new C2 numerical generation. It freezes:

- pinned solver `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- common bridge `Delta_m = delta_m + 3*(1+w_m)*Hconf*theta_m/k^2` and matched `r_Delta` power response;
- reference `(alpha,beta)=(0,0)`, alpha base point `(-1e-4,0)`, beta central pair `(0,+1e-4)/(0,-1e-4)`;
- exact z grid `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`;
- exact in-domain k subset `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`;
- explicit exclusion of legacy `0.067 Mpc^-1` because it exceeds `k_max=0.06664762008318016`;
- fail-closed source-variable identity, physical branch masks, deterministic JSON serialization and SHA256 requirements.

Hosted static-audit history is immutable support-only:

- run `34081553496`, job `101617650342`: `IMPLEMENTATION_STATIC_FAIL_PLUS_0_PLUS_0`; first audit harness used an incorrect square-bracket `ln[...]` literal against the prereg's frozen parenthesized `ln(...)` expression;
- run `34081596871`, job `101617772642`: diagnostic `IMPLEMENTATION_STATIC_FAIL_PLUS_0_PLUS_0`, explicitly identified the mismatched `r_Delta` literal;
- run `34081626964`, job `101617857129`: repair-attempt `IMPLEMENTATION_STATIC_FAIL_PLUS_0_PLUS_0`, still checked `ln[` and therefore remained harness-only failure;
- minimal harness-only repair commit `1b977af76a7ca2de438156a7ceb88c4e1a29844c` changed only the audit literal to the already-frozen prereg syntax; C2 science, domain, parameters and formula were not changed;
- repaired run `34081658093`, job `101617944759`: raw exact token `PASS_EXP073GJ_C2_IDE_DELTA_M_GENERATION_FREEZE_STATIC_AUDIT_V0_1`, `classification=SUPPORT_PLUS_0_PLUS_0`, `self_hosted_science_started=false`, `scientific_model_authority_created=false`.

Therefore Exp073GJ closes only the prospective generation-interface/static-audit prerequisite. C2 remains `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific contribution `+0/+0` until a generator is implemented, source-variable identities are proven from the pinned solver, a deterministic payload is generated, and its provenance is independently admitted.

Exact independent next step while FS runs: implement/audit the pinned-lineage generator without changing the frozen Exp073GJ interface and without using partial FS or downstream C2 results.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
