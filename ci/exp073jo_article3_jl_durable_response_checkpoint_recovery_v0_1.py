#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

CONTRACT_ID = "EXP073JO_ARTICLE3_JL_DURABLE_RESPONSE_CHECKPOINT_RECOVERY_V0_1"
PASS_PREFLIGHT = "PASS_EXP073JO_DURABLE_RESPONSE_CHECKPOINT_PREFLIGHT_V0_1"
INVALID_INFRA = "INVALID_INFRA_PLUS_0_PLUS_0"
FLUSH_EVERY = 16
CAPACITY = 4608
PARSER_CAPACITY = 131072
NATIVE_KPD = 20.0
H = 1e-4
REL_TOL = 1e-3
CHECKPOINT_NAMESPACE = "checkpoints/exp073jo-jl-response-v0-1"


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def f8_bytes(x) -> bytes:
    return np.ascontiguousarray(np.asarray(x, dtype="<f8")).tobytes()


def load_module(name: str, path: str | Path):
    spec = importlib.util.spec_from_file_location(name, Path(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def dynamic_audit(rec: dict) -> dict:
    return {
        "response_calls": int(rec.get("response_calls", 0)),
        "target_evaluations": int(rec.get("target_evaluations", 0)),
        "unsupported_target_evaluations": int(rec.get("unsupported_target_evaluations", 0)),
        "max_requested_node_coordinate_rel_mismatch": float(rec.get("max_requested_node_coordinate_rel_mismatch", 0.0)),
    }


def audit_equal(a: dict, b: dict) -> bool:
    return (
        int(a.get("response_calls", 0)) == int(b.get("response_calls", 0))
        and int(a.get("target_evaluations", 0)) == int(b.get("target_evaluations", 0))
        and int(a.get("unsupported_target_evaluations", 0)) == int(b.get("unsupported_target_evaluations", 0))
        and float(a.get("max_requested_node_coordinate_rel_mismatch", 0.0))
        == float(b.get("max_requested_node_coordinate_rel_mismatch", 0.0))
    )


def apply_audit(rec: dict, state: dict) -> None:
    for k, v in state.items():
        rec[k] = v


class CheckpointStore:
    def __init__(self, root: Path, git_repo: Path | None = None, branch: str | None = None):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.git_repo = Path(git_repo) if git_repo else None
        self.branch = branch
        self.entries: dict[tuple[int, int], dict] = {}
        self.pending = 0
        self.pushes = 0
        self.hits = 0
        self.misses = 0
        self._load_existing()

    def _slot_dir(self, slot: int) -> Path:
        p = self.root / f"slot{slot:02d}"
        p.mkdir(parents=True, exist_ok=True)
        return p

    def _meta_path(self, slot: int, index: int) -> Path:
        return self._slot_dir(slot) / f"call{index:06d}.json"

    def _bin_path(self, slot: int, index: int) -> Path:
        return self._slot_dir(slot) / f"call{index:06d}.f64"

    def _load_existing(self) -> None:
        for slot in (10, 20):
            p = self.root / f"slot{slot:02d}"
            if not p.exists():
                continue
            metas = sorted(p.glob("call*.json"))
            indices = []
            for mp in metas:
                stem = mp.stem
                try:
                    idx = int(stem.replace("call", "", 1))
                except Exception as e:
                    raise RuntimeError(f"invalid checkpoint filename {mp}") from e
                meta = json.loads(mp.read_text())
                bp = self._bin_path(slot, idx)
                if not bp.exists():
                    raise RuntimeError(f"checkpoint metadata without payload {mp}")
                if meta.get("contract_id") != CONTRACT_ID or int(meta.get("slot", -1)) != slot or int(meta.get("call_index", -1)) != idx:
                    raise RuntimeError(f"checkpoint identity mismatch {mp}")
                raw = bp.read_bytes()
                if len(raw) != int(meta.get("response_nbytes", -1)) or sha_bytes(raw) != meta.get("response_sha256"):
                    raise RuntimeError(f"checkpoint payload hash mismatch {bp}")
                self.entries[(slot, idx)] = meta
                indices.append(idx)
            if indices and indices != list(range(indices[-1] + 1)):
                raise RuntimeError(f"non-prefix checkpoint sequence for slot {slot}: {indices[:5]}...{indices[-5:]}")
            bins = sorted(p.glob("call*.f64"))
            if len(bins) != len(metas):
                raise RuntimeError(f"orphan checkpoint payload(s) in {p}")

    @staticmethod
    def key_material(slot: int, index: int, z: float, targets, nodes) -> dict:
        tb = f8_bytes(targets)
        nb = f8_bytes(nodes)
        return {
            "contract_id": CONTRACT_ID,
            "slot": int(slot),
            "call_index": int(index),
            "z_hex": float(z).hex(),
            "target_count": int(np.asarray(targets).size),
            "target_sha256": sha_bytes(tb),
            "node_count": int(np.asarray(nodes).size),
            "guarded_node_sha256": sha_bytes(nb),
        }

    def replay(self, slot: int, index: int, z: float, targets, nodes, current_audit: dict):
        meta = self.entries.get((slot, index))
        if meta is None:
            return None
        expected = self.key_material(slot, index, z, targets, nodes)
        for k, v in expected.items():
            if meta.get(k) != v:
                raise RuntimeError(f"checkpoint request mismatch slot={slot} index={index} field={k}: {meta.get(k)!r} != {v!r}")
        if not audit_equal(current_audit, meta.get("audit_before", {})):
            raise RuntimeError(f"checkpoint audit-prefix mismatch slot={slot} index={index}")
        shape = meta.get("response_shape")
        if shape != [int(np.asarray(targets).size), 2] or meta.get("response_dtype") != "<f8":
            raise RuntimeError(f"checkpoint response schema mismatch slot={slot} index={index}")
        bp = self._bin_path(slot, index)
        raw = bp.read_bytes()
        if len(raw) != int(meta["response_nbytes"]) or sha_bytes(raw) != meta["response_sha256"]:
            raise RuntimeError(f"checkpoint response hash mismatch slot={slot} index={index}")
        out = np.frombuffer(raw, dtype="<f8").copy().reshape(shape)
        self.hits += 1
        return out, meta

    def record(self, slot: int, index: int, z: float, targets, nodes, response, audit_before: dict, audit_after: dict, kkeys_after: set[str]) -> dict:
        if (slot, index) in self.entries:
            raise RuntimeError(f"refusing to overwrite checkpoint slot={slot} index={index}")
        out = np.ascontiguousarray(np.asarray(response, dtype="<f8"))
        if out.shape != (int(np.asarray(targets).size), 2):
            raise RuntimeError("response shape changed before checkpoint")
        raw = out.tobytes()
        meta = self.key_material(slot, index, z, targets, nodes)
        meta.update({
            "response_shape": [int(out.shape[0]), 2],
            "response_dtype": "<f8",
            "response_nbytes": len(raw),
            "response_sha256": sha_bytes(raw),
            "audit_before": audit_before,
            "audit_after": audit_after,
            "kkeys_after": sorted(str(x) for x in kkeys_after),
        })
        bp = self._bin_path(slot, index)
        mp = self._meta_path(slot, index)
        btmp = bp.with_suffix(bp.suffix + ".tmp")
        mtmp = mp.with_suffix(mp.suffix + ".tmp")
        btmp.write_bytes(raw)
        mtmp.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
        os.replace(btmp, bp)
        os.replace(mtmp, mp)
        self.entries[(slot, index)] = meta
        self.pending += 1
        self.misses += 1
        if self.pending >= FLUSH_EVERY:
            self.flush("cadence")
        return meta

    def flush(self, reason: str) -> None:
        if self.pending == 0:
            return
        if self.git_repo is None:
            self.pending = 0
            return
        rel = self.root.resolve().relative_to(self.git_repo.resolve())
        subprocess.run(["git", "-C", str(self.git_repo), "add", str(rel)], check=True)
        status = subprocess.run(["git", "-C", str(self.git_repo), "diff", "--cached", "--quiet"])
        if status.returncode == 0:
            self.pending = 0
            return
        msg = f"[skip ci] Exp073JO durable response checkpoint ({reason})"
        subprocess.run(["git", "-C", str(self.git_repo), "commit", "-m", msg], check=True)
        if not self.branch:
            raise RuntimeError("checkpoint branch missing")
        last = None
        for attempt in range(1, 5):
            p = subprocess.run(
                ["git", "-C", str(self.git_repo), "push", "origin", f"HEAD:refs/heads/{self.branch}"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            if p.returncode == 0:
                self.pending = 0
                self.pushes += 1
                return
            last = p.stdout
            if "non-fast-forward" in p.stdout.lower() or "fetch first" in p.stdout.lower():
                break
            time.sleep(2 ** (attempt - 1))
        raise RuntimeError(f"durable checkpoint push failed: {last}")

    def head_sha(self) -> str | None:
        if self.git_repo is None:
            return None
        return subprocess.check_output(["git", "-C", str(self.git_repo), "rev-parse", "HEAD"], text=True).strip()


def make_checkpoint_suite(parent_cls, store: CheckpointStore):
    class CheckpointResolutionSuite(parent_cls):
        _jo_next_index = {10: 0, 20: 0}

        def __init__(self, baseline, precision, kpd):
            super().__init__(baseline, precision, kpd)
            slot = int(round(float(getattr(self, "slot", kpd))))
            if slot not in (10, 20):
                raise RuntimeError(f"unexpected JO suite slot {slot}")
            self._jo_slot = slot

        def response(self, z, targets):
            slot = self._jo_slot
            index = type(self)._jo_next_index[slot]
            before = dynamic_audit(self.rec)
            replayed = store.replay(slot, index, float(z), targets, self.nodes, before)
            if replayed is not None:
                out, meta = replayed
                apply_audit(self.rec, meta["audit_after"])
                self.kkeys = set(meta.get("kkeys_after", []))
            else:
                out = super().response(z, targets)
                after = dynamic_audit(self.rec)
                store.record(slot, index, float(z), targets, self.nodes, out, before, after, set(self.kkeys))
            type(self)._jo_next_index[slot] += 1
            return out

        def close(self):
            try:
                store.flush(f"suite-close-slot{self._jo_slot}")
            finally:
                return super().close()

    CheckpointResolutionSuite.__name__ = "Exp073JOCheckpointResolutionSuite"
    return CheckpointResolutionSuite


def run_history_control(jj, baseline: str, precision: str) -> dict:
    jj.CAPACITY = CAPACITY
    coarse, *_ = jj.guarded_lattice(2048)
    fine, *_ = jj.guarded_lattice(4096)
    if len(coarse) != 2049 or len(fine) != 4097:
        raise RuntimeError("JL grid identity mismatch in JO live control")
    jj.ResolutionSuite.coarse_nodes = coarse
    jj.ResolutionSuite.fine_nodes = fine
    pre_z = float.fromhex("0x1.3851eb851eb85p-1")  # 0.61
    tail_z = float.fromhex("0x1.1c28f5c28f5c3p+0")  # 1.11
    pre_targets = np.asarray([0.0013, 0.0047, 0.013, 0.041], dtype=np.float64)
    tail_targets = np.asarray([0.0019, 0.0073, 0.021, 0.057], dtype=np.float64)
    result = {}
    for slot in (10, 20):
        jj.ResolutionSuite.audit = {}
        a = jj.ResolutionSuite(Path(baseline), Path(precision), float(slot))
        try:
            _ = a.response(pre_z, pre_targets)
            tail_after_history = np.ascontiguousarray(a.response(tail_z, tail_targets), dtype="<f8")
        finally:
            a.close()
        jj.ResolutionSuite.audit = {}
        b = jj.ResolutionSuite(Path(baseline), Path(precision), float(slot))
        try:
            tail_fresh = np.ascontiguousarray(b.response(tail_z, tail_targets), dtype="<f8")
        finally:
            b.close()
        exact = bool(np.array_equal(tail_after_history, tail_fresh) and np.array_equal(np.isfinite(tail_after_history), np.isfinite(tail_fresh)))
        if not exact:
            raise RuntimeError(f"history-independence exact equality failed for slot {slot}")
        result[str(slot)] = {
            "exact_array_equal": True,
            "tail_response_sha256": sha_bytes(tail_after_history.tobytes()),
            "node_sha256": sha_bytes(f8_bytes(coarse if slot == 10 else fine)),
            "node_count": len(coarse if slot == 10 else fine),
        }
    return {
        "pre_z_hex": pre_z.hex(),
        "tail_z_hex": tail_z.hex(),
        "pre_targets_hex": [float(x).hex() for x in pre_targets],
        "tail_targets_hex": [float(x).hex() for x in tail_targets],
        "slots": result,
    }


def run_roundtrip_control(jj, baseline: str, precision: str) -> dict:
    jj.CAPACITY = CAPACITY
    coarse, *_ = jj.guarded_lattice(2048)
    fine, *_ = jj.guarded_lattice(4096)
    parent = jj.ResolutionSuite
    parent.coarse_nodes = coarse
    parent.fine_nodes = fine
    z = float.fromhex("0x1.a8f5c28f5c28fp-1")  # 0.83
    targets = np.asarray([0.0016, 0.0081, 0.023, 0.052], dtype=np.float64)
    with tempfile.TemporaryDirectory(prefix="exp073jo-roundtrip-") as td:
        store = CheckpointStore(Path(td))
        wrapped = make_checkpoint_suite(parent, store)
        wrapped.coarse_nodes = coarse
        wrapped.fine_nodes = fine
        wrapped.audit = {}
        first = wrapped(Path(baseline), Path(precision), 10.0)
        try:
            miss = np.ascontiguousarray(first.response(z, targets), dtype="<f8")
            miss_audit = dynamic_audit(first.rec)
        finally:
            first.close()
        wrapped._jo_next_index = {10: 0, 20: 0}
        wrapped.audit = {}
        second = wrapped(Path(baseline), Path(precision), 10.0)
        try:
            hit = np.ascontiguousarray(second.response(z, targets), dtype="<f8")
            hit_audit = dynamic_audit(second.rec)
        finally:
            second.close()
        if not np.array_equal(miss, hit) or miss.tobytes() != hit.tobytes() or not audit_equal(miss_audit, hit_audit):
            raise RuntimeError("checkpoint round-trip exact identity failed")
        if store.hits != 1 or store.misses != 1:
            raise RuntimeError("checkpoint round-trip hit/miss accounting failed")
        return {
            "exact_response_bytes_equal": True,
            "exact_audit_restoration": True,
            "response_sha256": sha_bytes(miss.tobytes()),
            "audit_after": miss_audit,
            "z_hex": z.hex(),
            "targets_hex": [float(x).hex() for x in targets],
        }


def preflight(args) -> int:
    jj = load_module("exp073jj_jo_preflight", args.jj_script)
    if jj.H != H or jj.REL_TOL != REL_TOL or jj.NATIVE_KPD != NATIVE_KPD:
        raise RuntimeError("canonical JJ constants mismatch")
    history = run_history_control(jj, args.baseline, args.precision)
    roundtrip = run_roundtrip_control(jj, args.baseline, args.precision)
    result = {
        "schema": "EXP073JO_ARTICLE3_JL_DURABLE_RESPONSE_CHECKPOINT_PREFLIGHT_RESULT_V0_1",
        "experiment": "Exp073JO",
        "classification": "DURABLE_RESPONSE_CHECKPOINT_PREFLIGHT_PASS_PLUS_0_PLUS_0",
        "effect": "+0/+0",
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "contract_id": CONTRACT_ID,
        "flush_every_new_calls": FLUSH_EVERY,
        "capacity": CAPACITY,
        "parser_capacity": PARSER_CAPACITY,
        "native_kpd": NATIVE_KPD,
        "h": H,
        "rel_tol": REL_TOL,
        "jj_script_sha256": sha_file(Path(args.jj_script)),
        "history_independence": history,
        "cache_roundtrip": roundtrip,
        "token": PASS_PREFLIGHT,
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(PASS_PREFLIGHT)
    print(json.dumps(history, sort_keys=True))
    print(json.dumps(roundtrip, sort_keys=True))
    return 0


def recover(args, forwarded: list[str]) -> int:
    auth = json.loads(Path(args.preflight_authority).read_text())
    if auth.get("classification") != "DURABLE_RESPONSE_CHECKPOINT_PREFLIGHT_PASS_PLUS_0_PLUS_0":
        raise RuntimeError("JO preflight authority classification mismatch")
    if auth.get("artifact_verified_independently") is not True or not isinstance(auth.get("artifact_zip_sha256"), str):
        raise RuntimeError("JO preflight authority not independently verified")
    if auth.get("contract_id") != CONTRACT_ID:
        raise RuntimeError("JO preflight authority contract mismatch")

    store = CheckpointStore(Path(args.checkpoint_root), Path(args.checkpoint_repo), args.checkpoint_branch)
    jl = load_module("exp073jl_jo_exact_parent", args.jl_script)
    original_loader = jl.load_module
    wrapped_classes = []

    def intercept(name, path):
        mod = original_loader(name, path)
        if name == "exp073jj_jl_parent":
            if sha_file(Path(path)) != auth.get("jj_script_sha256"):
                raise RuntimeError("JJ source differs from JO preflight authority")
            wrapped = make_checkpoint_suite(mod.ResolutionSuite, store)
            mod.ResolutionSuite = wrapped
            wrapped_classes.append(wrapped)
        return mod

    jl.load_module = intercept
    old_argv = sys.argv
    sys.argv = ["exp073jl"] + forwarded
    started = time.time()
    try:
        rc = jl.main()
        store.flush("wrapper-success")
    finally:
        sys.argv = old_argv
        jl.load_module = original_loader
    if rc != 0:
        raise RuntimeError(f"frozen JL returned {rc}")
    if len(wrapped_classes) != 1:
        raise RuntimeError(f"expected one intercepted JJ module, got {len(wrapped_classes)}")
    next_index = wrapped_classes[0]._jo_next_index
    receipt = {
        "schema": "EXP073JO_ARTICLE3_JL_DURABLE_RESPONSE_CHECKPOINT_PROCESS_RECEIPT_V0_1",
        "experiment": "Exp073JO",
        "classification": "DURABLE_RESPONSE_CHECKPOINT_RECOVERY_COMPLETED_PLUS_0_PLUS_0",
        "effect": "+0/+0",
        "scientific_authority_created": False,
        "covariance_restriction_authorized": False,
        "contract_id": CONTRACT_ID,
        "checkpoint_namespace": CHECKPOINT_NAMESPACE,
        "checkpoint_branch": args.checkpoint_branch,
        "cache_hits": store.hits,
        "cache_misses": store.misses,
        "durable_pushes_this_run": store.pushes,
        "slot_completed_call_counts": {"10": int(next_index[10]), "20": int(next_index[20])},
        "final_checkpoint_commit": store.head_sha(),
        "preflight_authority_artifact_zip_sha256": auth.get("artifact_zip_sha256"),
        "wall_seconds": time.time() - started,
        "token": "PASS_EXP073JO_DURABLE_RESPONSE_CHECKPOINT_RECOVERY_COMPLETED_V0_1",
    }
    Path(args.process_receipt).parent.mkdir(parents=True, exist_ok=True)
    Path(args.process_receipt).write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(receipt["token"])
    print(json.dumps(receipt, sort_keys=True))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)

    p = sub.add_parser("preflight")
    p.add_argument("--jj-script", required=True)
    p.add_argument("--baseline", required=True)
    p.add_argument("--precision", required=True)
    p.add_argument("--out", required=True)

    r = sub.add_parser("recover")
    r.add_argument("--jl-script", required=True)
    r.add_argument("--preflight-authority", required=True)
    r.add_argument("--checkpoint-root", required=True)
    r.add_argument("--checkpoint-repo", required=True)
    r.add_argument("--checkpoint-branch", required=True)
    r.add_argument("--process-receipt", required=True)

    args, rest = ap.parse_known_args()
    try:
        if args.mode == "preflight":
            if rest:
                raise RuntimeError(f"unexpected preflight arguments: {rest}")
            return preflight(args)
        return recover(args, rest)
    except Exception as e:
        print(f"{INVALID_INFRA}: {type(e).__name__}: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
