#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from pathlib import Path

import numpy as np

FORMAT = 'EXP073CM_STAGE_CHECKPOINT_V0_1'
ORDER = ['pcl', 'reference', 'target', 'final']


def sha_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def canon_json(obj: dict) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode('utf-8')


def fingerprint(spec: dict) -> str:
    return hashlib.sha256(canon_json(spec)).hexdigest()


def atomic_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    os.replace(tmp, path)


def load_spec(path: str) -> dict:
    spec = json.loads(Path(path).read_text(encoding='utf-8'))
    if spec.get('format') != FORMAT or spec.get('experiment') != 'Exp073CM' or spec.get('task') != 'Wm_S3':
        raise RuntimeError('invalid Exp073CM checkpoint contract spec')
    if spec.get('remote_branch') != 'checkpoints/exp073cm-wm-s3-resource-v0-1':
        raise RuntimeError('checkpoint namespace mismatch')
    return spec


def bind(root: Path, spec: dict) -> str:
    root.mkdir(parents=True, exist_ok=True)
    cp = root / 'contract.json'
    expected = {'format': FORMAT, 'spec': spec, 'fingerprint': fingerprint(spec)}
    if cp.exists():
        got = json.loads(cp.read_text(encoding='utf-8'))
        if got != expected:
            raise RuntimeError('checkpoint contract mismatch; fail closed')
    else:
        atomic_json(cp, expected)
    return expected['fingerprint']


def file_record(path: Path, contract_fp: str) -> dict:
    rec = {'name': path.name, 'size_bytes': path.stat().st_size, 'sha256': sha_file(path)}
    if path.suffix == '.npy':
        a = np.load(path, allow_pickle=False, mmap_mode='r')
        rec.update({'shape': list(a.shape), 'dtype': str(a.dtype), 'finite': bool(np.all(np.isfinite(a)))})
        if not rec['finite']:
            raise RuntimeError(f'nonfinite checkpoint payload {path}')
    return rec


def validate(root: Path, spec: dict) -> list[str]:
    fp = bind(root, spec)
    stages_dir = root / 'stages'
    completed = []
    seen_gap = False
    for stage in ORDER:
        sd = stages_dir / stage
        rp = sd / 'receipt.json'
        if not rp.exists():
            seen_gap = True
            continue
        if seen_gap:
            raise RuntimeError(f'non-monotonic checkpoint stage {stage}; fail closed')
        rec = json.loads(rp.read_text(encoding='utf-8'))
        if rec.get('format') != FORMAT or rec.get('stage') != stage or rec.get('contract_fingerprint') != fp or rec.get('complete') is not True:
            raise RuntimeError(f'invalid receipt for stage {stage}')
        files = rec.get('files')
        if not isinstance(files, list) or not files:
            raise RuntimeError(f'empty receipt for stage {stage}')
        for fr in files:
            p = sd / fr['name']
            if not p.is_file() or p.stat().st_size != fr['size_bytes'] or sha_file(p) != fr['sha256']:
                raise RuntimeError(f'payload mismatch stage={stage} file={fr.get("name")}')
            if p.suffix == '.npy':
                a = np.load(p, allow_pickle=False, mmap_mode='r')
                if list(a.shape) != fr.get('shape') or str(a.dtype) != fr.get('dtype') or not np.all(np.isfinite(a)):
                    raise RuntimeError(f'npy metadata mismatch stage={stage} file={p.name}')
        completed.append(stage)
    atomic_json(root / 'state.json', {
        'format': FORMAT, 'contract_fingerprint': fp, 'completed_stages': completed,
        'next_stage': next((s for s in ORDER if s not in completed), None),
    })
    return completed


def add_stage(root: Path, spec: dict, stage: str, files: list[str]) -> None:
    if stage not in ORDER:
        raise RuntimeError(stage)
    completed = validate(root, spec)
    idx = ORDER.index(stage)
    if stage in completed:
        print(f'CHECKPOINT stage={stage} already_complete=true')
        return
    if completed != ORDER[:idx]:
        raise RuntimeError(f'stage order violation wanted={stage} completed={completed}')
    fp = fingerprint(spec)
    sd = root / 'stages' / stage
    if sd.exists():
        shutil.rmtree(sd)
    sd.mkdir(parents=True)
    records = []
    for raw in files:
        src = Path(raw)
        if not src.is_file():
            raise RuntimeError(f'missing stage payload {src}')
        dst = sd / src.name
        shutil.copy2(src, dst)
        records.append(file_record(dst, fp))
    atomic_json(sd / 'receipt.json', {
        'format': FORMAT, 'stage': stage, 'contract_fingerprint': fp,
        'files': records, 'complete': True,
    })
    validate(root, spec)
    print(f'CHECKPOINT local stage={stage} complete=true fingerprint={fp}', flush=True)


def materialize(root: Path, spec: dict, stage: str, dest: str) -> None:
    completed = validate(root, spec)
    if stage not in completed:
        raise RuntimeError(f'stage {stage} not complete')
    out = Path(dest); out.mkdir(parents=True, exist_ok=True)
    for p in (root / 'stages' / stage).iterdir():
        if p.name != 'receipt.json' and p.is_file():
            shutil.copy2(p, out / p.name)
    print(f'CHECKPOINT materialized stage={stage} dest={out}', flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True); ap.add_argument('--contract-spec', required=True)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('init'); sub.add_parser('verify')
    p = sub.add_parser('add'); p.add_argument('--stage', choices=ORDER, required=True); p.add_argument('files', nargs='+')
    p = sub.add_parser('materialize'); p.add_argument('--stage', choices=ORDER, required=True); p.add_argument('--dest', required=True)
    a = ap.parse_args(); root = Path(a.root); spec = load_spec(a.contract_spec)
    if a.cmd == 'init':
        fp = bind(root, spec); completed = validate(root, spec); print(json.dumps({'fingerprint': fp, 'completed_stages': completed}, sort_keys=True))
    elif a.cmd == 'verify':
        print(json.dumps({'completed_stages': validate(root, spec)}, sort_keys=True))
    elif a.cmd == 'add':
        add_stage(root, spec, a.stage, a.files)
    else:
        materialize(root, spec, a.stage, a.dest)


if __name__ == '__main__':
    main()
