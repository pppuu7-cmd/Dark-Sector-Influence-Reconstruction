#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
C3_PIN = "4c87916aab5ca124a68f1dd16f31846fc13d1829"
C5_PIN = "16d9c4e9f85751e30efd0a53b177941713078904"
ACT_PIN = "6302c30d9e70f8e4ff2d4a84a9977b4471705179"
EXP073A_RUN = 33032781761
EXP073A_ARTIFACT = 9630897385
EXP073A_DIGEST = "sha256:0f2212d691c38c3e953d2a0d823b498a5557b9485fc759079719000cdc48cb25"
EXP073A_JSON_SHA = "a8bbafa971283cadf9ff27a27af4d0c4e3042bc0aec590d690142d39c919abb2"
EXP073A_HEAD = "03c9d0281a6ea780d29c6fb4a689dbd55e51fdf5"
EXP073A_STATUS = "INELIGIBLE_GR_REFERENCE_LINEAR_ROUTE_EXP073A"
FRONT_ZMIN = 0.0087345857837422
FRONT_KMAX = 4.818261097432861
FEASIBLE = "FEASIBLE_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B"
GAP = "GAP_EXISTING_STACK_NONLINEAR_MATTER_WEYL_ROUTE_EXP073B"
FAIL = "FAIL_EXP073B_REPRODUCTION_OR_PROVENANCE"


def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for c in iter(lambda:f.read(1<<20),b''): h.update(c)
    return h.hexdigest()

def head(p: Path) -> str:
    return subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],text=True).strip()

def text(p: Path) -> str:
    return p.read_text(errors='replace')

def find_text_files(root: Path):
    for p in root.rglob('*'):
        if p.is_file() and p.stat().st_size < 2_000_000 and p.suffix.lower() in {'.py','.pyx','.pxd','.c','.h','.f90','.f','.F90'.lower(),'.md','.ini','.yaml','.yml','.txt'}:
            yield p

