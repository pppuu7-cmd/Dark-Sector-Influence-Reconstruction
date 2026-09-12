#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, os
from pathlib import Path
import numpy as np

FROZEN_ENGINE_PATH=Path(__file__).with_name('exp073jl_article3_canonical_one_live_recovered_third_refinement_convergence_v0_2.py')
CODEC_PATH=Path(__file__).with_name('layerb_chunk_call_codec_v0_1.py')
ROLE_ORDER=('reference','alpha_minus','beta_plus','beta_minus')
EXPECTED={
 'coarse':{'calls':441,'scalars':83666,'nodes':16385,'node_sha':'3e10cea6e46a6d0c07eac825a4e508829727914c8690d42b187ef894eaa2c975','physical_constructs':4},
 'fine':{'calls':569,'scalars':121682,'nodes':32769,'node_sha':'82c48c17dba812bd08a3437f7e48376208a8c506f4a63087191608793fba4599','physical_constructs':32},
}

def _load(name,path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

_frozen=_load('dsir_frozen_jl_engine_delegate',FROZEN_ENGINE_PATH)
_codec=_load('dsir_chunk_codec_delegate',CODEC_PATH)
for _k,_v in vars(_frozen).items():
    if not _k.startswith('__') and _k!='evaluate_lattice': globals()[_k]=_v

def _load_operands(label,calls):
    root=os.environ.get('DSIR_CHUNK_OPERANDS_ROOT')
    plan_path=os.environ.get('DSIR_CHUNK_PLAN')
    if not root or not plan_path: raise RuntimeError('chunk operand environment not configured')
    plan=json.loads(Path(plan_path).read_text())
    digest=_codec.calls_digest(calls); key=f'{label}_calls_digest'
    if digest!=plan.get(key): raise RuntimeError(f'{label} live call digest does not match materialized plan')
    rows={}
    for p in Path(root).rglob('operand.json'):
        d=json.loads(p.read_text())
        if d.get('schema')!='LAYERB_16385_32769_CHUNK_ROLE_OPERAND_V0_1': continue
        if d.get('grid')!=label: continue
        role=d.get('role')
        if role in rows: raise RuntimeError(f'duplicate {label} operand role {role}')
        rows[role]=d
    if set(rows)!=set(ROLE_ORDER): raise RuntimeError(f'{label} operand roles mismatch {sorted(rows)}')
    exp=EXPECTED[label]
    decoded={}; valid_by_role={}; auth_sha=None; run_id=None; max_lookup=0.0; kkeys=set()
    for role in ROLE_ORDER:
        d=rows[role]
        checks=[
          d.get('token')=='LAYERB_16385_32769_CHUNK_ROLE_OPERAND_PASS_PLUS_0_PLUS_0',
          d.get('calls_digest')==digest,
          d.get('call_count')==exp['calls'], d.get('target_scalar_count')==exp['scalars'],
          d.get('canonical_node_count')==exp['nodes'], d.get('canonical_node_sha256')==exp['node_sha'],
          d.get('scientific_response_read') is True,
          d.get('scientific_response_persisted_as_authorized_operand') is True,
          d.get('convergence_metric_computed') is False, d.get('scientific_classification_computed') is False,
          d.get('covariance_read') is False, d.get('whitening_read') is False, d.get('nuisance_read') is False,
          d.get('relation_null_read') is False, d.get('Wm_S3_opened') is False,
          d.get('max_live_instances')==1, d.get('final_live_instances')==0,
        ]
        if not all(checks): raise RuntimeError(f'{label}/{role} operand receipt mismatch')
        if label=='fine' and d.get('solver_constructions')!=8: raise RuntimeError(f'{label}/{role} chunk construction mismatch')
        if label=='coarse' and d.get('solver_constructions')!=1: raise RuntimeError(f'{label}/{role} monolithic construction mismatch')
        if auth_sha is None: auth_sha=d.get('authorization_json_sha256')
        elif auth_sha!=d.get('authorization_json_sha256'): raise RuntimeError('operand authorization hash mismatch')
        if run_id is None: run_id=d.get('current_run_id')
        elif run_id!=d.get('current_run_id'): raise RuntimeError('operand current-run mismatch')
        lengths=[int(x) for x in d['lengths']]
        if len(lengths)!=exp['calls'] or sum(lengths)!=exp['scalars']: raise RuntimeError(f'{label}/{role} length vector mismatch')
        rs=[_codec.b64_f8(s,n) for s,n in zip(d['responses_f8_b64'],lengths)]
        vs=[_codec.b64_bool(s,n) for s,n in zip(d['valid_masks_packbits_b64'],lengths)]
        decoded[role]=rs; valid_by_role[role]=vs
        max_lookup=max(max_lookup,float(d['max_requested_node_coordinate_rel_mismatch']))
        kkeys.update(d.get('native_transfer_k_keys',[]))
    expected_run=os.environ.get('GITHUB_RUN_ID')
    if expected_run and int(expected_run)!=int(run_id): raise RuntimeError('operand run id differs from finalizer run')
    return digest,decoded,valid_by_role,max_lookup,kkeys,auth_sha,run_id

def evaluate_lattice(jj,nodes,calls,baseline,precision,label,tracker):
    if label not in EXPECTED: raise RuntimeError(f'unexpected lattice label {label}')
    exp=EXPECTED[label]
    if len(nodes)!=exp['nodes']: raise RuntimeError(f'{label} node count mismatch')
    digest,raw,valid_by_role,max_lookup,kkeys,auth_sha,run_id=_load_operands(label,calls)
    responses=[]; unsupported=0
    for i in range(len(calls)):
        ref_valid=valid_by_role['reference'][i]
        for role in ROLE_ORDER[1:]:
            if not np.array_equal(ref_valid,valid_by_role[role][i]): raise RuntimeError(f'{label} model stencil-validity mismatch at call {i}')
        unsupported+=int(np.count_nonzero(~ref_valid))
        ref=raw['reference'][i]; al=raw['alpha_minus'][i]; bp=raw['beta_plus'][i]; bm=raw['beta_minus'][i]
        if not (ref.shape==al.shape==bp.shape==bm.shape): raise RuntimeError(f'{label} role response shape mismatch at call {i}')
        response=np.column_stack((np.abs((al-ref)/(-H)),np.abs((bp-bm)/(2*H))))
        responses.append(np.ascontiguousarray(response,dtype='<f8'))
    tracker['constructions']+=4
    tracker['max_live']=max(tracker['max_live'],1)
    tracker['live']=0
    audit={
      'slot_role':label,'native_k_per_decade_for_pk':NATIVE_KPD,'requested_node_count':int(len(nodes)),
      'response_calls':len(calls),'target_evaluations':calls_scalar_count(calls),
      'unsupported_target_evaluations':unsupported,'max_requested_node_coordinate_rel_mismatch':max_lookup,
      'solver_constructions':4,'logical_legacy_role_constructions':4,
      'physical_operand_solver_constructions':exp['physical_constructs'],
      'role_order':list(ROLE_ORDER),'native_transfer_k_keys':sorted(kkeys),
      'chunk_calls_digest':digest,'operand_authorization_json_sha256':auth_sha,'operand_current_run_id':run_id,
      'cross_process_raw_operand_combination':True,
    }
    return responses,audit,kkeys
