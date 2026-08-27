#!/usr/bin/env python3
"""Deterministic editorial audit for the DSIR-I JCAP submission layer.

This audit contains no scientific acceptance threshold. It checks only the
journal-facing presentation contract: self-contained abstract, no formulae or
citations, conservative claim wording, official-keyword candidates, arXiv
placeholder, availability statement, and the canonical AI-assistance disclosure.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRONT = HERE / "JCAP_FRONT_MATTER_DRAFT.md"
ACK = HERE / "ACKNOWLEDGMENTS_AND_DISCLOSURES.md"
CLAIM_AUDIT = HERE / "ABSTRACT_CONCLUSIONS_CLAIM_AUDIT.md"


def require(cond: bool, message: str) -> None:
    if not cond:
        raise AssertionError(message)


def extract_between(text: str, start: str, end: str) -> str:
    require(start in text and end in text, f"missing section boundary: {start!r} -> {end!r}")
    body = text.split(start, 1)[1].split(end, 1)[0].strip()
    require(body, f"empty section after {start!r}")
    return body


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE))


def main() -> None:
    text = FRONT.read_text(encoding="utf-8")
    ack = ACK.read_text(encoding="utf-8")
    claim_audit = CLAIM_AUDIT.read_text(encoding="utf-8")
    abstract = extract_between(
        text,
        "## JCAP-ready abstract candidate",
        "## Candidate JCAP keywords",
    )

    n = word_count(abstract)
    # Internal editorial target, deliberately stricter than the generic journal
    # requirement that the abstract be brief and fit on the first page.
    require(n <= 250, f"JCAP abstract exceeds internal 250-word target: {n}")
    require(n >= 150, f"JCAP abstract is unexpectedly short: {n}")

    for token in ("\\[", "\\]", "\\(", "\\)", "\\cite", "[@", "Figure ", "Table "):
        require(token not in abstract, f"JCAP abstract contains forbidden formula/reference token: {token!r}")

    for token in (
        "Dark-Sector Influence Reconstruction (DSIR)",
        "all 12 single-node deletion tests",
        "0.3226 degrees",
        "137.94 degrees",
        "prospectively frozen withheld test",
        "physical projection, covariance whitening, and nuisance quotient",
        "exact real-data operator is reproducible",
        "has not yet been scored for physical support",
        "not a universal dark-sector law",
    ):
        require(token in abstract, f"required conservative abstract claim missing: {token}")

    # Accept either grammatical form while preserving the same scientific
    # boundary; do not make the audit depend on one exact English construction.
    require(
        "claim of new fundamental physics" in abstract
        and ("not" in abstract.split("claim of new fundamental physics", 1)[0][-80:] or "or a claim of new fundamental physics" in abstract),
        "new-fundamental-physics non-claim boundary missing",
    )

    for forbidden in (
        "G7 is closed",
        "G8 is closed",
        "G9 is closed",
        "survey detection significance",
        "physical-support PASS",
        "discovery of new fundamental physics",
    ):
        require(forbidden not in abstract, f"forbidden overclaim in JCAP abstract: {forbidden}")

    official_keyword_candidates = (
        "dark energy theory",
        "modified gravity",
        "Cosmological perturbation theory in GR and beyond",
        "power spectrum",
    )
    for keyword in official_keyword_candidates:
        require(keyword in text, f"JCAP keyword candidate missing: {keyword}")
    require("dark matter theory" in text, "documented alternative official keyword missing")

    require("arXiv: [TO BE ASSIGNED BEFORE JCAP SUBMISSION]" in text, "arXiv placeholder missing")
    require("Data, software and code availability" in text, "data/software/code availability candidate missing")
    require("ACKNOWLEDGMENTS_AND_DISCLOSURES.md" in text, "canonical disclosure pointer missing")

    for token in (
        "OpenAI ChatGPT",
        "AI-assisted research and manuscript-preparation tool",
        "independently stored calculations",
        "takes full responsibility for the content of the manuscript",
        "AI-assisted tools are not authors",
    ):
        require(token in ack, f"canonical AI disclosure boundary missing: {token}")

    for token in (
        "Abstract audit",
        "Conclusions audit",
        "G7 relation",
        "G8 validation",
        "G9 dynamics reconstruction",
    ):
        require(token in claim_audit, f"headline-claim audit missing: {token}")

    print(f"PASS: JCAP abstract editorial audit ({n} words)")
    print("PASS: no formulae/citations/figure-table references in abstract")
    print("PASS: conservative science boundary retained")
    print("PASS: keyword, arXiv and availability fields present")
    print("PASS: canonical AI disclosure and headline-claim audit present")


if __name__ == "__main__":
    main()
