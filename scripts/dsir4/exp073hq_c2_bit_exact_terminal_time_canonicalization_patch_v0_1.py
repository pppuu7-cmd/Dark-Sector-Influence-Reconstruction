#!/usr/bin/env python3
"""Exp073HQ diagnostic-only bit-exact terminal-time canonicalization.

Apply only after the exact post-HM patch chain. It does not modify integration
state/arithmetic: accepted ynew remains unchanged. Only the opt-in DSIR terminal
observation hook receives the integrator's exact requested tfinal coordinate.
"""
from pathlib import Path
import hashlib, sys

ROOT=Path(sys.argv[1] if len(sys.argv)>1 else '.')
P=ROOT/'tools/evolver_ndf15.c'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def once(s,a,b,label):
    n=s.count(a)
    if n!=1: raise RuntimeError(f'{label}: expected 1 anchor, got {n}')
    return s.replace(a,b,1)

s=P.read_text()
old='''    if ((done==_TRUE_) && (dsir_c2_diag_enabled()!=0)) {\n      class_call(dsir_c2_diag_arm_terminal(tnew,parameters_and_workspace_for_derivs,error_message),\n                 error_message,error_message);\n      class_call((*derivs)(tnew,ynew+1,f0+1,parameters_and_workspace_for_derivs,error_message),\n                 error_message,error_message);\n      class_call(dsir_c2_diag_commit_terminal(tnew,parameters_and_workspace_for_derivs,error_message),\n                 error_message,error_message);\n    }'''
new='''    if ((done==_TRUE_) && (dsir_c2_diag_enabled()!=0)) {\n      /* Exp073HQ: tfinal is the exact requested dsir_tau_end coordinate.\n         Keep the already accepted ynew bit-for-bit; canonicalize only the\n         diagnostic observation-time argument to the exact terminal target. */\n      class_call(dsir_c2_diag_arm_terminal(tfinal,parameters_and_workspace_for_derivs,error_message),\n                 error_message,error_message);\n      class_call((*derivs)(tfinal,ynew+1,f0+1,parameters_and_workspace_for_derivs,error_message),\n                 error_message,error_message);\n      class_call(dsir_c2_diag_commit_terminal(tfinal,parameters_and_workspace_for_derivs,error_message),\n                 error_message,error_message);\n    }'''
s=once(s,old,new,'accepted terminal diagnostic hook')
P.write_text(s)
print('exp073hq_evolver_ndf15_sha256='+sha(P))
print('PASS_EXP073HQ_PATCH_APPLIED_EXACTLY_ONCE')
