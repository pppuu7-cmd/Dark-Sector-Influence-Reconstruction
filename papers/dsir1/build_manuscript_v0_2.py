#!/usr/bin/env python3
"""Deterministically assemble DSIR-I manuscript v0.2 from frozen text components.

The script does not edit manuscript.md in place. It injects the frozen author
metadata, inserts prospectively/retrospectively classified result components,
surfaces the support-eligibility results in Abstract/Introduction/Conclusions,
adds compact related-work positioning, adds deterministic Figure 1--7 textual
references at frozen narrative anchors, inserts the reproducibility section
before Outlook, renumbers the final headings, and writes manuscript_v0_2.md.
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "manuscript.md"
FALSIFICATION = HERE / "sections" / "prospective_falsification.md"
SUPPORT_CLOSURE = HERE / "sections" / "observation_space_support_closure.md"
RELATED_WORK = HERE / "sections" / "related_work_positioning.md"
KNOWN_SECTOR = HERE / "sections" / "known_sector_nonoverclaim.md"
REPRO = HERE / "sections" / "data_code_reproducibility.md"
OUT = HERE / "manuscript_v0_2.md"

RESULTS_INSERT_MARKER = "# 7. Failure-resistant numerical validation"
PRIOR_ART_MARKER = "# 8. Relation to existing dark-sector parameterizations"
INTERPRETATION_MARKER = "# 9. Interpretation"
LIMITATIONS_MARKER = "# 10. Limitations and claim boundary"
OUTLOOK_MARKER = "# 11. Outlook"
CONCLUSION_MARKER = "# 12. Conclusions"
AUTHOR_PLACEHOLDER = 'author:\n  - "[authors to be finalized]"'
AUTHOR_BLOCK = '''author:\n  - "Aleksey Buyanov"\naffiliation: "Independent Researcher"\nlocation: "Moscow, Russia"\nemail: "pppuu7@gmail.com"\norcid: "0009-0001-2621-9305"'''

ABSTRACT_FINAL_MARKER = (
    "DSIR-I is therefore a response-classification and identifiability result, not a claim of a universal dark-sector invariant or a discovery of new fundamental physics."
)
ABSTRACT_SUPPORT_SENTENCE = (
    "Prospectively frozen support audits further show that the observational quotient cannot be evaluated merely because its formal operator is defined: none of 26 ACTxunWISE candidate coordinates is supported by the current certified C3/C5 domain at the 5% leakage criterion, while the joint support extension that geometrically recovers 15 coordinates is ineligible under the tested linear perturbativity route. A separate KiDS operator audit finds the chosen positive absolute-response measure to be nonnormalizable. In a constructive replacement chain, an initially finite DES harmonic operator class subsequently fails exact real-data provenance, a public DES Y1 pseudo-C_ell replacement is selected under unchanged support criteria, and its checksum, mask/n(z), and raw-row-to-HEALPix reproduction prerequisites pass without yet scoring physical support. We therefore do not quote a covariance-whitened or nuisance-quotiented survey distance from an ineligible or pre-support route."
)

INTRO_OLD = (
    "This paper develops and tests the first part of that program. Its contributions are fivefold. First, we define a block-aware response geometry in which undefined model/channel combinations are masked rather than silently replaced by zeros. Second, we show quantitatively that a simple additive description of scale and time dependence fails for some mechanisms because an irreducible scale-time interaction carries substantial response power. Third, we demonstrate with frozen examples that degeneracy is channel conditional: matter-response lookalikes can be split by metric information, while scale-only lookalikes can be split by temporal evolution. Fourth, we separate microscopic parameter count from response-manifold curvature and linear representation rank. Fifth, we formalize exact channel-conditional equivalence through physical projection, covariance whitening, and nuisance quotienting, while keeping the current empirical atlas distinct from a completed survey-level detectability analysis."
)
INTRO_NEW = (
    "This paper develops and tests the first part of that program. Its contributions are sixfold. First, we define a block-aware response geometry in which undefined model/channel combinations are masked rather than silently replaced by zeros. Second, we show quantitatively that a simple additive description of scale and time dependence fails for some mechanisms because an irreducible scale-time interaction carries substantial response power. Third, we demonstrate with frozen examples that degeneracy is channel conditional: matter-response lookalikes can be split by metric information, while scale-only lookalikes can be split by temporal evolution. Fourth, we separate microscopic parameter count from response-manifold curvature and linear representation rank. Fifth, we formalize exact channel-conditional equivalence through physical projection, covariance whitening, and nuisance quotienting. Sixth, we make the eligibility of that quotient explicit: the positive support measure, the exact real-data operator realization, and the physical domain must all be certified before whitening. A concrete ACTxunWISE C3/C5 audit retains no coordinate on the current domain and reaches a nonperturbative planning frontier; an independent KiDS absolute-response audit is nonnormalizable under its frozen support measure; and a later DES harmonic route demonstrates how a provenance-failed candidate is prospectively replaced and reproduced without yet reading the physical-support statistic. Thus the paper distinguishes a mathematically defined quotient from a physically authorized one rather than manufacturing a survey distance through extrapolation, retrospective normalization, or incompletely reproducible operators."
)

CONCLUSION_COUNT_OLD = "The current atlas yields four main conclusions."
CONCLUSION_COUNT_NEW = "The current atlas and observation-route audits yield five main conclusions."
CONCLUSION_FOURTH = (
    "Fourth, mechanism diversity matters. Thermal WDM exhibits a strong scale-localized but nearly time-separable response, whereas withheld DCDM produces a distinct temporal-localization flow. These cases support the use of response localization and trajectory geometry as organizing tools while simultaneously ruling out a naive universal scale-time template."
)
CONCLUSION_FIFTH = (
    "Fifth, a formal observational quotient is not automatically a physically admissible one. The frozen support programme exposes three distinct prerequisites before covariance whitening: the positive support measure must possess a finite non-zero normalizer, the exact real-data operator/input realization must be reproducible, and the observational kernel must lie on a physically justified theory/provider domain. The current ACTxunWISE C3/C5 route fails the domain requirement on its certified support and its geometric extension is ineligible under the tested linear route; the tested KiDS absolute-response measure fails the normalizability requirement. A finite DES harmonic operator class was then rejected at the exact-realization provenance gate, after which a public DES Y1/BOSS replacement route was selected prospectively. Its released inputs, mask/n(z), and raw-row/HEALPix mapping prerequisites now pass, but its physical support has not yet been scored and therefore the observational quotient remains open."
)

FIGURE_INSERTIONS = [
    (
        "# 5. Theory atlas",
        "Figure 1 summarizes the induced signature operator and the compatibility condition for channel refinement.",
    ),
    (
        "## 6.3 The additive `(G,T,tau)` core is insufficient",
        "Figure 4 juxtaposes the two frozen examples of channel-conditional degeneracy breaking.",
    ),
    (
        "## 6.4 Finite-amplitude hierarchy and grid robustness",
        "Figure 2 shows the additive projection and irreducible interaction directly for the frozen low-k response atlas.",
    ),
    (
        "## 6.5 Irreducible scale-time structure carries GDM--\\(f(R)\\) separation",
        "Figure 3 summarizes the finite-amplitude hierarchy and its deterministic leave-one-node robustness.",
    ),
]

FIGURE5_REFERENCE = (
    "Figure 5 compares response-manifold curvature with the distinct WDM scale-localization "
    "and DCDM time-localization controls."
)
FIGURE6_REFERENCE = (
    "Figure 6 summarizes the failure-resistant chronology, retaining original failed contracts "
    "beside separately frozen corrective providers and the prospective F27 falsification."
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def require_once(text: str, marker: str) -> None:
    n = text.count(marker)
    if n != 1:
        raise RuntimeError(f"Expected exactly one marker {marker!r}, found {n}")


def insert_before(text: str, marker: str, inserted: str) -> str:
    require_once(text, marker)
    return text.replace(marker, inserted.rstrip() + "\n\n" + marker, 1)


def main() -> None:
    base = read(BASE)
    falsification = read(FALSIFICATION)
    support_closure = read(SUPPORT_CLOSURE)
    related_work = read(RELATED_WORK)
    known_sector = read(KNOWN_SECTOR)
    repro = read(REPRO)

    require_once(base, AUTHOR_PLACEHOLDER)
    base = base.replace(AUTHOR_PLACEHOLDER, AUTHOR_BLOCK, 1)

    require_once(base, ABSTRACT_FINAL_MARKER)
    base = base.replace(
        ABSTRACT_FINAL_MARKER,
        ABSTRACT_SUPPORT_SENTENCE + " " + ABSTRACT_FINAL_MARKER,
        1,
    )
    require_once(base, INTRO_OLD)
    base = base.replace(INTRO_OLD, INTRO_NEW, 1)

    require_once(base, CONCLUSION_COUNT_OLD)
    base = base.replace(CONCLUSION_COUNT_OLD, CONCLUSION_COUNT_NEW, 1)
    require_once(base, CONCLUSION_FOURTH)
    base = base.replace(CONCLUSION_FOURTH, CONCLUSION_FOURTH + "\n\n" + CONCLUSION_FIFTH, 1)

    for marker in (
        RESULTS_INSERT_MARKER,
        PRIOR_ART_MARKER,
        INTERPRETATION_MARKER,
        LIMITATIONS_MARKER,
        OUTLOOK_MARKER,
        CONCLUSION_MARKER,
    ):
        require_once(base, marker)

    for marker, reference in FIGURE_INSERTIONS:
        base = insert_before(base, marker, reference)

    base = insert_before(base, RESULTS_INSERT_MARKER, FIGURE5_REFERENCE)

    if falsification.startswith("## Prospective falsification"):
        falsification = falsification.replace(
            "## Prospective falsification",
            "## 6.9 Prospective falsification",
            1,
        )
    base = insert_before(base, RESULTS_INSERT_MARKER, falsification)

    base = insert_before(base, PRIOR_ART_MARKER, FIGURE6_REFERENCE)
    if support_closure.startswith("## Observation-space support closure"):
        support_closure = support_closure.replace(
            "## Observation-space support closure and perturbativity",
            "## 7.1 Observation-space support closure and perturbativity",
            1,
        )
    base = insert_before(base, PRIOR_ART_MARKER, support_closure)

    # Keep current prior-art prose in the immutable base and add the closest
    # modern neighboring approaches immediately before Interpretation.
    require(related_work.startswith("## 8.1 Closest neighboring approaches"), "related-work section heading changed")
    base = insert_before(base, INTERPRETATION_MARKER, related_work)

    if known_sector.startswith("## Known-sector specificity control"):
        known_sector = known_sector.replace(
            "## Known-sector specificity control",
            "## 9.4 Known-sector specificity control",
            1,
        )
    base = insert_before(base, LIMITATIONS_MARKER, known_sector)

    repro = repro.replace(
        "# Data, code, and reproducibility",
        "# 11. Data, code, and reproducibility",
        1,
    )
    assembled = base.replace(OUTLOOK_MARKER, "# 12. Outlook", 1)
    assembled = assembled.replace(CONCLUSION_MARKER, "# 13. Conclusions", 1)
    assembled = assembled.replace(
        "# 12. Outlook",
        repro + "\n\n# 12. Outlook",
        1,
    )

    checks = [
        "Aleksey Buyanov",
        'affiliation: "Independent Researcher"',
        'orcid: "0009-0001-2621-9305"',
        "contributions are sixfold",
        "none of 26 ACTxunWISE candidate coordinates",
        "positive absolute-response measure to be nonnormalizable",
        "exact real-data operator realization",
        "provenance-failed candidate",
        "five main conclusions",
        "formal observational quotient is not automatically a physically admissible one",
        "raw-row/HEALPix mapping prerequisites now pass",
        "physical support has not yet been scored",
        "FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1",
        "## 7.1 Observation-space support closure and perturbativity",
        "INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A",
        "PASS_RAW_ROW_HEALPIX_EQUIVALENCE_EXP073R0",
        "4.81826",
        "72.29",
        "Figure 7 summarizes",
        "## 8.1 Closest neighboring approaches",
        "Bashinsky2007DarkKinetics",
        "SaponeKunz2009Fingerprinting",
        "SaponeKunzAmendola2010Fingerprinting",
        "SaponeMajerotto2012Fingerprinting",
        "ReboucasEtAl2026Sound",
        "does **not** claim invention of dark-sector fingerprinting",
        "HojjatiEtAl2012",
        "PetriMarraVonMarttens2026",
        "KoppSkordisThomas2016",
        "BodeOstrikerTurok2001",
        "## 9.4 Known-sector specificity control",
        "0.9990439690",
        "169.692",
        "post-unblinding",
        "Figure 1 summarizes",
        "Figure 2 shows",
        "Figure 3 summarizes",
        "Figure 4 juxtaposes",
        "Figure 5 compares",
        "Figure 6 summarizes",
        "# 11. Data, code, and reproducibility",
        "# 12. Outlook",
        "# 13. Conclusions",
        "A_B=Q_BW_BK_B",
    ]
    for item in checks:
        if item not in assembled:
            raise RuntimeError(f"Required v0.2 content missing: {item}")

    for figure_number in range(1, 8):
        token = f"Figure {figure_number}"
        if assembled.count(token) != 1:
            raise RuntimeError(
                f"Expected exactly one body reference to {token}, found {assembled.count(token)}"
            )

    OUT.write_text(assembled.rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
