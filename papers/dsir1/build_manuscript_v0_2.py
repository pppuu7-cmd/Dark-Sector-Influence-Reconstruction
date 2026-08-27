#!/usr/bin/env python3
"""Deterministically assemble DSIR-I manuscript v0.2 from frozen text components.

The script does not edit manuscript.md in place. It injects the frozen author
metadata, inserts prospectively/retrospectively classified result components,
surfaces the support-eligibility results in Abstract/Introduction/Conclusions,
adds deterministic Figure 1--7 textual references at frozen narrative anchors,
inserts the reproducibility section before Outlook, renumbers the final
headings, and writes manuscript_v0_2.md.
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "manuscript.md"
FALSIFICATION = HERE / "sections" / "prospective_falsification.md"
SUPPORT_CLOSURE = HERE / "sections" / "observation_space_support_closure.md"
KNOWN_SECTOR = HERE / "sections" / "known_sector_nonoverclaim.md"
REPRO = HERE / "sections" / "data_code_reproducibility.md"
OUT = HERE / "manuscript_v0_2.md"

RESULTS_INSERT_MARKER = "# 7. Failure-resistant numerical validation"
PRIOR_ART_MARKER = "# 8. Relation to existing dark-sector parameterizations"
LIMITATIONS_MARKER = "# 10. Limitations and claim boundary"
OUTLOOK_MARKER = "# 11. Outlook"
CONCLUSION_MARKER = "# 12. Conclusions"
AUTHOR_PLACEHOLDER = 'author:\n  - "[authors to be finalized]"'
AUTHOR_BLOCK = '''author:\n  - "Aleksey Buyanov"\naffiliation: "Independent Researcher"\nlocation: "Moscow, Russia"\nemail: "pppuu7@gmail.com"\norcid: "0009-0001-2621-9305"'''

ABSTRACT_FINAL_MARKER = (
    "DSIR-I is therefore a response-classification and identifiability result, not a claim of a universal dark-sector invariant or a discovery of new fundamental physics."
)
ABSTRACT_SUPPORT_SENTENCE = (
    "Prospectively frozen support audits further show that the observational quotient cannot be evaluated merely because its formal operator is defined: none of 26 ACTxunWISE candidate coordinates is supported by the current certified C3/C5 domain at the 5% leakage criterion, while the joint support extension that geometrically recovers 15 coordinates is ineligible under the tested linear perturbativity route. A separate KiDS operator audit finds the chosen positive absolute-response measure to be nonnormalizable, establishing finite positive support normalization as an additional precondition. We therefore do not quote a covariance-whitened or nuisance-quotiented survey distance from an ineligible route."
)

INTRO_OLD = (
    "This paper develops and tests the first part of that program. Its contributions are fivefold. First, we define a block-aware response geometry in which undefined model/channel combinations are masked rather than silently replaced by zeros. Second, we show quantitatively that a simple additive description of scale and time dependence fails for some mechanisms because an irreducible scale-time interaction carries substantial response power. Third, we demonstrate with frozen examples that degeneracy is channel conditional: matter-response lookalikes can be split by metric information, while scale-only lookalikes can be split by temporal evolution. Fourth, we separate microscopic parameter count from response-manifold curvature and linear representation rank. Fifth, we formalize exact channel-conditional equivalence through physical projection, covariance whitening, and nuisance quotienting, while keeping the current empirical atlas distinct from a completed survey-level detectability analysis."
)
INTRO_NEW = (
    "This paper develops and tests the first part of that program. Its contributions are sixfold. First, we define a block-aware response geometry in which undefined model/channel combinations are masked rather than silently replaced by zeros. Second, we show quantitatively that a simple additive description of scale and time dependence fails for some mechanisms because an irreducible scale-time interaction carries substantial response power. Third, we demonstrate with frozen examples that degeneracy is channel conditional: matter-response lookalikes can be split by metric information, while scale-only lookalikes can be split by temporal evolution. Fourth, we separate microscopic parameter count from response-manifold curvature and linear representation rank. Fifth, we formalize exact channel-conditional equivalence through physical projection, covariance whitening, and nuisance quotienting. Sixth, we make the eligibility of that quotient explicit: both the physical domain and the positive support measure must be certified before whitening. A concrete ACTxunWISE C3/C5 audit retains no coordinate on the current domain and reaches a nonperturbative planning frontier, while an independent KiDS absolute-response audit is nonnormalizable under its frozen support measure. Thus the paper distinguishes a mathematically defined quotient from a physically authorized one rather than manufacturing a survey distance through extrapolation or retrospective normalization."
)

CONCLUSION_COUNT_OLD = "The current atlas yields four main conclusions."
CONCLUSION_COUNT_NEW = "The current atlas and observation-route audits yield five main conclusions."
CONCLUSION_FOURTH = (
    "Fourth, mechanism diversity matters. Thermal WDM exhibits a strong scale-localized but nearly time-separable response, whereas withheld DCDM produces a distinct temporal-localization flow. These cases support the use of response localization and trajectory geometry as organizing tools while simultaneously ruling out a naive universal scale-time template."
)
CONCLUSION_FIFTH = (
    "Fifth, a formal observational quotient is not automatically a physically admissible one. The frozen support programme exposes two distinct prerequisites before covariance whitening: the observational kernel must lie on a physically justified theory/provider domain, and the prospectively chosen positive support measure must possess a finite non-zero normalizer. The current ACTxunWISE C3/C5 route fails the first requirement on its certified domain and its geometric extension is ineligible under the tested linear route; the tested KiDS absolute-response measure fails the second by remaining nonnormalizable along the frozen ultraviolet ladder. A finite-positive DES/BOSS harmonic operator candidate has been identified and its public inputs are being reproduced prospectively, but its physical support has not yet been scored and therefore does not close the observational quotient."
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
    known_sector = read(KNOWN_SECTOR)
    repro = read(REPRO)

    require_once(base, AUTHOR_PLACEHOLDER)
    base = base.replace(AUTHOR_PLACEHOLDER, AUTHOR_BLOCK, 1)

    # The support-chain result is central enough to appear in the abstract and
    # contribution list, but the immutable numerical detail remains in §7.1.
    require_once(base, ABSTRACT_FINAL_MARKER)
    base = base.replace(
        ABSTRACT_FINAL_MARKER,
        ABSTRACT_SUPPORT_SENTENCE + " " + ABSTRACT_FINAL_MARKER,
        1,
    )
    require_once(base, INTRO_OLD)
    base = base.replace(INTRO_OLD, INTRO_NEW, 1)

    # Promote the completed eligibility logic into the conclusions without
    # changing the immutable base manuscript. The finite-positive DES/BOSS route
    # is explicitly described as pre-support, not as a passed survey quotient.
    require_once(base, CONCLUSION_COUNT_OLD)
    base = base.replace(CONCLUSION_COUNT_OLD, CONCLUSION_COUNT_NEW, 1)
    require_once(base, CONCLUSION_FOURTH)
    base = base.replace(CONCLUSION_FOURTH, CONCLUSION_FOURTH + "\n\n" + CONCLUSION_FIFTH, 1)

    for marker in (
        RESULTS_INSERT_MARKER,
        PRIOR_ART_MARKER,
        LIMITATIONS_MARKER,
        OUTLOOK_MARKER,
        CONCLUSION_MARKER,
    ):
        require_once(base, marker)

    # Freeze first-reference positions for Figures 1--4 without embedding opaque
    # binaries in the source manuscript. Generated figures live in the CI build
    # artifact; captions are canonical in FIGURE_CAPTIONS.md.
    for marker, reference in FIGURE_INSERTIONS:
        base = insert_before(base, marker, reference)

    # Keep Figure 5 after the withheld-mechanism discussion but before the
    # prospective cross-family falsification inserted as subsection 6.9.
    base = insert_before(base, RESULTS_INSERT_MARKER, FIGURE5_REFERENCE)

    # Keep the new prospective falsification test inside Results as subsection 6.9.
    if falsification.startswith("## Prospective falsification"):
        falsification = falsification.replace(
            "## Prospective falsification",
            "## 6.9 Prospective falsification",
            1,
        )
    base = insert_before(base, RESULTS_INSERT_MARKER, falsification)

    # Figure 6 closes the provider/falsification chronology. The new support-
    # closure subsection then extends Section 7 with an observation-space
    # eligibility result and contains the first body reference to Figure 7.
    base = insert_before(base, PRIOR_ART_MARKER, FIGURE6_REFERENCE)
    if support_closure.startswith("## Observation-space support closure"):
        support_closure = support_closure.replace(
            "## Observation-space support closure and perturbativity",
            "## 7.1 Observation-space support closure and perturbativity",
            1,
        )
    base = insert_before(base, PRIOR_ART_MARKER, support_closure)

    # Retrospective known-sector specificity control belongs in Interpretation,
    # not Results. It is explicitly post-unblinding and creates no new gate.
    if known_sector.startswith("## Known-sector specificity control"):
        known_sector = known_sector.replace(
            "## Known-sector specificity control",
            "## 9.4 Known-sector specificity control",
            1,
        )
    base = insert_before(base, LIMITATIONS_MARKER, known_sector)

    # Insert reproducibility as new top-level Section 11 and shift the two
    # existing trailing sections by one number.
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

    # Hard guards against accidental duplicate/incomplete assembly.
    checks = [
        "Aleksey Buyanov",
        'affiliation: "Independent Researcher"',
        'orcid: "0009-0001-2621-9305"',
        "contributions are sixfold",
        "none of 26 ACTxunWISE candidate coordinates",
        "positive absolute-response measure to be nonnormalizable",
        "five main conclusions",
        "formal observational quotient is not automatically a physically admissible one",
        "physical support has not yet been scored",
        "FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1",
        "## 7.1 Observation-space support closure and perturbativity",
        "INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A",
        "4.81826",
        "72.29",
        "Figure 7 summarizes",
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
