#!/usr/bin/env python3
"""Exp073HS: gate diagnostic terminal hook to exact overall target interval only."""
from pathlib import Path
import hashlib, sys
ROOT=Path(sys.argv[1] if len(sys.argv)>1 else '.')
P=ROOT/'source/perturbations.c'; E=ROOT/'tools/evolver_ndf15.c'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def once(s,a,b,label):
    n=s.count(a)
    if n!=1: raise RuntimeError(f'{label}: expected 1 anchor, got {n}')
    return s.replace(a,b,1)
p=P.read_text(); e=E.read_text()
p=once(p,
'''int dsir_c2_diag_enabled(void) { return dsir_c2_diag_enabled_flag; }\n\nint dsir_c2_diag_arm_terminal''',
'''int dsir_c2_diag_enabled(void) { return dsir_c2_diag_enabled_flag; }\n\n/* Exp073HS: exact control-flow guard. This is not a tolerance: only the\n   approximation interval whose exact tfinal equals the frozen literal-z\n   target is eligible to execute the diagnostic endpoint hook. */\nint dsir_c2_diag_is_exact_terminal_target(double tau) {\n  return (dsir_c2_diag_enabled_flag == _TRUE_ && tau == dsir_c2_diag_tau_target) ? _TRUE_ : _FALSE_;\n}\n\nint dsir_c2_diag_arm_terminal''','target predicate')
e=once(e,
'''extern int dsir_c2_diag_enabled(void);\nextern int dsir_c2_diag_arm_terminal''',
'''extern int dsir_c2_diag_enabled(void);\nextern int dsir_c2_diag_is_exact_terminal_target(double);\nextern int dsir_c2_diag_arm_terminal''','predicate extern')
e=once(e,
'''    if ((done==_TRUE_) && (dsir_c2_diag_enabled()!=0)) {''',
'''    if ((done==_TRUE_) && (dsir_c2_diag_is_exact_terminal_target(tfinal)!=0)) {''','final interval condition')
P.write_text(p); E.write_text(e)
print('exp073hs_perturbations_sha256='+sha(P))
print('exp073hs_evolver_ndf15_sha256='+sha(E))
print('PASS_EXP073HS_PATCH_APPLIED_EXACTLY_ONCE')
