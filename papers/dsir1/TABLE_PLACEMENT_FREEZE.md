# DSIR-I table placement freeze — v0.1

**Date:** 2026-08-28  
**Purpose:** keep Paper I focused on response geometry rather than allowing validation/provenance tables to dominate the journal narrative.

This document resolves the remaining editorial question in `TABLES_DRAFT.md`: which tables belong in the JCAP main text and which belong in the supplement/provenance package.

## 1. Main-text rule

A table remains in the main paper only if it adds information that is not already conveyed more efficiently by a main figure or by one concise numerical sentence.

The target is **two principal main-text tables**, with a third allowed only if the compiled page/flow audit shows a clear readability gain.

## 2. Frozen main-text tables

### Main Table 1 — evidence-graded mechanism-to-response map

Source: `sections/mechanism_response_map.md` / `TABLE_MECHANISM_RESPONSE_MAP.md`.

**Keep in main text.**

Reason: this table now carries the conceptual synthesis that emerged from the DSIR4 analysis. It links equation-level cues to the response structures that should be inspected and explicitly grades each row as HARD-ATLAS, WITHHELD, DESCRIPTIVE, STRUCTURAL, or prospective FAIL. No existing figure replaces this many-to-many map.

Mandatory boundaries retained in the table/caption:

- perturbation “fingerprinting” is prior art;
- response patterns are not one-to-one identifiers of microphysics;
- K2 demonstrates that matter-space simplicity is not dark-specific;
- C7 preserves a prospective failed scalar generalization;
- theory-response angles are not survey significance.

### Main Table 2 — compact scale-time morphology hierarchy

Source: current `TABLES_DRAFT.md` Table 2, compressed to the finite-amplitude family envelopes plus the `12/12` deletion result.

**Keep in main text, compressed.**

Recommended columns:

| Family | sampled `chi_I` envelope | robustness / boundary |

Rows: IDE, smooth DE, GDM, designer `f(R)`.

Do not repeat all tangent-direction values in the main table; those remain in supplement/provenance. Figure 3 gives the visual hierarchy, while this table gives the exact reproducible numerical ranges.

Mandatory boundary: sampled frozen-domain descriptive hierarchy, not a universal invariant.

## 3. Move out of the main narrative

### Existing broad theory-family atlas

Source: original manuscript §5 family table / `TABLES_DRAFT.md` Table 1.

**Move to Supplementary Table S1 or collapse into prose immediately before Main Table 1.**

Reason: the new evidence-graded mechanism-to-response table contains the scientifically stronger version of the same family bookkeeping. Keeping both as full main tables is redundant.

### Pairwise `eta_I` table

Source: `TABLES_DRAFT.md` Table 3.

**Supplementary Table S2.**

Reason: exact values are useful for audit, but Figure 3 and the §6.5 prose already establish the result. Main text should retain only the two flagship GDM/f(R) values and the GDM pressure/viscosity caveat in prose.

### Channel-angle table

Source: `TABLES_DRAFT.md` Table 4.

**Supplementary Table S3 by default.**

Reason: channel-conditional equivalence is central, but Figure 4 plus the exact matter/slip values in the text already carry the argument. A full table duplicates the figure. Promote back to main only if the compiled layout shows that Figure 4 is visually insufficient.

### Finite-amplitude turning table

Source: `TABLES_DRAFT.md` Table 5.

**Supplementary Table S4.**

Reason: Figure 5 and the text already convey the curvature/dimension distinction; the full direction-by-direction values are reproducibility detail.

### Mechanism-localization withheld tests

Source: `TABLES_DRAFT.md` Table 6.

**Supplementary Table S5.**

Reason: WDM, DCDM and C7 are important controls, but their role is already explained in the Results sequence and Figure 5 / prospective-falsification prose. The exact frozen coordinates belong in supplement.

### Observation-route eligibility ladder

Source: `TABLES_DRAFT.md` Table 7 / `OBSERVATION_ROUTE_LEDGER.md`.

**Supplementary Table S6.**

Reason: this is the strongest defense against provenance/referee questions, but expanding the M→N→O→P2→S0→R0/R1 chain in the main paper would turn DSIR-I into a survey-reproducibility paper. Main text should state only the methodological conclusion and representative terminal failures/prerequisites.

## 4. Figure/table redundancy contract

The following duplications are deliberately avoided:

- Figure 3 = visual hierarchy; Main Table 2 = exact hierarchy ranges.
- Figure 4 = channel-degeneracy geometry; S3 = exact complete angle matrix.
- Figure 5 = curvature/localization comparison; S4/S5 = exact numeric details.
- Figure 6 = failure-resistant chronology; provenance matrix = exact run/artifact/digest chain.
- Figure 7 = support/admissibility logic; S6 = detailed observation-route status ladder.

A numerical value should not appear in a main figure, main table, and surrounding prose unless all three are needed for independent comprehension.

## 5. Main-paper target after compression

Target journal structure:

- 7 figures;
- 2 main tables;
- 6 supplementary tables;
- one compact observation-route subsection in main text;
- full run/artifact/digest provenance outside the narrative body.

This composition preserves the Paper-I center:

`response geometry -> channel-conditional equivalence -> mechanism diversity -> prospective falsification -> admissibility before observational quotient`.

## 6. Status

`PASS_TABLE_PLACEMENT_SCOPE_FREEZE_DSIR1_V0_1`

This is an editorial/publication freeze, not a scientific gate. It changes no numerical result, no PASS/FAIL state, and leaves `G7=OPEN`, `G8=OPEN`, `G9=OPEN`.
