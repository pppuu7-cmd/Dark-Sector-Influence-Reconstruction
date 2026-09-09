#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path

PASS = "PASS_EXP073IM_C2_RADIAL_INTERFACE_V0_2_SYNTHETIC_QA"
SLOTS = [
    "Wm_S0", "Wm_S1", "Wm_S2", "Wm_S3",
    "WW_S0_S0", "WW_S0_S1", "WW_S0_S2", "WW_S0_S3",
    "WW_S1_S1", "WW_S1_S2", "WW_S1_S3",
    "WW_S2_S2", "WW_S2_S3", "WW_S3_S3",
]

@dataclass(frozen=True)
class Row:
    coordinate_id: str
    ordinal: int
    block: str
    slot: str
    band_index: int
    radial_index: int
    lens_bin: int | None
    source_i: int
    source_j: int | None
    representation: str = "FACTORIZED_BROAD_SUPPORT_V0_2"


def rows() -> list[Row]:
    out: list[Row] = []
    ordinal = 0
    # Exact pinned Cosmotheka pair ordering: lens-major, then source, then band.
    for lens in range(5):
        for source in range(4):
            slot = f"Wm_S{source}"
            radial_index = lens * 4 + source
            for band in range(39):
                cid = f"Wm|DESgc__{lens}|DESwl__{source}|TE|component=0|bp={band:02d}"
                out.append(Row(cid, ordinal, "Wm", slot, band, radial_index, lens, source, None))
                ordinal += 1
    # Exact unordered source-pair ordering i<=j, then band.
    ridx = 0
    for i in range(4):
        for j in range(i, 4):
            slot = f"WW_S{i}_S{j}"
            for band in range(39):
                cid = f"WW|DESwl__{i}|DESwl__{j}|EE|component=0|bp={band:02d}"
                out.append(Row(cid, ordinal, "WW", slot, band, ridx, None, i, j))
                ordinal += 1
            ridx += 1
    return out


def digest(rs: list[Row]) -> str:
    payload = "\n".join(json.dumps(asdict(r), sort_keys=True, separators=(",", ":")) for r in rs) + "\n"
    return hashlib.sha256(payload.encode()).hexdigest()


def reject_scalarization(metadata: dict) -> bool:
    forbidden = {"effective_ell", "effective_z", "effective_k", "z", "k_Mpc^-1"}
    return any(k in metadata for k in forbidden)


def trapz_piecewise(z: list[float], b: list[float]) -> float:
    return sum(0.5 * (b[i] + b[i+1]) * (z[i+1] - z[i]) for i in range(len(z)-1))


def factorized_weight(a_ell: list[float], z: list[float], b: list[float]) -> float:
    return sum(abs(x) for x in a_ell) * trapz_piecewise(z, b)


def explicit_cell_weight(a_ell: list[float], z: list[float], b: list[float]) -> float:
    total = 0.0
    for a in a_ell:
        for i in range(len(z)-1):
            total += abs(a) * 0.5 * (b[i] + b[i+1]) * (z[i+1] - z[i])
    return total


def main() -> None:
    rs = rows()
    assert len(rs) == 1170
    assert sum(r.block == "Wm" for r in rs) == 780
    assert sum(r.block == "WW" for r in rs) == 390
    assert len({r.coordinate_id for r in rs}) == 1170
    assert [r.ordinal for r in rs] == list(range(1170))
    assert set(r.slot for r in rs) == set(SLOTS)
    assert {r.radial_index for r in rs if r.block == "Wm"} == set(range(20))
    assert {r.radial_index for r in rs if r.block == "WW"} == set(range(10))
    assert all(0 <= r.band_index < 39 for r in rs)

    # Container/input permutation must not alter canonical inherited ordering.
    canonical = sorted(reversed(rs), key=lambda r: r.ordinal)
    assert digest(canonical) == digest(rs)

    # Any attempt to restore the superseded scalar-row representation fails closed.
    assert reject_scalarization({"effective_z": 0.5})
    assert reject_scalarization({"k_Mpc^-1": 0.02})
    assert not reject_scalarization({"representation": "FACTORIZED_BROAD_SUPPORT_V0_2"})

    # Small exact architecture equivalence: factorized broad support equals explicit
    # ell x radial-segment expansion, demonstrating that factorization is not an
    # effective-coordinate approximation.
    a = [0.0, -2.0, 1.5, 0.25]
    z = [0.0, 0.3, 0.9, 1.4]
    b = [0.0, 1.0, 0.4, 0.0]
    fw = factorized_weight(a, z, b)
    ew = explicit_cell_weight(a, z, b)
    assert math.isfinite(fw) and fw > 0
    assert abs(fw - ew) <= 1e-14 * max(1.0, abs(fw))

    result = {
        "experiment": "Exp073IM-v0.2-synthetic-QA",
        "status": PASS,
        "angular_slot_count": 14,
        "Wm_rows": 780,
        "WW_rows": 390,
        "total_rows": 1170,
        "Wm_radial_indices": 20,
        "WW_radial_indices": 10,
        "ordered_manifest_sha256": digest(rs),
        "factorized_explicit_equivalence_abs_delta": abs(fw-ew),
        "scalarization_rejection": True,
        "permutation_invariant": True,
        "science_gate_scored": False,
        "readiness_credit_authorized": False,
        "downstream_reads": [],
    }
    Path("artifacts").mkdir(exist_ok=True)
    Path("artifacts/exp073im_v0_2_synthetic_qa.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(PASS, result["ordered_manifest_sha256"])


if __name__ == "__main__":
    main()
