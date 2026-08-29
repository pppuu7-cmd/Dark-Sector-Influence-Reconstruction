#!/usr/bin/env python3
from __future__ import annotations

import argparse
import http.client
import importlib.util
import json
import shutil
import socket
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

MiB = 1 << 20
DEFAULT_QUALIFY_BYTES = 64 * MiB
DEFAULT_MIN_RATE_MIB_S = 8.0
DEFAULT_SOCKET_TIMEOUT = 45.0
DEFAULT_MAX_ROUTE_ATTEMPTS = 8
DEFAULT_MAX_MAP_ATTEMPTS = 3


class TransportTooSlow(RuntimeError):
    pass


class GuardedNetworkResponse:
    def __init__(self, raw, *, min_rate_bps: float, guard_after_bytes: int, record: dict):
        self.raw = raw
        self.min_rate_bps = float(min_rate_bps)
        self.guard_after_bytes = int(guard_after_bytes)
        self.record = record
        self.network_bytes = 0
        self.active_read_seconds = 0.0
        self.closed = False

    @property
    def status(self):
        return getattr(self.raw, "status", None)

    @property
    def headers(self):
        return self.raw.headers

    def geturl(self):
        return self.raw.geturl()

    def read(self, n: int = -1):
        t0 = time.monotonic()
        data = self.raw.read(n)
        dt = max(time.monotonic() - t0, 1e-9)
        if data:
            self.network_bytes += len(data)
            self.active_read_seconds += dt
            self.record["network_bytes"] = self.network_bytes
            self.record["active_read_seconds"] = self.active_read_seconds
            self.record["active_rate_MiB_s"] = self.network_bytes / MiB / self.active_read_seconds
            if self.network_bytes >= self.guard_after_bytes:
                rate = self.network_bytes / self.active_read_seconds
                if rate < self.min_rate_bps:
                    raise TransportTooSlow(
                        f"active network rate {rate/MiB:.3f} MiB/s "
                        f"< frozen {self.min_rate_bps/MiB:.3f} MiB/s"
                    )
        return data

    def close(self):
        if self.closed:
            return
        self.closed = True
        try:
            self.raw.close()
        finally:
            self.record["network_bytes"] = self.network_bytes
            self.record["active_read_seconds"] = self.active_read_seconds
            self.record["active_rate_MiB_s"] = (
                self.network_bytes / MiB / self.active_read_seconds
                if self.active_read_seconds > 0 else None
            )
            self.record["closed"] = True


class PrefixReplayResponse:
    """Replay a qualified prefix before continuing the same live HTTP response."""

    def __init__(self, prefix: bytes, guarded: GuardedNetworkResponse):
        self.prefix = memoryview(prefix)
        self.pos = 0
        self.guarded = guarded
        self.status = guarded.status
        self.headers = guarded.headers

    def geturl(self):
        return self.guarded.geturl()

    def read(self, n: int = -1):
        remaining = len(self.prefix) - self.pos
        if remaining:
            if n is None or n < 0:
                head = self.prefix[self.pos:].tobytes()
                self.pos = len(self.prefix)
                return head
            take = min(n, remaining)
            head = self.prefix[self.pos:self.pos + take].tobytes()
            self.pos += take
            return head
        return self.guarded.read(n)

    def close(self):
        self.guarded.close()


