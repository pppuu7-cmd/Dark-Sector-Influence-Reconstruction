#!/usr/bin/env python3
"""Supplemental fail-closed validation for Exp073P v0.3 artifact archive members.

This is implementation validation only. It does not authorize physical support and
must not alter any frozen scientific or reproduction criterion.
"""
from __future__ import annotations

import io
import json
import zipfile
from dataclasses import dataclass
from pathlib import PurePosixPath

REQUIRED = (
    "exp073r1_desy1_transport_stabilized_replay_v0_7_summary.json",
    "exp073r1_v0_7_remote_acquisition_provenance.json",
    "exp073r1_v0_7_runtime_provenance.txt",
)


@dataclass(frozen=True)
class ArchiveDecision:
    admitted: bool
    reason: str
    support_executor_authorized: bool = False
    support_fraction_evaluated: bool = False
    f_invalid_computed: bool = False
    covariance_read: bool = False
    whitening_read: bool = False
    nuisance_svd_read: bool = False
    relation_null_read: bool = False
    G8_read: bool = False


def inspect_archive(blob: bytes) -> ArchiveDecision:
    try:
        zf = zipfile.ZipFile(io.BytesIO(blob), "r")
    except (zipfile.BadZipFile, OSError):
        return ArchiveDecision(False, "bad_zip")

    infos = zf.infolist()
    names = [i.filename for i in infos]

    # No ambiguous duplicate names, even for files not consumed by the join.
    if len(names) != len(set(names)):
        return ArchiveDecision(False, "duplicate_member_name")

    # Fail closed on path traversal / absolute paths / backslash aliases.
    for name in names:
        if "\\" in name:
            return ArchiveDecision(False, "backslash_member_name")
        p = PurePosixPath(name)
        if p.is_absolute() or ".." in p.parts:
            return ArchiveDecision(False, "unsafe_member_path")

    # Required authority members must exist exactly once at archive root.
    for req in REQUIRED:
        matches = [i for i in infos if i.filename == req]
        if len(matches) != 1:
            return ArchiveDecision(False, f"required_member_count:{req}:{len(matches)}")
        info = matches[0]
        if info.is_dir():
            return ArchiveDecision(False, f"required_member_is_dir:{req}")

    # Required names under a prefix are not substitutes for exact root members.
    basenames = {}
    for info in infos:
        base = PurePosixPath(info.filename).name
        basenames.setdefault(base, []).append(info.filename)
    for req in REQUIRED:
        aliases = [n for n in basenames.get(req, []) if n != req]
        if aliases:
            return ArchiveDecision(False, f"required_member_basename_alias:{req}")

    return ArchiveDecision(True, "archive_structure_unambiguous")


def make_zip(entries: list[tuple[str, bytes]]) -> bytes:
    bio = io.BytesIO()
    with zipfile.ZipFile(bio, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, data in entries:
            zf.writestr(name, data)
    return bio.getvalue()


def baseline_entries() -> list[tuple[str, bytes]]:
    return [
        (REQUIRED[0], b'{"status":"PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1"}'),
        (REQUIRED[1], b'{"authorized_for_replay":true,"http_range_requests":0}'),
        (REQUIRED[2], b'python=3.14\nnumpy=2.5.2\nhealpy=1.20.0\n'),
        ("receipt/README.txt", b"synthetic archive-structure fixture\n"),
    ]


def assert_rejected(label: str, entries: list[tuple[str, bytes]], expected_reason_prefix: str) -> None:
    d = inspect_archive(make_zip(entries))
    assert not d.admitted, (label, d)
    assert d.reason.startswith(expected_reason_prefix), (label, d.reason)
    assert d.support_executor_authorized is False
    assert d.support_fraction_evaluated is False
    assert d.f_invalid_computed is False
    assert d.covariance_read is False
    assert d.whitening_read is False
    assert d.nuisance_svd_read is False
    assert d.relation_null_read is False
    assert d.G8_read is False


def main() -> None:
    base = baseline_entries()
    good = inspect_archive(make_zip(base))
    assert good.admitted and good.reason == "archive_structure_unambiguous"
    assert good.support_executor_authorized is False

    # 1-3: each required member missing.
    for idx, req in enumerate(REQUIRED):
        assert_rejected(
            f"missing-{idx}",
            [(n, b) for n, b in base if n != req],
            "required_member_count:",
        )

    # 4: duplicate exact required member.
    assert_rejected("duplicate-required", base + [(REQUIRED[0], b"second")], "duplicate_member_name")

    # 5: duplicate unrelated member is still ambiguous archive structure.
    assert_rejected("duplicate-unrelated", base + [("receipt/README.txt", b"second")], "duplicate_member_name")

    # 6-7: traversal and absolute-path members.
    assert_rejected("dotdot", base + [("../escape.txt", b"x")], "unsafe_member_path")
    assert_rejected("absolute", base + [("/absolute.txt", b"x")], "unsafe_member_path")

    # 8: Windows-style alias/path separator is rejected rather than normalized.
    assert_rejected("backslash", base + [("nested\\alias.txt", b"x")], "backslash_member_name")

    # 9-11: a required basename nested elsewhere creates alias ambiguity.
    for idx, req in enumerate(REQUIRED):
        assert_rejected(
            f"nested-alias-{idx}",
            base + [(f"nested/{req}", b"alias")],
            "required_member_basename_alias:",
        )

    # 12: nested-only required basename cannot replace root authority member.
    missing_root = [(n, b) for n, b in base if n != REQUIRED[1]] + [(f"nested/{REQUIRED[1]}", b"alias")]
    assert_rejected("nested-only", missing_root, "required_member_count:")

    # 13: malformed bytes are rejected.
    bad = inspect_archive(b"not-a-zip")
    assert not bad.admitted and bad.reason == "bad_zip"
    assert bad.support_executor_authorized is False

    receipt = {
        "status": "PASS_EXP073P_V03_ARCHIVE_MEMBER_FAILCLOSED_SELFTEST",
        "mutations_rejected": 13,
        "scope": "supplemental implementation validation only",
        "support_executor_authorized": False,
        "support_fraction_evaluated": False,
        "f_invalid_computed": False,
        "covariance_read": False,
        "whitening_read": False,
        "nuisance_svd_read": False,
        "relation_null_read": False,
        "G8_read": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()
