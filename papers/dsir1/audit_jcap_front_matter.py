#!/usr/bin/env python3
"""Deterministic editorial audit for the DSIR-I JCAP front matter.

This audit contains no scientific acceptance threshold.  It checks only the
journal-facing presentation contract: self-contained abstract, no formulae or
citations, conservative claim wording, official-keyword candidates, and an
AI-assistance disclosure candidate.
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
FRONT = HERE / "JCAP_FRONT_MATTER_DRAFT.md"


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
    abstract = extract_between(
        text,
        "## JCAP-ready abstract candidate",
        "## Candidate JCAP keywords",
    )

    n = word_count(abstract)
    # Internal editorial target, deliberately stricter than the generic IOP
    # 300-word guidance.  JCAP's binding requirement is that the abstract be
    # brief and fit the first page; actual first-page fit is checked in LaTeX.
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
        "not a claim of new fundamental physics",
    ):
        require(token in abstract, f"required conservative abstract claim missing: {token}")

    # Prevent accidental promotion of the open survey programme.
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

    require("AI-assisted technology statement" in text, "AI disclosure candidate missing")
    require("OpenAI ChatGPT" in text, "AI tool is not identified in disclosure candidate")
    require("not used as scientific evidence" in text, "AI disclosure evidence boundary missing")
    require("arXiv: [TO BE ASSIGNED BEFORE JCAP SUBMISSION]" in text, "arXiv placeholder missing")
    require("Data, software and code availability" in text, "data/software/code availability candidate missing")

    print(f"PASS: JCAP abstract editorial audit ({n} words)")
    print("PASS: no formulae/citations/figure-table references in abstract")
    print("PASS: conservative science boundary retained")
    print("PASS: keyword, arXiv, AI-disclosure and availability fields present")


if __name__ == "__main__":
    main()