class RouteManager:
    def __init__(self, *, qualify_bytes: int, min_rate_mib_s: float, socket_timeout: float,
                 max_route_attempts: int, provenance: dict):
        self.qualify_bytes = int(qualify_bytes)
        self.min_rate_bps = float(min_rate_mib_s) * MiB
        self.socket_timeout = float(socket_timeout)
        self.max_route_attempts = int(max_route_attempts)
        self.provenance = provenance

    def _open_raw(self, url: str, expected_bytes: int, user_agent: str):
        req = urllib.request.Request(
            url,
            headers={"Accept-Encoding": "identity", "User-Agent": user_agent},
        )
        response = urllib.request.urlopen(req, timeout=self.socket_timeout)
        status = getattr(response, "status", None)
        if status != 200:
            response.close()
            raise RuntimeError(f"whole-object GET returned HTTP {status}, expected 200")
        content_range = response.headers.get("Content-Range")
        if content_range is not None:
            response.close()
            raise RuntimeError(f"unexpected Content-Range on no-Range whole GET: {content_range!r}")
        content_length = response.headers.get("Content-Length")
        if content_length is not None and int(content_length) != expected_bytes:
            response.close()
            raise RuntimeError(f"Content-Length {content_length} != frozen {expected_bytes}")
        return response, content_length

    def open_whole(self, url: str, expected_bytes: int, user_agent: str):
        last_exc = None
        for route_no in range(1, self.max_route_attempts + 1):
            record = {
                "route_attempt": len(self.provenance["routes"]) + 1,
                "route_attempt_within_map": route_no,
                "started_from_byte": 0,
                "range_header_sent": False,
                "qualify_bytes_target": self.qualify_bytes,
                "min_active_rate_MiB_s": self.min_rate_bps / MiB,
                "status": "opening",
            }
            self.provenance["routes"].append(record)
            raw = None
            guarded = None
            try:
                raw, content_length = self._open_raw(url, expected_bytes, user_agent)
                record["http_status"] = getattr(raw, "status", None)
                record["final_url"] = raw.geturl()
                record["content_length_header"] = content_length
                record["content_range_header"] = raw.headers.get("Content-Range")
                guarded = GuardedNetworkResponse(
                    raw, min_rate_bps=self.min_rate_bps,
                    guard_after_bytes=self.qualify_bytes, record=record,
                )
                chunks = []
                left = self.qualify_bytes
                q0 = time.monotonic()
                while left:
                    block = guarded.read(min(left, 4 * MiB))
                    if not block:
                        raise EOFError(
                            f"whole stream ended during qualification after "
                            f"{self.qualify_bytes-left} bytes"
                        )
                    chunks.append(block)
                    left -= len(block)
                qdt = max(time.monotonic() - q0, 1e-9)
                qrate = self.qualify_bytes / MiB / qdt
                record["qualification_seconds"] = qdt
                record["qualification_rate_MiB_s"] = qrate
                if qrate < self.min_rate_bps / MiB:
                    raise TransportTooSlow(
                        f"qualification rate {qrate:.3f} MiB/s "
                        f"< frozen {self.min_rate_bps/MiB:.3f} MiB/s"
                    )
                record["status"] = "QUALIFIED"
                self.provenance["accepted_routes"] += 1
                return PrefixReplayResponse(b"".join(chunks), guarded), content_length
            except Exception as exc:
                last_exc = exc
                record["status"] = "REJECTED_TRANSPORT"
                record["error"] = f"{type(exc).__name__}: {exc}"
                if guarded is not None:
                    guarded.close()
                elif raw is not None:
                    raw.close()
                if not is_retryable_transport_exception(exc):
                    raise
        raise TransportTooSlow(
            f"all {self.max_route_attempts} whole-object routes rejected; last={last_exc}"
        )


def is_retryable_transport_exception(exc: BaseException) -> bool:
    return isinstance(exc, (
        TransportTooSlow, EOFError, TimeoutError, socket.timeout,
        urllib.error.URLError, ConnectionResetError, ConnectionAbortedError,
        http.client.IncompleteRead, http.client.RemoteDisconnected,
    ))


