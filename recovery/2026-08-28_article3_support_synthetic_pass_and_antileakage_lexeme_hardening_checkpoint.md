# DSIR recovery checkpoint — Article-3 support synthetic PASS + anti-leakage lexeme hardening

Date: 2026-08-28

## Authority and current G7 prerequisite

Authoritative upstream reproduction remains **Exp073R1 DESY1 sequential whole-stream reconstruction v0.5**, GitHub Actions run `33175886694`.

Observed state at this checkpoint:

- `source-index`: terminal `success`;
- Stage-A frozen no-Range identity assertion: `success`;
- `metacal-map`: still `in_progress`;
- `Sequentially stream authoritative metacal object and execute frozen mapper`: `in_progress`;
- final step `Assert true Exp073R1 reproduction PASS and parent-gated semantics`: not yet executed;
- therefore no genuine Exp073R1 PASS exists yet and no real physical-support evaluation is authorized.

Classification: **reproduction/infrastructure INCOMPLETE**, not a scientific FAIL.

No duplicate heavy run is authorized while run `33175886694` remains live.

## Independent support-contract QA result

The prospective Article-3 physical-support contract is frozen in `docs/ARTICLE3_PHYSICAL_SUPPORT_GATE_CONTRACT_2026-08-28.md` and explicitly preserves the required ordering:

`exact reproduction -> physical support -> finite operator -> covariance restriction/whitening -> full signed nuisance span -> nuisance projection -> relation/null -> later falsification gates`.

The synthetic-only QA workflow `.github/workflows/article3-physical-support-synthetic-v0-1.yml` ran automatically from commit `5f946b6b3572fb5989275ea7c5fb8f8c8ce5cfeb` as Actions run `33201997669` and finished terminal `success`.

The QA asserts, among other things:

- exact inclusive z/k boundary semantics and immediate `nextafter` rejection;
- row-permutation invariance through inherited ordinal ordering;
- exact `f_invalid = 0.05` acceptance and above-threshold scientific FAIL;
- 15 retained PASS / 14 retained scientific FAIL;
- common positive finite response-envelope semantics;
- positive-amplitude scale invariance;
- duplicate coordinate ID / ordinal rejection as `INVALID_FOR_SCIENCE`;
- frozen parent mismatch rejection;
- upstream final-assertion failure rejection;
- covariance/nuisance leakage rejection;
- crop-before-normalization and downstream selection-read rejection.

Critically, the synthetic output carries:

- `scope = SYNTHETIC_ONLY_NO_DES_ARTIFACT_ACCESS`;
- `real_science_gate_scored = false`;
- `covariance_restriction_authorized_by_this_QA = false`;
- `gate_state = {G7: OPEN, G8: OPEN, G9: OPEN}`.

Therefore this CI success is **reproducibility / contract-QA PASS only**. It is not a physical-support scientific PASS and cannot open covariance access.

## Newly identified integrity hardening gap

The synthetic reference classifier currently detects forbidden downstream-selection payloads using a finite tuple of lowercase substring tokens (`covariance`, `inverse_covariance`, `whitening`, `nuisance`, `svd`, `relation`, `pvalue`, `chi2`, `g7`, `g8`).

This correctly rejects the tested canonical key forms, but it is not yet a complete proof that semantically equivalent aliases cannot bypass the lexical scan. Examples that require explicit adversarial coverage before the real support executable is treated as hardened include forms such as `p_value`, `chi_squared`, spelling/case/separator variants, and nested aliases carrying the same downstream information.

Classification: **integrity / anti-leakage hardening gap**, not infrastructure failure and not scientific FAIL.

This finding does **not** change any frozen scientific criterion. It only tightens enforcement of the already-frozen rule that covariance, whitening, nuisance/SVD, relation/null, p-value, G7, and G8 information must not participate in support selection.

## Authorized next work

While Exp073R1 remains live, allowed work is limited to non-DES synthetic/adversarial hardening and provenance checks. Before any real physical-support run, the anti-leakage implementation should receive fail-closed semantic/alias adversarial tests or an explicit schema allow-list that makes downstream extra fields impossible by construction.

After a genuine Exp073R1 terminal PASS, preserve the frozen order exactly:

1. bind the exact upstream run/artifact identity and digest prospectively required by the support contract;
2. execute the preregistered real physical-support validity mask;
3. only on `PASS_PHYSICAL_SUPPORT_ARTICLE3`, restrict the already-bound covariance to the exact retained coordinate sequence;
4. whiten;
5. evaluate full signed nuisance tangent rank/SVD;
6. quotient/relation/null control;
7. only then open a fresh G8 withheld family.

Negative scientific results must remain terminal evidence under their frozen criteria; integrity/infrastructure failures must remain distinct from scientific FAIL.
