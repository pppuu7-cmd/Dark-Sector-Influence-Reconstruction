#!/usr/bin/env python3
"""Build DSIR-I Figure 6: failure-resistant scientific provenance.

The figure deliberately keeps original failed contracts visible next to later,
separately frozen corrective contracts. It also shows the prospective F27
universality falsification without post-hoc band widening or sign reversal.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = HERE / "generated"
OUT.mkdir(parents=True, exist_ok=True)

C3_FAIL = REPO / "data/derived/g7/exp070a_c3_gdm_readonly_dm_power_bridge_v0_1_result.json"
C3_PASS = REPO / "recovery/exp070c_provider_checkpoint_2026-08-27.md"
C5_FAIL = REPO / "data/derived/g7/exp069b_c5_explicit_eft_python_power_bridge_v0_1_result.json"
C5_LADDER_PASS = REPO / "recovery/exp069h_c5_provider_certification_checkpoint_2026-08-27.md"
F27 = REPO / "docs/SCIENTIFIC_FINDING_F27_COMMON_RESPONSE_CENTROID_WITHHELD_FAILURE.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def require_token(text: str, token: str, where: str) -> None:
    if token not in text:
        raise RuntimeError(f"Required frozen token {token!r} missing in {where}")


def main() -> None:
    c3_fail = load(C3_FAIL)
    c5_fail = load(C5_FAIL)
    c3_pass_text = read(C3_PASS)
    c5_text = read(C5_LADDER_PASS)
    f27_text = read(F27)

    if c3_fail["status"] != "FAIL_C3_GDM_READONLY_DM_PHYSICAL_POWER_BRIDGE_V0_1":
        raise RuntimeError("Exp070A original C3 FAIL was reclassified")
    if c5_fail["status"] != "FAIL_C5_EXPLICIT_EFT_PYTHON_POWER_BRIDGE_V0_1":
        raise RuntimeError("Exp069B original C5 FAIL was reclassified")

    c3_initial = float(c3_fail["checks"]["V3_Dm_native_mPk_reconstruction"]["max_relative_error"]["cs2_0"])
    c3_initial_threshold = float(c3_fail["checks"]["V3_Dm_native_mPk_reconstruction"]["threshold"])
    if not c3_initial > c3_initial_threshold:
        raise RuntimeError("Exp070A no longer violates its frozen V3 threshold")

    # Later C3 provider is a distinct contract. Verify exact provenance/value
    # tokens from its immutable recovery checkpoint rather than reclassifying A.
    for token in [
        "PASS_C3_GDM_NATIVE_GRID_PHYSICAL_POWER_PROVIDER_V0_1",
        "33017214292",
        "9625032179",
        "2.8144898798669162e-14",
        "against frozen `1e-10`",
        "Exp070A remains permanent scientific FAIL",
    ]:
        require_token(c3_pass_text, token, "C3 checkpoint")
    c3_corrected = 2.8144898798669162e-14
    c3_corrected_threshold = 1e-10

    c5_initial = float(c5_fail["checks"]["B5_exact_designer_GR_limit"]["mm_max_relative_error"])
    c5_threshold = float(c5_fail["checks"]["B5_exact_designer_GR_limit"]["threshold"])
    if not c5_initial > c5_threshold:
        raise RuntimeError("Exp069B no longer violates its frozen B5 threshold")

    # Frozen Exp069F accuracy ladder values, verified against the checkpoint.
    ladder = np.asarray([5.302921926164412e-6, 2.904403568550871e-6, 1.7011186858522977e-6, 1.3107890273503598e-6])
    raw_ladder = np.asarray([9.938162077359033e-6, 5.400555774622087e-6, 2.8421302380756537e-6, 1.5177816179258466e-6])
    for token in [
        "M_q = [5.302921926164412e-6, 2.904403568550871e-6, 1.7011186858522977e-6, 1.3107890273503598e-6]",
        "R_q = [9.938162077359033e-6, 5.400555774622087e-6, 2.8421302380756537e-6, 1.5177816179258466e-6]",
        "GENERAL_ACCURACY_RECOVERS_FROZEN_GR_LIMIT",
        "PASS_C5_Q3_UNMODIFIED_UPSTREAM_PHYSICAL_PROVIDER_V0_1",
        "Exp069B remains a permanent scientific FAIL",
    ]:
        require_token(c5_text, token, "C5 checkpoint")
    if not np.all(np.diff(ladder) <= 0) or not np.all(np.diff(raw_ladder) <= 0):
        raise RuntimeError("C5 accuracy ladder lost monotone convergence")
    if not ladder[0] > c5_threshold or not ladder[1] <= c5_threshold:
        raise RuntimeError("C5 frozen threshold crossing changed")

    # F27 was prospectively frozen from C3/C5 before C7 response generation.
    band = (0.0022992620786061375, 0.09951219222831723)
    slopes = np.asarray([-1.38559414, -0.66851005, -0.21906458, -0.07156512])
    for token in [
        "0.0022992620786061375",
        "0.09951219222831723",
        "C = {-1.38559414, -0.66851005, -0.21906458, -0.07156512}",
        "FAIL_IDM_DR_COMMON_SOURCE_RESPONSE_SLOPE_V0_1",
        "band must not be widened",
        "G7 remains OPEN",
    ]:
        require_token(f27_text, token, "F27")
    if not np.all((slopes < band[0]) | (slopes > band[1])):
        raise RuntimeError("At least one F27 withheld slope unexpectedly entered the frozen band")
    if not np.all(slopes < 0):
        raise RuntimeError("F27 opposite-sign result changed")

    fig, axes = plt.subplots(1, 3, figsize=(14.2, 4.9), constrained_layout=True)

    ax = axes[0]
    values = np.asarray([c3_initial, c3_corrected])
    labels = ["Exp070A\noriginal bridge", "Exp070C\nnew provider"]
    ax.bar(np.arange(2), values)
    ax.set_yscale("log")
    ax.set_xticks(np.arange(2), labels)
    ax.set_ylabel("relative closure error")
    ax.set_title("A  C3: diagnose, do not overwrite")
    ax.axhline(c3_initial_threshold, linestyle="--", linewidth=1.0, label="070A threshold")
    ax.axhline(c3_corrected_threshold, linestyle=":", linewidth=1.0, label="070C threshold")
    ax.legend(frameon=False, fontsize=7.5)
    ax.grid(True, which="both", axis="y", alpha=0.22)
    ax.text(0, c3_initial * 1.35, "FAIL", ha="center", fontsize=9, fontweight="bold")
    ax.text(1, c3_corrected * 2.0, "PASS\n(new contract)", ha="center", fontsize=8.5, fontweight="bold")

    ax = axes[1]
    q = np.arange(1, 5)
    ax.plot(q, ladder, marker="o", label=r"target $M_q$")
    ax.plot(q, raw_ladder, marker="s", label=r"raw $R_q$")
    ax.axhline(c5_threshold, linestyle="--", linewidth=1.1, label=r"frozen $5\times10^{-6}$")
    ax.set_yscale("log")
    ax.set_xticks(q)
    ax.set_xlabel("accuracy level q")
    ax.set_ylabel("GR-limit closure error")
    ax.set_title("B  C5: prospective accuracy ladder")
    ax.grid(True, which="both", alpha=0.22)
    ax.legend(frameon=False, fontsize=7.5)
    ax.text(1, ladder[0] * 1.25, "q=1 FAIL", ha="center", fontsize=8)
    ax.text(3, ladder[2] * 0.72, "q=3 certified PASS", ha="center", va="top", fontsize=8)

    ax = axes[2]
    x = np.arange(1, len(slopes) + 1)
    ax.axhspan(band[0], band[1], alpha=0.18, label="prefrozen C3/C5 acceptance band")
    ax.axhline(0.0, linewidth=0.8)
    ax.scatter(x, slopes, zorder=3)
    ax.plot(x, slopes, linewidth=0.9, alpha=0.65)
    ax.set_xticks(x, ["pair 1", "pair 2", "pair 3", "pair 4"])
    ax.set_ylabel(r"withheld slope $\mathcal{C}_i$")
    ax.set_title("C  F27: prospective universality FAIL")
    ax.grid(True, alpha=0.22)
    ax.legend(frameon=False, fontsize=7.3, loc="lower right")
    for xx, yy in zip(x, slopes):
        ax.text(xx, yy - 0.045, f"{yy:.3f}", ha="center", va="top", fontsize=7.5)

    fig.suptitle("DSIR-I: failed contracts remain scientific evidence")

    pdf = OUT / "fig06_failure_resistant_science.pdf"
    png = OUT / "fig06_failure_resistant_science.png"
    svg = OUT / "fig06_failure_resistant_science.svg"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)

    provenance = {
        "figure": "DSIR-I Figure 6",
        "script": str(Path(__file__).relative_to(REPO)),
        "sources": {
            "C3_original_FAIL": {"path": str(C3_FAIL.relative_to(REPO)), "file_sha256": sha256(C3_FAIL), "run_id": c3_fail["workflow_run"], "artifact_id": c3_fail["artifact_id"]},
            "C3_new_provider_PASS": {"path": str(C3_PASS.relative_to(REPO)), "file_sha256": sha256(C3_PASS), "run_id": 33017214292, "artifact_id": 9625032179},
            "C5_original_FAIL": {"path": str(C5_FAIL.relative_to(REPO)), "file_sha256": sha256(C5_FAIL), "run_id": c5_fail["workflow_run"], "artifact_id": c5_fail["artifact_id"]},
            "C5_accuracy_and_new_provider": {"path": str(C5_LADDER_PASS.relative_to(REPO)), "file_sha256": sha256(C5_LADDER_PASS), "accuracy_run_id": 33023027901, "provider_run_id": 33024638764},
            "F27_prospective_FAIL": {"path": str(F27.relative_to(REPO)), "file_sha256": sha256(F27), "run_id": 32920776596, "artifact_id": 9589768992},
        },
        "checked_facts": {
            "C3_original_error": c3_initial,
            "C3_original_threshold": c3_initial_threshold,
            "C3_new_contract_closure": c3_corrected,
            "C3_new_contract_threshold": c3_corrected_threshold,
            "C5_original_q1_error": c5_initial,
            "C5_frozen_threshold": c5_threshold,
            "C5_M_q": ladder.tolist(),
            "C5_R_q": raw_ladder.tolist(),
            "F27_prefrozen_band": list(band),
            "F27_withheld_slopes": slopes.tolist(),
        },
        "outputs": {
            "pdf": {"path": pdf.name, "sha256": sha256(pdf)},
            "png": {"path": png.name, "sha256": sha256(png)},
            "svg": {"path": svg.name, "sha256": sha256(svg)},
        },
        "interpretation_boundary": [
            "Exp070C and Exp069H are separately frozen corrective provider contracts; they do not reclassify Exp070A or Exp069B",
            "the C5 accuracy ladder diagnoses numerical convergence and does not certify the provider by itself",
            "F27 falsifies the specified raw full-response-centroid common slope law; its acceptance band must not be widened post hoc",
            "F27 does not falsify all mechanism-native localization ideas and does not close G7/G8/G9",
        ],
    }
    prov = OUT / "fig06_failure_resistant_science_provenance.json"
    prov.write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {pdf}")
    print(f"wrote {png}")
    print(f"wrote {svg}")
    print(f"wrote {prov}")


if __name__ == "__main__":
    main()
