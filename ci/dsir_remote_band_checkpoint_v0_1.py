#!/usr/bin/env python3
"""DSIR durable band-checkpoint utilities.

Infrastructure only. This module never changes scientific classification.
It stores canonical completed rows locally, validates provenance+SHA on resume,
and prints plain-text progress suitable for a GitHub Actions/self-hosted runner log.
Remote durability is provided by syncing the checkpoint directory to a dedicated
Git branch after each completed band.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import pathlib
import time
from dataclasses import dataclass
from typing import Iterable

import numpy as np

FORMAT = "DSIR_REMOTE_BAND_CHECKPOINT_V0_1"


def _sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canonical_row(row: np.ndarray) -> np.ndarray:
    a = np.ascontiguousarray(np.asarray(row, dtype="<f8"))
    if a.ndim != 1:
        raise ValueError(f"checkpoint row must be 1-D, got {a.shape}")
    if not np.all(np.isfinite(a)):
        raise ValueError("checkpoint row contains non-finite values")
    return a


def row_sha(row: np.ndarray) -> str:
    a = canonical_row(row)
    return _sha_bytes(a.tobytes(order="C"))


def fmt_seconds(seconds: float | None) -> str:
    if seconds is None or not math.isfinite(seconds) or seconds < 0:
        return "--:--:--"
    s = int(round(seconds))
    h, r = divmod(s, 3600)
    m, s = divmod(r, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def progress_line(done: int, total: int, elapsed: float, eta: float | None,
                  threads: int, label: str = "bands") -> str:
    total = max(1, int(total))
    done = min(max(0, int(done)), total)
    frac = done / total
    width = 30
    filled = int(round(width * frac))
    bar = "█" * filled + "-" * (width - filled)
    return (
        f"PROGRESS [{bar}] {100.0*frac:6.2f}% | {label} {done}/{total} | "
        f"elapsed {fmt_seconds(elapsed)} | ETA {fmt_seconds(eta)} | threads={threads}"
    )


@dataclass(frozen=True)
class CheckpointContract:
    experiment: str
    source_commit: str
    helper_commit: str
    prereg_commit: str
    task: str
    lmax: int
    nbands: int
    row_length: int
    threads: int
    extra: dict

    def as_dict(self) -> dict:
        return {
            "format": FORMAT,
            "experiment": self.experiment,
            "source_commit": self.source_commit,
            "helper_commit": self.helper_commit,
            "prereg_commit": self.prereg_commit,
            "task": self.task,
            "lmax": int(self.lmax),
            "nbands": int(self.nbands),
            "row_length": int(self.row_length),
            "dtype": "<f8",
            "threads": int(self.threads),
            "extra": self.extra,
        }

    def fingerprint(self) -> str:
        b = json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":")).encode()
        return _sha_bytes(b)


class BandCheckpointStore:
    def __init__(self, root: os.PathLike | str, contract: CheckpointContract):
        self.root = pathlib.Path(root)
        self.contract = contract
        self.rows = self.root / "rows"
        self.root.mkdir(parents=True, exist_ok=True)
        self.rows.mkdir(parents=True, exist_ok=True)
        self.contract_path = self.root / "contract.json"
        self.state_path = self.root / "state.json"
        self._bind_or_create_contract()

    def _bind_or_create_contract(self) -> None:
        expected = self.contract.as_dict()
        expected["fingerprint"] = self.contract.fingerprint()
        if self.contract_path.exists():
            got = json.loads(self.contract_path.read_text())
            if got != expected:
                raise RuntimeError("checkpoint contract mismatch; fail closed")
        else:
            self._atomic_json(self.contract_path, expected)

    @staticmethod
    def _atomic_json(path: pathlib.Path, obj: dict) -> None:
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
        os.replace(tmp, path)

    def _paths(self, band: int) -> tuple[pathlib.Path, pathlib.Path]:
        if not (0 <= band < self.contract.nbands):
            raise IndexError(band)
        stem = f"band_{band:03d}"
        return self.rows / f"{stem}.bin", self.rows / f"{stem}.json"

    def save_completed_band(self, band: int, row: np.ndarray, *, ell_lo: int,
                            ell_hi_exclusive: int, wall_seconds: float) -> str:
        a = canonical_row(row)
        if a.size != self.contract.row_length:
            raise ValueError(f"row length {a.size} != {self.contract.row_length}")
        sha = row_sha(a)
        bin_path, meta_path = self._paths(band)
        tmp = bin_path.with_suffix(".bin.tmp")
        tmp.write_bytes(a.tobytes(order="C"))
        os.replace(tmp, bin_path)
        meta = {
            "format": FORMAT,
            "contract_fingerprint": self.contract.fingerprint(),
            "band": int(band),
            "ell_lo": int(ell_lo),
            "ell_hi_exclusive": int(ell_hi_exclusive),
            "shape": [int(a.size)],
            "dtype": "<f8",
            "sha256": sha,
            "wall_seconds": float(wall_seconds),
            "complete": True,
        }
        self._atomic_json(meta_path, meta)
        self._write_state()
        print(f"CHECKPOINT local band={band+1}/{self.contract.nbands} sha256={sha}", flush=True)
        return sha

    def load_band(self, band: int) -> np.ndarray | None:
        bin_path, meta_path = self._paths(band)
        if not (bin_path.exists() and meta_path.exists()):
            return None
        meta = json.loads(meta_path.read_text())
        if meta.get("format") != FORMAT:
            raise RuntimeError(f"band {band}: checkpoint format mismatch")
        if meta.get("contract_fingerprint") != self.contract.fingerprint():
            raise RuntimeError(f"band {band}: contract fingerprint mismatch")
        if meta.get("complete") is not True or meta.get("band") != band:
            raise RuntimeError(f"band {band}: incomplete/misindexed checkpoint")
        raw = bin_path.read_bytes()
        expected_bytes = self.contract.row_length * 8
        if len(raw) != expected_bytes:
            raise RuntimeError(f"band {band}: byte length mismatch")
        sha = _sha_bytes(raw)
        if sha != meta.get("sha256"):
            raise RuntimeError(f"band {band}: SHA mismatch")
        a = np.frombuffer(raw, dtype="<f8").copy()
        if not np.all(np.isfinite(a)):
            raise RuntimeError(f"band {band}: non-finite restored row")
        return a

    def completed_bands(self) -> list[int]:
        out: list[int] = []
        for b in range(self.contract.nbands):
            if self.load_band(b) is not None:
                out.append(b)
        return out

    def restore_matrix(self) -> tuple[np.ndarray, list[int]]:
        arr = np.zeros((self.contract.nbands, self.contract.row_length), dtype="<f8")
        completed = []
        for b in range(self.contract.nbands):
            row = self.load_band(b)
            if row is not None:
                arr[b] = row
                completed.append(b)
        if completed:
            print(
                f"RESUME restored {len(completed)}/{self.contract.nbands} completed bands; "
                f"next={next((b+1 for b in range(self.contract.nbands) if b not in completed), self.contract.nbands+1)}",
                flush=True,
            )
        return arr, completed

    def band_durations(self) -> list[float]:
        vals = []
        for b in self.completed_bands():
            _, meta_path = self._paths(b)
            vals.append(float(json.loads(meta_path.read_text()).get("wall_seconds", 0.0)))
        return [x for x in vals if x > 0 and math.isfinite(x)]

    def estimate_eta(self, remaining: int) -> float | None:
        d = self.band_durations()
        if not d:
            return None
        # Recent-band mean reacts to changing band cost without becoming noisy.
        tail = d[-min(6, len(d)):]
        return (sum(tail) / len(tail)) * max(0, remaining)

    def _write_state(self) -> None:
        done = self.completed_bands()
        self._atomic_json(self.state_path, {
            "format": FORMAT,
            "contract_fingerprint": self.contract.fingerprint(),
            "completed_bands": done,
            "completed_count": len(done),
            "total_bands": self.contract.nbands,
            "next_band": next((b for b in range(self.contract.nbands) if b not in done), None),
        })


def print_progress(store: BandCheckpointStore, started: float, threads: int) -> None:
    done = len(store.completed_bands())
    total = store.contract.nbands
    eta = store.estimate_eta(total - done)
    print(progress_line(done, total, time.monotonic() - started, eta, threads), flush=True)
