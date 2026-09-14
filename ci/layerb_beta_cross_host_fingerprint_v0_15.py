#!/usr/bin/env python3
from __future__ import annotations
import argparse, contextlib, hashlib, importlib.util, io, itertools, json, math, os, platform, subprocess
from pathlib import Path
import numpy as np


def load(name, path):
    s = importlib.util.spec_from_file_location(name, Path(path))
    if s is None or s.loader is None:
        raise RuntimeError(f'cannot import {path}')
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def f64hex(h):
    import struct
    return struct.unpack('>d', bytes.fromhex(h))[0]


def rel(a, b):
    return abs(a-b) / max(abs(a), abs(b), np.finfo(np.float64).tiny)


def cmd_first(argv):
    try:
        p = subprocess.run(argv, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return (p.stdout or '').splitlines()[0].strip()
    except Exception as e:
        return f'UNAVAILABLE:{type(e).__name__}'


def first_cpu_fields():
    wanted = {'vendor_id','cpu family','model','stepping','microcode','model name','flags','Features'}
    out = {}
    p = Path('/proc/cpuinfo')
    if p.exists():
        for line in p.read_text(errors='replace').splitlines():
            if ':' not in line:
                continue
            k, v = [x.strip() for x in line.split(':', 1)]
            if k in wanted and k not in out:
                out[k] = ' '.join(v.split())
    flags = out.pop('flags', out.pop('Features', ''))
    if flags:
        flags = ' '.join(sorted(flags.split()))
    out['flags_sha256'] = hashlib.sha256(flags.encode()).hexdigest()
    return out


def image_fields():
    d = {}
    p = Path('/etc/os-release')
    if p.exists():
        for line in p.read_text(errors='replace').splitlines():
            if '=' in line:
                k, v = line.split('=', 1)
                if k in {'ID','VERSION_ID','VERSION_CODENAME','PRETTY_NAME'}:
                    d[k] = v.strip().strip('"')
    return d


def fingerprint():
    import scipy
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            np.__config__.show()
        except Exception as e:
            print('numpy-config-unavailable', type(e).__name__)
    npcfg = '\n'.join(x.rstrip() for x in buf.getvalue().splitlines() if x.strip())
    cpu = first_cpu_fields()
    hardware = {
        'runner_arch': os.environ.get('RUNNER_ARCH',''),
        'platform_machine': platform.machine(),
        'cpu_vendor_id': cpu.get('vendor_id',''),
        'cpu_family': cpu.get('cpu family',''),
        'cpu_model': cpu.get('model',''),
        'cpu_stepping': cpu.get('stepping',''),
        'cpu_microcode': cpu.get('microcode',''),
        'cpu_model_name': cpu.get('model name',''),
        'cpu_flags_sha256': cpu.get('flags_sha256','')
    }
    software = {
        'runner_os': os.environ.get('RUNNER_OS',''),
        'image_os': os.environ.get('ImageOS',''),
        'image_version': os.environ.get('ImageVersion',''),
        'platform_system': platform.system(),
        'platform_release': platform.release(),
        'platform_version': platform.version(),
        'os_release': image_fields(),
        'libc': platform.libc_ver(),
        'gcc': cmd_first(['gcc','--version']),
        'gfortran': cmd_first(['gfortran','--version']),
        'ldd': cmd_first(['ldd','--version']),
        'python': platform.python_version(),
        'numpy': np.__version__,
        'scipy': scipy.__version__,
        'numpy_config_sha256': hashlib.sha256(npcfg.encode()).hexdigest()
    }
    def hid(x):
        return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',',':')).encode()).hexdigest()
    combined = {'hardware':hardware,'software':software}
    return {
        'hardware': hardware,
        'software': software,
        'hardware_fingerprint_id': hid(hardware),
        'software_fingerprint_id': hid(software),
        'combined_fingerprint_id': hid(combined),
        'ephemeral_provenance': {
            'runner_name': os.environ.get('RUNNER_NAME',''),
            'github_run_id': os.environ.get('GITHUB_RUN_ID',''),
            'github_job': os.environ.get('GITHUB_JOB',''),
            'github_run_attempt': os.environ.get('GITHUB_RUN_ATTEMPT','')
        },
        'ephemeral_fields_used_in_scientific_fingerprint': False
    }


