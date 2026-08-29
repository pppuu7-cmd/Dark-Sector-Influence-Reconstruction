#!/usr/bin/env python3
"""Exp073R1 v0.7 infrastructure-only whole-object acquisition.

Every retry is a new HTTP GET from byte zero. Range/resume is forbidden.
The output is authorized only by exact byte count and SHA256.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

EXPECTED_BYTES = 84_075_649_920
EXPECTED_SHA256 = "39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8"
USER_AGENT = "DSIR-Exp073R1-v0.7-whole-object-acquire/1.0"


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def acquire(url: str, dest: Path, provenance: Path, max_attempts: int, retry_sleep: int) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    state = {
        "experiment": "Exp073R1",
        "route": "v0.7_transport_stabilized_exact_byte_replay",
        "authoritative_url": url,
        "expected_bytes": EXPECTED_BYTES,
        "expected_sha256": EXPECTED_SHA256,
        "http_range_requests": 0,
        "whole_object_attempts_from_zero": True,
        "attempts": [],
        "authorized_for_replay": False,
        "science_gate_scored": False,
        "f_invalid_computed": False,
        "covariance_read": False,
        "G8_read": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }
    write_json(provenance, state)

    for attempt in range(1, max_attempts + 1):
        if dest.exists():
            dest.unlink()
        h = hashlib.sha256()
        observed = 0
        rec = {"attempt": attempt, "started_from_byte": 0, "range_header_sent": False}
        state["attempts"].append(rec)
        write_json(provenance, state)
        req = urllib.request.Request(
            url,
            headers={"Accept-Encoding": "identity", "User-Agent": USER_AGENT},
            method="GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                status = getattr(r, "status", None)
                rec["http_status"] = status
                if status != 200:
                    raise RuntimeError(f"HTTP status {status}, expected 200")
                cr = r.headers.get("Content-Range")
                rec["content_range"] = cr
                if cr is not None:
                    raise RuntimeError(f"unexpected Content-Range {cr!r}")
                cl = r.headers.get("Content-Length")
                rec["content_length"] = int(cl) if cl is not None else None
                if cl is not None and int(cl) != EXPECTED_BYTES:
                    raise RuntimeError(f"Content-Length {cl} != {EXPECTED_BYTES}")
                with dest.open("wb") as f:
                    while True:
                        block = r.read(8 << 20)
                        if not block:
                            break
                        f.write(block)
                        h.update(block)
                        observed += len(block)
                        if observed % (1 << 30) < len(block):
                            print(json.dumps({"stage": "acquire", "attempt": attempt, "bytes": observed}), flush=True)
            rec["observed_bytes"] = observed
            rec["sha256"] = h.hexdigest()
            if observed != EXPECTED_BYTES:
                raise EOFError(f"whole-object attempt ended at {observed} of {EXPECTED_BYTES} bytes")
            if rec["sha256"] != EXPECTED_SHA256:
                rec["outcome"] = "REPRODUCTION_IDENTITY_FAIL"
                state["terminal_status"] = "REPRODUCTION_IDENTITY_FAIL"
                write_json(provenance, state)
                dest.unlink(missing_ok=True)
                raise SystemExit("complete authoritative object SHA256 mismatch; fail closed")
            rec["outcome"] = "PASS_EXACT_OBJECT_IDENTITY"
            state["authorized_for_replay"] = True
            state["final_bytes"] = observed
            state["final_sha256"] = rec["sha256"]
            state["terminal_status"] = "PASS_EXACT_OBJECT_IDENTITY_FOR_REPLAY"
            write_json(provenance, state)
            print("PASS_EXACT_OBJECT_IDENTITY_FOR_REPLAY", observed, rec["sha256"], flush=True)
            return
        except SystemExit:
            raise
        except Exception as exc:
            rec["observed_bytes"] = observed
            rec["outcome"] = "INFRASTRUCTURE_TRANSPORT_FAILURE"
            rec["error_type"] = type(exc).__name__
            rec["error"] = str(exc)[:1000]
            write_json(provenance, state)
            dest.unlink(missing_ok=True)
            print(json.dumps({"stage": "acquire-retry", "attempt": attempt, "bytes": observed, "error": repr(exc)}), flush=True)
            if attempt == max_attempts:
                state["terminal_status"] = "INFRASTRUCTURE_TRANSPORT_FAILURE_MAX_ATTEMPTS"
                write_json(provenance, state)
                raise
            time.sleep(retry_sleep)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--dest", type=Path, required=True)
    ap.add_argument("--provenance", type=Path, required=True)
    ap.add_argument("--max-attempts", type=int, default=12)
    ap.add_argument("--retry-sleep", type=int, default=30)
    args = ap.parse_args()
    if args.max_attempts < 1:
        raise SystemExit("max-attempts must be >=1")
    acquire(args.url, args.dest, args.provenance, args.max_attempts, args.retry_sleep)


if __name__ == "__main__":
    main()
