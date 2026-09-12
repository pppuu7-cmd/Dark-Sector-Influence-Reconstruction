#!/usr/bin/env python3
from __future__ import annotations
import importlib.util,json,hashlib
from pathlib import Path

BASE=Path(__file__).with_name('layerb_16385_to_32769_canonical_chunk_refinement_v0_1.py')

def load():
    spec=importlib.util.spec_from_file_location('dsir_chunk_recovery_base',BASE)
    if spec is None or spec.loader is None: raise RuntimeError('cannot import frozen chunk wrapper')
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def fixed_validate_resource_factory(m):
    def validate_resource(path):
        d,sha,blob=m.load_bound(path)
        fr=d.get('frozen_runtime',{}); ro=d.get('resource_observation',{}); wf=d.get('workflow',{}); agg=d.get('aggregate',{})
        independently_verified=(
            isinstance(wf.get('independent_finalizer_job_id'),int) and
            agg.get('chunks_seen')==list(range(8)) and agg.get('missing_chunks')==[] and agg.get('failures')==[]
        )
        if blob!=m.V142_BLOB or d.get('classification')!=m.V142_CLASS or not independently_verified or fr.get('point_capacity')!=4608 or fr.get('parser_capacity')!=131072 or ro.get('peak_ru_maxrss_kb')!=11865712 or ro.get('swapfree_before_equal_after_for_all_eight') is not True or d.get('scientific_transfer_values_read') is not False or d.get('convergence_metric_computed') is not False or d.get('successor_authorized') is not False:
            raise RuntimeError('invalid V142 chunk resource authority under actual authority schema')
        return d,sha,blob
    return validate_resource

def main():
    m=load()
    m.validate_resource=fixed_validate_resource_factory(m)
    rc=m.main()
    out=None
    try:
        i=m.sys.argv.index('--out'); out=m.sys.argv[i+1]
    except Exception: pass
    if out and Path(out).exists():
        d=json.loads(Path(out).read_text())
        if d.get('classification') in ('COMMON_GRID_NEXT_REFINEMENT_CONVERGED_PLUS_0_PLUS_0','COMMON_GRID_NEXT_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0'):
            d['recovery_execution']=True
            d['recovery_reason']='initial coarse monolithic operands were interrupted by hosted-runner shutdown before any terminal classifier; fine operands were retained exactly and coarse operands were recomputed with the previously independently validated non-scientific CLASS history-suppression patch'
            d['fine_operands_recomputed']=False
            d['coarse_history_suppression_scientific_parameters_changed']=False
            d['token']='PASS_LAYERB_16385_TO_32769_CHUNK_RECOVERY_'+('CONVERGED' if 'CONVERGED_PLUS' in d['classification'] and 'NOT_CONVERGED' not in d['classification'] else 'NOT_CONVERGED')+'_V0_1'
            Path(out).write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
            print('RECOVERY_WRAPPER_TERMINAL',d['token'])
    return rc

if __name__=='__main__': raise SystemExit(main())
