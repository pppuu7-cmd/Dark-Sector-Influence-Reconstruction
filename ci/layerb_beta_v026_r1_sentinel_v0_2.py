#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import struct
import subprocess
import sys
from pathlib import Path

BASE_PATH = Path(__file__).with_name('layerb_beta_v026_r1_sentinel_v0_1.py')

spec = importlib.util.spec_from_file_location('layerb_beta_v026_r1_sentinel_v0_1_base', BASE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError('cannot import v0.1 sentinel base')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

_original_load = base.load


def _native_guarded_lattice(n: int):
    """Materialize the frozen lattice in a clean native NumPy process.

    The v0.1 successor intentionally ran the scientific child with a forced
    NumPy CPU-feature mask. The terminal response-blind diagnostic proved that
    recomputing GRID896 under that forced mask changes 247 IEEE-754 nodes even
    though the geometry is unchanged. V0.2 therefore freezes the grid before
    the forced child imports NumPy and transports exact float bits, while all
    downstream scientific code remains in the forced profile.
    """
    helper = r'''
import importlib.util, json, struct, sys
from pathlib import Path
p = Path(sys.argv[1])
n = int(sys.argv[2])
spec = importlib.util.spec_from_file_location('v026_r1_static_probe_native_grid', p)
if spec is None or spec.loader is None:
    raise RuntimeError('cannot import static probe')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
common, ratio, nlo, nhi = m.guarded_lattice(n)
out = {
    'common_u64hex': [struct.pack('>d', float(x)).hex() for x in common],
    'ratio_u64hex': struct.pack('>d', float(ratio)).hex(),
    'nlo': int(nlo),
    'nhi': int(nhi),
}
print(json.dumps(out, sort_keys=True, separators=(',', ':')))
'''
    env = base.clean_env()
    raw = subprocess.check_output(
        [sys.executable, '-c', helper, str(Path(base.STATIC_PROBE).resolve()), str(int(n))],
        text=True,
        env=env,
    )
    d = json.loads(raw)
    import numpy as np
    common = np.asarray(
        [struct.unpack('>d', bytes.fromhex(x))[0] for x in d['common_u64hex']],
        dtype=np.float64,
    )
    ratio = struct.unpack('>d', bytes.fromhex(d['ratio_u64hex']))[0]
    return common, ratio, int(d['nlo']), int(d['nhi'])


def _load_v0_2(name: str, path: str):
    module = _original_load(name, path)
    if path == base.STATIC_PROBE:
        module.guarded_lattice = _native_guarded_lattice
    return module


# Keep the complete v0.1 scientific implementation and classifier unchanged.
# Only substitute the response-blind GRID896 materialization primitive.
base.load = _load_v0_2

# base.run_self uses Path(__file__) from the imported module. Point it to this
# prospectively distinct executor so child/fingerprint subprocesses remain V0.2.
base.__file__ = __file__


if __name__ == '__main__':
    raise SystemExit(base.main())
