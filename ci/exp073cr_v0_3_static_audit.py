#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re

BASE=Path('ci/exp073cr_wm_s3_ll3_sharded_resource_v0_1.py')
V2=Path('ci/exp073cr_wm_s3_ll3_sharded_resource_v0_2.py')
V3=Path('ci/exp073cr_wm_s3_ll3_sharded_resource_v0_3.py')
CAND=Path('experiments/073cr_wm_s3_ll3_sharded_resource_candidate_v0_1.json')
MAN=Path('experiments/073cr_wm_s3_ll3_sharded_heavy_first_manifest_v0_1.json')
HELPER=Path('ci/exp073cr_stream_band_ll3_range_v0_1.c')
CAND_SHA='d48e46197b48a6fcdf7d3eb3b0817973a2eadb25bbb617e7b8060c8c17209462'
QUEUE_SHA='3ba315d9bc24883ef746d92e785e0a040f9b13e751f59dda9a93e825a6390db4'
SYMBOL='exp073cr_stream_compress_band_ll3_range_v0_1'

src=BASE.read_text()
v2=V2.read_text()
v3=V3.read_text()
helper=HELPER.read_text()

assert hashlib.sha256(CAND.read_bytes()).hexdigest()==CAND_SHA
manifest=json.loads(MAN.read_text())
queue=manifest['queue']
assert len(queue)==64
assert hashlib.sha256(json.dumps(queue,sort_keys=True,separators=(',',':')).encode()).hexdigest()==QUEUE_SHA
assert manifest['queue_sha256']==QUEUE_SHA

# Core architecture and unchanged frozen resource threshold.
assert 'cf.ProcessPoolExecutor(max_workers=8' in src
assert "'max_inflight_futures':8" in src
assert 'CPU_MIN=.90' in src
assert "'durability_before_refill':True" in src
assert "base.CAND_SHA='d48e46197b48a6fcdf7d3eb3b0817973a2eadb25bbb617e7b8060c8c17209462'" in v2
assert "base.NS='checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3'" in v3
assert "base.VER='v0.3'" in v3

# Fail closed on the actual compute-loop ordering, not a prose grep.
store="store_shard(root,got,a,tel)"
sync="sync(root,branch,script,f'shard-b{got.band:02d}-l{got.lo:05d}-{got.hi:05d}')"
refill="futs[ex.submit(worker,nxt)]=nxt"
pos=[src.find(store),src.find(sync),src.find(refill)]
assert all(p>=0 for p in pos), pos
assert pos[0] < pos[1] < pos[2], pos
assert src.count(store)==1 and src.count(sync)==1 and src.count(refill)==1

# Shard output is placement-only during reconstruction.
assert 'out[s.lo:s.hi]=a; cov[s.lo:s.hi]=1' in src
assert 'np.array_equal(a,ref)' in src
assert "FAIL_EXACT='FAIL_EXP073CR_WM_S3_LL3_EXACT_EQUIVALENCE_V0_1'" in src
assert "'no_tolerance_rescue':True" in src

# Thread pins and exact helper ABI.
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','BLIS_NUM_THREADS','NUMEXPR_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    assert k in src
assert "os.environ.get('OMP_DYNAMIC','').upper()!='FALSE'" in src
assert SYMBOL in helper
assert 'if((nthreads!=1)' in helper
assert 'for(int ll2=lo;ll2<hi;ll2++)' in helper
assert 'for(int ll3=ll3_lo;ll3<ll3_hi;ll3++)' in helper
assert 'for(int l1=lmin_here;l1<=lmax_here;l1++)' in helper
assert 'acc[ll3-ll3_lo] += xi;' in helper

print(json.dumps({
    'complete':True,
    'experiment':'Exp073CR',
    'version':'v0.3',
    'candidate_sha256':CAND_SHA,
    'queue_sha256':QUEUE_SHA,
    'shard_count':64,
    'outer_workers':8,
    'cpu_fraction_min':0.90,
    'durability_order':['store_shard','durable_sync','refill_submit'],
    'token':'PASS_EXP073CR_V0_3_SOURCE_ORDER_STATIC_AUDIT'
},sort_keys=True))
print('PASS_EXP073CR_V0_3_SOURCE_ORDER_STATIC_AUDIT')
