#!/usr/bin/env python3
"""Fail-closed byte-identity guard for the frozen Exp073P v0.3 production route.

This guard is prospective launch control only.  It does not alter any scientific
acceptance criterion and must be evaluated before any real v0.3 dispatch.
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

EXPECTED = {
    ".github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-3.yml": {
        "git_blob_sha1": "2950750312c153f75fe79c2c16fca6f74c7df5dc",
    },
    "experiments/073p_aggregate_prerequisite_join_v07_r1_authority_prereg_v0_3.md": {
        "git_blob_sha1": "6dd4ba0df9ed2be321b7f69966d7636d940e40d1",
        "sha256": "e27761b2db4a81283bb9fbac1decb95f62fadb785c40cb3e3f676f8651711f40",
    },
}


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def verify_file(path: Path, expected: dict[str, str]) -> None:
    data = path.read_bytes()
    got_blob = git_blob_sha1(data)
    if got_blob != expected["git_blob_sha1"]:
        raise SystemExit(
            f"REJECTED_EXP073P_V03_ROUTE_BYTE_IDENTITY: {path}: "
            f"git_blob_sha1={got_blob} expected={expected['git_blob_sha1']}"
        )
    if "sha256" in expected:
        got_sha256 = hashlib.sha256(data).hexdigest()
        if got_sha256 != expected["sha256"]:
            raise SystemExit(
                f"REJECTED_EXP073P_V03_ROUTE_BYTE_IDENTITY: {path}: "
                f"sha256={got_sha256} expected={expected['sha256']}"
            )


def verify(root: Path) -> None:
    for rel, expected in EXPECTED.items():
        path = root / rel
        if not path.is_file():
            raise SystemExit(f"REJECTED_EXP073P_V03_ROUTE_BYTE_IDENTITY: missing {rel}")
        verify_file(path, expected)
    print("PASS_EXP073P_V03_PRODUCTION_ROUTE_BYTE_FREEZE_V0_1")
    print("support_executor_authorized=false")


def mutation_selftest(root: Path) -> None:
    route = root / ".github/workflows/exp073p-aggregate-prerequisite-join-actual-v0-3.yml"
    data = route.read_bytes()
    expected = EXPECTED[str(route.relative_to(root))]["git_blob_sha1"]
    cases = {
        "append-newline": data + b"\n",
        "flip-first-byte": bytes([data[0] ^ 1]) + data[1:],
        "truncate-one-byte": data[:-1],
        "prepend-comment": b"# mutation\n" + data,
    }
    for name, mutated in cases.items():
        got = git_blob_sha1(mutated)
        if got == expected:
            raise AssertionError(f"mutation unexpectedly preserved route identity: {name}")
    print(f"PASS_EXP073P_V03_ROUTE_BYTE_MUTATION_SELFTEST_V0_1 cases={len(cases)}")
    print("support_executor_authorized=false")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path("."))
    ap.add_argument("--mutation-selftest", action="store_true")
    args = ap.parse_args()
    verify(args.root)
    if args.mutation_selftest:
        mutation_selftest(args.root)


if __name__ == "__main__":
    main()
