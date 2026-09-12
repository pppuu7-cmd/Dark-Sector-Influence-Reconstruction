#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, hashlib, heapq, json, math, pathlib, struct, sys

H=1e-4
ROLES=('reference','alpha_minus','beta_plus','beta_minus')
LABELS=('abs_dDelta_m_dalpha_left','abs_dDelta_m_dbeta_symmetric')
SCHEMA_CODEC='LAYERB_CHUNK_CALL_CODEC_V0_1'
EXPECTED_MAX=0.007384797439715474
COARSE_DIGEST='9e829d5127457085f18d79901d4aa621a050ce8406ff30c4d7e157dd069b80b4'
FINE_DIGEST='9f5f85e92570b68576bae91f52163cb0c005a1e003bfc09b8ccc80b332f79b36'


def load_json(p): return json.loads(pathlib.Path(p).read_text())
def dump(p,o): pathlib.Path(p).parent.mkdir(parents=True,exist_ok=True); pathlib.Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def fhex(x): return struct.unpack('<d',struct.pack('<Q',int(x,16)))[0]
def decode_f64(s,n):
    b=base64.b64decode(s.encode(),validate=True)
    if len(b)!=8*n: raise RuntimeError(f'f64 length {len(b)} != {8*n}')
    return struct.unpack('<'+str(n)+'d',b)
def decode_bool(s,n):
    b=base64.b64decode(s.encode(),validate=True)
    if len(b)*8<n: raise RuntimeError('packed bool too short')
    return tuple(bool((b[i>>3]>>(i&7))&1) for i in range(n))
def calls_digest(rows):
    h=hashlib.sha256(); h.update(SCHEMA_CODEC.encode()+b'\0'); h.update(struct.pack('<Q',len(rows)))
    for r in rows:
        z=fhex(r['z_u64hex']); ts=r['targets_u64hex']
        h.update(struct.pack('<dQ',z,len(ts)))
        for x in ts: h.update(struct.pack('<Q',int(x,16)))
    return h.hexdigest()
def find_call_lists(plan):
    found={}
    def walk(o,path='$'):
        if isinstance(o,list):
            if o and all(isinstance(x,dict) and 'z_u64hex' in x and 'targets_u64hex' in x for x in o):
                d=calls_digest(o); found.setdefault(d,[]).append((path,o))
            for i,x in enumerate(o): walk(x,f'{path}/{i}')
        elif isinstance(o,dict):
            for k,v in o.items(): walk(v,f'{path}/{k}')
    walk(plan); return found
def pick_plans(plan):
    found=find_call_lists(plan)
    if COARSE_DIGEST not in found or FINE_DIGEST not in found: raise RuntimeError(f'frozen plan digests absent; found={list(found)}')
    cp,coarse=found[COARSE_DIGEST][0]; fp,fine=found[FINE_DIGEST][0]
    if len(coarse)!=441 or len(fine)!=569: raise RuntimeError('frozen call-count mismatch')
    for i in range(441):
        if coarse[i]['z_u64hex']!=fine[i]['z_u64hex'] or coarse[i]['targets_u64hex']!=fine[i]['targets_u64hex']:
            raise RuntimeError(f'coarse/fine common plan mismatch at call {i}')
    return cp,coarse,fp,fine

def load_grid(root,g,with_valid=False):
    root=pathlib.Path(root); ds={r:load_json(root/g/r/'operand.json') for r in ROLES}
    L=[int(x) for x in ds['reference']['lengths']]
    for r in ROLES:
        if [int(x) for x in ds[r]['lengths']]!=L: raise RuntimeError(f'{g} role length vector mismatch')
    raw={r:[decode_f64(s,n) for s,n in zip(ds[r]['responses_f8_b64'],L)] for r in ROLES}
    valid=None
    if with_valid:
        valid={r:[decode_bool(s,n) for s,n in zip(ds[r]['valid_masks_packbits_b64'],L)] for r in ROLES}
        for i in range(len(L)):
            v=valid['reference'][i]
            for r in ROLES[1:]:
                if valid[r][i]!=v: raise RuntimeError(f'{g} model validity mismatch call {i}')
    return L,raw,valid

def response(raw,i,j,comp):
    if comp==0: return abs((raw['alpha_minus'][i][j]-raw['reference'][i][j])/(-H))
    return abs((raw['beta_plus'][i][j]-raw['beta_minus'][i][j])/(2*H))
def rel_metric(a,b): return abs(a-b)/max(abs(a),abs(b))
def rec_base(v,i,j,q,cr,fr):
    return {'relative_difference':v,'call_index':i,'target_index':j,'component_index':q,'component':LABELS[q],'coarse_response':cr,'fine_response':fr}

