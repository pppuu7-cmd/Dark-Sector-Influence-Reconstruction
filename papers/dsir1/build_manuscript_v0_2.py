#!/usr/bin/env python3
"""Deterministically assemble DSIR-I manuscript v0.2 from frozen text components.

The script does not edit manuscript.md in place. It inserts the prospective
falsification subsection into Results, inserts the reproducibility section
before Outlook, renumbers the final top-level headings, and writes
manuscript_v0_2.md.
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "manuscript.md"
FALSIFICATION = HERE / "sections" / "prospective_falsification.md"
REPRO = HERE / "sections" / "data_code_reproducibility.md"
OUT = HERE / "manuscript_v0_2.md"

RESULTS_INSERT_MARKER = "# 7. Failure-resistant numerical validation"
OUTLOOK_MARKER = "# 11. Outlook"
CONCLUSION_MARKER = "# 12. Conclusions"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def require_once(text: str, marker: str) -> None:
    n = text.count(marker)
    if n != 1:
        raise RuntimeError(f"Expected exactly one marker {marker!r}, found {n}")


def main() -> None:
    base = read(BASE)
    falsification = read(FALSIFICATION)
    repro = read(REPRO)

    for marker in (RESULTS_INSERT_MARKER, OUTLOOK_MARKER, CONCLUSION_MARKER):
        require_once(base, marker)

    # Keep the new falsification test inside Results as subsection 6.9.
    if falsification.startswith("## Prospective falsification"):
        falsification = falsification.replace(
            "## Prospective falsification",
            "## 6.9 Prospective falsification",
            1,
        )

    assembled = base.replace(
        RESULTS_INSERT_MARKER,
        falsification + "\n\n" + RESULTS_INSERT_MARKER,
        1,
    )

    # Insert reproducibility as new top-level Section 11 and shift the two
    # existing trailing sections by one number.
    repro = repro.replace(
        "# Data, code, and reproducibility",
        "# 11. Data, code, and reproducibility",
        1,
    )
    assembled = assembled.replace(OUTLOOK_MARKER, "# 12. Outlook", 1)
    assembled = assembled.replace(CONCLUSION_MARKER, "# 13. Conclusions", 1)
    assembled = assembled.replace(
        "# 12. Outlook",
        repro + "\n\n# 12. Outlook",
        1,
    )

    # Hard guards against accidental duplicate/incomplete assembly.
    checks = [
        "FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1",
        "# 11. Data, code, and reproducibility",
        "# 12. Outlook",
        "# 13. Conclusions",
        "A_B=Q_BW_BK_B",
    ]
    for item in checks:
        if item not in assembled:
            raise RuntimeError(f"Required v0.2 content missing: {item}")

    OUT.write_text(assembled.rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
