#!/usr/bin/env python3
"""Validate and byte-preserve the complete Exp073R1 v0.7 result payload."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
import struct
import tempfile
import warnings
import zipfile
from pathlib import Path
from pathlib import PurePosixPath
from typing import Any

import exp073p_aggregate_prerequisite_join_v0_3 as evaluator
from exp073p_r1_admissibility_interlock_v0_1 import InterlockError, validate_r1_summary

SUMMARY_NAME = "exp073r1_desy1_transport_stabilized_replay_v0_7_summary.json"
ACQUISITION_NAME = "exp073r1_v0_7_remote_acquisition_provenance.json"
RUNTIME_NAME = "exp073r1_v0_7_runtime_provenance.txt"
RECORD_NAMES = {
    str(b): f"exp073r1_v05_bin{b}_pixel_indices_le_u32.bin" for b in range(4)
}
MASK_NAMES = {
    str(b): f"exp073r1_v05_source_bin{b}_mask_ring_nside4096_bitpack_little.bin"
    for b in range(4)
}
ARCHIVE_MEMBERS = {
    SUMMARY_NAME,
    ACQUISITION_NAME,
    RUNTIME_NAME,
    *(f"exp073r1_v05_records/{name}" for name in RECORD_NAMES.values()),
    *(f"exp073r1_v05_masks/{name}" for name in MASK_NAMES.values()),
}


class PayloadError(ValueError):
    pass


def need(condition: bool, message: str) -> None:
    if not condition:
        raise PayloadError(message)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def file_record(path: Path) -> dict[str, Any]:
    need(path.is_file(), f"payload file unavailable: {path}")
    size = path.stat().st_size
    need(size > 0, f"payload file empty: {path.name}")
    return {"basename": path.name, "bytes": size, "sha256": sha256_file(path)}


def unique_basename(root: Path, basename: str) -> Path:
    matches = [path for path in root.rglob(basename) if path.is_file()]
    need(len(matches) == 1, f"payload basename multiplicity {basename}: {len(matches)}")
    return matches[0]


def exact_bin_files(root: Path, expected: dict[str, str], pattern: str, where: str) -> dict[str, Path]:
    found = [path for path in root.rglob(pattern) if path.is_file()]
    names = [path.name for path in found]
    need(len(names) == len(set(names)), f"duplicate {where} basename")
    need(set(names) == set(expected.values()), f"{where} bin identity set drift: {sorted(names)}")
    return {key: unique_basename(root, name) for key, name in expected.items()}


def read_json_object(path: Path, where: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_bytes())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PayloadError(f"invalid {where} JSON: {exc}") from exc
    need(isinstance(value, dict), f"{where} JSON is not an object")
    return value


def inspect_and_extract_archive(zip_path: Path, out_dir: Path) -> None:
    need(zip_path.is_file() and zip_path.stat().st_size > 0, "R1 artifact ZIP unavailable or empty")
    try:
        archive = zipfile.ZipFile(zip_path, "r")
    except (zipfile.BadZipFile, OSError) as exc:
        raise PayloadError(f"invalid R1 artifact ZIP: {exc}") from exc
    with archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        need(len(names) == len(set(names)), "duplicate artifact ZIP member name")
        for info in infos:
            name = info.filename
            posix = PurePosixPath(name)
            need("\\" not in name, f"backslash ZIP member rejected: {name}")
            need(not posix.is_absolute() and ".." not in posix.parts, f"unsafe ZIP member path: {name}")
            need(not info.is_dir(), f"unexpected directory ZIP member: {name}")
            need(info.flag_bits & 0x1 == 0, f"encrypted ZIP member rejected: {name}")
            need(info.file_size > 0, f"empty ZIP member rejected: {name}")
        need(set(names) == ARCHIVE_MEMBERS, f"artifact ZIP member set drift: {sorted(names)}")

        by_name = {info.filename: info for info in infos}
        for name in (SUMMARY_NAME, ACQUISITION_NAME):
            need(by_name[name].file_size <= 10_000_000, f"oversized JSON authority member: {name}")
        need(by_name[RUNTIME_NAME].file_size <= 1_000_000, "oversized runtime authority member")
        for b, name in RECORD_NAMES.items():
            size = by_name[f"exp073r1_v05_records/{name}"].file_size
            need(0 < size <= 4 * 136_930_995, f"record archive size invalid for bin {b}")
        for b, name in MASK_NAMES.items():
            need(
                by_name[f"exp073r1_v05_masks/{name}"].file_size == 25_165_824,
                f"mask archive size invalid for bin {b}",
            )

        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True)
        for info in infos:
            target = out_dir / info.filename
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info, "r") as source, target.open("wb") as destination:
                shutil.copyfileobj(source, destination, length=8 << 20)


def build_manifest(root: Path) -> tuple[dict[str, Any], dict[str, Path]]:
    need(root.is_dir(), f"R1 payload root unavailable: {root}")
    summary_path = unique_basename(root, SUMMARY_NAME)
    acquisition_path = unique_basename(root, ACQUISITION_NAME)
    runtime_path = unique_basename(root, RUNTIME_NAME)
    record_paths = exact_bin_files(root, RECORD_NAMES, "exp073r1_v05_bin*_pixel_indices_le_u32.bin", "record")
    mask_paths = exact_bin_files(
        root,
        MASK_NAMES,
        "exp073r1_v05_source_bin*_mask_ring_nside4096_bitpack_little.bin",
        "mask",
    )

    summary = read_json_object(summary_path, "R1 summary")
    acquisition = read_json_object(acquisition_path, "R1 acquisition")
    try:
        validate_r1_summary(summary)
        evaluator.validate_acquisition(acquisition, summary)
    except (InterlockError, evaluator.JoinError) as exc:
        raise PayloadError(str(exc)) from exc

    paths: dict[str, Path] = {
        "summary": summary_path,
        "acquisition": acquisition_path,
        "runtime": runtime_path,
    }
    paths.update({f"record_{key}": value for key, value in record_paths.items()})
    paths.update({f"mask_{key}": value for key, value in mask_paths.items()})
    files = {
        "summary": file_record(summary_path),
        "acquisition": file_record(acquisition_path),
        "runtime": file_record(runtime_path),
        "records": {key: file_record(record_paths[key]) for key in sorted(record_paths)},
        "masks": {key: file_record(mask_paths[key]) for key in sorted(mask_paths)},
    }
    manifest = {
        "schema": evaluator.PAYLOAD_SCHEMA,
        "experiment": "Exp073P-v0.3-R1-payload-normalizer",
        "status": evaluator.PAYLOAD_PASS,
        "complete_payload": True,
        "duplicate_basenames_rejected": True,
        "extra_bin_identities_rejected": True,
        "files": files,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "retained_dimension_evaluated": False,
        "covariance_read": False,
        "whitening_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "heldout_read": False,
        "G8_read": False,
        "gate_state": copy.deepcopy(evaluator.EXPECTED_GATE_STATE),
    }
    try:
        evaluator.validate_payload_manifest(
            manifest,
            summary,
            files["summary"]["sha256"],
            acquisition,
            files["acquisition"]["sha256"],
        )
    except evaluator.JoinError as exc:
        raise PayloadError(str(exc)) from exc
    return manifest, paths


def copy_validated(paths: dict[str, Path], out_dir: Path) -> None:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "records").mkdir(parents=True)
    (out_dir / "masks").mkdir(parents=True)
    for key in ("summary", "acquisition", "runtime"):
        shutil.copyfile(paths[key], out_dir / paths[key].name)
    for b in range(4):
        shutil.copyfile(paths[f"record_{b}"], out_dir / "records" / paths[f"record_{b}"].name)
        shutil.copyfile(paths[f"mask_{b}"], out_dir / "masks" / paths[f"mask_{b}"].name)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_fixture(root: Path) -> None:
    records = evaluator.valid_record_fixture()
    summary = records["r1"][0]
    acquisition = evaluator.valid_acquisition_fixture()
    (root / "records").mkdir(parents=True)
    (root / "masks").mkdir(parents=True)

    for b in range(4):
        key = str(b)
        record_path = root / "records" / RECORD_NAMES[key]
        record_path.write_bytes(struct.pack("<I", b))
        summary["pixel_records"][key]["sha256"] = sha256_file(record_path)
        summary["pixel_records"][key]["file_bytes"] = record_path.stat().st_size

        mask_path = root / "masks" / MASK_NAMES[key]
        with mask_path.open("wb") as handle:
            handle.truncate(25_165_824)
        with mask_path.open("r+b") as handle:
            handle.seek(b)
            handle.write(bytes([1 << b]))
        summary["masks"][key]["sha256"] = sha256_file(mask_path)
        summary["masks"][key]["file_bytes"] = mask_path.stat().st_size

    write_json(root / SUMMARY_NAME, summary)
    write_json(root / ACQUISITION_NAME, acquisition)
    (root / RUNTIME_NAME).write_text("Python synthetic\nnumpy==synthetic\nhealpy==synthetic\n", encoding="utf-8")


def _write_fixture_zip(root: Path, zip_path: Path, *, omit: str | None = None, unsafe: bool = False) -> None:
    members: list[tuple[Path, str]] = [
        (root / SUMMARY_NAME, SUMMARY_NAME),
        (root / ACQUISITION_NAME, ACQUISITION_NAME),
        (root / RUNTIME_NAME, RUNTIME_NAME),
    ]
    members.extend((root / "records" / name, f"exp073r1_v05_records/{name}") for name in RECORD_NAMES.values())
    members.extend((root / "masks" / name, f"exp073r1_v05_masks/{name}") for name in MASK_NAMES.values())
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, name in members:
            if name != omit:
                archive.write(path, name)
        if unsafe:
            archive.writestr("../escape.txt", b"x")


def selftest() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="exp073p-v03-payload-") as tmp:
        root = Path(tmp) / "payload"
        out_dir = Path(tmp) / "normalized"
        root.mkdir()
        _write_fixture(root)
        zip_path = Path(tmp) / "r1.zip"
        archive_out = Path(tmp) / "archive-normalized"
        _write_fixture_zip(root, zip_path)
        inspect_and_extract_archive(zip_path, archive_out)
        archive_manifest, _ = build_manifest(archive_out)
        need(archive_manifest["status"] == evaluator.PAYLOAD_PASS, "valid archive did not cross payload validator")
        manifest, paths = build_manifest(root)
        copy_validated(paths, out_dir)
        need((out_dir / SUMMARY_NAME).is_file(), "normalized summary absent")
        need((out_dir / "records" / RECORD_NAMES["3"]).is_file(), "normalized records absent")

        failures = 0
        target = root / "masks" / MASK_NAMES["3"]
        backup = target.read_bytes()
        target.unlink()
        try:
            build_manifest(root)
        except PayloadError:
            failures += 1
        target.write_bytes(backup)

        duplicate = root / "duplicate"
        duplicate.mkdir()
        shutil.copyfile(root / SUMMARY_NAME, duplicate / SUMMARY_NAME)
        try:
            build_manifest(root)
        except PayloadError:
            failures += 1
        (duplicate / SUMMARY_NAME).unlink()

        record = root / "records" / RECORD_NAMES["1"]
        original = record.read_bytes()
        record.write_bytes(original + b"x")
        try:
            build_manifest(root)
        except PayloadError:
            failures += 1
        record.write_bytes(original)

        runtime = root / RUNTIME_NAME
        runtime_text = runtime.read_text()
        runtime.write_bytes(b"")
        try:
            build_manifest(root)
        except PayloadError:
            failures += 1
        runtime.write_text(runtime_text)

        need(failures == 4, f"payload fail-closed mutation count drift: {failures}")

        archive_failures = 0
        _write_fixture_zip(root, zip_path, omit=SUMMARY_NAME)
        try:
            inspect_and_extract_archive(zip_path, archive_out)
        except PayloadError:
            archive_failures += 1
        _write_fixture_zip(root, zip_path, unsafe=True)
        try:
            inspect_and_extract_archive(zip_path, archive_out)
        except PayloadError:
            archive_failures += 1
        _write_fixture_zip(root, zip_path)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(zip_path, "a") as archive:
                archive.writestr(SUMMARY_NAME, b"duplicate")
        try:
            inspect_and_extract_archive(zip_path, archive_out)
        except PayloadError:
            archive_failures += 1
        need(archive_failures == 3, f"archive fail-closed mutation count drift: {archive_failures}")
        return {
            "experiment": "Exp073P-v0.3-R1-payload-normalizer-selftest",
            "status": "PASS_EXP073P_V07_R1_PAYLOAD_SYNTHETIC_SELFTEST_V0_3",
            "synthetic": True,
            "complete_payload_fixture_passed": manifest["status"] == evaluator.PAYLOAD_PASS,
            "failclosed_mutations": failures,
            "archive_failclosed_mutations": archive_failures,
            "support_executor_authorized": False,
            "support_fraction_evaluated": False,
            "f_invalid_computed": False,
            "retained_dimension_evaluated": False,
            "covariance_read": False,
            "whitening_read": False,
            "nuisance_svd_read": False,
            "relation_null_read": False,
            "heldout_read": False,
            "G8_read": False,
            "gate_state": copy.deepcopy(evaluator.EXPECTED_GATE_STATE),
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--root", type=Path)
    parser.add_argument("--zip", type=Path)
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--manifest-out", type=Path, required=True)
    args = parser.parse_args()

    if args.selftest:
        write_json(args.manifest_out, selftest())
        print("PASS_EXP073P_V07_R1_PAYLOAD_SYNTHETIC_SELFTEST_V0_3")
        return
    if args.out_dir is None or (args.root is None) == (args.zip is None):
        parser.error("exactly one of --root/--zip and --out-dir are required outside --selftest")

    if args.zip is not None:
        inspect_and_extract_archive(args.zip, args.out_dir)
        manifest, _ = build_manifest(args.out_dir)
    else:
        manifest, paths = build_manifest(args.root)
        copy_validated(paths, args.out_dir)
    write_json(args.manifest_out, manifest)
    print(evaluator.PAYLOAD_PASS)


if __name__ == "__main__":
    main()