def atomic(a):
    cp,calls,fp,fine=pick_plans(load_json(a.plan))
    CL,C,CV=load_grid(a.operands,'coarse',True); FL,F,FV=load_grid(a.operands,'fine',True)
    if len(CL)!=441 or len(FL)!=569 or CL!=FL[:441]: raise RuntimeError('operand call lengths do not match frozen common plan')
    top=[]; maxcomp={}; maxdom={}; counts={str(x):0 for x in (0.001,0.002,0.005)}; atoms=0; status=0
    for i,n in enumerate(CL):
        if len(calls[i]['targets_u64hex'])!=n: raise RuntimeError(f'plan/operand target count mismatch call {i}')
        domain='DES' if i<377 else 'BOSS_GL64'
        for j in range(n):
            if CV['reference'][i][j]!=FV['reference'][i][j]: raise RuntimeError(f'grid validity mismatch {i}/{j}')
            if not CV['reference'][i][j]: continue
            for q in (0,1):
                cr=response(C,i,j,q); fr=response(F,i,j,q)
                good=math.isfinite(cr) and math.isfinite(fr) and cr>0 and fr>0
                if not good:
                    status+=1; continue
                atoms+=1; v=rel_metric(cr,fr)
                for t in (0.001,0.002,0.005):
                    if v>t: counts[str(t)]+=1
                r=rec_base(v,i,j,q,cr,fr); r.update({'domain':domain,'z':fhex(calls[i]['z_u64hex']),'target_k_Mpc^-1':fhex(calls[i]['targets_u64hex'][j])})
                if v>maxcomp.get(LABELS[q],{}).get('relative_difference',-1): maxcomp[LABELS[q]]=r.copy()
                if v>maxdom.get(domain,{}).get('relative_difference',-1): maxdom[domain]=r.copy()
                item=(v,i,j,q,r)
                if len(top)<30: heapq.heappush(top,item)
                elif v>top[0][0]: heapq.heapreplace(top,item)
    top_records=[x[4] for x in sorted(top,reverse=True,key=lambda x:x[0])]
    if not top_records: raise RuntimeError('no comparable atoms')
    g=top_records[0]; err=abs(g['relative_difference']-EXPECTED_MAX)
    if err>5e-15: raise RuntimeError(f'authoritative max not reproduced {g["relative_difference"]} vs {EXPECTED_MAX}')
    out={'schema':'LAYERB_EXACT_ATOMIC_OPERAND_LOCALIZATION_V0_2','classification':'EXACT_AUTHORITATIVE_MAX_REPRODUCED_AND_LOCALIZED','authoritative_max_expected':EXPECTED_MAX,'authoritative_max_reproduced':g['relative_difference'],'absolute_reproduction_error':err,'global_argmax':g,'max_by_component':maxcomp,'max_by_domain':maxdom,'counts_above_threshold':counts,'finite_positive_compared_atoms':atoms,'noncomparable_or_status_count':status,'coarse_plan_path':cp,'fine_plan_path':fp,'common_plan_bitwise_identical':True,'top_30':top_records,'class_solver_invoked':False,'scientific_operand_recomputed':False,'denser_successor_65537_authorized':False,'effect':'+0/+0'}
    dump(a.out,out); print(json.dumps(out,indent=2,sort_keys=True))

def role(a):
    CL,C,_=load_grid(a.operands,'coarse',False); FL,F,_=load_grid(a.operands,'fine',False)
    if CL!=FL[:441]: raise RuntimeError('role reconstruction length mismatch')
    best=None; comp=[None,None]
    for i,n in enumerate(CL):
        for j in range(n):
            for q in (0,1):
                cr=response(C,i,j,q); fr=response(F,i,j,q)
                if not (math.isfinite(cr) and math.isfinite(fr) and cr>0 and fr>0): continue
                v=rel_metric(cr,fr); r=rec_base(v,i,j,q,cr,fr)
                r['coarse_roles']={x:C[x][i][j] for x in ROLES}; r['fine_roles']={x:F[x][i][j] for x in ROLES}
                if best is None or v>best['relative_difference']: best=r
                if comp[q] is None or v>comp[q]['relative_difference']: comp[q]=r
    if best is None: raise RuntimeError('no role-comparable atoms')
    err=abs(best['relative_difference']-EXPECTED_MAX)
    if err>5e-15: raise RuntimeError(f'independent max mismatch {best["relative_difference"]}')
    out={'schema':'LAYERB_INDEPENDENT_ROLE_ATTRIBUTION_V0_2','classification':'INDEPENDENT_ROLE_RECONSTRUCTION_REPRODUCES_AUTHORITATIVE_MAX','global_argmax':best,'max_by_component':{LABELS[i]:comp[i] for i in range(2)},'authoritative_max_expected':EXPECTED_MAX,'absolute_reproduction_error':err,'class_solver_invoked':False,'scientific_operand_recomputed':False,'denser_successor_65537_authorized':False,'effect':'+0/+0'}
    dump(a.out,out); print(json.dumps(out,indent=2,sort_keys=True))
