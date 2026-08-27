#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ARCHIVE_SHA256 = "23bb7813a7b6ae0e041f070f40716511ff21243e11f6c2783fec64d72de5b823"
PASS = "PASS_FOURIER_MM_OPERATOR_SOURCE_BINDING_EXP073H"
FAIL = "FAIL_FOURIER_MM_OPERATOR_SOURCE_BINDING_EXP073H"
INCOMPLETE = "INCOMPLETE_EXP073H"

WINDOWS = [f"Beutleretal_window_z{z}_{cap}.dat" for z in (1,2,3) for cap in ("NGC","SGC")]
MEASUREMENTS_Z3 = [
    f"Beutleretal_pk_{kind}_DR12_{cap}_z3_prerecon_120.dat"
    for kind in ("monopole","quadrupole","hexadecapole")
    for cap in ("NGC","SGC")
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def numeric_rows(path: Path):
    rows = []
    for line in path.read_text(errors="strict").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        try:
            rows.append([float(x) for x in s.replace(",", " ").split()])
        except ValueError:
            continue
    return rows


def locate(root: Path, name: str) -> Path:
    hits = [p for p in root.rglob(name) if p.is_file() and not p.name.startswith("._")]
    if len(hits) != 1:
        raise RuntimeError(f"expected exactly one {name}, found {len(hits)}")
    return hits[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", required=True)
    ap.add_argument("--root", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    archive = Path(args.archive)
    root = Path(args.root)
    out = Path(args.output)

    record = {
        "experiment": "Exp073H",
        "date": "2026-08-27",
        "record_type": "FROZEN_BEUTLER_WINDOW_SEMANTICS_AUDIT",
        "official_archive_url": "https://data.sdss.org/sas/dr12/boss/papers/clustering/Beutler_etal_DR12COMBINED_fullshape_powspec.tar.gz",
        "archive_sha256": sha256(archive),
        "expected_archive_sha256": ARCHIVE_SHA256,
        "paper": {
            "title": "The clustering of galaxies in the completed SDSS-III Baryon Oscillation Spectroscopic Survey: anisotropic galaxy clustering in Fourier space",
            "arxiv": "1607.03150",
            "doi": "10.1093/mnras/stw3298",
            "window_semantics": "Appendix A / Eq. 22 defines released window multipoles W_l^2(s) from random-pair counts; theory is convolved via correlation-space multipoles and Hankel transforms, not by a released finite true-k mixing matrix.",
            "redshift_bins": ["0.2<z<0.5", "0.4<z<0.6", "0.5<z<0.75"],
            "units": {"measurement_k": "h/Mpc", "window_separation_s": "Mpc/h"},
        },
        "support_fraction_computed": False,
        "covariance_values_read": False,
        "nuisance_rank_read": False,
        "relation_residual_read": False,
        "G8_read": False,
    }

    tests = {}
    try:
        if record["archive_sha256"] != ARCHIVE_SHA256:
            raise RuntimeError("official archive SHA256 mismatch")

        window_meta = []
        for name in WINDOWS:
            p = locate(root, name)
            rows = numeric_rows(p)
            if not rows:
                raise RuntimeError(f"no numeric rows in {name}")
            widths = sorted(set(map(len, rows)))
            first = [r[0] for r in rows]
            window_meta.append({
                "name": name,
                "sha256": sha256(p),
                "size_bytes": p.stat().st_size,
                "rows": len(rows),
                "column_widths": widths,
                "first_column_min": min(first),
                "first_column_max": max(first),
                "first_column_monotone_non_decreasing": all(b >= a for a,b in zip(first, first[1:])),
            })

        measurement_meta = []
        for name in MEASUREMENTS_Z3:
            p = locate(root, name)
            rows = numeric_rows(p)
            if not rows:
                raise RuntimeError(f"no numeric rows in {name}")
            k = [r[0] for r in rows]
            measurement_meta.append({
                "name": name,
                "sha256": sha256(p),
                "size_bytes": p.stat().st_size,
                "rows": len(rows),
                "column_widths": sorted(set(map(len, rows))),
                "k_min_h_Mpc^-1": min(k),
                "k_max_h_Mpc^-1": max(k),
                "k_monotone_non_decreasing": all(b >= a for a,b in zip(k, k[1:])),
            })

        record["bound_objects"] = {"windows": window_meta, "z3_measurements": measurement_meta}

        h1 = len(window_meta) == 6 and len(measurement_meta) == 6 and all(x["sha256"] for x in window_meta + measurement_meta)
        h2 = all(x["rows"] > 1 and x["k_monotone_non_decreasing"] for x in measurement_meta)
        # Frozen H3 requires a finite non-negative true-k support envelope without a fiducial P(k)
        # or post-hoc cutoff. The public Beutler files are W_l^2(s) multipoles in separation space;
        # the paper's Appendix A maps theory through correlation-space multipoles and Hankel transforms.
        # The archive does not release a finite non-negative true-k mixing matrix for these measurements.
        h3 = False
        h4 = True  # paper/release convention explicitly gives k in h/Mpc and s in Mpc/h; exact unit map is defined.
        h5 = True  # z3 is the immutable 0.5<z<0.75 high-z bin.
        h6 = True  # released P0/P2/P4 are galaxy-density clustering multipoles.
        h7 = record["covariance_values_read"] is False
        h8 = not any(record[k] for k in ("nuisance_rank_read","relation_residual_read","G8_read"))

        tests = {
            "H1_immutable_public_identity": {"pass": h1, "detail": "official archive SHA256 plus per-object SHA256 recorded"},
            "H2_explicit_Fourier_coordinate": {"pass": h2, "detail": "z3 P0/P2/P4 measurements are direct finite k-bin tables"},
            "H3_finite_positive_support_normalization": {"pass": h3, "detail": "FAIL: released survey-window objects are W_l^2(s) separation-space multipoles; no finite non-negative true-k mixing matrix is released, so an all-k positive support envelope would require an extra theory weighting/cutoff"},
            "H4_physical_unit_traceability": {"pass": h4, "detail": "paper/release conventions explicitly trace k[h/Mpc] and s[Mpc/h]; no support limit was reinterpreted"},
            "H5_high_z_compatibility": {"pass": h5, "detail": "z3 corresponds to 0.5<z<0.75"},
            "H6_mm_semantics": {"pass": h6, "detail": "P0/P2/P4 are galaxy-density power-spectrum multipoles"},
            "H7_no_covariance_dependence": {"pass": h7},
            "H8_no_downstream_leakage": {"pass": h8},
        }
        record["tests"] = tests
        record["status"] = PASS if all(v["pass"] for v in tests.values()) else FAIL
        record["interpretation"] = "This is an Exp073H source/operator feasibility result, not a 5%-support result. The Beutler fallback is immutably bound and Fourier-binned, but its released window representation does not satisfy frozen H3."
        record["next_admissible_step"] = "prospectively freeze a search for a public clustering release with an explicit finite true-k window/mixing matrix; do not compute KiDS+BNT common support or covariance yet"
    except Exception as exc:
        record["status"] = INCOMPLETE
        record["error"] = f"{type(exc).__name__}: {exc}"
        record["tests"] = tests
        record["next_admissible_step"] = "repair retrieval/reproduction only; do not reinterpret as scientific FAIL"

    record["gate_state"] = {"G7":"OPEN","G8":"OPEN","G9":"OPEN"}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(record, indent=2) + "\n")
    print("EXP073H_STATUS", record["status"])
    if record.get("tests"):
        print("H1_H8", {k:v["pass"] for k,v in record["tests"].items()})

if __name__ == "__main__":
    main()
