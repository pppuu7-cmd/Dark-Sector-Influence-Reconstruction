# DSIR-I intake from DSIR4 / current main — 2026-08-28

**Purpose:** prevent ongoing DSIR research from either being missed by Paper I or silently expanding Paper-I scope after its scientific closure.

## Snapshot

Paper branch baseline considered here:

- branch: `paper/dsir-i-observable-response-geometry`
- last fully green compact JCAP baseline before current prose cleanup: `5e74a304e8e3b6b5a4fd09144f2c00b224ea7818`
- paper build: run `33120663553` — PASS
- JCAP compile: run `33120663569` — PASS
- compiled PDF: `26` pages
- main tables: `2`
- unresolved references: `0`.

Current DSIR `main` snapshot examined for intake:

- head: `e61c61a370cdc4cee5da2aa26cc677a6ad373c70`
- recent research focus: Exp073R1 deterministic DES Y1 operator/input reproduction and transport/provenance hardening.

The paper branch is intentionally not rebased wholesale onto current `main`. Intake is selective and claim-scoped so that infrastructure or downstream research does not silently rewrite a closed first-paper argument.

## New material already admitted to Paper I

### Moving-scale / nonseparability bridge

**Classification:** MAIN TEXT — explanatory analytic bridge + retrospective consistency check.

Admitted statement:

\[
R(x,z)=a(z)+F[x-\delta(z)]
\quad\Rightarrow\quad
\partial_x\partial_zR=-\delta'(z)F''[x-\delta(z)].
\]

For small drift the double-centered interaction is leading-order rank one,

\[
I_{ij}\simeq-(\epsilon_i-\bar\epsilon)\left(F'_j-\overline{F'}\right).
\]

The immutable Exp050A WDM matrices provide a retrospective consistency check: the residual interaction is nearly one-dimensional and its temporal direction follows the very small cutoff drift, while the already-frozen `chi_I` stays of order `2e-10`.

**Boundary:** explanatory geometry only; no universal `chi_I=f(Delta ln k_*)` law, no fresh withheld test, no G7/G8/G9 advance.

## Current Exp073R1 work

### Canonical v0.4 state at intake

Run examined: `33160570463`, workflow `Exp073R1 canonical whole-stream bound microshards v0.4`.

At the intake snapshot:

- preflight: PASS;
- source whole-stream canonical manifest: PASS;
- metacal whole-stream canonical manifest: still running;
- the workflow binds the genuine R0 prerequisite and authoritative prior whole-object SHA256 identities;
- the canonical manifest stage is provenance-only.

The launcher explicitly does **not** score or authorize:

- `f_invalid`;
- physical-support PASS/FAIL;
- covariance restriction;
- covariance whitening;
- nuisance SVD/quotient;
- relation/null statistics;
- G8;
- G9.

### Paper-I intake decision

`SUPPLEMENT_OR_PROVENANCE_ONLY_WHILE_R1_REMAINS_REPRODUCTION_SCOPED`

No current R1 v0.4 state changes the Paper-I scientific conclusion that an observational quotient requires finite normalization, exact reproducibility and physical support before covariance/nuisance operations.

Paper I therefore does **not** wait for R1 v0.4 to complete.

## Admission rule for later R1 output

When a completed frozen R1 result exists, classify it before editing the manuscript:

1. **transport/checksum/catalogue/operator reproduction only** -> supplement/provenance;
2. **physical-support result under the unchanged frozen criterion** -> inspect whether it changes a stated Paper-I limitation;
3. **if it changes a Paper-I limitation materially** -> re-open only that sentence/figure/table under `SUBMISSION_SCOPE_FREEZE.md` and rerun all paper gates;
4. **covariance/whitening/nuisance or relation-null progress** -> Paper II by default;
5. **G7/G8/G9/new-physics progress** -> later paper(s), not Paper I;
6. **infrastructure-incomplete** -> no scientific manuscript claim.

## Scope-preservation conclusion

The newest DSIR4 work strengthens the project but does not invalidate Paper-I closure. The correct publication strategy is to finish and freeze Paper I while downstream observation-space reconstruction continues independently on `main`.

`G7=OPEN`, `G8=OPEN`, `G9=OPEN` at this intake snapshot.
