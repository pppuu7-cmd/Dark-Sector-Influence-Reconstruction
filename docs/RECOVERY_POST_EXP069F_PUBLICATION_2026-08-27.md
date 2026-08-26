# DSIR recovery checkpoint — post Exp069F + publication architecture

**Date:** 2026-08-27  
**Scope:** restores the active research state after Exp069F and records the new manuscript-oriented repository layer.

## Non-negotiable project boundary

DSIR is independent of RTK. Do not modify, import or silently reuse RTK evidence in DSIR. A later RTK↔DSIR comparative manuscript may reference immutable outputs from both projects only after each evidence chain is independently mature. See `docs/publications/RTK_DSIR_PUBLICATION_BOUNDARY_V0_1.md`.

## Core scientific interpretation

DSIR is a reconstruction/meta-inference framework, not a fundamental theory.

Current strongest synthesis:

1. heterogeneous dark-sector/MG mechanisms can be organized in common response coordinates with explicit solver provenance and masked domain support;
2. response equivalence is channel-conditional rather than a global microscopic parameter identity;
3. matter-only response geometry can be low-dimensional and predictive yet not dark-specific;
4. known-sector K2 passing the F30 normalized-path gate forces F30 to be interpreted as response-direction/transfer-shape geometry, not a dark detector;
5. independent Weyl/slip/lensing information is therefore central to stronger discrimination;
6. no universal residual law has survived G7 because G7 has not yet been legitimately executed through the full physical-provider/support/covariance/nuisance chain;
7. G8/G9 remain open.

## Immutable recent scientific history

### F27/F29 failures and F30 specificity boundary

- Exp054C/F27: prospective withheld-family relation FAIL.
- Exp056B/F29: fresh-family candidate relation FAIL.
- Exp061A/F30: prospective multicoordinate response-path PASS on fresh C9.
- Exp071C: ordinary known-sector controls; K2 passes the same normalized-path behavior.
- Consequence: F30 is a valid response-geometry result but not dark-specific.

### Observation-space preparation

- ACT DR6 × unWISE selected 26D covariance/window/shot-noise/whitening chain has passed its source/operator gates.
- CAMB↔CLASS matter/Weyl convention has a separately certified precision-aware route; preserve the earlier failed convention gate.
- Do not fit a dark-sector law until physical providers, common support and nuisance quotient prerequisites are complete.

## C3 physical provider

C3 native physical provider is eligible from Exp070C. Preserve earlier C3 accessor reconstruction failures; do not replace native source semantics with the rejected reconstruction.

## C5 physical-provider history

### Exp069B — permanent FAIL

Literal explicit-EFT designer `B0=0` missed the frozen target closure `5e-6` by a small amount. This remains permanent:

`FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1`.

### Exp069C

The zero-limit residual is already present on same raw nodes and does not converge away under `k_per_logint=40..320`. Interpolation/k-density is not an authorized correction.

### Exp069D

Background grid density and RGR threshold variation do not explain the target floor. A skip-RGR branch was unstable, so the audit is formally incomplete for that branch.

### Exp069E

Source-native RGR subset at exact designer zero:

`F0 = 4.7401579076280133e-17`.

Power floor remains:

`M0 = 5.302921926164412e-6`.

Therefore a physical-size EFT background residue does not explain the ppm power mismatch.

### Analytic source theorem

Pinned designer equations possess exact `A=0` GR solution for the LCDM designer background, while literal `EFTB0=0` still uses generic numerical `B0(A)=0` inversion. This is an implementation/theory boundary theorem, not provider certification.

Merge: `f827e80740ed4d5d27d8a1f4c6982ba412c8895e`.

### Exp069F — COMPLETE mechanism PASS

Preregistration commit:

`43ef913645a43f091e728623291bc21642a56ab9`.

Execution merge:

`30706773a0069b6bbe3144443debeeffa6fba328`.

Run/artifact:

- run `33023027901`;
- artifact `9627458877`;
- digest `sha256:d8e1a42bf813d5ae105ea33e723868d454ff7584424373ecfe4594a2dfe49358`.

Scientific classification:

`GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT`.

Frozen target maxima for q=`[1,2,3,4]`:

`[5.302921926e-6, 2.904403569e-6, 1.701118686e-6, 1.310789027e-6]`.

Frozen raw same-node maxima:

