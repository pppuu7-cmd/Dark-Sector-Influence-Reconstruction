#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

from astropy.io import fits


SOURCE_PIN = "6accbf70e55e8a55e7a61289c85d8665bfb1e310"
SOURCE_TREE = "06ca903788fbb2c0791ac7c80e276ce6a78230fd"
README_GIT_BLOB = "056306bfca9d6425073d965fa6a718e34f843c9e"
PAPER_ID = "2105.12108"
REQUESTED_URL = (
    "https://entangled.physics.ox.ac.uk/index.php/s/"
    "cF1x6j4biWXjDy3/download"
)

SOURCE_PATHS = [
    "README.md",
    "xCell/input/desy1_ebossqso_p18cmbk.yml",
    "xCell/xcell/mappers/mapper_DESY1gc.py",
    "xCell/xcell/mappers/mapper_DESY1wl.py",
    "xCell/xcell/cls/cl.py",
    "xCell/xcell/cls/to_sacc.py",
]

SAFE_RESPONSE_HEADERS = {
    "content-type",
    "content-length",
    "content-disposition",
    "etag",
    "last-modified",
    "digest",
    "x-checksum-sha256",
    "x-checksum-md5",
}


def git_output(root: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(root), *args], text=True
    ).strip()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_transfer(path: Path) -> dict:
    lines = path.read_text(errors="replace").splitlines()
    if len(lines) < 3:
        return {
            "effective_url": None,
            "http_status": None,
            "reported_download_bytes": None,
            "parse_error": "expected URL, HTTP status and byte count",
        }
    try:
        http_status = int(lines[-2])
    except ValueError:
        http_status = None
    try:
        reported_bytes = int(lines[-1])
    except ValueError:
        reported_bytes = None
    return {
        "effective_url": lines[-3],
        "http_status": http_status,
        "reported_download_bytes": reported_bytes,
        "parse_error": None,
    }


def parse_safe_headers(path: Path) -> dict:
    headers: dict[str, str] = {}
    for raw in path.read_text(errors="replace").splitlines():
        if ":" not in raw:
            if raw.startswith("HTTP/"):
                headers = {}
            continue
        name, value = raw.split(":", 1)
        key = name.strip().lower()
        if key in SAFE_RESPONSE_HEADERS:
            headers[key] = value.strip()
    return headers


