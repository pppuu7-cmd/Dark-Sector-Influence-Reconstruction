#!/usr/bin/env python3
"""Build DSIR-I Figure 4: channel-conditional degeneracy breaking.

The figure consumes only hard-gated entries in the frozen discriminant-edge
registry. It does not recompute theory responses and does not introduce a new
scientific threshold.

Outputs are written to papers/dsir1/figures/generated/.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = HERE / "generated"
OUT.mkdir(parents=True, exist_ok=True)

SOURCE = REPO / "data/derived/comparison_readiness/discriminant_edges_v0_1.json"

EXPECTED = {
    "C3_cs2_vs_cv2_low_k_P": {
        "run_id": 32774501069,
        "artifact_digest": "sha256:4197b9286e53481164f5a842796199ea94ded202d4e62f6cb232186247291d0e",
    },
    "C3_cs2_vs_C5_fR_scale_only": {
        "run_id": 32774501126,
        "artifact_digest": "sha256:3d7e86924030ff946da05297174df3bb2db09cf3c0ce534356270177dfa1f7f0",
    },
    "C3_cv2_vs_C5_fR_scale_only": {
        "run_id": 32774501126,
        "artifact_digest": "sha256:3d7e86924030ff946da05297174df3bb2db09cf3c0ce534356270177dfa1f7f0",
    },
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    d = load(SOURCE)
    edges = {edge["id"]: edge for edge in d["edges"]}

    for edge_id, expected in EXPECTED.items():
        if edge_id not in edges:
            raise RuntimeError(f"Required frozen discriminant edge missing: {edge_id}")
        evidence = edges[edge_id]["evidence"]
        if evidence["run_id"] != expected["run_id"]:
            raise RuntimeError(f"Unexpected run provenance for {edge_id}")
        if evidence["artifact_digest"] != expected["artifact_digest"]:
            raise RuntimeError(f"Unexpected artifact digest for {edge_id}")

    gdm = edges["C3_cs2_vs_cv2_low_k_P"]["evidence"]
    cs_fr = edges["C3_cs2_vs_C5_fR_scale_only"]["evidence"]
    cv_fr = edges["C3_cv2_vs_C5_fR_scale_only"]["evidence"]

    # Re-evaluate the original frozen hard gates.
    gm = gdm["metrics"]
    gt = gdm["hard_thresholds"]
    if not gm["r_W_angle_deg_at_1e-7"] <= gt["r_W_angle_deg_max"]:
        raise RuntimeError("Frozen Weyl near-degeneracy gate no longer passes")
    if not gm["slip_angle_deg_at_1e-7"] >= gt["slip_angle_deg_min"]:
        raise RuntimeError("Frozen slip-separation gate no longer passes")
    if not gm["combined_angle_deg"] >= gt["combined_angle_deg_min"]:
        raise RuntimeError("Frozen combined-channel separation gate no longer passes")

    for evidence in (cs_fr, cv_fr):
        m = evidence["metrics"]
        t = evidence["hard_thresholds"]
        if not m["scale_angle_deg"] <= t["scale_angle_deg_max"]:
            raise RuntimeError("Frozen scale-mode near-degeneracy gate no longer passes")
        if not m["time_unoriented_angle_deg"] >= t["time_unoriented_angle_deg_min"]:
            raise RuntimeError("Frozen time-mode separation gate no longer passes")
        if not m["full_oriented_angle_deg"] >= t["full_oriented_angle_deg_min"]:
            raise RuntimeError("Frozen full-response separation gate no longer passes")

    fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.8), constrained_layout=True)

    ax = axes[0]
    labels = ["matter", "Weyl", "slip", "Weyl+slip"]
    values = [
        gm["P_angle_deg"],
        gm["r_W_angle_deg_at_1e-7"],
        gm["slip_angle_deg_at_1e-7"],
        gm["combined_angle_deg"],
    ]
    x = np.arange(len(labels))
    bars = ax.bar(x, values)
    ax.set_yscale("log")
    ax.set_xticks(x, labels, rotation=15, ha="right")
    ax.set_ylabel("response-space angle [deg]")
    ax.set_title(r"GDM $c_s^2$ vs $c_v^2$")
    ax.grid(True, which="both", axis="y", alpha=0.25)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, value * 1.12, f"{value:.3g}°", ha="center", va="bottom", fontsize=8)

    ax = axes[1]
    groups = [r"GDM $c_s^2$ vs $f(R)$", r"GDM $c_v^2$ vs $f(R)$"]
    channels = ["scale mode", "time mode", "full response"]
    values2 = np.asarray([
        [
            cs_fr["metrics"]["scale_angle_deg"],
            cs_fr["metrics"]["time_unoriented_angle_deg"],
            cs_fr["metrics"]["full_oriented_angle_deg"],
        ],
        [
            cv_fr["metrics"]["scale_angle_deg"],
            cv_fr["metrics"]["time_unoriented_angle_deg"],
            cv_fr["metrics"]["full_oriented_angle_deg"],
        ],
    ])
    x = np.arange(len(groups))
    width = 0.24
    for j, channel in enumerate(channels):
        ax.bar(x + (j - 1) * width, values2[:, j], width=width, label=channel)
    ax.set_yscale("log")
    ax.set_xticks(x, groups)
    ax.set_ylabel("response-space angle [deg]")
    ax.set_title("Scale lookalikes separate in time/full response")
    ax.grid(True, which="both", axis="y", alpha=0.25)
    ax.legend(frameon=False, fontsize=8)

    fig.suptitle("DSIR-I: degeneracy is conditional on the retained response channel")

    pdf = OUT / "fig04_channel_conditional_degeneracy.pdf"
    png = OUT / "fig04_channel_conditional_degeneracy.png"
    svg = OUT / "fig04_channel_conditional_degeneracy.svg"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)

    provenance = {
        "figure": "DSIR-I Figure 4",
        "script": str(Path(__file__).relative_to(REPO)),
        "source": {
            "path": str(SOURCE.relative_to(REPO)),
            "file_sha256": sha256(SOURCE),
        },
        "hard_gated_edges": {
            edge_id: {
                "run_id": edges[edge_id]["evidence"]["run_id"],
                "artifact_digest": edges[edge_id]["evidence"]["artifact_digest"],
                "metrics": edges[edge_id]["evidence"]["metrics"],
                "hard_thresholds": edges[edge_id]["evidence"]["hard_thresholds"],
            }
            for edge_id in EXPECTED
        },
        "outputs": {
            "pdf": {"path": pdf.name, "sha256": sha256(pdf)},
            "png": {"path": png.name, "sha256": sha256(png)},
            "svg": {"path": svg.name, "sha256": sha256(svg)},
        },
        "interpretation_boundary": [
            "angles are certified theory-response geometry on the frozen domains, not survey detection significances",
            "the combined Weyl+slip result is the frozen equalized response-space construction used by Exp032",
            "no universal parameter translation is inferred from a single-channel near-degeneracy",
        ],
    }
    prov = OUT / "fig04_channel_conditional_degeneracy_provenance.json"
    prov.write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {pdf}")
    print(f"wrote {png}")
    print(f"wrote {svg}")
    print(f"wrote {prov}")


if __name__ == "__main__":
    main()
