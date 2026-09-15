#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
from pathlib import Path

R1_BLOB = 'b510d8e97baf1c0b7b216c0605d83cdd029254e9'
PROMOTION_BLOB = 'cdbcea2622564d40aa9d1edc045a5808f8cdd1c4'
CLASSES = ('NATIVE_AVX512_ACTIVE', 'NATIVE_AVX512_INACTIVE')
SERIES = ('pure_common_response','mixed_common_response','exact_target_response','direct_response')
EXPECTED_NODE_COUNTS = {'PURE':897,'M076':1152,'M298':1141,'M300':996,'D50':1146,'D00':1152,'D58':99}


def blob(path: str) -> str:
    return subprocess.check_output(['git','hash-object',path], text=True).strip()


def rel(a: float, b: float) -> float:
    tiny = 2.2250738585072014e-308
    return abs(a-b)/max(abs(a),abs(b),tiny)


def rkey(r):
    return (r['mixed_batch_id'],r['direct_batch_id'],int(r['call_index']),r['z_u64hex'],r['k_u64hex'])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--contract',required=True)
    ap.add_argument('--promotion-authority',required=True)
    ap.add_argument('--inputs',nargs='+',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if blob(a.contract)!=R1_BLOB or blob(a.promotion_authority)!=PROMOTION_BLOB:
        raise RuntimeError('frozen R1/authority blob mismatch')
    c=json.load(open(a.contract)); auth=json.load(open(a.promotion_authority))
    if auth.get('sentinel_science_execution_authorized') is not False:
        raise RuntimeError('promotion authority must not be mistaken for launch authority')
    s=c['sentinel']
    docs=[json.load(open(p)) for p in a.inputs]
    expected={f'R{i:02d}' for i in range(1,33)}
    reps=[d.get('replicate') for d in docs]
    invalid=(len(docs)!=32 or set(reps)!=expected or len(set(reps))!=32)
    candidates=[d for d in docs if d.get('candidate')]
    eligible=[d for d in docs if d.get('eligible')]
    invalid |= any(d.get('preflight_valid') is not True for d in candidates)
    invalid |= any(d.get('substantive_response_computed') and d.get('preflight_valid') is not True for d in docs)

    maps={}; binary_keys=[]; software_keys=[]; max_lookup=0.0; invariant_ok=True
    expected_record_keys=None
    forbidden=['full_layerb_107_row_traversal_launched','covariance_read','whitening_read','nuisance_read','relation_null_read','Wm_S3_opened','science_gate_opened']
    for d in eligible:
        r=d.get('result')
        if not isinstance(r,dict) or r.get('forced_profile_valid') is not True:
            invalid=True; continue
        if r.get('solver_construction_count')!=int(s['class_constructions_per_lane']): invalid=True
        if r.get('requested_node_counts')!=EXPECTED_NODE_COUNTS: invalid=True
        if any(bool(r.get(k,True)) for k in forbidden): invalid=True
        q=float(r.get('max_requested_node_coordinate_rel_mismatch',float('inf'))); max_lookup=max(max_lookup,q)
        invariant_ok &= q <= float(s['requested_node_binding_le'])
        fp=r.get('fingerprint',{}); bk=fp.get('binary',{}).get('key'); sk=r.get('software_control_key')
        if not bk or not sk: invalid=True
        binary_keys.append(bk); software_keys.append(sk)
        rr=r.get('primitive_records',[]); km={rkey(x):x for x in rr}
        if len(km)!=len(rr) or not rr: invalid=True
        keys=set(km)
        if expected_record_keys is None: expected_record_keys=keys
        elif keys!=expected_record_keys: invalid=True
        for x in rr:
            invariant_ok &= all(math.isfinite(float(x[z])) for z in SERIES)
            invariant_ok &= math.isfinite(float(x['mixed_common_vs_pure_common_rel'])) and math.isfinite(float(x['exact_vs_direct_rel']))
        maps[d['replicate']]=km
    if eligible and (len(set(binary_keys))!=1 or len(set(software_keys))!=1): invalid=True

    counts={cls:sum(d.get('native_class')==cls for d in eligible) for cls in CLASSES}
    powered=(len(eligible)>=int(s['minimum_eligible_lanes']) and
             counts[CLASSES[0]]>=int(s['minimum_native_avx512_active']) and
             counts[CLASSES[1]]>=int(s['minimum_native_avx512_inactive']))

    metrics=[]; reproducible=False; node_ok=False; direct_ok=False
    max_spread=0.0; max_sep=0.0; max_node_rel=0.0; max_direct_rel=0.0
    if not invalid and invariant_ok and powered:
        reproducible=True
        for key in sorted(expected_record_keys):
            for series in SERIES:
                vals=[float(maps[d['replicate']][key][series]) for d in eligible]
                spread=max([rel(x,y) for x,y in itertools.combinations(vals,2)] or [0.0])
                means={}
                for cls in CLASSES:
                    vv=[float(maps[d['replicate']][key][series]) for d in eligible if d['native_class']==cls]
                    means[cls]=sum(vv)/len(vv)
                sep=rel(means[CLASSES[0]],means[CLASSES[1]])
                ok=spread<float(s['cross_host_primitive_spread_strict_lt']) and sep<float(s['native_class_mean_separation_strict_lt'])
                reproducible &= ok; max_spread=max(max_spread,spread); max_sep=max(max_sep,sep)
                metrics.append({'record_key':list(key),'series':series,'cross_host_max_pairwise_rel_spread':spread,'native_class_mean_rel_separation':sep,'reproducible':ok})
        node_ok=True; direct_ok=True
        for d in eligible:
            for x in maps[d['replicate']].values():
                nr=float(x['mixed_common_vs_pure_common_rel']); dr=float(x['exact_vs_direct_rel'])
                max_node_rel=max(max_node_rel,nr); max_direct_rel=max(max_direct_rel,dr)
                node_ok &= nr<float(s['mixed_common_vs_pure_common_strict_lt'])
                direct_ok &= dr<float(s['exact_vs_direct_strict_lt'])

    if invalid:
        cls='SENTINEL_INVALID'
    elif not invariant_ok:
        cls='SENTINEL_INCONCLUSIVE'
    elif not powered:
        cls='SENTINEL_UNDERPOWERED'
    elif not reproducible:
        cls='SENTINEL_REPRODUCIBILITY_BLOCKED'
    elif not node_ok:
        cls='SENTINEL_NODE_SET_SIDE_EFFECT_BLOCKED'
    elif not direct_ok:
        cls='SENTINEL_DIRECT_REFERENCE_BLOCKED'
    else:
        cls='SENTINEL_PASS'
    pass_gate=(cls=='SENTINEL_PASS')
    out={
      'schema':'LAYERB_BETA_V0_26_R1_SENTINEL_DECISION_V0_1','classification':cls,'effect':'+0/+0',
      'candidate_lane_count':len(candidates),'eligible_lane_count':len(eligible),'native_class_counts':counts,
      'invalid':invalid,'invariant_ok':invariant_ok,'powered':powered,'primitive_response_reproducibility_ok':reproducible,
      'primitive_response_metrics':metrics,'primitive_metric_count':len(metrics),
      'cross_host_max_pairwise_rel_spread_max':max_spread,'native_class_mean_rel_separation_max':max_sep,
      'node_set_side_effect_ok':node_ok,'direct_reference_ok':direct_ok,
      'mixed_common_vs_pure_common_rel_max':max_node_rel,'exact_vs_direct_rel_max':max_direct_rel,
      'max_requested_node_coordinate_rel_mismatch':max_lookup,'sentinel_pass':pass_gate,
      'full_replay_launch_authorized':False,'full_107_row_execution_authorized':False,
      'full_replay_must_not_launch_if_sentinel_not_pass':True,
      'next_admissible_action':('SEPARATE_SENTINEL_RESULT_FUNNEL_AUDIT_AND_EXPLICIT_FULL_REPLAY_LAUNCH_AUTHORITY' if pass_gate else 'DIAGNOSE_WITHIN_FROZEN_SENTINEL_CLASSIFICATION_ONLY'),
      'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,
      'global_65537_launched':False,'science_gate_opened':False,
      'token':'PASS_LAYERB_BETA_V0_26_R1_SENTINEL_DECISION_FINALIZER_PLUS_0_PLUS_0'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'],cls,len(metrics))
    return 0
if __name__=='__main__': raise SystemExit(main())
