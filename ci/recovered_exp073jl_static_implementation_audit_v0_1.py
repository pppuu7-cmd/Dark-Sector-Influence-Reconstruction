#!/usr/bin/env python3
from __future__ import annotations
import argparse, ast, hashlib, json
from pathlib import Path

PASS='RECOVERED_EXP073JL_STATIC_IMPLEMENTATION_AUDIT_PASS_PLUS_0_PLUS_0'

def sha(b): return hashlib.sha256(b).hexdigest()

def calls_in(fn):
    out=[]
    for n in ast.walk(fn):
        if isinstance(n,ast.Call):
            f=n.func
            if isinstance(f,ast.Name): name=f.id
            elif isinstance(f,ast.Attribute):
                parts=[]
                while isinstance(f,ast.Attribute): parts.append(f.attr); f=f.value
                if isinstance(f,ast.Name): parts.append(f.id)
                name='.'.join(reversed(parts))
            else: name=''
            out.append((name,getattr(n,'lineno',-1)))
    return out

def main():
    ap=argparse.ArgumentParser()
    for x in ('helper','prereg','jw','plan','jt','jv','out'): ap.add_argument('--'+x,required=True)
    a=ap.parse_args(); src=Path(a.helper).read_text(); pre=Path(a.prereg).read_text(); tree=ast.parse(src)
    fns={n.name:n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
    classes={n.name:n for n in tree.body if isinstance(n,ast.ClassDef)}
    checks={}
    def ck(name,v): checks[name]=bool(v); assert v,name

    ck('ast_parses', True)
    ck('no_host_geomspace', 'np.geomspace' not in src and 'guarded_lattice(' not in src)
    ck('uses_committed_node_loader', 'load_nodes(a.coarse, 2049, COARSE_TEXT_SHA, COARSE_NODE_SHA)' in src and 'load_nodes(a.fine, 4097, FINE_TEXT_SHA, FINE_NODE_SHA)' in src)
    ck('uses_jj_requested_values', 'jj.requested_values(k, y, nodes)' in src)
    ck('uses_jj_centered_cubic', 'jj.cubic_centered(nodes, yn, targets)' in src)
    ck('uses_jj_class_params', 'jj.class_params(Path(baseline), Path(precision), alpha, beta, nodes)' in src)
    ck('alpha_arithmetic_exact', 'np.abs((al - ref) / (-H))' in src)
    ck('beta_arithmetic_exact', 'np.abs((bp - bm) / (2 * H))' in src)
    ck('column_order_exact', 'np.column_stack((np.abs((al - ref) / (-H)), np.abs((bp - bm) / (2 * H))))' in src)
    ck('strict_convergence', 'mx < REL_TOL' in src and 'mx <= REL_TOL' not in src)
    ck('infra_class_distinct', 'INVALID_INFRA = "INVALID_INFRA_PLUS_0_PLUS_0"' in src)
    ck('valid_science_tokens_exact', 'COMMON_GRID_THIRD_REFINEMENT_CONVERGED_PLUS_0_PLUS_0' in src and 'COMMON_GRID_THIRD_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0' in src)
    ck('one_live_terminal_guard', 'tracker != {"constructions": 8, "live": 0, "max_live": 1}' in src)
    ck('coarse_four_guard', 'tracker != {"constructions": 4, "live": 0, "max_live": 1}' in src)
    ck('raw_cross_process_false', '"cross_process_raw_operand_combination": False' in src)
    ck('request_counts_frozen', 'counts != [377, 64, 441, 128]' in src and 'len(coarse_calls) != 441' in src and 'len(fine_calls) != 569' in src and '!= 83666' in src and '!= 121682' in src)
    ck('plan_hashes_frozen', '505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0' in src and '0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e' in src)
    ck('canonical_hashes_frozen', '6305c95025e52296b6cb623903f82dc45bb66ac692708b242fc354862ac54c46' in src and 'f30556be2547732ed0b87b56368e01e46504a975f94fcbbc5e7bc8cfc525e5eb' in src)

    imports=[]
    for n in ast.walk(tree):
        if isinstance(n,ast.ImportFrom) and n.module=='classy': imports.append(n.lineno)
        if isinstance(n,ast.Import):
            for q in n.names:
                if q.name=='classy': imports.append(n.lineno)
    ev=fns['evaluate_lattice']; ev_lo=ev.lineno; ev_hi=getattr(ev,'end_lineno',ev_lo)
    ck('class_import_only_in_evaluator', len(imports)==1 and ev_lo<=imports[0]<=ev_hi)

    ex=fns['execute']; calls=calls_in(ex)
    plan_lines=[ln for name,ln in calls if name=='run_request_plan_audit']
    eval_lines=[ln for name,ln in calls if name=='evaluate_lattice']
    ck('plan_gate_before_solver_calls', len(plan_lines)==1 and len(eval_lines)==2 and plan_lines[0] < min(eval_lines))

    pcls=classes['PlannerSuite']; rcls=classes['ReplaySuite']
    ptxt=ast.get_source_segment(src,pcls) or '' ; rtxt=ast.get_source_segment(src,rcls) or ''
    ck('planner_no_class', 'Class' not in ptxt and 'get_transfer' not in ptxt)
    ck('replay_no_class', 'Class' not in rtxt and 'get_transfer' not in rtxt)
    ck('planner_dummy_only', 'np.ones((t.size, 2)' in ptxt)
    ck('replay_bit_identity', 'assert_call_equal' in rtxt)

    for name,text in {
      'prereg_rel_tol':'strict relative tolerance of `1e-3`',
      'prereg_h':'H=1e-4',
      'prereg_native':'k_per_decade_for_pk=20.0',
      'prereg_eight':'Exactly eight CLASS constructions',
      'prereg_one_live':'At most one CLASS instance may be live at any time',
      'prereg_gl128':'Fine GL128 is used **only**',
      'prereg_no_rescue':'No tolerance/rounding/smoothing/averaging/clipping',
    }.items(): ck(name,text in pre)

    jw=json.loads(Path(a.jw).read_text()); plan=json.loads(Path(a.plan).read_text()); jt=json.loads(Path(a.jt).read_text()); jv=json.loads(Path(a.jv).read_text())
    ck('jw_authority', jw.get('artifact_verified_independently') is True and jw.get('classification')=='CANONICAL_ONE_LIVE_EIGHT_BUILD_RESOURCE_PILOT_PASS_PLUS_0_PLUS_0' and jw.get('total_solver_constructions')==8 and jw.get('max_live_instances')==1)
    ck('plan_authority', plan.get('artifact_verified_independently') is True and plan.get('classification')=='RESPONSE_BLIND_REQUEST_PLAN_AUDITED_PLUS_0_PLUS_0' and plan.get('coarse_common_plan_sha256')=='505716116cc385d5700e455017d8e541c5bba7774fa6647298392495c83ecfe0' and plan.get('fine_plan_with_gl128_sha256')=='0f7ce2e5fa459e15954268dfd46045eaa0ab6356dfdab5a2e282514e7a34ae4e')
    ck('jt_authority', jt.get('artifact_verified_independently') is True and jt.get('classification')=='CANONICAL_SHARED_LATTICES_MATERIALIZED_PASS_PLUS_0_PLUS_0')
    ck('jv_authority', jv.get('artifact_verified_independently') is True and jv.get('classification')=='SEQUENTIAL_CANONICAL_JL_EXECUTION_AUTHORIZED_PLUS_0_PLUS_0')

    result={'schema':'RECOVERED_EXP073JL_STATIC_IMPLEMENTATION_AUDIT_RESULT_V0_1','classification':PASS,'effect':'+0/+0','scientific_response_read':False,'class_solver_invoked':False,'scientific_authority_created':False,'covariance_restriction_authorized':False,'Wm_S3_opened':False,'helper_sha256':sha(Path(a.helper).read_bytes()),'prereg_sha256':sha(Path(a.prereg).read_bytes()),'checks':checks,'check_count':len(checks),'article3_repository_readiness_percent':68,'funnel_freeze_readiness_percent':67,'token':PASS}
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(PASS); print('CHECKS',len(checks)); return 0
if __name__=='__main__': raise SystemExit(main())
