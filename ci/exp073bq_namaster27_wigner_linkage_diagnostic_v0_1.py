#!/usr/bin/env python3
from __future__ import annotations
import ctypes, importlib, importlib.metadata, json, os, pathlib, re, subprocess


def run(cmd):
    p=subprocess.run(cmd,text=True,capture_output=True)
    return {'cmd':cmd,'returncode':p.returncode,'stdout':p.stdout[-20000:],'stderr':p.stderr[-8000:]}


def main():
    ver=importlib.metadata.version('pymaster')
    if not (ver=='2.7' or ver.startswith('2.7.')): raise AssertionError(ver)
    ext=importlib.import_module('pymaster._nmtlib')
    ep=pathlib.Path(ext.__file__).resolve()
    out={'experiment':'Exp073BQ','classification':'NONCLASSIFYING_INFRASTRUCTURE_SOURCE_LINKAGE_DIAGNOSTIC','pymaster_version':ver,'extension':str(ep),'authority':False,'scientific_pass_claimed':False,'scientific_readiness_increment':0,'draft_data_readiness_increment':0,'Exp073AQ_preserved_as_FAIL':True,'Exp073BJ_preserved_as_PASS':True}
    cd=ctypes.CDLL(str(ep))
    try:
        addr=ctypes.cast(getattr(cd,'drc3jj'),ctypes.c_void_p).value
        out['extension_drc3jj']={'found':bool(addr),'address_nonzero':bool(addr),'error':None}
    except Exception as e:
        out['extension_drc3jj']={'found':False,'address_nonzero':False,'error':repr(e)}
    out['extension_nm']=run(['nm','-D',str(ep)])
    out['extension_readelf']=run(['readelf','-Ws',str(ep)])
    ldd=run(['ldd',str(ep)]); out['ldd']=ldd
    deps=[]
    for line in ldd['stdout'].splitlines():
        m=re.search(r'=>\s+(\/\S+)',line)
        if m: deps.append(m.group(1))
        else:
            m=re.match(r'\s*(\/\S+)\s+\(',line)
            if m: deps.append(m.group(1))
    dep_records=[]; dep_export=False
    for d in sorted(set(deps)):
        p=pathlib.Path(d)
        if not p.exists(): continue
        rec={'path':d,'nm':run(['nm','-D',d]),'readelf':run(['readelf','-Ws',d])}
        try:
            lib=ctypes.CDLL(d); a=ctypes.cast(getattr(lib,'drc3jj'),ctypes.c_void_p).value
            rec['drc3jj']={'found':bool(a),'address_nonzero':bool(a),'error':None}; dep_export |= bool(a)
        except Exception as e:
            rec['drc3jj']={'found':False,'address_nonzero':False,'error':repr(e)}
        dep_records.append(rec)
    out['dependencies']=dep_records
    prefix=pathlib.Path(os.environ.get('CONDA_PREFIX',ep.parents[2]))
    grep=run(['bash','-lc',f"grep -RIn --binary-files=without-match --include='*.h' --include='*.c' --include='*.cc' --include='*.cpp' --include='*.f' --include='*.f90' --include='*.py' --include='*.pc' --include='*.cmake' 'drc3jj' '{prefix}' 2>/dev/null | head -200"])
    out['installed_text_search']=grep
    source_found=bool(grep['stdout'].strip())
    ext_export=out['extension_drc3jj']['found'] and out['extension_drc3jj']['address_nonzero']
    if ext_export: status='BQ_Q1_EXTENSION_EXPORTS_DRC3JJ'
    elif dep_export: status='BQ_Q2_LINKED_DEPENDENCY_EXPORTS_DRC3JJ'
    elif source_found: status='BQ_Q3_RUNTIME_DYNAMIC_SYMBOL_ABSENT_SOURCE_REFERENCE_FOUND'
    else: status='BQ_Q4_RUNTIME_DYNAMIC_SYMBOL_AND_INSTALLED_SOURCE_REFERENCE_ABSENT'
    out['status']=status
    pathlib.Path('data/derived/g7').mkdir(parents=True,exist_ok=True)
    dst=pathlib.Path('data/derived/g7/exp073bq_wigner_linkage_result_v0_1.json')
    dst.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