def load_v05(path: Path):
    spec = importlib.util.spec_from_file_location("dsir_exp073r1_v05_frozen", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import frozen evaluator {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def promote_success(attempt_out: Path, final_out: Path):
    final_out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(attempt_out, final_out)
    for dirname in ("exp073r1_v05_records", "exp073r1_v05_masks"):
        src = attempt_out.parent / dirname
        dst = final_out.parent / dirname
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)


def write_provenance(path: Path, provenance: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(provenance, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen-evaluator", required=True)
    ap.add_argument("--url", required=True)
    ap.add_argument("--source-index", required=True)
    ap.add_argument("--source-summary", required=True)
    ap.add_argument("--parent-json", required=True)
    ap.add_argument("--workdir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--provenance", required=True)
    ap.add_argument("--qualify-bytes", type=int, default=DEFAULT_QUALIFY_BYTES)
    ap.add_argument("--min-active-read-mib-s", type=float, default=DEFAULT_MIN_RATE_MIB_S)
    ap.add_argument("--socket-timeout", type=float, default=DEFAULT_SOCKET_TIMEOUT)
    ap.add_argument("--max-route-attempts", type=int, default=DEFAULT_MAX_ROUTE_ATTEMPTS)
    ap.add_argument("--max-map-attempts", type=int, default=DEFAULT_MAX_MAP_ATTEMPTS)
    args = ap.parse_args()

    if args.qualify_bytes <= 0 or args.min_active_read_mib_s <= 0:
        raise SystemExit("qualification parameters must be positive")
    if args.max_route_attempts <= 0 or args.max_map_attempts <= 0:
        raise SystemExit("attempt counts must be positive")

    v05_path = Path(args.frozen_evaluator)
    v05 = load_v05(v05_path)
    if getattr(v05, "METACAL_BYTES", None) != 84_075_649_920:
        raise AssertionError("frozen evaluator metacal byte constant drift")
    if getattr(v05, "METACAL_SHA256", None) != "39a7fe03e54d96b85cee2fb523ea108c2a548ba1584368203f0464ed6241ebc8":
        raise AssertionError("frozen evaluator metacal SHA drift")
    if getattr(v05, "CHUNK_ROWS", None) != 65_536:
        raise AssertionError("frozen evaluator chunk-row drift")

    provenance = {
        "schema": "dsir.exp073r1.v0.8.github_hosted_rate_qualified_wholestream",
        "scope": "TRANSPORT_EXECUTION_ONLY_NO_SCIENCE_GATE",
        "frozen_evaluator_path": str(v05_path),
        "qualify_bytes": args.qualify_bytes,
        "min_active_read_MiB_s": args.min_active_read_mib_s,
        "socket_timeout_seconds": args.socket_timeout,
        "max_route_attempts_per_map": args.max_route_attempts,
        "max_map_attempts": args.max_map_attempts,
        "http_range_requests": 0,
        "whole_object_attempts_from_zero": True,
        "routes": [], "map_attempts": [], "accepted_routes": 0,
        "status": "INCOMPLETE_EXP073R1_V08",
        "science_gate_scored": False, "f_invalid_computed": False,
        "covariance_read": False, "G8_read": False,
        "gate_state": {"G7": "OPEN", "G8": "OPEN", "G9": "OPEN"},
    }

    final_out = Path(args.out)
    work_root = Path(args.workdir)
    work_root.mkdir(parents=True, exist_ok=True)
    manager = RouteManager(
        qualify_bytes=args.qualify_bytes,
        min_rate_mib_s=args.min_active_read_mib_s,
        socket_timeout=args.socket_timeout,
        max_route_attempts=args.max_route_attempts,
        provenance=provenance,
    )
    v05.open_whole = manager.open_whole

    for map_no in range(1, args.max_map_attempts + 1):
        attempt_root = work_root / f"map-attempt-{map_no:02d}"
        if attempt_root.exists():
            shutil.rmtree(attempt_root)
        attempt_out_dir = attempt_root / "out"
        attempt_out_dir.mkdir(parents=True)
        attempt_out = attempt_out_dir / "summary.json"
        attempt_work = attempt_root / "scratch"
        attempt = {"map_attempt": map_no, "started_at_unix": time.time(), "status": "RUNNING"}
        provenance["map_attempts"].append(attempt)
        ns = argparse.Namespace(
            url=args.url, source_index=args.source_index,
            source_summary=args.source_summary, parent_json=args.parent_json,
            workdir=str(attempt_work), out=str(attempt_out),
        )
        try:
            v05.metacal_map(ns)
            summary = json.loads(attempt_out.read_text(encoding="utf-8"))
            if summary.get("status") != "PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1":
                raise AssertionError(f"frozen mapper returned non-PASS status: {summary.get('status')!r}")
            attempt["status"] = "PASS"
            attempt["finished_at_unix"] = time.time()
            promote_success(attempt_out, final_out)
            provenance["status"] = "PASS_EXP073R1_V08_HOSTED_RATE_QUALIFIED_WHOLESTREAM"
            provenance["successful_map_attempt"] = map_no
            provenance["final_mapper_status"] = summary["status"]
            complete_routes = [r for r in provenance["routes"] if r.get("network_bytes") == 84_075_649_920]
            provenance["complete_whole_object_routes"] = len(complete_routes)
            if not complete_routes:
                raise AssertionError("no transport record consumed the complete frozen object")
            write_provenance(Path(args.provenance), provenance)
            print(json.dumps({
                "status": provenance["status"], "successful_map_attempt": map_no,
                "routes_total": len(provenance["routes"]),
            }, sort_keys=True))
            return
        except Exception as exc:
            attempt["finished_at_unix"] = time.time()
            attempt["error"] = f"{type(exc).__name__}: {exc}"
            if is_retryable_transport_exception(exc):
                attempt["status"] = "RETRYABLE_TRANSPORT_FAILURE"
                if attempt_root.exists():
                    shutil.rmtree(attempt_root)
                write_provenance(Path(args.provenance), provenance)
                continue
            attempt["status"] = "NON_TRANSPORT_FAIL_CLOSED"
            provenance["status"] = "INVALID_FOR_EXECUTION_EXP073R1_V08"
            write_provenance(Path(args.provenance), provenance)
            raise

    provenance["status"] = "INCOMPLETE_EXP073R1_V08_TRANSPORT_EXHAUSTED"
    write_provenance(Path(args.provenance), provenance)
    raise RuntimeError(provenance["status"])


if __name__ == "__main__":
    main()