`[9.938162077e-6, 5.400555775e-6, 2.842130238e-6, 1.517781618e-6]`.

Primary first target PASS is q=2 exactly as preregistered. q=3 is descriptively the first tested q with both target and raw maxima below `5e-6`.

Background `H(z)`, conformal-time and common returned recombination/equality quantities are identical within each paired q. The mismatch therefore behaves as a numerical accuracy-sensitive transfer/integration residue, not a physical zero-limit f(R) signal.

Exp069F does **not** certify C5.

### Exp069G minimum provider contract

Commit `731f0824379a977ed9a8a3f9107538854c24de65` froze C1–C8 minimum obligations before Exp069F output became available.

### Exp069H — current next C5 protocol

Preregistered before any Exp069H solver execution:

`experiments/069h_c5_q3_unmodified_upstream_provider_certification_prereg_v0_1.md`.

Key frozen choices:

- unmodified pinned upstream;
- q=3 selected prospectively as the smallest tested Exp069F point with both target and raw residuals below the historical 5e-6 scale;
- B0 `[0,1e-12,1e-10,1e-8,1e-6]`;
- hard target and raw zero closure both `<=5e-6`;
- tiny-positive continuity target/raw `<=5e-6`;
- production signal `>=1e-3`;
- signed `P_Wm` preserved;
- repeated forward/reverse accessor exact equality;
- independent zero rerun repeatability `<=1e-12`;
- no floor subtraction/source patch/renormalization/threshold change.

Only a full PASS makes C5 eligible for the next support-mask preregistration.

## Publication architecture added 2026-08-27

New manuscript layer:

- `docs/publications/README.md`;
- `ARTICLE_SERIES_ROADMAP_V0_1.md`;
- `ARTICLE_READINESS_LEDGER_V0_1.md`;
- `ARTICLE_01_EVIDENCE_MAP_V0_1.md`;
- `RTK_DSIR_PUBLICATION_BOUNDARY_V0_1.md`;
- `RESEARCH_CHRONOLOGY_V0_1.md`.

Current publication readiness:

- **DSIR-1 observable-response geometry: `READY_FOR_DRAFTING`**;
- DSIR-2 blocked by C5 provider certification;
- DSIR-3 blocked by support/covariance/nuisance/G7 sequence;
- DSIR-4 blocked by fresh G8;
- RTK–DSIR comparative synthesis blocked until both projects independently support mature papers.

`READY_FOR_DRAFTING` does not mean submission-ready and does not change G7/G8/G9.

## Current gate/order state

- G1 PASS.
- G2 PASS.
- G3A/G3B PASS block-aware.
- G4 PASS synthetic recovery.
- G5 partial/observation path still being completed.
- G6 layers established.
- C3 physical provider: eligible.
- C5 physical provider: NOT YET CERTIFIED.
- common physical support-validity mask: NOT AUTHORIZED until C5 PASS.
- G7 OPEN.
- G8 OPEN.
- G9 OPEN.

## Exact continuation order

1. Merge the Exp069F result/publication architecture/Exp069H preregistration without executing Exp069H beforehand.
2. Implement Exp069H exactly to its frozen q=3 contract.
3. Execute Exp069H and classify PASS/FAIL without threshold changes.
4. If PASS: preregister the common C3+C5 physical support-validity mask; only then restrict covariance/whitener to physical support.
5. Freeze nuisance tangent SVD/rank rule before quotienting.
6. Execute quotient/relation/null G7 stage.
7. Only after a frozen G7 candidate, select a genuinely fresh withheld family for G8.
8. In parallel, manuscript DSIR-1 can be drafted from the already complete response-geometry evidence map; keep it isolated from unresolved G7/G8 claims.
9. Continue N1 full-text/citation-graph novelty audit before submission-level novelty wording.

## Recovery entry order after chat loss

1. `docs/RECOVERY_MANUAL.md`.
2. `docs/RECOVERY_POST_EXP067E_2026-08-26.md` for the prior late-stage observation/convention history.
3. this file: `docs/RECOVERY_POST_EXP069F_PUBLICATION_2026-08-27.md`.
4. `docs/publications/RESEARCH_CHRONOLOGY_V0_1.md`.
5. `docs/publications/ARTICLE_READINESS_LEDGER_V0_1.md`.
6. current numbered experiment protocol/result.

Never infer scientific status from a green workflow alone; read the experiment classification and frozen criteria.