def segment(rows,a,b,name):
    zs=[fhex(rows[i]['z_u64hex']) for i in range(a,b)]; ts=[fhex(x) for i in range(a,b) for x in rows[i]['targets_u64hex']]
    return {'name':name,'call_start':a,'call_stop_exclusive':b,'call_count':b-a,'target_scalar_count':len(ts),'unique_z_count':len(set(zs)),'z_min':min(zs),'z_max':max(zs),'target_k_min_Mpc^-1':min(ts),'target_k_max_Mpc^-1':max(ts)}
def plan(a):
    cp,c,fp,f=pick_plans(load_json(a.plan))
    out={'schema':'LAYERB_COMMON_PLAN_IDENTITY_V0_2','classification':'COARSE_PLAN_BITWISE_IDENTICAL_TO_FINE_COMMON_PREFIX','coarse_digest':COARSE_DIGEST,'fine_digest':FINE_DIGEST,'coarse_plan_path':cp,'fine_plan_path':fp,'coarse_call_count':len(c),'fine_call_count':len(f),'common_prefix_call_count':441,'common_prefix_bitwise_identical':True,'segments':[segment(c,0,377,'DES_COMMON'),segment(c,377,441,'BOSS_GL64_COMMON'),segment(f,441,569,'BOSS_GL128_FINE_ONLY')],'coarse_target_scalar_count':sum(len(x['targets_u64hex']) for x in c),'fine_target_scalar_count':sum(len(x['targets_u64hex']) for x in f),'class_solver_invoked':False,'denser_successor_65537_authorized':False,'effect':'+0/+0'}
    dump(a.out,out); print(json.dumps(out,indent=2,sort_keys=True))
def decision(a):
    root=pathlib.Path(a.combined)
    def maybe(n):
        p=root/n; return load_json(p) if p.exists() else None
    x=maybe('atomic_localization.json'); r=maybe('role_attribution.json'); p=maybe('plan_identity.json'); present=all(v is not None for v in (x,r,p)); agree=False
    if present:
        xa=x['global_argmax']; ra=r['global_argmax']; agree=(xa['call_index']==ra['call_index'] and xa['target_index']==ra['target_index'] and xa['component_index']==ra['component_index'] and abs(xa['relative_difference']-ra['relative_difference'])<=5e-15 and p['common_prefix_bitwise_identical'] is True)
    if present and agree:
        cls='EXACT_OPERAND_LEVEL_DISCREPANCY_LOCALIZED_WITHOUT_SOLVER_RECOMPUTE'; loc=x['global_argmax']; nxt='TARGETED_DES_EXISTING_OPERAND_DIAGNOSTIC' if loc['domain']=='DES' else 'TARGETED_BOSS_EXISTING_OPERAND_DIAGNOSTIC'
    elif present:
        cls='OPERAND_LOCALIZATION_STREAM_DISAGREEMENT_REQUIRES_AUDIT'; loc=None; nxt='AUDIT_LOCALIZATION_STREAM_DISAGREEMENT'
    else:
        cls='OPERAND_LOCALIZATION_INFRASTRUCTURE_INCOMPLETE'; loc=None; nxt='REPAIR_LOCALIZATION_INFRASTRUCTURE_ONLY'
    out={'schema':'LAYERB_OPERAND_LOCALIZATION_DECISION_V0_2','classification':cls,'all_streams_present':present,'independent_streams_agree':agree,'localized_global_argmax':loc,'next_permitted_stage':nxt,'class_solver_invoked':False,'scientific_operand_recomputed':False,'criterion_mutated':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'denser_successor_65537_authorized':False,'requires_separate_prospective_authorization_for_any_heavy_rung':True,'effect':'+0/+0'}
    dump(a.out,out); print(json.dumps(out,indent=2,sort_keys=True))
def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    q=sub.add_parser('atomic'); q.add_argument('--plan',required=True); q.add_argument('--operands',required=True); q.add_argument('--out',required=True)
    q=sub.add_parser('role'); q.add_argument('--operands',required=True); q.add_argument('--out',required=True)
    q=sub.add_parser('plan'); q.add_argument('--plan',required=True); q.add_argument('--out',required=True)
    q=sub.add_parser('decision'); q.add_argument('--combined',required=True); q.add_argument('--out',required=True)
    a=ap.parse_args(); {'atomic':atomic,'role':role,'plan':plan,'decision':decision}[a.cmd](a)
if __name__=='__main__': main()
