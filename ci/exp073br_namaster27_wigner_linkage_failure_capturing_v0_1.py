#!/usr/bin/env python3
from __future__ import annotations
import ctypes, importlib, importlib.metadata, json, os, pathlib, re, subprocess, traceback

OUT = pathlib.Path('data/derived/g7/exp073br_wigner_linkage_failure_capturing_result_v0_1.json')


def shell(cmd):
    try:
        p = subprocess.run(cmd, text=True, capture_output=True, timeout=120)
        return {'ok': True, 'cmd': cmd, 'returncode': p.returncode,
                'stdout': p.stdout[-20000:], 'stderr': p.stderr[-8000:]}
    except Exception as e:
        return {'ok': False, 'cmd': cmd, 'error': repr(e)}


def symbol(path):
    try:
        lib = ctypes.CDLL(str(path))
        addr = ctypes.cast(getattr(lib, 'drc3jj'), ctypes.c_void_p).value
        return {'ok': True, 'found': bool(addr), 'address_nonzero': bool(addr), 'error': None}
    except Exception as e:
        return {'ok': True, 'found': False, 'address_nonzero': False, 'error': repr(e)}


def write(out):
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')


def main():
    out = {
        'experiment': 'Exp073BR',
        'classification': 'NONCLASSIFYING_INFRASTRUCTURE_SOURCE_LINKAGE_DIAGNOSTIC',
        'authority': False,
        'scientific_pass_claimed': False,
        'scientific_readiness_increment': 0,
        'draft_data_readiness_increment': 0,
        'Exp073AQ_preserved_as_FAIL': True,
        'Exp073BJ_preserved_as_PASS': True,
        'probes': {},
        'status': 'BR_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE'
    }
    try:
        try:
            ver = importlib.metadata.version('pymaster')
            out['pymaster_version'] = ver
            out['probes']['version'] = {'ok': True, 'value': ver}
        except Exception as e:
            out['probes']['version'] = {'ok': False, 'error': repr(e)}
            ver = None

        ep = None
        try:
            ext = importlib.import_module('pymaster._nmtlib')
            ep = pathlib.Path(ext.__file__).resolve()
            out['extension'] = str(ep)
            out['probes']['extension_import'] = {'ok': True, 'path': str(ep)}
        except Exception as e:
            out['probes']['extension_import'] = {'ok': False, 'error': repr(e)}

        ext_export = False
        dep_export = False
        ldd_complete = False
        search_complete = False
        source_found = False

        if ep is not None:
            out['probes']['extension_drc3jj'] = symbol(ep)
            ext_export = bool(out['probes']['extension_drc3jj'].get('found'))
            out['probes']['extension_nm'] = shell(['nm', '-D', str(ep)])
            out['probes']['extension_readelf'] = shell(['readelf', '-Ws', str(ep)])
            ldd = shell(['ldd', str(ep)])
            out['probes']['ldd'] = ldd
            ldd_complete = bool(ldd.get('ok') and ldd.get('returncode') == 0)
            deps = []
            if ldd_complete:
                for line in ldd.get('stdout', '').splitlines():
                    m = re.search(r'=>\s+(\/\S+)', line)
                    if m:
                        deps.append(m.group(1))
                    else:
                        m = re.match(r'\s*(\/\S+)\s+\(', line)
                        if m:
                            deps.append(m.group(1))
            records = []
            for d in sorted(set(deps)):
                p = pathlib.Path(d)
                if not p.exists():
                    records.append({'path': d, 'exists': False})
                    continue
                rec = {'path': d, 'exists': True, 'drc3jj': symbol(d),
                       'nm': shell(['nm', '-D', d]), 'readelf': shell(['readelf', '-Ws', d])}
                dep_export = dep_export or bool(rec['drc3jj'].get('found'))
                records.append(rec)
            out['probes']['dependencies'] = records

        try:
            roots = []
            if ep is not None:
                roots.extend([ep.parent, ep.parent.parent])
            for envname in ('CONDA_PREFIX', 'VIRTUAL_ENV'):
                if os.environ.get(envname):
                    roots.append(pathlib.Path(os.environ[envname]))
            roots.append(pathlib.Path(os.sys.prefix))
            uniq = []
            seen = set()
            for r in roots:
                rr = str(pathlib.Path(r).resolve())
                if rr not in seen:
                    seen.add(rr); uniq.append(rr)
            qroots = ' '.join("'" + r.replace("'", "'\\''") + "'" for r in uniq)
            cmd = ['bash', '-lc',
                   "grep -RIn --binary-files=without-match --include='*.h' --include='*.c' --include='*.cc' --include='*.cpp' --include='*.f' --include='*.f90' --include='*.py' --include='*.pc' --include='*.cmake' 'drc3jj' " + qroots + " 2>/dev/null | head -200"]
            sr = shell(cmd)
            out['probes']['installed_text_search'] = sr
            search_complete = bool(sr.get('ok') and sr.get('returncode') in (0, 1))
            source_found = bool(sr.get('stdout', '').strip())
        except Exception as e:
            out['probes']['installed_text_search'] = {'ok': False, 'error': repr(e)}

        essential = (ep is not None and ldd_complete and search_complete)
        if ext_export:
            out['status'] = 'BR_Q1_EXTENSION_EXPORTS_DRC3JJ'
        elif dep_export:
            out['status'] = 'BR_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ'
        elif essential and source_found:
            out['status'] = 'BR_Q3_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND'
        elif essential and not source_found:
            out['status'] = 'BR_Q4_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT'
        else:
            out['status'] = 'BR_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE'
    except Exception as e:
        out['top_level_error'] = repr(e)
        out['top_level_traceback'] = traceback.format_exc()[-12000:]
        out['status'] = 'BR_Q5_PARTIAL_DIAGNOSTIC_INCOMPLETE'
    finally:
        write(out)
        print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
