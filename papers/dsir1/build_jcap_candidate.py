#!/usr/bin/env python3
"""Build a journal-facing DSIR-I markdown candidate from manuscript_v0_2.

The scientific body remains the audited v0.2 assembly. This builder changes
only presentation required for JCAP preparation: formula-free abstract and an
explicit AI-assisted-technology disclosure. It does not alter any scientific
result, threshold, gate state, figure, or provenance binding.
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "manuscript_v0_2.md"
FRONT = HERE / "JCAP_FRONT_MATTER_DRAFT.md"
ACK = HERE / "ACKNOWLEDGMENTS_AND_DISCLOSURES.md"
OUT = HERE / "manuscript_jcap_candidate.md"

ABSTRACT_START = "# Abstract"
INTRO_START = "# 1. Introduction"
OUTLOOK_START = "# 12. Outlook"


def require(cond: bool, message: str) -> None:
    if not cond:
        raise RuntimeError(message)


def extract_between(text: str, start: str, end: str) -> str:
    require(start in text and end in text, f"missing section boundary: {start} -> {end}")
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def main() -> None:
    src = SOURCE.read_text(encoding="utf-8")
    front = FRONT.read_text(encoding="utf-8")
    ack = ACK.read_text(encoding="utf-8")

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

    for token in (
        "has not yet been scored for physical support",
        "not a universal dark-sector law",
        "claim of new fundamental physics",
        "AI-assisted technology disclosure",
        "OpenAI ChatGPT",
        "takes full responsibility for the content of the manuscript",
    ):
        require(token in out, f"JCAP candidate lost required boundary: {token}")

    # Gate boundary may be written compactly or in journal prose. Require all
    # three gates to be explicitly open without depending on one punctuation
    # style.
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


if __name__ == "__main__":
    main()
