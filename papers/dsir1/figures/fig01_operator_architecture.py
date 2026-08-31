#!/usr/bin/env python3
"""Build DSIR-I Figure 1: operator architecture and conditional equivalence.

This is a formal schematic, not a numerical result. The script verifies that
its equations are present in the frozen theorem note before rendering.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = HERE / "generated"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE = REPO / "docs/CHANNEL_CONDITIONAL_EQUIVALENCE_QUOTIENT_THEOREMS_2026-08-27.md"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def box(ax, x, y, w, h, title, subtitle):
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.015", fill=False, linewidth=1.4)
    ax.add_patch(patch)
    ax.text(x + w/2, y + 0.64*h, title, ha="center", va="center", fontsize=11, fontweight="bold")
    ax.text(x + w/2, y + 0.31*h, subtitle, ha="center", va="center", fontsize=9)


def arrow(ax, x1, y1, x2, y2, label):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=14, linewidth=1.2)
    ax.add_patch(a)
    ax.text((x1+x2)/2, (y1+y2)/2 + 0.035, label, ha="center", va="bottom", fontsize=9)


def main() -> None:
    theorem = SOURCE.read_text(encoding="utf-8")
    for token in ["A_B", "Q_B", "W_B", "K_B", "ker", "equivalence"]:
        if token not in theorem:
            raise RuntimeError(f"Formal source missing required token: {token}")

    fig, ax = plt.subplots(figsize=(12.2, 6.4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    y = 0.60
    w = 0.155
    h = 0.19
    xs = [0.03, 0.235, 0.44, 0.645, 0.83]

    box(ax, xs[0], y, w, h, r"Theory response", r"$r(\theta)\in\mathbb{R}^n$")
    box(ax, xs[1], y, w, h, r"Physical/window", r"$K_B$")
    box(ax, xs[2], y, w, h, r"Whitening", r"$W_B=C_B^{-1/2}$")
    box(ax, xs[3], y, w, h, r"Nuisance quotient", r"$Q_B$")
    box(ax, xs[4], y, 0.14, h, r"Signature", r"$s_B=A_Br$")

    arrow(ax, xs[0] + w, y + h/2, xs[1], y + h/2, "project")
    arrow(ax, xs[1] + w, y + h/2, xs[2], y + h/2, "weight")
    arrow(ax, xs[2] + w, y + h/2, xs[3], y + h/2, "quotient")
    arrow(ax, xs[3] + w, y + h/2, xs[4], y + h/2, "retain")

    ax.text(0.5, 0.47, r"$A_B = Q_B W_B K_B$", ha="center", va="center", fontsize=16)
    ax.text(0.5, 0.37, r"$r_1\sim_B r_2\;\Longleftrightarrow\;A_B(r_1-r_2)=0\;\Longleftrightarrow\;r_1-r_2\in\ker A_B$", ha="center", va="center", fontsize=13)

    # Compatible-channel refinement shown separately to keep its assumption explicit.
    # Baseline MathText only: avoid matrix/style extensions so CI needs no TeX engine.
    ax.text(0.08, 0.19, "Compatible independent channel stacking", fontsize=10, fontweight="bold", ha="left")
    ax.text(0.08, 0.12, r"$A_{B\oplus C}=(A_B,A_C)^T$", fontsize=12, ha="left")
    ax.text(0.39, 0.12, r"$\Rightarrow\quad\ker A_{B\oplus C}=\ker A_B\cap\ker A_C$", fontsize=12, ha="left")
    ax.text(0.08, 0.045, "Caveat: if a joint analysis refits shared nuisance directions, the quotient need not be blockwise compatible.", fontsize=9.5, ha="left")

    fig.suptitle("DSIR-I: observational equivalence is induced by the retained analysis operator", fontsize=14)

    pdf = OUT / "fig01_operator_architecture.pdf"
    png = OUT / "fig01_operator_architecture.png"
    svg = OUT / "fig01_operator_architecture.svg"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)

    provenance = {
        "figure": "DSIR-I Figure 1",
        "script": str(Path(__file__).relative_to(REPO)),
        "formal_source": {"path": str(SOURCE.relative_to(REPO)), "file_sha256": sha256(SOURCE)},
        "equations": [
            "A_B = Q_B W_B K_B",
            "r1 ~_B r2 iff A_B(r1-r2)=0",
            "under compatible independent stacking: A_(B+C)=(A_B,A_C)^T and ker A_(B+C)=ker A_B intersect ker A_C",
        ],
        "outputs": {
            "pdf": {"path": pdf.name, "sha256": sha256(pdf)},
            "png": {"path": png.name, "sha256": sha256(png)},
            "svg": {"path": svg.name, "sha256": sha256(svg)},
        },
        "interpretation_boundary": [
            "formal identifiability architecture, not a new physical law",
            "whitening changes metric/statistical weighting but an invertible whitener does not create a pre-nuisance exact null",
            "joint shared-nuisance refitting can invalidate simple blockwise kernel refinement",
            "full survey-level quotient closure remains a later DSIR stage",
        ],
    }
    prov = OUT / "fig01_operator_architecture_provenance.json"
    prov.write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {pdf}")
    print(f"wrote {png}")
    print(f"wrote {svg}")
    print(f"wrote {prov}")


if __name__ == "__main__":
    main()
