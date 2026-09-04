#!/usr/bin/env python3
"""DSIR large checkpoint payload sharding, infrastructure only.

This module never changes scientific bytes. It packages arbitrary checkpoint files
into bounded Git-safe chunks plus a canonical manifest and restores them only
under exact identity/SHA verification. Remote-ref/push sequencing remains the
responsibility of the checkpoint orchestration layer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

FORMAT = "DSIR_SHARDED_CHECKPOINT_PAYLOAD_V0_1"
CHUNK_BYTES = 64 * 1024 * 1024
BATCH_BYTES_MAX = 1024 * 1024 * 1024
GITHUB_GIT_OBJECT_LIMIT = 100 * 1024 * 1024
GITHUB_PUSH_LIMIT = 2 * 1024 * 1024 * 1024


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def canonical_json(obj: dict) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def pack_file(src: Path, out_dir: Path, *, logical_path: str, source_head: str,
              contract_fingerprint: str, stage: str, replica: str,
              checkpoint_namespace: str, chunk_bytes: int = CHUNK_BYTES) -> dict:
    if not checkpoint_namespace.startswith("checkpoints/"):
        raise RuntimeError("checkpoint namespace must be checkpoints/*")
    if replica not in {"A", "B", "TEST"}:
        raise RuntimeError("invalid replica")
    if chunk_bytes <= 0 or chunk_bytes > CHUNK_BYTES:
        raise RuntimeError("chunk bound violation")
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks = []
    whole = hashlib.sha256()
    offset = 0
    with src.open("rb") as f:
        index = 0
        while True:
            data = f.read(chunk_bytes)
            if not data:
                break
            whole.update(data)
            ch_sha = hashlib.sha256(data).hexdigest()
            name = f"chunk_{index:06d}_{ch_sha}.bin"
            p = out_dir / name
            tmp = p.with_suffix(".tmp")
            tmp.write_bytes(data)
            os.replace(tmp, p)
            chunks.append({"index": index, "offset": offset, "bytes": len(data), "sha256": ch_sha, "name": name})
            offset += len(data)
            index += 1
    manifest = {
        "format": FORMAT,
        "complete": True,
        "logical_path": logical_path,
        "source_head": source_head,
        "contract_fingerprint": contract_fingerprint,
        "stage": stage,
        "replica": replica,
        "checkpoint_namespace": checkpoint_namespace,
        "bytes": offset,
        "sha256": whole.hexdigest(),
        "chunk_bytes_max": chunk_bytes,
        "batch_bytes_max": BATCH_BYTES_MAX,
        "chunks": chunks,
        "historical_wm_s3_numerical_import": False,
        "science_gate_scored": False,
    }
    (out_dir / "manifest.json").write_bytes(canonical_json(manifest))
    return manifest


def validate_manifest(manifest: dict, *, source_head: str, contract_fingerprint: str,
                      stage: str, replica: str, checkpoint_namespace: str) -> None:
    if manifest.get("format") != FORMAT or manifest.get("complete") is not True:
        raise RuntimeError("manifest format/completion mismatch")
    expected = {
        "source_head": source_head,
        "contract_fingerprint": contract_fingerprint,
        "stage": stage,
        "replica": replica,
        "checkpoint_namespace": checkpoint_namespace,
    }
    for k, v in expected.items():
        if manifest.get(k) != v:
            raise RuntimeError(f"manifest identity mismatch: {k}")
    if manifest.get("historical_wm_s3_numerical_import") is not False or manifest.get("science_gate_scored") is not False:
        raise RuntimeError("manifest science firewall mismatch")
    chunks = manifest.get("chunks")
    if not isinstance(chunks, list):
        raise RuntimeError("chunks missing")
    offset = 0
    for i, c in enumerate(chunks):
        if c.get("index") != i or c.get("offset") != offset:
            raise RuntimeError("chunk order/offset mismatch")
        n = int(c.get("bytes", -1))
        if n < 0 or n > CHUNK_BYTES:
            raise RuntimeError("chunk byte bound mismatch")
        offset += n
    if offset != int(manifest.get("bytes", -1)):
        raise RuntimeError("manifest total byte mismatch")


def restore_file(shard_dir: Path, dest: Path, *, source_head: str,
                 contract_fingerprint: str, stage: str, replica: str,
                 checkpoint_namespace: str) -> dict:
    manifest = json.loads((shard_dir / "manifest.json").read_text())
    validate_manifest(manifest, source_head=source_head, contract_fingerprint=contract_fingerprint,
                      stage=stage, replica=replica, checkpoint_namespace=checkpoint_namespace)
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".tmp")
    whole = hashlib.sha256()
    wrote = 0
    with tmp.open("wb") as out:
        for c in manifest["chunks"]:
            p = shard_dir / c["name"]
            data = p.read_bytes()
            if len(data) != c["bytes"] or hashlib.sha256(data).hexdigest() != c["sha256"]:
                raise RuntimeError("chunk SHA/length mismatch")
            out.write(data)
            whole.update(data)
            wrote += len(data)
    if wrote != manifest["bytes"] or whole.hexdigest() != manifest["sha256"]:
        tmp.unlink(missing_ok=True)
        raise RuntimeError("whole-file reassembly mismatch")
    os.replace(tmp, dest)
    return manifest


def remote_transition_ok(expected_old: str | None, observed_pre: str | None,
                         candidate: str, observed_post: str | None) -> bool:
    """Pure fail-closed lease/race model used by orchestration audits."""
    if expected_old != observed_pre:
        return False
    return observed_post == candidate


def self_test(work: Path) -> dict:
    work.mkdir(parents=True, exist_ok=True)
    # Deterministic nontrivial payload; small enough for hosted CI, same byte semantics.
    payload = work / "payload.bin"
    block = hashlib.sha256(b"DSIR-Exp073DA-v0.1").digest()
    payload.write_bytes((block * ((5 * 1024 * 1024 + 123) // len(block) + 1))[:5 * 1024 * 1024 + 123])
    src_sha = sha256_file(payload)
    shards = work / "shards"
    ident = dict(source_head="a" * 40, contract_fingerprint="b" * 64,
                 stage="fresh_workspace_mcm_complete", replica="TEST",
                 checkpoint_namespace="checkpoints/exp073da-test-v0-1")
    m = pack_file(payload, shards, logical_path="fresh_workspace.fits", chunk_bytes=1024 * 1024, **ident)
    restored = work / "restored.bin"
    restore_file(shards, restored, **ident)
    roundtrip = sha256_file(restored) == src_sha == m["sha256"] and restored.read_bytes() == payload.read_bytes()

    # Corruption must fail closed.
    corrupt_rejected = False
    cp = shards / m["chunks"][0]["name"]
    original = cp.read_bytes()
    cp.write_bytes(bytes([original[0] ^ 1]) + original[1:])
    try:
        restore_file(shards, work / "bad.bin", **ident)
    except RuntimeError:
        corrupt_rejected = True
    cp.write_bytes(original)

    # Missing and reordered chunks must fail closed.
    missing_rejected = False
    last = shards / m["chunks"][-1]["name"]
    saved = last.read_bytes(); last.unlink()
    try:
        restore_file(shards, work / "missing.bin", **ident)
    except (RuntimeError, FileNotFoundError):
        missing_rejected = True
    last.write_bytes(saved)
    reordered_rejected = False
    bad_manifest = dict(m); bad_manifest["chunks"] = [dict(x) for x in m["chunks"]]
    if len(bad_manifest["chunks"]) > 1:
        bad_manifest["chunks"][0], bad_manifest["chunks"][1] = bad_manifest["chunks"][1], bad_manifest["chunks"][0]
    try:
        validate_manifest(bad_manifest, **ident)
    except RuntimeError:
        reordered_rejected = True

    race_rejected = (not remote_transition_ok("1" * 40, "2" * 40, "3" * 40, "3" * 40)
                     and not remote_transition_ok("1" * 40, "1" * 40, "3" * 40, "2" * 40)
                     and remote_transition_ok("1" * 40, "1" * 40, "3" * 40, "3" * 40))
    return {
        "roundtrip_exact": roundtrip,
        "corruption_rejected": corrupt_rejected,
        "missing_rejected": missing_rejected,
        "reordered_rejected": reordered_rejected,
        "race_model_failclosed": race_rejected,
        "chunk_cap_below_git_object_limit": CHUNK_BYTES < GITHUB_GIT_OBJECT_LIMIT,
        "batch_cap_below_git_push_limit": BATCH_BYTES_MAX < GITHUB_PUSH_LIMIT,
        "source_sha256": src_sha,
        "restored_sha256": sha256_file(restored),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--work", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    if not args.self_test:
        raise SystemExit("only hosted self-test CLI is exposed in v0.1")
    rec = self_test(Path(args.work))
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
    if not all(v for k, v in rec.items() if isinstance(v, bool)):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
