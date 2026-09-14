#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json, math, os, platform, struct, subprocess, sys
from pathlib import Path

NUMPY_DISABLE = 'AVX512F,AVX512CD,AVX512_KNL,AVX512_KNM,AVX512_SKX,AVX512_CLX,AVX512_CNL,AVX512_ICL'
GLIBC_DISABLE = 'glibc.cpu.hwcaps=-AVX512F,-AVX512DQ,-AVX512CD,-AVX512BW,-AVX512VL'
CONDITIONS = ['NATIVE','NUMPY_NO_AVX512','GLIBC_NO_AVX512','COMBINED_NO_AVX512']

def load(name, path):
    spec=importlib.util.spec_from_file_location(name,Path(path))
    if spec is None or spec.loader is None: raise RuntimeError(f'cannot import {path}')
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

def sha256_file(path):
    p=Path(path)
    if not p.exists() or not p.is_file(): return None
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''): h.update(chunk)
    return h.hexdigest()

def canonical_hash(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def f64hex(h): return struct.unpack('>d',bytes.fromhex(h))[0]
def rel(a,b):
    import numpy as np
    return abs(a-b)/max(abs(a),abs(b),np.finfo(np.float64).tiny)

def cpuinfo_record():
    fields={}; flags=set(); p=Path('/proc/cpuinfo')
    if p.exists():
        for line in p.read_text(errors='replace').splitlines():
            if ':' not in line: continue
            k,v=[x.strip() for x in line.split(':',1)]
            if k in {'vendor_id','cpu family','model','stepping','microcode','model name'} and k not in fields: fields[k]=' '.join(v.split())
            if k in {'flags','Features'} and not flags: flags=set(v.split())
    model={'vendor_id':fields.get('vendor_id',''),'family':fields.get('cpu family',''),'model':fields.get('model',''),'stepping':fields.get('stepping',''),'model_name':fields.get('model name','')}
    selected={k:(k in flags) for k in ['avx','avx2','avx512f','avx512dq','avx512cd','avx512bw','avx512vl','fma','sse4_2']}
    return {'cpu_model':model,'microcode':fields.get('microcode',''),'selected_cpu_features':selected,'cpu_flags_sha256':hashlib.sha256(' '.join(sorted(flags)).encode()).hexdigest()}

def loader_record():
    candidates=['/lib64/ld-linux-x86-64.so.2','/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2']; loader=next((x for x in candidates if Path(x).exists()),None)
    if loader is None: return {'loader':None,'selected_lines':[],'dl_hwcaps_subdirs_active':None,'v4_active':None,'sha256':None}
    try: txt=subprocess.run([loader,'--list-diagnostics'],check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout
    except Exception as e: return {'loader':loader,'error':type(e).__name__,'selected_lines':[],'dl_hwcaps_subdirs_active':None,'v4_active':None,'sha256':None}
    selected=[line.strip() for line in txt.splitlines() if line.startswith('dl_hwcaps_subdirs') or line.startswith('x86.cpu_features.')]
    active=None
    for line in selected:
        if line.startswith('dl_hwcaps_subdirs_active='):
            try: active=int(line.split('=',1)[1],0)
            except Exception: pass
    return {'loader':loader,'selected_lines':selected,'dl_hwcaps_subdirs_active':active,'v4_active':None if active is None else bool(active&1),'sha256':hashlib.sha256('\n'.join(selected).encode()).hexdigest()}

def numpy_record():
    import numpy as np, scipy
    try: feats=dict(getattr(np.core._multiarray_umath,'__cpu_features__'))
    except Exception: feats={}
    avx512={k:bool(v) for k,v in feats.items() if k.upper().startswith('AVX512')}
    return {'numpy':np.__version__,'scipy':scipy.__version__,'avx512_features':avx512,'any_avx512_enabled':any(avx512.values())}

def binary_record():
    import classy
    files={}
    for label,p in {'classy':getattr(classy,'__file__',None),'libclass_a':'external_class/libclass.a','class_binary':'external_class/class'}.items():
        if p: files[label]={'path':str(p),'sha256':sha256_file(p)}
    return {'files':files,'key':canonical_hash(files)}

def fingerprint():
    return {'cpu':cpuinfo_record(),'loader':loader_record(),'numpy':numpy_record(),'binary':binary_record(),'environment':{'NPY_DISABLE_CPU_FEATURES':os.environ.get('NPY_DISABLE_CPU_FEATURES',''),'GLIBC_TUNABLES':os.environ.get('GLIBC_TUNABLES','')},'software':{'python':platform.python_version(),'system':platform.system(),'release':platform.release(),'machine':platform.machine()}}

def condition_valid(condition,fp):
    raw=fp['cpu']['selected_cpu_features'].get('avx512f',False); v4=fp['loader']['v4_active']; npavx=fp['numpy']['any_avx512_enabled']
    if not raw: return False
    if condition=='NATIVE': return v4 is True and npavx is True and not fp['environment']['NPY_DISABLE_CPU_FEATURES'] and not fp['environment']['GLIBC_TUNABLES']
    if condition=='NUMPY_NO_AVX512': return v4 is True and npavx is False and fp['environment']['NPY_DISABLE_CPU_FEATURES']==NUMPY_DISABLE and not fp['environment']['GLIBC_TUNABLES']
    if condition=='GLIBC_NO_AVX512': return v4 is False and npavx is True and not fp['environment']['NPY_DISABLE_CPU_FEATURES'] and fp['environment']['GLIBC_TUNABLES']==GLIBC_DISABLE
    if condition=='COMBINED_NO_AVX512': return v4 is False and npavx is False and fp['environment']['NPY_DISABLE_CPU_FEATURES']==NUMPY_DISABLE and fp['environment']['GLIBC_TUNABLES']==GLIBC_DISABLE
    return False

def compute_child(a,C):
    import numpy as np
    v12=load('v12',a.v12_executor); jj=load('jj',a.jj_script); exp=C['grid']; common,ratio,nlo,nhi=jj.guarded_lattice(int(exp['base_n']))
    if [nlo,nhi,len(common)] != [exp['lower_guard_count'],exp['upper_guard_count'],exp['requested_node_count']]: raise RuntimeError('grid identity mismatch')
    hs=sorted({float(x['h']) for x in C['diagnostic_cells']},reverse=True); from classy import Class
    cells=[]; max_lookup=0.; solver_count=0
    for h in hs:
        pure={}
        try:
            for label,beta in [('plus',h),('minus',-h)]:
                p=jj.class_params(Path(a.baseline),Path(a.precision),0.0,beta,common); p['tol_perturb_integration']=C['tol300_override']; c=Class(); c.set(p); c.compute(['transfer']); pure[label]=c; solver_count+=1
            for cell in [x for x in C['diagnostic_cells'] if float(x['h'])==h]:
                z=f64hex(cell['z']); k=f64hex(cell['k']); vals={}
                for label in ['plus','minus']:
                    yn,mx,_=v12.extract(jj,pure[label],common,z); max_lookup=max(max_lookup,float(mx)); vv,ok=jj.cubic_centered(common,yn,np.asarray([k],dtype=np.float64))
                    if not bool(ok[0]): raise RuntimeError('unsupported frozen target')
                    vals[label]=float(vv[0])
                response=(vals['plus']-vals['minus'])/(2*h)
                if not math.isfinite(response): raise RuntimeError('non-finite response')
                cells.append({'role':cell['role'],'h':h,'kind':cell['kind'],'d':cell['d'],'z':cell['z'],'k':cell['k'],'response':response})
        finally:
            for c in pure.values():
                try: c.struct_cleanup()
                except Exception: pass
    fp=fingerprint(); out={'schema':'LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_CHILD_V0_18','condition':a.condition,'fingerprint':fp,'intervention_valid':condition_valid(a.condition,fp),'cells':cells,'solver_construction_count':solver_count,'max_requested_node_coordinate_rel_mismatch':max_lookup,'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,'token':'PASS_LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_CHILD_V0_18'}
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')

def child_env(condition):
    env=os.environ.copy(); env.pop('NPY_DISABLE_CPU_FEATURES',None); env.pop('GLIBC_TUNABLES',None)
    if condition in {'NUMPY_NO_AVX512','COMBINED_NO_AVX512'}: env['NPY_DISABLE_CPU_FEATURES']=NUMPY_DISABLE
    if condition in {'GLIBC_NO_AVX512','COMBINED_NO_AVX512'}: env['GLIBC_TUNABLES']=GLIBC_DISABLE
    return env

def run_child(a,condition,outpath):
    cmd=[sys.executable,str(Path(__file__).resolve()),'--mode','child','--condition',condition,'--contract',a.contract,'--v12-executor',a.v12_executor,'--jj-script',a.jj_script,'--baseline',a.baseline,'--precision',a.precision,'--out',str(outpath)]
    subprocess.run(cmd,check=True,env=child_env(condition)); return json.load(open(outpath))

def lane(a,C):
    if a.replicate not in C['replicates']: raise RuntimeError('unfrozen replicate')
    tmp=Path(a.out).parent/f'.v018_{a.replicate}'; tmp.mkdir(parents=True,exist_ok=True); native=run_child(a,'NATIVE',tmp/'native_probe.json'); fp=native['fingerprint']
    target=fp['cpu']['cpu_model']==C['target_cpu_model']; eligible=bool(target and fp['cpu']['selected_cpu_features'].get('avx512f') and fp['loader']['v4_active'] is True and fp['numpy']['any_avx512_enabled'] is True)
    conditions={}
    if eligible:
        conditions={'NATIVE':native}
        for condition in CONDITIONS[1:]: conditions[condition]=run_child(a,condition,tmp/f'{condition}.json')
    out={'schema':'LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_LANE_V0_18','replicate':a.replicate,'eligible':eligible,'native_fingerprint':fp,'conditions':conditions,'effect':'+0/+0','production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,'token':'PASS_LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_LANE_V0_18'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'],a.replicate,'ELIGIBLE' if eligible else 'SKIP')

def cellkey(c): return (format(float(c['h']),'.17g'),c['kind'],c['d'],c['z'],c['k'])
def values(doc): return {cellkey(c):float(c['response']) for c in doc['cells']}

def decision(a,C):
    docs=[json.load(open(p)) for p in a.inputs]; expected=set(C['replicates']); got={d['replicate'] for d in docs}
    if got!=expected or len(docs)!=len(expected): raise RuntimeError('lane identity mismatch')
    eligible=[d for d in docs if d['eligible']]; tol=float(C['replay_relative_tolerance']); bindtol=float(C['exact_target_binding_tolerance']); invalid=False; invariant_ok=True; max_lookup=0.; diagnostics=[]
    for d in eligible:
        if set(d['conditions'])!=set(CONDITIONS): invalid=True; continue
        keys=[]
        for condition in CONDITIONS:
            x=d['conditions'][condition]
            if not x.get('intervention_valid',False): invalid=True
            keys.append(x['fingerprint']['binary']['key']); max_lookup=max(max_lookup,float(x['max_requested_node_coordinate_rel_mismatch'])); invariant_ok &= all(math.isfinite(float(c['response'])) for c in x['cells']); invariant_ok &= not any(bool(x[k]) for k in ['production_h_mutated','sampling_stepsize_changed','global_65537_launched','covariance_read','whitening_read','nuisance_read','relation_null_read','Wm_S3_opened','science_gate_opened'])
        if len(set(keys))!=1: invalid=True
        vv={condition:values(d['conditions'][condition]) for condition in CONDITIONS}
        for cell in C['diagnostic_cells']:
            ck=cellkey(cell)
            if cell['role']=='ANCHOR':
                spread=max(rel(vv[x][ck],vv[y][ck]) for x,y in itertools.combinations(CONDITIONS,2)); invariant_ok &= spread<tol; diagnostics.append({'replicate':d['replicate'],'role':'ANCHOR','max_condition_rel_spread':spread})
    invariant_ok &= max_lookup<=bindtol; refs=C['branch_references']; failures=[x for x in C['diagnostic_cells'] if x['role']=='REPLAY_FAILURE']
    def refval(which,cell): return float(refs[which][f"h{format(float(cell['h']),'.0e').replace('-','m')}"])
    def switches(condition):
        if not eligible:return False
        for d in eligible:
            vv={c:values(d['conditions'][c]) for c in CONDITIONS}
            for cell in failures:
                ck=cellkey(cell); n=vv['NATIVE'][ck]; q=vv[condition][ck]
                if not (rel(n,refval('native',cell))<tol and rel(q,refval('alternate',cell))<tol and rel(n,q)>=tol): return False
        return True
    numpy_switch=switches('NUMPY_NO_AVX512') if not invalid and invariant_ok else False; glibc_switch=switches('GLIBC_NO_AVX512') if not invalid and invariant_ok else False; combined_switch=switches('COMBINED_NO_AVX512') if not invalid and invariant_ok else False
    combined_no_effect=bool(eligible) and not invalid and invariant_ok
    if combined_no_effect:
        for d in eligible:
            vv={c:values(d['conditions'][c]) for c in CONDITIONS}
            for cell in failures:
                ck=cellkey(cell)
                if rel(vv['NATIVE'][ck],vv['COMBINED_NO_AVX512'][ck])>=tol: combined_no_effect=False
    if invalid: cls='CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INVALID'; nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_18_INTERVENTION_VALIDATION'
    elif not invariant_ok: cls='CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_INCONCLUSIVE'; nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_18_INVARIANT_FAILURE'
    elif len(eligible)<int(C['minimum_eligible_lane_n']): cls='CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_UNDERPOWERED'; nxt='PROSPECTIVELY_FROZEN_EXPANDED_CONTROLLED_DISPATCH_PAIRED_REPLICATION_AUDIT'
    elif numpy_switch and not glibc_switch: cls='NUMPY_AVX512_DISPATCH_INTERVENTION_SUPPORTED'; nxt='PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT'
    elif glibc_switch and not numpy_switch: cls='GLIBC_AVX512_DISPATCH_INTERVENTION_SUPPORTED'; nxt='PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT'
    elif numpy_switch and glibc_switch: cls='NUMPY_AND_GLIBC_AVX512_DISPATCH_INTERVENTIONS_SUPPORTED'; nxt='PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT'
    elif combined_switch: cls='COMBINED_CPU_CAPABILITY_DISPATCH_INTERVENTION_SUPPORTED_NOT_COMPONENT_ISOLATED'; nxt='PROSPECTIVELY_FROZEN_FORCED_BASELINE_CROSS_HOST_REPRODUCIBILITY_AUDIT'
    elif combined_no_effect: cls='CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_NO_EFFECT'; nxt='PROSPECTIVELY_FROZEN_PROCESS_INITIALIZATION_MEMORY_LAYOUT_AUDIT'
    else: cls='CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_MIXED'; nxt='PROSPECTIVELY_FROZEN_CONTROLLED_DISPATCH_INTERVENTION_REPLICATION_AUDIT'
    out={'schema':'LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_DECISION_V0_18','classification':cls,'effect':'+0/+0','eligible_lane_count':len(eligible),'minimum_eligible_lane_n':int(C['minimum_eligible_lane_n']),'eligible_replicates':[d['replicate'] for d in eligible],'invalid_intervention':invalid,'invariant_ok':invariant_ok,'max_requested_node_coordinate_rel_mismatch':max_lookup,'numpy_switch_supported':numpy_switch,'glibc_switch_supported':glibc_switch,'combined_switch_supported':combined_switch,'combined_no_effect':combined_no_effect,'diagnostics':diagnostics,'next_stage':nxt,'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,'token':'PASS_LAYERB_BETA_CONTROLLED_CPU_CAPABILITY_DISPATCH_DECISION_V0_18'}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(out['token'],cls,len(eligible),nxt)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['lane','child','decision'],required=True); p.add_argument('--replicate'); p.add_argument('--condition'); p.add_argument('--contract',required=True); p.add_argument('--v12-executor'); p.add_argument('--jj-script'); p.add_argument('--baseline'); p.add_argument('--precision'); p.add_argument('--inputs',nargs='*'); p.add_argument('--out',required=True); a=p.parse_args(); C=json.load(open(a.contract))
    if a.mode=='child': compute_child(a,C)
    elif a.mode=='lane': lane(a,C)
    else: decision(a,C)
if __name__=='__main__': main()
