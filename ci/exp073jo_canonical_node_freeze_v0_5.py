#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os
from pathlib import Path
import numpy as np

BASE_N=4096
EXPECTED_NODE_COUNT=4097
CAPACITY=4608
KMIN=1e-4
KMAX=0.06664762008318016
TARGET_MIN=0.00033800000000000003
TARGET_MAX=0.06664596609379447


def load_module(path: Path):
    spec=importlib.util.spec_from_file_location('jj_v05_grid_freeze',path)
    if spec is None or spec.loader is None:
        raise RuntimeError('cannot import frozen JJ implementation')
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--jj-script',required=True)
    ap.add_argument('--out-bin',required=True)
    ap.add_argument('--out-hex',required=True)
    ap.add_argument('--out-json',required=True)
    a=ap.parse_args()

    jj=load_module(Path(a.jj_script))
    if jj.KMIN!=KMIN or jj.KMAX!=KMAX or jj.TARGET_MIN!=TARGET_MIN or jj.TARGET_MAX!=TARGET_MAX:
        raise SystemExit('frozen JJ geometry constants mismatch')
    jj.CAPACITY=CAPACITY
    nodes,ratio,lo,hi=jj.guarded_lattice(BASE_N)
    nodes=np.asarray(nodes,dtype=np.float64)

    if (lo,hi,len(nodes))!=(0,1,EXPECTED_NODE_COUNT):
        raise SystemExit('canonical guard/count mismatch')
    if nodes.dtype!=np.dtype('float64') or nodes.ndim!=1:
        raise SystemExit('canonical dtype/shape mismatch')
    if np.any(~np.isfinite(nodes)) or np.any(nodes<=0.0) or np.any(np.diff(nodes)<=0.0):
        raise SystemExit('canonical monotonicity/finite mismatch')
    if nodes[0]!=np.float64(KMIN) or nodes[BASE_N-1]!=np.float64(KMAX) or not (nodes[-1]>nodes[BASE_N-1]):
        raise SystemExit('canonical endpoint/guard mismatch')

    dummy=np.zeros(nodes.shape,dtype=np.float64)
    _,valid=jj.cubic_centered(nodes,dummy,np.asarray([TARGET_MIN,TARGET_MAX],dtype=np.float64))
    if not bool(np.all(valid)):
        raise SystemExit('canonical frozen-target stencil support mismatch')

    raw=np.ascontiguousarray(nodes,dtype='<f8').tobytes(order='C')
    if len(raw)!=EXPECTED_NODE_COUNT*8:
        raise SystemExit('canonical raw byte count mismatch')
    hex_lines=''.join(float(x).hex()+'\n' for x in nodes)
    decoded=np.asarray([float.fromhex(s) for s in hex_lines.splitlines()],dtype='<f8')
    if decoded.tobytes(order='C')!=raw:
        raise SystemExit('hex roundtrip mismatch')

    out_bin=Path(a.out_bin); out_hex=Path(a.out_hex); out_json=Path(a.out_json)
    out_bin.parent.mkdir(parents=True,exist_ok=True); out_hex.parent.mkdir(parents=True,exist_ok=True); out_json.parent.mkdir(parents=True,exist_ok=True)
    out_bin.write_bytes(raw); out_hex.write_text(hex_lines)
    result={
      'schema':'EXP073JO_CANONICAL_NODE_FREEZE_RESULT_V0_5',
      'experiment':'Exp073JO',
      'classification':'CANONICAL_4097_NODE_PAYLOAD_FROZEN_PLUS_0_PLUS_0',
      'effect':'+0/+0',
      'response_blind':True,
      'class_imported_or_run':False,
      'observational_artifacts_read':False,
      'prior_response_artifacts_read':False,
      'base_n':BASE_N,
      'requested_node_count':EXPECTED_NODE_COUNT,
      'lower_guard_count':lo,
      'upper_guard_count':hi,
      'kmin_hex':float(nodes[0]).hex(),
      'base_kmax_hex':float(nodes[BASE_N-1]).hex(),
      'guard_kmax_hex':float(nodes[-1]).hex(),
      'ratio_binary64':float(ratio),
      'ratio_hex':float(ratio).hex(),
      'node_payload_dtype':'<f8',
      'node_payload_nbytes':len(raw),
      'node_payload_sha256':sha256(raw),
      'node_hex_sha256':sha256(hex_lines.encode()),
      'numpy_version':np.__version__,
      'workflow_head_sha':os.environ.get('GITHUB_SHA'),
      'token':'PASS_EXP073JO_CANONICAL_NODE_FREEZE_V0_5'
    }
    if result['numpy_version']!='1.26.4':
        raise SystemExit('unexpected numpy version')
    out_json.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['token'])
    print(json.dumps(result,sort_keys=True))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