def fits_header_inventory(path: Path) -> tuple[list[dict], bool, str | None]:
    inventory: list[dict] = []
    try:
        with fits.open(
            path,
            mode="readonly",
            memmap=True,
            lazy_load_hdus=True,
            checksum=False,
        ) as hdus:
            for index, hdu in enumerate(hdus):
                header = hdu.header
                tfields = int(header.get("TFIELDS", 0) or 0)
                columns = [
                    str(header.get(f"TTYPE{i}", ""))
                    for i in range(1, tfields + 1)
                ]
                columns = [name for name in columns if name]
                extname = str(header.get("EXTNAME", "PRIMARY"))
                inventory.append(
                    {
                        "index": index,
                        "extname": extname,
                        "hdu_class": type(hdu).__name__,
                        "naxis": int(header.get("NAXIS", 0) or 0),
                        "naxis1": header.get("NAXIS1"),
                        "naxis2": header.get("NAXIS2"),
                        "tfields": tfields,
                        "column_names": columns,
                        "covariance_like_name": bool(
                            re.search(r"cov", extname, flags=re.IGNORECASE)
                        ),
                        "data_payload_accessed": False,
                    }
                )
        return inventory, len(inventory) >= 2, None
    except Exception as exc:
        return [], False, f"{type(exc).__name__}: {exc}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--sacc", required=True)
    parser.add_argument("--headers", required=True)
    parser.add_argument("--transfer", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    root = Path(args.source_root)
    sacc_path = Path(args.sacc)
    out = Path(args.output)

    observed_pin = git_output(root, "rev-parse", "HEAD")
    observed_tree = git_output(root, "rev-parse", "HEAD^{tree}")
    observed_readme_blob = git_output(root, "rev-parse", "HEAD:README.md")

    source_records = []
    for rel in SOURCE_PATHS:
        source_path = root / rel
        source_records.append(
            {
                "path": rel,
                "exists": source_path.is_file(),
                "git_blob": (
                    git_output(root, "rev-parse", f"HEAD:{rel}")
                    if source_path.is_file()
                    else None
                ),
                "sha256": sha256_file(source_path) if source_path.is_file() else None,
            }
        )

    readme = (root / "README.md").read_text(errors="replace")
    source_pass = bool(
        observed_pin == SOURCE_PIN
        and observed_tree == SOURCE_TREE
        and observed_readme_blob == README_GIT_BLOB
        and all(record["exists"] for record in source_records)
        and PAPER_ID in readme
        and REQUESTED_URL in readme
    )

    transfer = parse_transfer(Path(args.transfer))
    actual_bytes = sacc_path.stat().st_size if sacc_path.is_file() else None
    checksum = sha256_file(sacc_path) if actual_bytes else None
    headers = parse_safe_headers(Path(args.headers))
    inventory, fits_pass, fits_error = (
        fits_header_inventory(sacc_path)
        if actual_bytes
        else ([], False, "downloaded object is absent or empty")
    )

    transport_pass = bool(
        transfer["http_status"] == 200
        and actual_bytes
        and transfer["reported_download_bytes"] == actual_bytes
        and checksum
    )
    binding_pass = bool(source_pass and transport_pass and fits_pass)
    status = (
        "BOUND_GROWTH_HISTORY_SD_SACC_CHECKSUM_FOR_OPERATOR_AUDIT_EXP073P"
        if binding_pass
        else "INCOMPLETE_EXP073P_GROWTH_HISTORY_SD_SACC_BINDING"
    )

    result = {
        "experiment": "Exp073P-growth-history-SD-SACC-binding",
        "date": "2026-08-27",
        "status": status,
        "scientific_classification": None,
        "source": {
            "repository": "Cosmotheka/growth-history",
            "expected_pin": SOURCE_PIN,
            "observed_pin": observed_pin,
            "expected_tree": SOURCE_TREE,
            "observed_tree": observed_tree,
            "expected_readme_git_blob": README_GIT_BLOB,
            "observed_readme_git_blob": observed_readme_blob,
            "paper_arxiv": PAPER_ID,
            "requested_url": REQUESTED_URL,
            "source_records": source_records,
            "pass": source_pass,
        },
        "download": {
            "requested_url": REQUESTED_URL,
            **transfer,
            "actual_bytes": actual_bytes,
            "sha256": checksum,
            "selected_response_headers": headers,
            "transport_pass": transport_pass,
        },
        "fits_header_inventory": inventory,
        "fits_container_pass": fits_pass,
        "fits_error": fits_error,
        "binding_pass": binding_pass,
        "large_raw_des_objects_consumed": False,
        "operator_payload_semantics_read": False,
        "covariance_data_read": False,
        "support_fraction_evaluated": False,
        "retained_dimension_evaluated": False,
        "input_checksum_gate_complete": False,
        "support_evaluation_authorized": False,
        "frozen_contract_preserved": {
            "z_min": 0.295,
            "z_max": 2.33,
            "k_max_Mpc^-1": 0.06664762008318016,
            "f_invalid_max": 0.05,
            "minimum_retained_dimension": 15,
            "nside_classifying": 4096,
            "covariance_read": False,
            "nuisance_read": False,
            "relation_null_read": False,
            "G8_read": False,
        },
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
        "next_admissible_step": (
            "Commit the observed SACC SHA256, then audit only its non-covariance "
            "DES tracer, n(z) and bandpower-window payloads before any support output."
            if binding_pass
            else "Resolve public SD SACC transport/container access without changing Exp073P."
        ),
    }

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "status": status,
                "source_pass": source_pass,
                "transport_pass": transport_pass,
                "fits_container_pass": fits_pass,
                "actual_bytes": actual_bytes,
                "sha256": checksum,
                "hdu_count": len(inventory),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
