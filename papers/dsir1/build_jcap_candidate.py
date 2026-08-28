#!/usr/bin/env python3
"""Build a journal-facing DSIR-I markdown candidate from manuscript_v0_2.

The scientific body remains the audited v0.2 assembly. This builder changes
only presentation required for JCAP preparation: formula-free abstract,
canonical AI disclosure, the frozen compact main-table policy, and a small
fail-closed set of journal-layout prose/heading edits. Detailed removed table
content remains in supplement/numerical_tables.md. No scientific result,
threshold, gate state, figure, or provenance binding is altered.
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "manuscript_v0_2.md"
FRONT = HERE / "JCAP_FRONT_MATTER_DRAFT.md"
ACK = HERE / "ACKNOWLEDGMENTS_AND_DISCLOSURES.md"
SUPP_TABLES = HERE / "supplement" / "numerical_tables.md"
OUT = HERE / "manuscript_jcap_candidate.md"

ABSTRACT_START = "# Abstract"
INTRO_START = "# 1. Introduction"
OUTLOOK_START = "# 12. Outlook"

FAMILY_ATLAS_HEADER = "| Class | Representative mechanism | Main response character used here |"
TANGENT_CHI_HEADER = "| Direction | \\(\\chi_I\\) |"
MECHANISM_RESPONSE_HEADER = "| Family / control | Equation cue and block to inspect | Frozen response pattern / evidence boundary |"
ENVELOPE_HEADER = "| Family | sampled \\(\\chi_I\\) range |"

# Presentation-only replacements motivated by the compiled JCAP log and the
# final referee-facing claim-boundary audit. They are exact-count guarded so a
# scientific-source change cannot be silently masked by this release renderer.
LAYOUT_POLISH = (
    (
        "## 6.2 Scale-only similarity between GDM and designer-\\(f(R)\\) is broken by time evolution",
        "## 6.2 Scale-only similarity between GDM and designer-f(R) is broken by time evolution",
    ),
    (
        "## 6.5 Irreducible scale-time structure carries GDM--\\(f(R)\\) separation",
        "## 6.5 Irreducible scale-time structure in GDM--f(R) separation",
    ),
    (
        "Figure 5 compares response-manifold curvature with the distinct WDM scale-localization and DCDM time-localization controls.",
        "Figure 5 compares response-manifold curvature with WDM scale localization and DCDM time localization.",
    ),
    (
        "Finally, DSIR has not passed its discovery gates. There is no completed model-independent residual law with a fresh withheld-family prediction, and no reconstructed underlying dynamics/action. We therefore make no claim of new fundamental physics in this paper.",
        "Finally, DSIR has not passed its discovery gates. No model-independent residual law has yet passed a fresh withheld-family test, and the underlying dynamics have not been reconstructed. We therefore make no claim of new fundamental physics in this paper.",
    ),
    (
        "A parallel goal is to determine whether mechanism-native localization coordinates---viscous transitions, Compton-like transitions, free-streaming cutoffs, decay epochs, and others---can be mapped into a common observable coordinate without erasing the physical distinctions that make the atlas informative. The present results justify asking that question, but do not prejudge the answer.",
        "A parallel goal is to determine whether mechanism-native localization coordinates can be mapped into a common observable coordinate without erasing the distinctions that make the atlas informative. Examples include viscous and Compton-like transitions, free-streaming cutoffs, and decay epochs. The present results justify asking that question, but do not prejudge the answer.",
    ),
    (
        "Publication figures are generated deterministically from repository products by manuscript-scoped plotting scripts. The figure manifest records exact input products, scientific selection rules, and caption boundaries. Plotting scripts may change presentation details, but they may not silently change the scientific domain, mask, normalization, response orientation, or frozen threshold. Final figure outputs are accompanied by checksums in the build artifact.",
        "Publication figures are generated deterministically from frozen repository products. Manuscript-scoped scripts record the exact inputs, scientific selection rules, and caption boundaries. They may change presentation details but not the scientific domain, mask, normalization, response orientation, or frozen threshold. Final figure outputs carry checksums in the build artifact.",
    ),
    (
        "The hierarchy does not establish that the dark sector possesses a universal coordinate \\(I\\), nor that there are four fundamental influence ``hairs''. The values are conditional on response definition, scale/redshift domain, solver-certified providers, and masking. A future observation-space projection can change statistical distances even when the underlying theory-response morphology is unchanged.",
        "The hierarchy does not establish that the dark sector possesses a universal coordinate \\(I\\), nor that there are four fundamental influence ``hairs''. The values are conditional on response definition, scale/redshift domain, solver-certified providers, masking, and the frozen norm/weighting used by the additive projection. The reported raw response angles and \\(\\chi_I\\) values are therefore not invariants under arbitrary reweighting of the sampled coordinates. A future observation-space projection can change statistical distances even when the underlying theory-response morphology is unchanged.",
    ),
    (
        "First, much of the numerical atlas is a **theory-response** comparison. Although DSIR has already validated data-layer ingredients and observational operators in separate stages, the final common support mask, covariance restriction/whitening, nuisance tangent SVD, and quotient-space relation test are not yet complete for the full cross-family comparison. Theory-space angles must therefore not be read as survey detection significances.",
        "First, much of the numerical atlas is a **theory-response** comparison. Although DSIR has already validated data-layer ingredients and observational operators in separate stages, the final common support mask, covariance restriction/whitening, nuisance tangent SVD, and quotient-space relation test are not yet complete for the full cross-family comparison. Theory-space angles must therefore not be read as survey detection significances. The exact kernel statements in Section 4 apply to the stated linear operator with a fixed covariance and retained nuisance tangent subspace; parameter-dependent covariances or genuinely nonlinear nuisance manifolds would require a local re-linearization or redefinition of \\(A_B\\).",
    ),
)


def require(cond: bool, message: str) -> None:
    if not cond:
        raise RuntimeError(message)


def extract_between(text: str, start: str, end: str) -> str:
    require(start in text and end in text, f"missing section boundary: {start} -> {end}")
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def replace_markdown_table(text: str, header: str, replacement: str) -> str:
    lines = text.splitlines()
    hits = [i for i, line in enumerate(lines) if line.rstrip() == header]
    require(len(hits) == 1, f"expected exactly one table header {header!r}, found {len(hits)}")
    i = hits[0]
    require(i + 1 < len(lines) and lines[i + 1].lstrip().startswith("|---"),
            f"table separator missing after {header!r}")
    j = i + 2
    while j < len(lines) and lines[j].lstrip().startswith("|"):
        j += 1
    new_lines = lines[:i] + [replacement] + lines[j:]
    return "\n".join(new_lines)


def table_count(text: str) -> int:
    lines = text.splitlines()
    count = 0
    for i in range(len(lines) - 1):
        if lines[i].lstrip().startswith("|") and lines[i + 1].lstrip().startswith("|---"):
            count += 1
    return count


def apply_layout_polish(text: str) -> str:
    out = text
    for old, new in LAYOUT_POLISH:
        n = out.count(old)
        require(n == 1, f"expected exactly one JCAP layout-polish source string, found {n}: {old[:80]!r}")
        out = out.replace(old, new, 1)
    return out


def main() -> None:
    src = SOURCE.read_text(encoding="utf-8")
    front = FRONT.read_text(encoding="utf-8")
    ack = ACK.read_text(encoding="utf-8")
    supplement = SUPP_TABLES.read_text(encoding="utf-8")

    # Prove the removed details still exist in the supplement before compacting
    # the journal rendering.
    for token in (
        "Supplementary Table S1",
        "C3 GDM `c_s^2` | `4.5305e-2`",
        "Supplementary Table S2",
        "Supplementary Table S3",
        "Supplementary Table S4",
        "Supplementary Table S5",
        "Supplementary Table S6",
        "G7=OPEN",
    ):
        require(token in supplement, f"supplementary table contract missing: {token}")

    abstract = extract_between(
        front,
        "## JCAP-ready abstract candidate",
        "## Candidate JCAP keywords",
    )
    ai_statement = extract_between(
        ack,
        "## AI-assisted technology disclosure",
        "## Authorship boundary",
    )

    require(src.count(ABSTRACT_START) == 1, "assembled manuscript must contain one Abstract heading")
    require(src.count(INTRO_START) == 1, "assembled manuscript must contain one Introduction heading")
    before_abstract, rest = src.split(ABSTRACT_START, 1)
    _, after_abstract = rest.split(INTRO_START, 1)
    out = (
        before_abstract.rstrip()
        + "\n\n# Abstract\n\n"
        + abstract
        + "\n\n# 1. Introduction"
        + after_abstract
    )

    require(out.count(OUTLOOK_START) == 1, "assembled manuscript must contain one Outlook heading")
    disclosure = (
        "## AI-assisted technology disclosure\n\n"
        + ai_statement
        + "\n\n"
    )
    out = out.replace(OUTLOOK_START, disclosure + OUTLOOK_START, 1)

    # Frozen two-table main-text policy. Scientific details are not deleted from
    # the project; they are retained in supplementary numerical tables.
    out = replace_markdown_table(
        out,
        FAMILY_ATLAS_HEADER,
        "The full class-by-class response-block inventory is retained in Supplementary Table S1a; the main text uses the evidence-graded mechanism-to-response map below as the nonredundant atlas summary.",
    )
    out = replace_markdown_table(
        out,
        TANGENT_CHI_HEADER,
        "Exact direction-by-direction tangent interaction fractions are retained in Supplementary Table S1b. The main-text quantitative comparison below focuses on the finite-amplitude class envelopes and their deterministic node robustness.",
    )

    out = apply_layout_polish(out)

    require(FAMILY_ATLAS_HEADER not in out, "broad family atlas table leaked into JCAP main text")
    require(TANGENT_CHI_HEADER not in out, "tangent chi_I table leaked into JCAP main text")
    require(MECHANISM_RESPONSE_HEADER in out, "mechanism-to-response main table missing")
    require(ENVELOPE_HEADER in out, "finite-amplitude envelope main table missing")
    require(table_count(out) == 2, f"JCAP main text must contain exactly two Markdown tables; found {table_count(out)}")

    for token in (
        "Completed audits reject current routes at the support and normalizability stages",
        "not a universal dark-sector law",
        "claim of new fundamental physics",
        "AI-assisted technology disclosure",
        "OpenAI ChatGPT",
        "takes full responsibility for the content of the manuscript",
        "Supplementary Table S1a",
        "Supplementary Table S1b",
        "No model-independent residual law has yet passed a fresh withheld-family test",
        "Publication figures are generated deterministically from frozen repository products",
        "Examples include viscous and Compton-like transitions",
        "frozen norm/weighting used by the additive projection",
        "not invariants under arbitrary reweighting of the sampled coordinates",
        "parameter-dependent covariances or genuinely nonlinear nuisance manifolds",
        "## 6.2 Scale-only similarity between GDM and designer-f(R) is broken by time evolution",
        "## 6.5 Irreducible scale-time structure in GDM--f(R) separation",
    ):
        require(token in out, f"JCAP candidate lost required boundary: {token}")

    gate_boundary_ok = (
        all(f"{g}=OPEN" in out for g in ("G7", "G8", "G9"))
        or "G7, G8, and G9 remain open" in out
        or "G7, G8, G9 remain OPEN" in out
        or "G7/G8/G9 remain OPEN" in out
    )
    require(gate_boundary_ok, "JCAP candidate lost explicit G7/G8/G9 OPEN boundary")

    for forbidden in (
        "G7 is closed",
        "G8 is closed",
        "G9 is closed",
        "G7=CLOSED",
        "G8=CLOSED",
        "G9=CLOSED",
    ):
        require(forbidden not in out, f"JCAP candidate contains forbidden gate promotion: {forbidden}")

    OUT.write_text(out.rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT}")
    print("PASS: frozen JCAP main-table policy = 2 tables")
    print(f"PASS: JCAP presentation-only layout polish rules = {len(LAYOUT_POLISH)}")


if __name__ == "__main__":
    main()