def lane(a, C):
    if a.grid not in C['grids'] or a.replicate not in C['replicates']:
        raise RuntimeError('unfrozen lane')
    v12 = load('v12', a.v12_executor)
    jj = load('jj', a.jj_script)
    exp = C['grids'][a.grid]
    common, ratio, nlo, nhi = jj.guarded_lattice(int(exp['base_n']))
    if [nlo, nhi, len(common)] != [exp['lower_guard_count'], exp['upper_guard_count'], exp['requested_node_count']]:
        raise RuntimeError('grid identity mismatch')
    lane_cells = [x for x in C['diagnostic_cells'] if x['grid'] == a.grid]
    hs = sorted({float(x['h']) for x in lane_cells}, reverse=True)
    from classy import Class
    cells = []
    max_lookup = 0.0
    solver_count = 0
    for h in hs:
        pure = {}
        try:
            for label, beta in [('plus', h), ('minus', -h)]:
                p = jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, common)
                p['tol_perturb_integration'] = C['tol300_override']
                c = Class(); c.set(p); c.compute(['transfer']); pure[label] = c; solver_count += 1
            for cell in [x for x in lane_cells if float(x['h']) == h]:
                z = f64hex(cell['z']); k = f64hex(cell['k']); vals = {}
                for label in ['plus','minus']:
                    yn, mx, _ = v12.extract(jj, pure[label], common, z)
                    max_lookup = max(max_lookup, mx)
                    vv, ok = jj.cubic_centered(common, yn, np.asarray([k], dtype=np.float64))
                    if not bool(ok[0]):
                        raise RuntimeError('unsupported frozen target')
                    vals[label] = float(vv[0])
                response = (vals['plus'] - vals['minus'])/(2*h)
                if not math.isfinite(response):
                    raise RuntimeError('non-finite response')
                cells.append({
                    'role':cell['role'],'grid':a.grid,'replicate':a.replicate,
                    'h':h,'h_key':format(h,'.17g'),'kind':cell['kind'],'d':cell['d'],
                    'z':cell['z'],'k':cell['k'],'response':response
                })
        finally:
            for c in pure.values():
                try: c.struct_cleanup()
                except Exception: pass
    out = {
        'schema':'LAYERB_BETA_CROSS_HOST_FINGERPRINT_LANE_V0_15',
        'grid':a.grid,'replicate':a.replicate,'profile':'PURE_PAIR','effect':'+0/+0',
        'tol_perturb_integration':C['tol300'],'solver_construction_count':solver_count,
        'max_requested_node_coordinate_rel_mismatch':max_lookup,'cells':cells,
        'fingerprint':fingerprint(),
        'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,
        'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
        'Wm_S3_opened':False,'science_gate_opened':False,
        'token':'PASS_LAYERB_BETA_CROSS_HOST_FINGERPRINT_LANE_V0_15'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(out['token'], a.grid, a.replicate, out['fingerprint']['combined_fingerprint_id'], solver_count, max_lookup)


def key_cell(c):
    return (c['grid'], format(float(c['h']),'.17g'), c['kind'], c['d'], c['z'], c['k'])


def decision(a, C):
    docs = [json.load(open(p)) for p in a.inputs]
    expected = {(g,r) for g in C['grids'] for r in C['replicates']}
    got = {(d['grid'],d['replicate']) for d in docs}
    if got != expected:
        raise RuntimeError('lane identity mismatch')
    if any(d.get('profile') != 'PURE_PAIR' for d in docs):
        raise RuntimeError('profile identity mismatch')
    max_lookup = max(float(d['max_requested_node_coordinate_rel_mismatch']) for d in docs)
    flags_ok = all(not any(bool(d[k]) for k in ['production_h_mutated','sampling_stepsize_changed','global_65537_launched','covariance_read','whitening_read','nuisance_read','relation_null_read','Wm_S3_opened','science_gate_opened']) for d in docs)
    fp_ok = all(d['fingerprint'].get('ephemeral_fields_used_in_scientific_fingerprint') is False for d in docs)
    vals = {}
    fps = {}
    for d in docs:
        fp = d['fingerprint']
        combined = {'hardware':fp['hardware'],'software':fp['software']}
        chk = hashlib.sha256(json.dumps(combined, sort_keys=True, separators=(',',':')).encode()).hexdigest()
        if chk != fp['combined_fingerprint_id']:
            raise RuntimeError('fingerprint hash mismatch')
        fps[(d['grid'],d['replicate'])] = fp
        for c in d['cells']:
            vals[(d['grid'],d['replicate'],format(float(c['h']),'.17g'),c['kind'],c['d'],c['z'],c['k'])] = float(c['response'])
    finite_ok = all(math.isfinite(x) for x in vals.values())
    tol = float(C['replay_relative_tolerance'])
    summaries = []
    anchors_ok = True
    cross_job_variation = False
    for cell in C['diagnostic_cells']:
        hkey = format(float(cell['h']),'.17g')
        rr = [vals[(cell['grid'],r,hkey,cell['kind'],cell['d'],cell['z'],cell['k'])] for r in C['replicates']]
        spread = max(rel(x,y) for x,y in itertools.combinations(rr,2))
        if cell['role']=='ANCHOR' and spread >= tol:
            anchors_ok = False
        if cell['role']=='REPLAY_FAILURE' and spread >= tol:
            cross_job_variation = True
        summaries.append({'role':cell['role'],'grid':cell['grid'],'h':cell['h'],'z':cell['z'],'k':cell['k'],'responses':rr,'max_pairwise_cross_job_rel':spread,'cross_job_stable':spread<tol})
    groups = {}
    for d in docs:
        fid = d['fingerprint']['combined_fingerprint_id']
        groups.setdefault((d['grid'],fid), []).append(d['replicate'])
    group_summary = []
    same_fp_nondet = False
    repeated_groups_by_grid = {g:[] for g in C['grids']}
    for (g,fid), reps in sorted(groups.items()):
        rec = {'grid':g,'combined_fingerprint_id':fid,'replicates':sorted(reps),'n':len(reps),'failure_cell_spreads':{}}
        if len(reps) >= 2:
            repeated_groups_by_grid[g].append(fid)
            for cell in [x for x in C['diagnostic_cells'] if x['grid']==g and x['role']=='REPLAY_FAILURE']:
                hkey=format(float(cell['h']),'.17g')
                rr=[vals[(g,r,hkey,cell['kind'],cell['d'],cell['z'],cell['k'])] for r in reps]
                spread=max(rel(x,y) for x,y in itertools.combinations(rr,2))
                rec['failure_cell_spreads'][f"{hkey}:{cell['z']}:{cell['k']}"]=spread
                if spread >= tol:
                    same_fp_nondet = True
        group_summary.append(rec)
    fingerprint_stratification = False
    stratification_witnesses = []
    if cross_job_variation and not same_fp_nondet:
        for g in C['grids']:
            fids = repeated_groups_by_grid[g]
            if len(fids) < 2:
                continue
            for cell in [x for x in C['diagnostic_cells'] if x['grid']==g and x['role']=='REPLAY_FAILURE']:
                hkey=format(float(cell['h']),'.17g')
                means=[]
                for fid in fids:
                    reps=groups[(g,fid)]
                    rr=[vals[(g,r,hkey,cell['kind'],cell['d'],cell['z'],cell['k'])] for r in reps]
                    means.append((fid,float(sum(rr)/len(rr))))
                between=max(rel(a[1],b[1]) for a,b in itertools.combinations(means,2))
                if between >= tol:
                    fingerprint_stratification=True
                    stratification_witnesses.append({'grid':g,'h':cell['h'],'z':cell['z'],'k':cell['k'],'max_between_repeated_fingerprint_mean_rel':between,'fingerprint_means':means})
    invariant_ok = flags_ok and fp_ok and finite_ok and max_lookup <= float(C['exact_target_binding_tolerance']) and anchors_ok
    if not invariant_ok:
        cls='CROSS_HOST_FINGERPRINT_AUDIT_INCONCLUSIVE'
        nxt='NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_15_INVARIANT_FAILURE'
    elif not cross_job_variation:
        cls='V013_CROSS_JOB_NONDETERMINISM_NOT_REPRODUCED_IN_V015'
        nxt='PROSPECTIVELY_FROZEN_SEPARATED_INTERPOLATION_CONFIRMATION_AUDIT'
    elif same_fp_nondet:
        cls='RECORDED_HOST_FINGERPRINT_INSUFFICIENT_CROSS_JOB_VARIATION_PERSISTS'
        nxt='PROSPECTIVELY_FROZEN_NUMERICAL_RUNTIME_STATE_FINGERPRINT_AUDIT'
    elif fingerprint_stratification:
        cls='HOST_ENVIRONMENT_FINGERPRINT_STRATIFICATION_SUPPORTED'
        nxt='PROSPECTIVELY_FROZEN_HOST_FACTOR_ISOLATION_AUDIT'
    else:
        cls='HOST_ENVIRONMENT_FINGERPRINT_AUDIT_UNDERPOWERED_OR_MIXED'
        nxt='PROSPECTIVELY_FROZEN_EXPANDED_HOST_FINGERPRINT_REPLICATION_AUDIT'
    out={
        'schema':'LAYERB_BETA_CROSS_HOST_FINGERPRINT_DECISION_V0_15','classification':cls,'effect':'+0/+0',
        'diagnostic_cells':summaries,'fingerprint_groups':group_summary,
        'cross_job_failure_variation_reproduced':cross_job_variation,
        'same_recorded_fingerprint_nondeterminism':same_fp_nondet,
        'fingerprint_stratification_supported':fingerprint_stratification,
        'stratification_witnesses':stratification_witnesses,
        'anchor_invariant_ok':anchors_ok,'finite_ok':finite_ok,'fingerprint_integrity_ok':fp_ok,
        'max_requested_node_coordinate_rel_mismatch':max_lookup,'replay_relative_tolerance':tol,'invariant_ok':invariant_ok,
        'ephemeral_fields_used_in_scientific_fingerprint':False,
        'production_h_mutated':False,'sampling_stepsize_changed':False,'global_65537_launched':False,
        'covariance_read':False,'whitening_read':False,'nuisance_read':False,'relation_null_read':False,
        'Wm_S3_opened':False,'science_gate_opened':False,'next_stage':nxt,
        'token':'PASS_LAYERB_BETA_CROSS_HOST_FINGERPRINT_DECISION_V0_15'
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(out['token'], json.dumps({'classification':cls,'next_stage':nxt,'cross_job_variation':cross_job_variation,'same_fp_nondet':same_fp_nondet,'stratified':fingerprint_stratification}, sort_keys=True))


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode', choices=['lane','decision'], required=True)
    p.add_argument('--contract', required=True)
    p.add_argument('--grid'); p.add_argument('--replicate')
    p.add_argument('--v12-executor'); p.add_argument('--jj-script'); p.add_argument('--baseline'); p.add_argument('--precision')
    p.add_argument('--inputs', nargs='*', default=[]); p.add_argument('--out', required=True)
    a=p.parse_args(); C=json.load(open(a.contract))
    lane(a,C) if a.mode=='lane' else decision(a,C)

if __name__=='__main__':
    main()
