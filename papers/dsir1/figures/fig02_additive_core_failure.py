#!/usr/bin/env python3
"""Build DSIR-I Figure 2: failure of the additive scale+time core.

The additive decomposition is recomputed from the frozen low-k response vectors:

    R(z,k) = mu + T(k) + tau(z) + I(z,k)

with the standard two-way additive projection under the frozen unweighted
Euclidean grid norm. The recomputed interaction fractions are checked against
Exp045A before plotting.
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

RESPONSES = REPO / "data/derived/comparison_readiness/local_response_tangents_v0_1.json"
EXP045A = REPO / "data/derived/comparison_readiness/experiment_045a_core_G_T_tau_additive_projection_v0_1.json"

EXPECTED_RUN = 32883280742
EXPECTED_ARTIFACT = 9576600500
EXPECTED_DIGEST = "59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def additive_decomposition(r: np.ndarray) -> tuple[float, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    mu = float(np.mean(r))
    T = np.mean(r, axis=0) - mu
    tau = np.mean(r, axis=1) - mu
    core = mu + tau[:, None] + T[None, :]
    interaction = r - core
    return mu, T, tau, core, interaction


def main() -> None:
    source = load(RESPONSES)
    gate = load(EXP045A)

    prov = gate["hard_provenance"]
    if prov["run_id"] != EXPECTED_RUN or prov["artifact_id"] != EXPECTED_ARTIFACT:
        raise RuntimeError("Unexpected Exp045A hard provenance")
    if prov["artifact_sha256"] != EXPECTED_DIGEST:
        raise RuntimeError("Unexpected Exp045A artifact digest")
    if gate["status"] != "FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1":
        raise RuntimeError("Exp045A scientific FAIL was reclassified")
    if not gate["operator_controls"]["pass"]:
        raise RuntimeError("Exp045A operator controls do not pass")

    z = np.asarray(source["z_nodes"], dtype=float)
    k = np.asarray(source["k_h_mpc"], dtype=float)
    nz, nk = len(z), len(k)
    vectors = {d["id"]: np.asarray(d["vector"], dtype=float).reshape(nz, nk) for d in source["directions"]}
    stored = {d["id"]: d for d in gate["directions"]}

    recomputed = {}
    for direction_id, r in vectors.items():
        mu, T, tau, core, interaction = additive_decomposition(r)
        chi = float(np.sum(interaction * interaction) / np.sum(r * r))
        target = float(stored[direction_id]["interaction_power_fraction"])
        if not np.isclose(chi, target, rtol=2e-12, atol=1e-18):
            raise RuntimeError(f"Recomputed chi_I mismatch for {direction_id}: {chi} vs {target}")
        reconstruction = core + interaction
        err = float(np.max(np.abs(reconstruction - r)))
        if err > 1e-10 * max(1.0, float(np.max(np.abs(r)))):
            raise RuntimeError(f"Additive decomposition reconstruction failure for {direction_id}")
        recomputed[direction_id] = {
            "mu": mu,
            "T": T,
            "tau": tau,
            "core": core,
            "interaction": interaction,
            "chi_I": chi,
        }

    exemplar_id = "C5_designer_fR_B0"
    r = vectors[exemplar_id]
    dec = recomputed[exemplar_id]
    norm = float(np.linalg.norm(r))

    fig = plt.figure(figsize=(12.2, 7.0), constrained_layout=True)
    gs = fig.add_gridspec(2, 3, height_ratios=[1.0, 0.9])
    axes = [fig.add_subplot(gs[0, i]) for i in range(3)]
    axbar = fig.add_subplot(gs[1, :])

    panels = [
        (r / norm, r"A  normalized $R(z,k)$"),
        (dec["core"] / norm, r"B  additive $\mu+T+\tau$"),
        (dec["interaction"] / norm, r"C  irreducible $I(z,k)$"),
    ]
    vmax = max(float(np.max(np.abs(x))) for x, _ in panels)
    for ax, (arr, title) in zip(axes, panels):
        im = ax.imshow(arr, aspect="auto", origin="lower", vmin=-vmax, vmax=vmax, cmap="coolwarm")
        ax.set_title(title)
        ax.set_xticks(np.arange(nk), [f"{x:g}" for x in k])
        ax.set_yticks(np.arange(nz), [f"{x:g}" for x in z])
        ax.set_xlabel(r"$k\,[h\,\mathrm{Mpc}^{-1}]$")
        ax.set_ylabel("z")
    cbar = fig.colorbar(im, ax=axes, shrink=0.85)
    cbar.set_label(r"response divided by $\|R\|_2$")

    ids = [d["id"] for d in gate["directions"]]
    labels = ["smooth DE", r"IDE $\alpha<0$", r"IDE $\beta$", r"GDM $c_s^2$", r"GDM $c_v^2$", r"designer $f(R)$"]
    chi = [recomputed[i]["chi_I"] for i in ids]
    x = np.arange(len(ids))
    bars = axbar.bar(x, chi)
    axbar.set_yscale("log")
    axbar.set_xticks(x, labels, rotation=18, ha="right")
    axbar.set_ylabel(r"irreducible interaction fraction $\chi_I$")
    axbar.set_title("D  Frozen low-k directions")
    axbar.grid(True, which="both", axis="y", alpha=0.25)
    for bar, value in zip(bars, chi):
        axbar.text(bar.get_x() + bar.get_width()/2, value * 1.25, f"{value:.2e}", ha="center", va="bottom", fontsize=8)

    fig.suptitle(r"DSIR-I: the additive scale+time core fails for material $k\times z$ structure")

    pdf = OUT / "fig02_additive_core_failure.pdf"
    png = OUT / "fig02_additive_core_failure.png"
    svg = OUT / "fig02_additive_core_failure.svg"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)

    out_prov = {
        "figure": "DSIR-I Figure 2",
        "script": str(Path(__file__).relative_to(REPO)),
        "sources": {
            "responses": {"path": str(RESPONSES.relative_to(REPO)), "file_sha256": sha256(RESPONSES)},
            "Exp045A": {
                "path": str(EXP045A.relative_to(REPO)),
                "run_id": prov["run_id"],
                "artifact_id": prov["artifact_id"],
                "artifact_sha256": prov["artifact_sha256"],
                "status": gate["status"],
            },
        },
        "decomposition": "mu=mean(R); T(k)=mean_z(R)-mu; tau(z)=mean_k(R)-mu; I=R-mu-T-tau",
        "recomputed_chi_I": {direction_id: recomputed[direction_id]["chi_I"] for direction_id in ids},
        "exemplar": exemplar_id,
        "outputs": {
            "pdf": {"path": pdf.name, "sha256": sha256(pdf)},
            "png": {"path": png.name, "sha256": sha256(png)},
            "svg": {"path": svg.name, "sha256": sha256(svg)},
        },
        "interpretation_boundary": [
            "C4 WDM is absent because its informative high-k support is not the frozen common low-k block; it is not zero-imputed",
            "chi_I is a representation diagnostic on the stated domain, not a fundamental dark-sector degree of freedom",
            "Exp045A remains a scientific FAIL of the compact additive core",
            "theory-response morphology is not survey detection significance",
        ],
    }
    prov_path = OUT / "fig02_additive_core_failure_provenance.json"
    prov_path.write_text(json.dumps(out_prov, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {pdf}")
    print(f"wrote {png}")
    print(f"wrote {svg}")
    print(f"wrote {prov_path}")


if __name__ == "__main__":
    main()
