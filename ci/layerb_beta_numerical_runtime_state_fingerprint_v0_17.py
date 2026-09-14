#!/usr/bin/env python3
from __future__ import annotations
import argparse, contextlib, ctypes, hashlib, importlib.util, io, itertools, json, math, os, platform, subprocess, tempfile
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


def canonical_hash(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def sha256_file(path):
    p = Path(path)
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def cmd(argv):
    try:
        p = subprocess.run(argv, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.stdout or ''
    except Exception as e:
        return f'UNAVAILABLE:{type(e).__name__}'


def cmd_first(argv):
    out = cmd(argv)
    return out.splitlines()[0].strip() if out.splitlines() else out.strip()


def cpuinfo():
    fields = {}
    flags = set()
    p = Path('/proc/cpuinfo')
    if p.exists():
        for line in p.read_text(errors='replace').splitlines():
            if ':' not in line:
                continue
            k, v = [x.strip() for x in line.split(':', 1)]
            if k in {'vendor_id', 'cpu family', 'model', 'stepping', 'microcode', 'model name'} and k not in fields:
                fields[k] = ' '.join(v.split())
            if k in {'flags', 'Features'} and not flags:
                flags = set(v.split())
    return fields, flags


def auxv_record():
    libc = ctypes.CDLL(None)
    f = libc.getauxval
    f.argtypes = [ctypes.c_ulong]
    f.restype = ctypes.c_ulong
    return {'AT_HWCAP': int(f(16)), 'AT_HWCAP2': int(f(26))}


def fpu_record():
    src = r'''
#include <stdint.h>
#include <xmmintrin.h>
unsigned int dsir_get_mxcsr(void){ return _mm_getcsr(); }
unsigned int dsir_get_x87cw(void){ unsigned short x=0; __asm__ __volatile__("fnstcw %0" : "=m"(x)); return (unsigned int)x; }
'''
    with tempfile.TemporaryDirectory(prefix='dsir_fpu_') as td:
        c = Path(td) / 'fpu.c'
        so = Path(td) / 'fpu.so'
        c.write_text(src)
        subprocess.run(['gcc', '-shared', '-fPIC', '-O0', str(c), '-o', str(so)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        lib = ctypes.CDLL(str(so))
        lib.dsir_get_mxcsr.restype = ctypes.c_uint
        lib.dsir_get_x87cw.restype = ctypes.c_uint
        mxcsr = int(lib.dsir_get_mxcsr())
        x87cw = int(lib.dsir_get_x87cw())
    libc = ctypes.CDLL(None)
    libc.fegetround.restype = ctypes.c_int
    fe = int(libc.fegetround())
    return {
        'fegetround': fe,
        'mxcsr_raw': mxcsr,
        'mxcsr_control_bits_6_to_15': mxcsr & 0xFFC0,
        'x87_control_word': x87cw,
    }


def numpy_record():
    import scipy
    cfg = io.StringIO()
    with contextlib.redirect_stdout(cfg):
        try:
            np.__config__.show()
        except Exception as e:
            print('numpy-config-unavailable', type(e).__name__)
    rt = io.StringIO()
    with contextlib.redirect_stdout(rt):
        try:
            if hasattr(np, 'show_runtime'):
                np.show_runtime()
            else:
                print('numpy-show-runtime-unavailable')
        except Exception as e:
            print('numpy-runtime-unavailable', type(e).__name__)
    cfg_text = '\n'.join(x.rstrip() for x in cfg.getvalue().splitlines() if x.strip())
    rt_text = '\n'.join(x.rstrip() for x in rt.getvalue().splitlines() if x.strip())
    return {
        'config_sha256': hashlib.sha256(cfg_text.encode()).hexdigest(),
        'runtime_sha256': hashlib.sha256(rt_text.encode()).hexdigest(),
        'numpy_version': np.__version__,
        'scipy_version': scipy.__version__,
    }


def loader_cpu_record():
    candidates = [Path('/lib64/ld-linux-x86-64.so.2'), Path('/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2')]
    exe = next((p for p in candidates if p.exists()), None)
    if exe is None:
        return {'loader': 'UNAVAILABLE', 'selected_lines': [], 'selected_sha256': canonical_hash([])}
    out = cmd([str(exe), '--list-diagnostics', '/bin/true'])
    lines = []
    for line in out.splitlines():
        low = line.lower()
        if ('hwcaps' in low or 'cpu_features' in low) and 'env' not in low:
            lines.append(line.strip())
    lines = sorted(set(lines))
    return {'loader': str(exe), 'selected_lines': lines, 'selected_sha256': canonical_hash(lines)}


def loaded_numerical_libraries():
    p = Path('/proc/self/maps')
    paths = set()
    if p.exists():
        for line in p.read_text(errors='replace').splitlines():
            parts = line.split()
            if not parts:
                continue
            q = parts[-1]
            if not q.startswith('/'):
                continue
            name = Path(q).name.lower()
            if any(token in name for token in ['libc.so', 'libm.so', 'libgsl', 'libgomp', 'libopenblas', 'libgcc_s', 'libstdc++', 'libpython']):
                paths.add(q)
    records = []
    for q in sorted(paths):
        try:
            records.append({'name': Path(q).name, 'sha256': sha256_file(q)})
        except Exception as e:
            records.append({'name': Path(q).name, 'sha256': f'UNAVAILABLE:{type(e).__name__}'})
    return records


def binary_record():
    import classy
    paths = []
    q = Path(classy.__file__)
    if q.exists():
        paths.append(('classy_extension', q))
    for label, q in [('class_executable', Path('external_class/class')), ('libclass_archive', Path('external_class/libclass.a'))]:
        if q.exists():
            paths.append((label, q))
    return {label: sha256_file(q) for label, q in paths}


def software_control():
    import scipy
    return {
        'runner_arch': os.environ.get('RUNNER_ARCH', ''),
        'runner_os': os.environ.get('RUNNER_OS', ''),
        'image_os': os.environ.get('ImageOS', ''),
        'image_version': os.environ.get('ImageVersion', ''),
        'machine': platform.machine(),
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'libc': platform.libc_ver(),
        'gcc': cmd_first(['gcc', '--version']),
        'gfortran': cmd_first(['gfortran', '--version']),
        'ldd': cmd_first(['ldd', '--version']),
        'python': platform.python_version(),
        'numpy': np.__version__,
        'scipy': scipy.__version__,
        'OMP_NUM_THREADS': os.environ.get('OMP_NUM_THREADS', ''),
        'OPENBLAS_NUM_THREADS': os.environ.get('OPENBLAS_NUM_THREADS', ''),
        'MKL_NUM_THREADS': os.environ.get('MKL_NUM_THREADS', ''),
        'GLIBC_TUNABLES': os.environ.get('GLIBC_TUNABLES', ''),
        'NPY_DISABLE_CPU_FEATURES': os.environ.get('NPY_DISABLE_CPU_FEATURES', ''),
    }


def runtime_state_record():
    fields, flags = cpuinfo()
    selected = {k: (k in flags) for k in ['avx', 'avx2', 'avx512f', 'avx512dq', 'avx512bw', 'avx512vl', 'fma', 'sse4_2']}
    cpu_model = {
        'vendor_id': fields.get('vendor_id', ''),
        'family': fields.get('cpu family', ''),
        'model': fields.get('model', ''),
        'stepping': fields.get('stepping', ''),
        'model_name': fields.get('model name', ''),
    }
    auxv = auxv_record()
    fpu = fpu_record()
    numpy_rt = numpy_record()
    loader = loader_cpu_record()
    binaries = binary_record()
    libraries = loaded_numerical_libraries()
    sw = software_control()
    capability = {
        'cpu_model': cpu_model,
        'microcode': fields.get('microcode', ''),
        'cpu_flags_sha256': hashlib.sha256(' '.join(sorted(flags)).encode()).hexdigest(),
        'selected_cpu_features': selected,
        'auxv': auxv,
        'loader_cpu_selected_sha256': loader['selected_sha256'],
    }
    fpu_control = {
        'fegetround': fpu['fegetround'],
        'mxcsr_control_bits_6_to_15': fpu['mxcsr_control_bits_6_to_15'],
        'x87_control_word': fpu['x87_control_word'],
    }
    binary_runtime = {'binaries': binaries, 'loaded_numerical_libraries': libraries}
    numpy_dispatch = numpy_rt
    full = {
        'capability': capability,
        'fpu_control': fpu_control,
        'binary_runtime': binary_runtime,
        'numpy_dispatch': numpy_dispatch,
        'software_control': sw,
    }
    complete = bool(binaries.get('classy_extension')) and all(k in fpu_control for k in ['fegetround', 'mxcsr_control_bits_6_to_15', 'x87_control_word'])
    return {
        'cpu_model': cpu_model,
        'cpu_model_key': canonical_hash(cpu_model),
        'capability': capability,
        'cpu_capability_key': canonical_hash(capability),
        'fpu_pre': fpu,
        'fpu_control_key': canonical_hash(fpu_control),
        'binary_runtime': binary_runtime,
        'binary_runtime_key': canonical_hash(binary_runtime),
        'numpy_dispatch': numpy_dispatch,
        'numpy_runtime_key': canonical_hash(numpy_dispatch),
        'software_control': sw,
        'software_control_key': canonical_hash(sw),
        'loader_cpu_record': loader,
        'full_runtime_state_key': canonical_hash(full),
        'fingerprint_complete': complete,
        'ephemeral_provenance': {
            'runner_name': os.environ.get('RUNNER_NAME', ''),
            'github_run_id': os.environ.get('GITHUB_RUN_ID', ''),
            'github_job': os.environ.get('GITHUB_JOB', ''),
            'github_run_attempt': os.environ.get('GITHUB_RUN_ATTEMPT', ''),
        },
        'ephemeral_fields_used_in_classifier': False,
    }


def lane(a, C):
    if a.replicate not in C['replicates']:
        raise RuntimeError('unfrozen replicate')
    v12 = load('v12', a.v12_executor)
    jj = load('jj', a.jj_script)
    exp = C['grid']
    common, ratio, nlo, nhi = jj.guarded_lattice(int(exp['base_n']))
    if [nlo, nhi, len(common)] != [exp['lower_guard_count'], exp['upper_guard_count'], exp['requested_node_count']]:
        raise RuntimeError('grid identity mismatch')
    from classy import Class
    state = runtime_state_record()
    hs = sorted({float(x['h']) for x in C['diagnostic_cells']}, reverse=True)
    cells = []
    max_lookup = 0.0
    solver_count = 0
    for h in hs:
        pure = {}
        try:
            for label, beta in [('plus', h), ('minus', -h)]:
                p = jj.class_params(Path(a.baseline), Path(a.precision), 0.0, beta, common)
                p['tol_perturb_integration'] = C['tol300_override']
                c = Class()
                c.set(p)
                c.compute(['transfer'])
                pure[label] = c
                solver_count += 1
            for cell in [x for x in C['diagnostic_cells'] if float(x['h']) == h]:
                z = f64hex(cell['z'])
                k = f64hex(cell['k'])
                vals = {}
                for label in ['plus', 'minus']:
                    yn, mx, _ = v12.extract(jj, pure[label], common, z)
                    max_lookup = max(max_lookup, mx)
                    vv, ok = jj.cubic_centered(common, yn, np.asarray([k], dtype=np.float64))
                    if not bool(ok[0]):
                        raise RuntimeError('unsupported frozen target')
                    vals[label] = float(vv[0])
                response = (vals['plus'] - vals['minus']) / (2*h)
                if not math.isfinite(response):
                    raise RuntimeError('non-finite response')
                cells.append({
                    'role': cell['role'], 'h': h, 'h_key': format(h, '.17g'), 'kind': cell['kind'], 'd': cell['d'],
                    'z': cell['z'], 'k': cell['k'], 'response': response,
                })
        finally:
            for c in pure.values():
                try:
                    c.struct_cleanup()
                except Exception:
                    pass
    post_fpu = fpu_record()
    out = {
        'schema': 'LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_LANE_V0_17',
        'grid': 'GRID1024', 'replicate': a.replicate, 'effect': '+0/+0',
        'runtime_state': state, 'post_solver_fpu': post_fpu, 'cells': cells,
        'solver_construction_count': solver_count,
        'max_requested_node_coordinate_rel_mismatch': max_lookup,
        'tol_perturb_integration': C['tol300'],
        'production_h_mutated': False, 'sampling_stepsize_changed': False, 'global_65537_launched': False,
        'covariance_read': False, 'whitening_read': False, 'nuisance_read': False, 'relation_null_read': False,
        'Wm_S3_opened': False, 'science_gate_opened': False,
        'token': 'PASS_LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_LANE_V0_17',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], a.replicate, state['cpu_model']['model_name'], state['cpu_capability_key'], state['full_runtime_state_key'], solver_count, max_lookup)


def cellkey(c):
    return (format(float(c['h']), '.17g'), c['kind'], c['d'], c['z'], c['k'])


def maxspread(xs):
    return 0.0 if len(xs) < 2 else max(rel(a, b) for a, b in itertools.combinations(xs, 2))


def factor_summary(target_docs, vals, failures, field, tol, min_group_n):
    groups = {}
    for d in target_docs:
        key = d['runtime_state'][field]
        groups.setdefault(key, []).append(d)
    records = []
    repeated = []
    all_repeated_stable = True
    for key, dd in sorted(groups.items()):
        rec = {'key': key, 'n': len(dd), 'replicates': sorted(d['replicate'] for d in dd), 'failure_cells': []}
        if len(dd) >= min_group_n:
            repeated.append((key, dd))
        for cell in failures:
            ck = cellkey(cell)
            rr = [vals[(d['replicate'],) + ck] for d in dd]
            sp = maxspread(rr)
            rec['failure_cells'].append({'h': cell['h'], 'z': cell['z'], 'k': cell['k'], 'mean': sum(rr)/len(rr), 'spread': sp})
            if len(dd) >= min_group_n and sp >= tol:
                all_repeated_stable = False
        records.append(rec)
    separated = False
    witnesses = []
    for (ka, da), (kb, db) in itertools.combinations(repeated, 2):
        per_cell = []
        all_sep = True
        for cell in failures:
            ck = cellkey(cell)
            ma = sum(vals[(d['replicate'],) + ck] for d in da) / len(da)
            mb = sum(vals[(d['replicate'],) + ck] for d in db) / len(db)
            sep = rel(ma, mb)
            per_cell.append({'h': cell['h'], 'z': cell['z'], 'k': cell['k'], 'relative_mean_separation': sep})
            if sep < tol:
                all_sep = False
        if all_sep:
            separated = True
            witnesses.append({'key_a': ka, 'key_b': kb, 'cells': per_cell})
    return {
        'field': field, 'group_count': len(groups), 'repeated_group_count': len(repeated),
        'all_repeated_groups_stable': all_repeated_stable, 'between_repeated_groups_separated_on_all_failure_cells': separated,
        'groups': records, 'witnesses': witnesses,
    }


def decision(a, C):
    docs = [json.load(open(p)) for p in a.inputs]
    expected = set(C['replicates'])
    got = {d['replicate'] for d in docs}
    if got != expected or len(docs) != len(expected):
        raise RuntimeError('lane identity mismatch')
    if any(d.get('grid') != 'GRID1024' for d in docs):
        raise RuntimeError('grid identity mismatch')
    vals = {}
    max_lookup = 0.0
    flags_ok = True
    fingerprint_ok = True
    ephemeral_ok = True
    for d in docs:
        max_lookup = max(max_lookup, float(d['max_requested_node_coordinate_rel_mismatch']))
        flags_ok &= not any(bool(d[k]) for k in ['production_h_mutated', 'sampling_stepsize_changed', 'global_65537_launched', 'covariance_read', 'whitening_read', 'nuisance_read', 'relation_null_read', 'Wm_S3_opened', 'science_gate_opened'])
        fingerprint_ok &= bool(d['runtime_state'].get('fingerprint_complete'))
        ephemeral_ok &= d['runtime_state'].get('ephemeral_fields_used_in_classifier') is False
        for c in d['cells']:
            vals[(d['replicate'],) + cellkey(c)] = float(c['response'])
    finite_ok = all(math.isfinite(v) for v in vals.values())
    tol = float(C['replay_relative_tolerance'])
    failures = [x for x in C['diagnostic_cells'] if x['role'] == 'REPLAY_FAILURE']
    allrep = sorted(expected)
    diagnostics = []
    anchors_ok = True
    for cell in C['diagnostic_cells']:
        ck = cellkey(cell)
        rr = [vals[(r,) + ck] for r in allrep]
        sp = maxspread(rr)
        if cell['role'] == 'ANCHOR' and sp >= tol:
            anchors_ok = False
        diagnostics.append({'role': cell['role'], 'h': cell['h'], 'z': cell['z'], 'k': cell['k'], 'max_pairwise_cross_job_rel': sp})
    target_model = C['target_cpu_model']
    target_docs = [d for d in docs if d['runtime_state']['cpu_model'] == target_model]
    target_n = len(target_docs)
    target_variation = False
    target_failure_spreads = []
    for cell in failures:
        ck = cellkey(cell)
        rr = [vals[(d['replicate'],) + ck] for d in target_docs]
        sp = maxspread(rr)
        target_failure_spreads.append({'h': cell['h'], 'z': cell['z'], 'k': cell['k'], 'spread': sp})
        if sp >= tol:
            target_variation = True
    software_keys = sorted({d['runtime_state']['software_control_key'] for d in docs})
    software_constant = len(software_keys) == 1
    min_group_n = int(C['minimum_runtime_group_n'])
    factor_fields = C['factor_hierarchy']
    summaries = {field: factor_summary(target_docs, vals, failures, field, tol, min_group_n) for field in factor_fields}
    invariant_ok = flags_ok and fingerprint_ok and ephemeral_ok and finite_ok and anchors_ok and max_lookup <= float(C['exact_target_binding_tolerance'])
    if not invariant_ok:
        cls = 'NUMERICAL_RUNTIME_STATE_FINGERPRINT_AUDIT_INCONCLUSIVE'
        nxt = 'NO_SCIENTIFIC_PROMOTION_DIAGNOSE_V0_17_INVARIANT_FAILURE'
        selected = None
    elif not software_constant:
        cls = 'NUMERICAL_RUNTIME_STATE_FINGERPRINT_CONFOUNDED_BY_SOFTWARE_CONTROL_VARIATION'
        nxt = 'PROSPECTIVELY_FROZEN_CONTROLLED_SOFTWARE_IMAGE_FACTOR_AUDIT'
        selected = None
    elif target_n < int(C['minimum_target_cpu_model_n']):
        cls = 'NUMERICAL_RUNTIME_STATE_FINGERPRINT_UNDERPOWERED_TARGET_CPU_MODEL'
        nxt = 'PROSPECTIVELY_FROZEN_EXPANDED_RUNTIME_STATE_REPLICATION_AUDIT'
        selected = None
    elif not target_variation:
        cls = 'V016_SAME_CPU_MODEL_VARIATION_NOT_REPRODUCED_IN_V017'
        nxt = 'PROSPECTIVELY_FROZEN_SAME_CPU_MODEL_VARIATION_CONFIRMATION_AUDIT'
        selected = None
    else:
        selected = None
        class_map = {
            'cpu_capability_key': ('CPU_CAPABILITY_RUNTIME_STATE_STRATIFICATION_SUPPORTED', 'PROSPECTIVELY_FROZEN_CONTROLLED_CPU_CAPABILITY_DISPATCH_INTERVENTION_AUDIT'),
            'fpu_control_key': ('FPU_CONTROL_RUNTIME_STATE_STRATIFICATION_SUPPORTED', 'PROSPECTIVELY_FROZEN_CONTROLLED_FPU_STATE_INTERVENTION_AUDIT'),
            'binary_runtime_key': ('BINARY_RUNTIME_STATE_STRATIFICATION_SUPPORTED', 'PROSPECTIVELY_FROZEN_CONTROLLED_BINARY_RUNTIME_ISOLATION_AUDIT'),
            'numpy_runtime_key': ('NUMPY_DISPATCH_RUNTIME_STATE_STRATIFICATION_SUPPORTED', 'PROSPECTIVELY_FROZEN_CONTROLLED_NUMPY_DISPATCH_INTERVENTION_AUDIT'),
            'full_runtime_state_key': ('NUMERICAL_RUNTIME_STATE_STRATIFICATION_SUPPORTED', 'PROSPECTIVELY_FROZEN_CONTROLLED_RUNTIME_STATE_INTERVENTION_AUDIT'),
        }
        for field in factor_fields:
            s = summaries[field]
            if s['repeated_group_count'] >= 2 and s['all_repeated_groups_stable'] and s['between_repeated_groups_separated_on_all_failure_cells']:
                selected = field
                cls, nxt = class_map[field]
                break
        if selected is None:
            full = summaries['full_runtime_state_key']
            same_full_state_nondet = any(
                g['n'] >= min_group_n and any(c['spread'] >= tol for c in g['failure_cells'])
                for g in full['groups']
            )
            if same_full_state_nondet:
                cls = 'RECORDED_NUMERICAL_RUNTIME_STATE_INSUFFICIENT_SAME_STATE_VARIATION'
                nxt = 'PROSPECTIVELY_FROZEN_PROCESS_INITIALIZATION_MEMORY_LAYOUT_AUDIT'
            else:
                cls = 'NUMERICAL_RUNTIME_STATE_FINGERPRINT_UNDERPOWERED_OR_MIXED'
                nxt = 'PROSPECTIVELY_FROZEN_EXPANDED_RUNTIME_STATE_REPLICATION_AUDIT'
    out = {
        'schema': 'LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_DECISION_V0_17',
        'classification': cls, 'effect': '+0/+0', 'diagnostic_cells': diagnostics,
        'target_cpu_model': target_model, 'target_cpu_model_n': target_n,
        'minimum_target_cpu_model_n': int(C['minimum_target_cpu_model_n']),
        'target_failure_spreads': target_failure_spreads, 'target_same_cpu_model_variation_reproduced': target_variation,
        'software_control_signature_count': len(software_keys), 'software_controls_constant': software_constant,
        'factor_hierarchy': factor_fields, 'factor_summaries': summaries, 'selected_runtime_factor': selected,
        'fingerprint_integrity_ok': fingerprint_ok, 'anchor_invariant_ok': anchors_ok, 'finite_ok': finite_ok,
        'max_requested_node_coordinate_rel_mismatch': max_lookup, 'replay_relative_tolerance': tol, 'invariant_ok': invariant_ok,
        'production_h_mutated': False, 'sampling_stepsize_changed': False, 'global_65537_launched': False,
        'covariance_read': False, 'whitening_read': False, 'nuisance_read': False, 'relation_null_read': False,
        'Wm_S3_opened': False, 'science_gate_opened': False,
        'next_stage': nxt, 'token': 'PASS_LAYERB_BETA_NUMERICAL_RUNTIME_STATE_FINGERPRINT_DECISION_V0_17',
    }
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(out['token'], json.dumps({'classification': cls, 'selected_runtime_factor': selected, 'next_stage': nxt, 'target_n': target_n}, sort_keys=True))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--mode', choices=['lane', 'decision'], required=True)
    p.add_argument('--contract', required=True)
    p.add_argument('--replicate')
    p.add_argument('--v12-executor')
    p.add_argument('--jj-script')
    p.add_argument('--baseline')
    p.add_argument('--precision')
    p.add_argument('--inputs', nargs='*', default=[])
    p.add_argument('--out', required=True)
    a = p.parse_args()
    C = json.load(open(a.contract))
    lane(a, C) if a.mode == 'lane' else decision(a, C)


if __name__ == '__main__':
    main()
