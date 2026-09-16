#!/usr/bin/env python3
"""Audit the DSIR-I retrospective known-sector specificity control.

Exp071D is deliberately post-unblinding and descriptive. This audit verifies
both the numerical provenance and, just as importantly, that the manuscript and
claims ledger do not promote it to a prospective threshold, hard gate, or
new dark-sector specificity theorem.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SOURCE = REPO / "data/derived/retrospective/exp071d_matter_response_geometry_taxonomy_key_metrics_v0_1.json"
CLAIMS = HERE / "CLAIMS_LEDGER.md"
PROVENANCE = HERE / "PROVENANCE_MATRIX.md"
SECTION = HERE / "sections/known_sector_nonoverclaim.md"
MANUSCRIPT = HERE / "manuscript_v0_2.md"

EXPECTED_RUN = 33024722072
EXPECTED_ARTIFACT = 9627946054
EXPECTED_DIGEST = "2805a5312cbbabbd408861e340426e5b7d02db5c5499cbbd3ae9d6b52b30b9f7"
EXPECTED_PC1 = 0.999043969028475
EXPECTED_TURN = 169.69204275430147


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(a: float, b: float) -> bool:
    return math.isclose(float(a), float(b), rel_tol=1e-12, abs_tol=0.0)


def main() -> None:
    d = json.loads(SOURCE.read_text(encoding="utf-8"))
    require(d["status"] == "DESCRIPTIVE_POST_UNBLINDING_ONLY", "Exp071D status changed")
    require(d["workflow_run_id"] == EXPECTED_RUN, "Exp071D run provenance changed")
    require(d["artifact_id"] == EXPECTED_ARTIFACT, "Exp071D artifact provenance changed")
    require(d["artifact_sha256"] == EXPECTED_DIGEST, "Exp071D digest changed")

    k2 = d["families"]["K2_baryon_fraction"]
    require(close(k2["PC1_fraction"], EXPECTED_PC1), "K2 PC1 fraction changed")
    require(k2["endpoint_progress_strictly_increasing"] is False, "K2 backtracking control changed")
    require(close(k2["max_tangent_turn_degrees"], EXPECTED_TURN), "K2 maximum tangent turn changed")

    interpretation = "\n".join(d["interpretation"])
    require("not dark-specific" in interpretation, "Exp071D no longer records non-specificity interpretation")
    require("matter-only response geometry" in interpretation, "Exp071D matter-only taxonomy boundary missing")
    require(d["gate_state"] == {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"}, "Exp071D gate boundary changed")

    claims = CLAIMS.read_text(encoding="utf-8")
    provenance = PROVENANCE.read_text(encoding="utf-8")
    section = SECTION.read_text(encoding="utf-8")
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")

    require("Matter-response geometric simplicity is not dark-sector-specific" in claims, "Claims ledger lacks Exp071D boundary")
    require("No promotion of Exp071D" in claims, "Claims ledger lacks post-unblinding prohibition")
    require("| P15 |" in provenance, "P15 provenance row missing")
    for token in [str(EXPECTED_RUN), str(EXPECTED_ARTIFACT), EXPECTED_DIGEST]:
        require(token in provenance, f"P15 provenance token missing: {token}")

    for text, name in [(section, "section"), (manuscript, "assembled manuscript")]:
        require("post-unblinding" in text, f"{name} does not label Exp071D post-unblinding")
        require("no new hard gate" in text, f"{name} does not state no new hard gate")
        require("does not close G7, G8, or G9" in text, f"{name} does not preserve gate boundary")

    require("## 9.4 Known-sector specificity control" in manuscript, "Known-sector control not inserted as §9.4")

    print("PASS: retrospective Exp071D specificity/non-overclaim control")


if __name__ == "__main__":
    main()
