#!/usr/bin/env python3
from __future__ import annotations
import argparse, contextlib, hashlib, importlib.util, io, itertools, json, math, os, platform, subprocess
from pathlib import Path
import numpy as np


def load(name, path):
    s=importlib.util.spec_from_file_location(name,Path(path))
    if s is None or s.loader is None: raise RuntimeError(f'cannot import {path}')
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def f64hex(h):
    import struct
    return struct.unpack('>d',bytes.fromhex(h))[0]


def rel(a,b): return abs(a-b)/max(abs(a),abs(b),np.finfo(np.float64).tiny)


def cmd_first(argv):
    try:
        p=subprocess.run(argv,check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        return (p.stdout or '').splitlines()[0].strip()
    except Exception as e:
        return f'UNAVAILABLE:{type(e).__name__}'


def canonical_hash(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def cpuinfo():
    fields={}; flags=set(); p=Path('/proc/cpuinfo')
    if p.exists():
        for line in p.read_text(errors='replace').splitlines():
            if ':' not in line: continue
            k,v=[x.strip() for x in line.split(':',1)]
            if k in {'vendor_id','cpu family','model','stepping','microcode','model name'} and k not in fields:
                fields[k]=' '.join(v.split())
            if k in {'flags','Features'} and not flags:
                flags=set(v.split())
    return fields,flags


def factor_record():
    import scipy
    f,flags=cpuinfo()
    selected={k:(k in flags) for k in ['avx','avx2','avx512f','avx512dq','avx512bw','avx512vl','fma','sse4_2']}
    cpu_model={
        'vendor_id':f.get('vendor_id',''),'family':f.get('cpu family',''),'model':f.get('model',''),
        'stepping':f.get('stepping',''),'model_name':f.get('model name','')
    }
    cfg=io.StringIO()
    with contextlib.redirect_stdout(cfg):
        try: np.__config__.show()
        except Exception as e: print('numpy-config-unavailable',type(e).__name__)
    runtime=io.StringIO()
    with contextlib.redirect_stdout(runtime):
        try:
            if hasattr(np,'show_runtime'): np.show_runtime()
            else: print('numpy-show-runtime-unavailable')
        except Exception as e: print('numpy-runtime-unavailable',type(e).__name__)
    controls={
        'runner_arch':os.environ.get('RUNNER_ARCH',''),'runner_os':os.environ.get('RUNNER_OS',''),
        'image_os':os.environ.get('ImageOS',''),'image_version':os.environ.get('ImageVersion',''),
        'machine':platform.machine(),'system':platform.system(),'release':platform.release(),'version':platform.version(),
        'libc':platform.libc_ver(),'gcc':cmd_first(['gcc','--version']),'gfortran':cmd_first(['gfortran','--version']),
        'ldd':cmd_first(['ldd','--version']),'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__
    }
    return {
        'avx512_class':'AVX512F_PRESENT' if selected['avx512f'] else 'AVX512F_ABSENT',
        'selected_cpu_features':selected,
        'cpu_model':cpu_model,
        'cpu_model_key':canonical_hash(cpu_model),
        'cpu_flags_sha256':hashlib.sha256(' '.join(sorted(flags)).encode()).hexdigest(),
        'microcode':f.get('microcode',''),
        'numpy_config_sha256':hashlib.sha256(cfg.getvalue().encode()).hexdigest(),
        'numpy_runtime_sha256':hashlib.sha256(runtime.getvalue().encode()).hexdigest(),
        'software_control':controls,
        'software_control_key':canonical_hash(controls),
        'ephemeral_provenance':{
            'runner_name':os.environ.get('RUNNER_NAME',''),'github_run_id':os.environ.get('GITHUB_RUN_ID',''),
            'github_job':os.environ.get('GITHUB_JOB',''),'github_run_attempt':os.environ.get('GITHUB_RUN_ATTEMPT','')
        },
        'ephemeral_fields_used_in_classifier':False
    }


def lane(a,C):
    if a.replicate not in C['replicates']: raise RuntimeError('unfrozen replicate')
    v12=load('v12',a.v12_executor); jj=load('jj',a.jj_script)
    exp=C['grid']; common,ratio,nlo,nhi=jj.guarded_lattice(int(exp['base_n']))
    if [nlo,nhi,len(common)] != [exp['lower_guard_count'],exp['upper_guard_count'],exp['requested_node_count']]: raise RuntimeError('grid identity mismatch')
    hs=sorted({float(x['h']) for x in C['diagnostic_cells']},reverse=True)
    from classy import Class
    cells=[]; max_lookup=0.; solver_count=0
    for h in hs:
        pure={}
        try:
            for label,beta in [('plus',h),('minus',-h)]:
                p=jj.class_params(Path(a.baseline),Path(a.precision),0.0,beta,common); p['tol_perturb_integration']=C['tol300_override']
                c=Class(); c.set(p); c.compute(['transfer']); pure[label]=c; solver_count+=1
            for cell in [x for x in C['diagnostic_cells'] if float(x['h'])==h]:
                z=f64hex(cell['z']); k=f64hex(cell['k']); vals={}
                for label in ['plus','minus']:
                    yn,mx,_=v12.extract(jj,pure[label],common,z); max_lookup=max(max_lookup,mx)
                    vv,ok=jj.cubic_centered(common,yn,np.asarray([k],dtype=np.float64))
                    if not bool(ok[0]): raise RuntimeError('unsupported frozen target')
                    vals[label]=float(vv[0])
                response=(vals['plus']-vals['minus'])/(2*h)
                if not math.isfinite(response): raise RuntimeError('non-finite response')
                cells.append({'role':cell['role'],'h':h,'h_key':format(h,'.17g'),'kind':cell['kind'],'d':cell['d'],'z':cell['z'],'k':cell['k'],'response':response})
        finally:
            for c in pure.values():
                try: c.struct_cleanup()
                except Exception: pass
    out={
        'schema':'LAYERB_BETA_HOST_FACTOR_ISOLATION_LANE_V0_16','grid':'GRID1024','replicate':a.replicate,'effect':'+0/+0',
        'factor':factor_record(),'cells':cells,'solver_construction_count':solver_count,
        'max_requested_node_coordinate_rel_mismatch':max_lookup,'tol_perturb_integration':C['tol300'],
        'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,
        'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
        'Wm_S3_opened':False,'science_gate_opened':False,
        'token':'PASS_LAYERB_BETA_HOST_FACTOR_ISOLATION_LANE_V0_16'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'],a.replicate,out['factor']['avx512_class'],out['factor']['cpu_model']['model_name'],solver_count,max_lookup)


def cellkey(c): return (format(float(c['h']),'.17g'),c['kind'],c['d'],c['z'],c['k'])


def maxspread(xs):
    return 0.0 if len(xs)<2 else max(rel(a,b) for a,b in itertools.combinations(xs,2))


def decision(a,C):
    docs=[json.load(open(p)) for p in a.inputs]
    expected=set(C['replicates']); got={d['replicate'] for d in docs}
    if got!=expected or len(docs)!=len(expected): raise RuntimeError('lane identity mismatch')
    if any(d.get('grid')!='GRID1024' for d in docs): raise RuntimeError('grid identity mismatch')
    vals={}; max_lookup=0.; flags_ok=True; ephemeral_ok=True
    for d in docs:
        max_lookup=max(max_lookup,float(d['max_requested_node_coordinate_rel_mismatch']))
        flags_ok &= not any(bool(d[k]) for k in ['production_h_mutated','sampling_stepsize_changed','global_65537_launched','covariance_read','whitening_read','nuisance_read','relation_null_read','Wm_S3_opened','science_gate_opened'])
        ephemeral_ok &= d['factor'].get('ephemeral_fields_used_in_classifier') is False
        for c in d['cells']: vals[(d['replicate'],)+cellkey(c)]=float(c['response'])
    finite_ok=all(math.isfinite(v) for v in vals.values()); tol=float(C['replay_relative_tolerance'])
    failures=[x for x in C['diagnostic_cells'] if x['role']=='REPLAY_FAILURE']; anchors=[x for x in C['diagnostic_cells'] if x['role']=='ANCHOR']
    allrep=sorted(expected)
    diagnostics=[]; cross_variation=False; anchors_ok=True
    for cell in C['diagnostic_cells']:
        ck=cellkey(cell); rr=[vals[(r,)+ck] for r in allrep]; spread=maxspread(rr)
        if cell['role']=='REPLAY_FAILURE' and spread>=tol: cross_variation=True
        if cell['role']=='ANCHOR' and spread>=tol: anchors_ok=False
        diagnostics.append({'role':cell['role'],'h':cell['h'],'z':cell['z'],'k':cell['k'],'max_pairwise_cross_job_rel':spread})
    byavx={c:[d for d in docs if d['factor']['avx512_class']==c] for c in ['AVX512F_PRESENT','AVX512F_ABSENT']}
    avx_summary={}; avx_within=True; avx_between=True
    for cls,dd in byavx.items():
        rec={'n':len(dd),'cpu_model_keys':sorted({d['factor']['cpu_model_key'] for d in dd}),'numpy_config_hashes':sorted({d['factor']['numpy_config_sha256'] for d in dd}),'failure_cells':[]}
        for cell in failures:
            ck=cellkey(cell); rr=[vals[(d['replicate'],)+ck] for d in dd]; spread=maxspread(rr); mean=(sum(rr)/len(rr)) if rr else None
            rec['failure_cells'].append({'h':cell['h'],'z':cell['z'],'k':cell['k'],'mean':mean,'within_class_spread':spread})
            if len(rr)>=2 and spread>=tol: avx_within=False
        avx_summary[cls]=rec
    avx_populated=all(len(byavx[c])>=int(C['minimum_factor_class_n']) for c in byavx)
    if avx_populated:
        for cell in failures:
            ck=cellkey(cell); means=[]
            for cls in ['AVX512F_PRESENT','AVX512F_ABSENT']:
                rr=[vals[(d['replicate'],)+ck] for d in byavx[cls]]; means.append(sum(rr)/len(rr))
            if rel(means[0],means[1])<tol: avx_between=False
    else: avx_between=False
    cpugroups={}
    for d in docs: cpugroups.setdefault(d['factor']['cpu_model_key'],[]).append(d)
    cpu_summary=[]; same_cpu_model_nondet=False; repeated_cpu_groups=0
    for key,dd in sorted(cpugroups.items()):
        rec={'cpu_model_key':key,'n':len(dd),'cpu_model':dd[0]['factor']['cpu_model'],'avx512_class':dd[0]['factor']['avx512_class'],'failure_cells':[]}
        if len(dd)>=2: repeated_cpu_groups+=1
        for cell in failures:
            ck=cellkey(cell); rr=[vals[(d['replicate'],)+ck] for d in dd]; spread=maxspread(rr)
            rec['failure_cells'].append({'h':cell['h'],'z':cell['z'],'k':cell['k'],'within_cpu_model_spread':spread,'mean':(sum(rr)/len(rr)) if rr else None})
            if len(dd)>=2 and spread>=tol: same_cpu_model_nondet=True
        cpu_summary.append(rec)
    software_keys=sorted({d['factor']['software_control_key'] for d in docs}); software_controls_constant=len(software_keys)==1
    numpy_by_avx={cls:sorted({d['factor']['numpy_config_sha256'] for d in dd}) for cls,dd in byavx.items()}
    runtime_by_avx={cls:sorted({d['factor']['numpy_runtime_sha256'] for d in dd}) for cls,dd in byavx.items()}
    numpy_signature_confounded=(avx_populated and all(len(numpy_by_avx[c])==1 for c in numpy_by_avx) and set(numpy_by_avx['AVX512F_PRESENT']).isdisjoint(set(numpy_by_avx['AVX512F_ABSENT'])))
    invariant_ok=flags_ok and ephemeral_ok and finite_ok and anchors_ok and max_lookup<=float(C['exact_target_binding_tolerance'])
    if not invariant_ok:
        cls='HOST_FACTOR_ISOLATION_AUDIT_INCONCLUSIVE'; nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_16_INVARIANT_FAILURE'
    elif not cross_variation:
        cls='V015_HOST_STRATIFICATION_NOT_REPRODUCED_IN_V016'; nxt='PROSPECTIVELY_FROZEN_CROSS_HOST_STRATIFICATION_CONFIRMATION_AUDIT'
    elif not software_controls_constant:
        cls='HOST_FACTOR_ISOLATION_CONFOUNDED_BY_SOFTWARE_CONTROL_VARIATION'; nxt='PROSPECTIVELY_FROZEN_CONTROLLED_SOFTWARE_IMAGE_FACTOR_AUDIT'
    elif not avx_populated:
        cls='HOST_FACTOR_ISOLATION_UNDERPOWERED_AVX512_CLASS'; nxt='PROSPECTIVELY_FROZEN_EXPANDED_HOST_FACTOR_REPLICATION_AUDIT'
    elif same_cpu_model_nondet:
        cls='HOST_FACTOR_ISOLATION_INCOMPLETE_SAME_CPU_MODEL_VARIATION'; nxt='PROSPECTIVELY_FROZEN_NUMERICAL_RUNTIME_STATE_FINGERPRINT_AUDIT'
    elif avx_within and avx_between:
        cls='RUNTIME_AVX512_CLASS_STRATIFICATION_SUPPORTED'; nxt='PROSPECTIVELY_FROZEN_CONTROLLED_AVX512_DISPATCH_INTERVENTION_AUDIT'
    else:
        cls='HOST_FACTOR_ISOLATION_MIXED_OR_CPU_MODEL_REQUIRED'; nxt='PROSPECTIVELY_FROZEN_EXPANDED_CPU_MODEL_FACTOR_REPLICATION_AUDIT'
    out={
        'schema':'LAYERB_BETA_HOST_FACTOR_ISOLATION_DECISION_V0_16','classification':cls,'effect':'+0/+0','diagnostic_cells':diagnostics,
        'cross_job_failure_variation_reproduced':cross_variation,'anchor_invariant_ok':anchors_ok,'finite_ok':finite_ok,'invariant_ok':invariant_ok,
        'max_requested_node_coordinate_rel_mismatch':max_lookup,'replay_relative_tolerance':tol,
        'avx512_class_minimum_n':int(C['minimum_factor_class_n']),'avx512_classes_populated':avx_populated,
        'avx512_within_class_stable':avx_within if avx_populated else False,'avx512_between_class_separation_supported':avx_between,
        'avx512_summary':avx_summary,'cpu_model_summary':cpu_summary,'repeated_cpu_model_group_count':repeated_cpu_groups,
        'same_cpu_model_nondeterminism':same_cpu_model_nondet,'software_control_signature_count':len(software_keys),
        'software_controls_constant':software_controls_constant,'numpy_config_hashes_by_avx512':numpy_by_avx,'numpy_runtime_hashes_by_avx512':runtime_by_avx,
        'numpy_config_signature_confounded_with_avx512_class':numpy_signature_confounded,
        'interpretation_note':'AVX512 classification is stratification, not causal proof; NumPy/runtime SIMD signatures may remain correlated and require intervention.',
        'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,'covariance_read':False,
        'whitening_read':False,'nuisance_read':False,'relation_null_read':False,'Wm_S3_opened':False,'science_gate_opened':False,
        'next_stage':nxt,'token':'PASS_LAYERB_BETA_HOST_FACTOR_ISOLATION_DECISION_V0_16'
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(out['token'],json.dumps({'classification':cls,'next_stage':nxt,'avx_populated':avx_populated,'avx_within':out['avx512_within_class_stable'],'avx_between':avx_between,'same_cpu_model_nondet':same_cpu_model_nondet},sort_keys=True))


def main():
    p=argparse.ArgumentParser(); p.add_argument('--mode',choices=['lane','decision'],required=True); p.add_argument('--contract',required=True)
    p.add_argument('--replicate'); p.add_argument('--v12-executor'); p.add_argument('--jj-script'); p.add_argument('--baseline'); p.add_argument('--precision')
    p.add_argument('--inputs',nargs='*',default=[]); p.add_argument('--out',required=True); a=p.parse_args(); C=json.load(open(a.contract))
    lane(a,C) if a.mode=='lane' else decision(a,C)

if __name__=='__main__': main()
