#!/usr/bin/env python3
"""Reproduce the retrospective Paper-I moving-scale/nonseparability bridge.

This is an integrity/reproducibility audit, not a newly preregistered science
gate. The numerical tolerances below only detect accidental changes to the
compact evidence snapshot; they are not physical acceptance thresholds.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE / "evidence" / "moving_scale_nonseparability_bridge_v0_1.json"

# Reproduction tolerances only; not scientific thresholds.
RTOL = 5e-10
ATOL = 5e-13
CHI_ATOL = 1e-18


def require(cond: bool, message: str) -> None:
    if not cond:
        raise RuntimeError(message)


def close(a: float, b: float, *, atol: float = ATOL) -> bool:
    return bool(np.isclose(float(a), float(b), rtol=RTOL, atol=atol))


def abs_cos(a: np.ndarray, b: np.ndarray) -> float:
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    require(na > 0 and nb > 0, "cosine requires non-zero vectors")
    return float(abs(np.dot(a, b) / (na * nb)))


def abs_frobenius_cos(a: np.ndarray, b: np.ndarray) -> float:
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    require(na > 0 and nb > 0, "Frobenius cosine requires non-zero matrices")
    return float(abs(np.sum(a * b) / (na * nb)))


def double_center(r: np.ndarray) -> np.ndarray:
    return r - r.mean(axis=0, keepdims=True) - r.mean(axis=1, keepdims=True) + r.mean()


def wdm_metrics(model: dict, k: np.ndarray) -> dict[str, float]:
    r = np.asarray(model["r_wdm"], dtype=float)
    require(r.shape == (7, 6), f"unexpected WDM response shape: {r.shape}")
    require(np.all(np.isfinite(r)), "non-finite WDM response")

    interaction = double_center(r)
    chi_i = float(np.sum(interaction * interaction) / np.sum(r * r))

    u, s, vh = np.linalg.svd(interaction, full_matrices=False)
    require(np.all(np.isfinite(s)) and float(np.sum(s * s)) > 0, "invalid interaction SVD")
    pc1_energy = float(s[0] ** 2 / np.sum(s * s))

    cutoff = np.asarray(model["k_rminus0p1_h_mpc_by_z"], dtype=float)
    require(cutoff.shape == (7,) and np.all(cutoff > 0), "invalid WDM cutoff vector")
    delta = np.log(cutoff)
    delta_c = delta - delta.mean()
    delta_log_span = float(np.ptp(delta))

    x = np.log(k)
    mean_profile = r.mean(axis=0)
    profile_prime = np.gradient(mean_profile, x)
    profile_prime_c = profile_prime - profile_prime.mean()
    first_order_template = -np.outer(delta_c, profile_prime_c)

    return {
        "chi_I_recomputed": chi_i,
        "delta_log_span": delta_log_span,
        "interaction_pc1_energy": pc1_energy,
        "abs_cos_temporal_mode_vs_cutoff_drift": abs_cos(u[:, 0], delta_c),
        "abs_cos_scale_mode_vs_centered_profile_derivative": abs_cos(vh[0], profile_prime_c),
        "abs_frobenius_cos_first_order_outer_template": abs_frobenius_cos(
            interaction, first_order_template
        ),
    }


def main() -> None:
    data = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    require(
        data.get("schema") == "dsir.paper1.moving_scale_nonseparability_bridge.evidence.v0.1",
        "unexpected moving-scale evidence schema",
    )
    require(
        data.get("classification") == "RETROSPECTIVE_EVIDENCE_SNAPSHOT_NOT_NEW_PROSPECTIVE_GATE",
        "retrospective classification boundary missing",
    )
    correction = data.get("correction_note", "")
    require("not byte-equivalent" in correction and "audit must reproduce" in correction,
            "fail-closed evidence-correction note missing")

    boundaries = "\n".join(data.get("boundaries", []))
    for token in (
        "not a universal dark-sector law",
        "retrospective",
        "no universal chi_I calibration across domains",
        "quasi-steady proxy",
        "No G7/G8/G9",
    ):
        require(token in boundaries, f"missing interpretation boundary: {token}")

    z = np.asarray(data["z_nodes"], dtype=float)
    require(z.shape == (7,) and np.all(np.diff(z) > 0), "unexpected redshift grid")
    k = np.asarray(data["wdm"]["k_h_mpc"], dtype=float)
    require(k.shape == (6,) and np.all(np.diff(k) > 0), "unexpected WDM k grid")
    require(data["wdm"]["target_log_power_response"] == -0.1, "cutoff target changed")
    require("rechecked directly against the raw CLASS P(k) files" in data["wdm"]["crossing_extraction"],
            "raw cutoff recheck provenance missing")

    expected_by_mass = {
        float(row["m_keV"]): row
        for row in data["reference_metrics_for_integrity_reproduction"]["wdm"]
    }
    seen: list[float] = []
    observed: list[dict[str, float]] = []
    for model in data["wdm"]["models"]:
        mass = float(model["m_keV"])
        seen.append(mass)
        require(mass in expected_by_mass, f"missing reference metrics for WDM {mass} keV")
        got = wdm_metrics(model, k)
        ref = expected_by_mass[mass]

        require(close(got["chi_I_recomputed"], model["artifact_chi_I"], atol=CHI_ATOL),
                f"WDM {mass}: compact response no longer reproduces artifact chi_I")
        for key, value in got.items():
            atol = CHI_ATOL if key == "chi_I_recomputed" else ATOL
            require(close(value, ref[key], atol=atol),
                    f"WDM {mass}: integrity mismatch for {key}: {value} vs {ref[key]}")
        observed.append({"m_keV": mass, **got})

    require(seen == [2.0, 3.0, 5.0], f"unexpected WDM model order/content: {seen}")

    ctx = data["contextual_artifact_metrics"]
    gdm = ctx["gdm"]
    fr = ctx["designer_fR"]
    require(gdm["original_status"] == "PASS_GDM_WINDOW_CROSSING_VALIDATION_V0_1",
            "GDM source status changed")
    require(fr["original_status"] == "PASS_FR_WINDOW_CROSSING_VALIDATION_V0_1",
            "f(R) source status changed")
    require(gdm["delta_log_span_min"] <= gdm["delta_log_span_max"], "bad GDM span range")
    require(fr["delta_log_span_min"] <= fr["delta_log_span_max"], "bad f(R) span range")

    # Snapshot-only descriptive ordering. This is not a universal threshold or gate.
    wdm_span_max = max(row["delta_log_span"] for row in observed)
    require(wdm_span_max < gdm["delta_log_span_min"] < fr["delta_log_span_min"],
            "retrospective source-scale-motion ordering changed")

    print("RETROSPECTIVE moving-scale/nonseparability reproduction")
    for row in observed:
        print(
            "WDM {m_keV:g} keV: chi_I={chi_I_recomputed:.6e}, "
            "dlogk_span={delta_log_span:.6e}, PC1(I)={interaction_pc1_energy:.9f}, "
            "cos_t={abs_cos_temporal_mode_vs_cutoff_drift:.9f}, "
            "cos_k={abs_cos_scale_mode_vs_centered_profile_derivative:.9f}, "
            "cos_outer={abs_frobenius_cos_first_order_outer_template:.9f}".format(**row)
        )
    print(
        "context spans: WDM<=%.6e, GDM=[%.6e, %.6e], f(R)=[%.6e, %.6e]"
        % (
            wdm_span_max,
            gdm["delta_log_span_min"],
            gdm["delta_log_span_max"],
            fr["delta_log_span_min"],
            fr["delta_log_span_max"],
        )
    )
    print("PASS: retrospective moving-scale bridge integrity reproduction")
    print("BOUNDARY: no new prospective gate, universality, G7/G8/G9, or survey claim")


if __name__ == "__main__":
    main()