def grep_inventory(root: Path, terms: tuple[str,...], cap=80):
    out=[]
    for p in find_text_files(root):
        try: s=text(p)
        except Exception: continue
        low=s.lower()
        hits=[t for t in terms if t.lower() in low]
        if hits:
            out.append({'path':str(p.relative_to(root)),'terms':hits})
            if len(out)>=cap: break
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--c3-root',required=True); ap.add_argument('--c5-root',required=True); ap.add_argument('--act-root',required=True)
    ap.add_argument('--parent-json',required=True); ap.add_argument('--parent-meta',required=True); ap.add_argument('--output',required=True)
    a=ap.parse_args(); c3=Path(a.c3_root); c5=Path(a.c5_root); act=Path(a.act_root)
    pj=Path(a.parent_json); pm=Path(a.parent_meta); out=Path(a.output)
    parent=json.loads(pj.read_text()); meta=json.loads(pm.read_text()); wr=meta.get('workflow_run') or {}
    pchecks={
      'artifact_id':meta.get('id')==EXP073A_ARTIFACT,'artifact_digest':meta.get('digest')==EXP073A_DIGEST,
      'run':wr.get('id')==EXP073A_RUN,'head':wr.get('head_sha')==EXP073A_HEAD,
      'json_sha':sha256(pj)==EXP073A_JSON_SHA,'status':parent.get('status')==EXP073A_STATUS,
      'hard_controls':bool(parent.get('hard_controls')) and all(v is True for v in parent['hard_controls'].values()),
      'routes_zero':all(parent.get('routes',{}).get(str(t),{}).get('retained_dimension')==0 for t in (0.5,1.0,2.0)),
    }
    pins={'C3':head(c3),'C5':head(c5),'ACT':head(act)}
    pinpass=pins=={'C3':C3_PIN,'C5':C5_PIN,'ACT':ACT_PIN}

    dsir_src=text(ROOT/'src/dsir/act_unwise_projection.py')
    f1_checks={
      'three_independent_args':all(x in dsir_src for x in ('pk_weyl_weyl','pk_weyl_matter','pk_matter_matter')),
      'separate_evaluations':all(x in dsir_src for x in ('p_ww =','p_wm =','p_mm =')),
      'explicit_no_poisson_statement':'No Poisson relation is' in dsir_src,
    }
    F1=all(f1_checks.values())

    act_free=act/'unWISExLens_lklh/theory_modules/unWISExkappa_model_freeCLEFT.py'
    acts=text(act_free)
    f2_checks={
      'accepts_three_nonlinear_blocks':all(x in acts for x in ('pk_weyl_weyl','pk_weyl_dnonu','pk_dnonu_dnonu')),
      'cleft_wm_uses_matter2weyl_factor':'cleft_pk_evals_weyl_dnonu' in acts and 'matter2weyl_factor * cleft_interpolations_dtot_dnonu' in acts,
      'matter2weyl_factor_defined':'matter2weyl_factor =' in acts,
    }
    F2=all(f2_checks.values())

    c3_cert=text(ROOT/'ci/c3_gdm_native_grid_physical_power_provider_v0_1.py')
    c3_linear={'uses_pk_lin':'pk_lin(' in c3_cert,'uses_phi_psi':all(x in c3_cert for x in ('["phi"]','["psi"]')),'constructs_weyl_from_linear_transfer':'weyl = 0.5 * k**2 * (ph + ps)' in c3_cert}
    c3_inv=grep_inventory(c3,('non linear','nonlinear','halofit','hmcode','weyl','phi','psi'))
    # The frozen question requires an explicit model-specific nonlinear source for all three independent blocks.
    # The certified C3 provider is linear; generic CLASS nonlinear matter modules do not establish nonlinear Weyl auto/cross physics for GDM.
    c3_complete_nonlinear_three_block=False
    F3=c3_complete_nonlinear_three_block

    c5_cert=text(ROOT/'ci/c5_q3_unmodified_upstream_provider_certification_v0_1.py')
    c5_linear={'nonlinear_false':'nonlinear=False' in c5_cert,'nonlinear_none':'NonLinear_none' in c5_cert,'three_linear_var_pairs':all(x in c5_cert for x in ('("delta_nonu","delta_nonu")','("Weyl","delta_nonu")','("Weyl","Weyl")'))}
    c5_inv=grep_inventory(c5,('nonlinear','halofit','hmcode','weyl','designer','eftb0'))
    # Current C5 certification explicitly disables nonlinear correction. Generic CAMB nonlinear correction is not a designer-f(R) independent Weyl provider under the frozen forbidden-shortcut rule.
    c5_complete_nonlinear_three_block=False
    F4=c5_complete_nonlinear_three_block

    f5_detail={
      'required_z_min':FRONT_ZMIN,'required_k_max_Mpc^-1':FRONT_KMAX,
      'current_C3_cert_k_max_Mpc^-1':0.067,'current_C3_cert_z_min':0.295,
      'current_C5_cert_k_max_Mpc^-1':0.20,'current_C5_internal_kmax_Mpc^-1':0.30,'current_C5_cert_z_min':0.0,
      'complete_candidate_exists':False,
    }
    F5=False
    # Projector keeps signed cross semantics, but there is no complete nonlinear provider candidate to certify independence/sign behavior.
    f6_detail={'projector_signed_independent_cross_capable':F1,'complete_nonlinear_candidate_exists':False}
    F6=False
    F7=bool(pinpass and act_free.is_file() and (ROOT/'ci/c3_gdm_native_grid_physical_power_provider_v0_1.py').is_file() and (ROOT/'ci/c5_q3_unmodified_upstream_provider_certification_v0_1.py').is_file())
    F8=True

    audit_trust=bool(all(pchecks.values()) and pinpass and F1 and F2 and F7 and F8)
    if not audit_trust: status=FAIL
    elif F3 and F4 and F5 and F6: status=FEASIBLE
    else: status=GAP
    result={
      'experiment':'Exp073B','date':'2026-08-27','status':status,
      'parent_binding':{'checks':pchecks,'pass':all(pchecks.values())},'pins':pins,'pin_pass':pinpass,
      'tests':{
        'F1_projector_separability':{'pass':F1,'checks':f1_checks,'source':'src/dsir/act_unwise_projection.py'},
        'F2_upstream_nonlinear_CLEFT_scope':{'pass':F2,'checks':f2_checks,'source':str(act_free.relative_to(act)),'interpretation':'Upstream accepts independent nonlinear WW/Wm/mm inputs, while its CLEFT Wm correction uses an explicit matter2weyl_factor; CLEFT is therefore not evidence for an independent nonlinear MG Weyl provider.'},
        'F3_C3_GDM_nonlinear_provider':{'pass':F3,'certified_provider':c3_linear,'inventory':c3_inv,'interpretation':'Current certified C3 route is linear pk_lin plus linear phi/psi. Generic nonlinear matter modules in CLASS do not constitute model-specific independent nonlinear P_Wm/P_WW for GDM.'},
        'F4_C5_designer_fR_nonlinear_provider':{'pass':F4,'certified_provider':c5_linear,'inventory':c5_inv,'interpretation':'Current certified C5 q=3 route explicitly uses nonlinear=False/NonLinear_none. No certified designer-f(R) independent nonlinear WW/Wm/mm provider exists in the pinned stack.'},
        'F5_support_plausibility':{'pass':F5,'detail':f5_detail},
        'F6_independence_sign_semantics':{'pass':F6,'detail':f6_detail},
        'F7_provenance_completeness':{'pass':F7},'F8_no_downstream_leakage':{'pass':F8},
      },
      'audit_trustworthy':audit_trust,
      'scientific_interpretation':'Existing projector architecture is suitable for independent nonlinear blocks, but the pinned C3 and C5 provider stack lacks certified physically justified independent nonlinear matter/Weyl auto/cross predictions over the Exp072C frontier. A new provider/calibrated nonlinear theory ingredient is required before G7 can proceed.',
      'controls':{'covariance_read':False,'whitener_read':False,'nuisance_SVD_read':False,'G7_relation_read':False,'G8_read':False,'provider_numerical_extension_run':False},
      'gate_state':{'G7':'OPEN','G8':'OPEN','G9':'OPEN'},
    }
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n'); print(json.dumps(result,indent=2,allow_nan=False))

if __name__=='__main__': main()
