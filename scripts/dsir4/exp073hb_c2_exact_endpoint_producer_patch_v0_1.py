#!/usr/bin/env python3
"""Exp073HB deterministic diagnostic-only exact-endpoint producer patcher.

Applies only after the workflow has fail-closed on the pinned upstream Git
commit/blob identities. The patch is opt-in via DSIR_C2_EXACT_Z and creates no
C2 packet itself.
"""
from pathlib import Path
import hashlib
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
P = ROOT / "source/perturbations.c"
E = ROOT / "tools/evolver_ndf15.c"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def replace_once(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"{label}: expected exact anchor count 1, got {n}")
    return text.replace(old, new, 1)

p = P.read_text()
e = E.read_text()

p = replace_once(
    p,
    '#include "perturbations.h"\n',
    '''#include "perturbations.h"\n#include <stdlib.h>\n#include <string.h>\n#include <errno.h>\n\n/* DSIR Exp073HB diagnostic-only exact-endpoint observation state.\n   Ordinary CLASS behavior is unchanged unless DSIR_C2_EXACT_Z is set. */\nstatic int dsir_c2_diag_enabled_flag = _FALSE_;\nstatic int dsir_c2_diag_armed = _FALSE_;\nstatic int dsir_c2_diag_captured = _FALSE_;\nstatic double dsir_c2_diag_tau_target = 0.;\nstatic double dsir_c2_diag_k_target = 0.;\nstatic double dsir_c2_diag_delta_m_raw = 0.;\nstatic double dsir_c2_diag_theta_m_raw = 0.;\nstatic const char * dsir_c2_diag_z_literal = NULL;\n\nstatic int dsir_c2_diag_parse_literal_z(const char *s, double *z, ErrorMsg error_message) {\n  static const char * allowed[] = {"0.295","0.51","0.706","0.934","1.317","1.491","2.33"};\n  int i, ok = _FALSE_;\n  char *end = NULL;\n  for (i=0; i<7; i++) if (strcmp(s,allowed[i]) == 0) ok = _TRUE_;\n  class_test(ok == _FALSE_,error_message,"DSIR C2 z literal is not in the frozen request set: %s",s);\n  errno = 0;\n  *z = strtod(s,&end);\n  class_test(errno != 0 || end == s || *end != '\\0',error_message,"DSIR C2 invalid literal z: %s",s);\n  return _SUCCESS_;\n}\n\nstatic int dsir_c2_diag_prepare(struct background *pba, struct perturbs *ppt, int index_md, int index_k, double k, double *tau_end, ErrorMsg error_message) {\n  const char *ztext = getenv("DSIR_C2_EXACT_Z");\n  const char *omp = getenv("OMP_NUM_THREADS");\n  double z = 0.;\n  int native_index;\n  dsir_c2_diag_enabled_flag = _FALSE_;\n  dsir_c2_diag_armed = _FALSE_;\n  dsir_c2_diag_captured = _FALSE_;\n  if (ztext == NULL || *ztext == '\\0') return _SUCCESS_;\n  class_test(omp == NULL || strcmp(omp,"1") != 0,error_message,"DSIR C2 diagnostic requires OMP_NUM_THREADS=1");\n  class_test(ppt->k_output_values_num != 1,error_message,"DSIR C2 diagnostic requires exactly one native k_output_values request");\n  native_index = ppt->index_k_output_values[index_md*ppt->k_output_values_num];\n  if (index_k != native_index) return _SUCCESS_;\n  class_test(ppt->has_source_delta_m != _TRUE_ || ppt->has_source_theta_m != _TRUE_,error_message,"DSIR C2 diagnostic requires native delta_m and theta_m sources enabled");\n  class_call(dsir_c2_diag_parse_literal_z(ztext,&z,error_message),error_message,error_message);\n  class_call(background_tau_of_z(pba,z,&dsir_c2_diag_tau_target),pba->error_message,error_message);\n  dsir_c2_diag_z_literal = ztext;\n  dsir_c2_diag_k_target = k;\n  *tau_end = dsir_c2_diag_tau_target;\n  dsir_c2_diag_enabled_flag = _TRUE_;\n  return _SUCCESS_;\n}\n\nint dsir_c2_diag_enabled(void) { return dsir_c2_diag_enabled_flag; }\n\nint dsir_c2_diag_arm_terminal(double tau, void *parameters_and_workspace, ErrorMsg error_message) {\n  struct perturb_parameters_and_workspace *pppaw = (struct perturb_parameters_and_workspace *)parameters_and_workspace;\n  if (dsir_c2_diag_enabled_flag == _FALSE_) return _SUCCESS_;\n  class_test(tau != dsir_c2_diag_tau_target,error_message,"DSIR C2 terminal tau is not the exact background_tau_of_z endpoint");\n  class_test(pppaw->k != dsir_c2_diag_k_target,error_message,"DSIR C2 terminal k is not the native k_output_values mode");\n  dsir_c2_diag_armed = _TRUE_;\n  dsir_c2_diag_captured = _FALSE_;\n  return _SUCCESS_;\n}\n\nint dsir_c2_diag_commit_terminal(double tau, void *parameters_and_workspace, ErrorMsg error_message) {\n  struct perturb_parameters_and_workspace *pppaw = (struct perturb_parameters_and_workspace *)parameters_and_workspace;\n  if (dsir_c2_diag_enabled_flag == _FALSE_) return _SUCCESS_;\n  class_test(dsir_c2_diag_armed == _FALSE_ || dsir_c2_diag_captured == _FALSE_,error_message,"DSIR C2 exact endpoint raw matter state was not captured");\n  class_test(tau != dsir_c2_diag_tau_target || pppaw->k != dsir_c2_diag_k_target,error_message,"DSIR C2 committed endpoint identity mismatch");\n  /* %a is exact hexadecimal IEEE-754 text; external frozen recorder owns serialization. */\n  printf("DSIR_C2_EXACT_ENDPOINT z=%s tau=%a k=%a delta_m=%a theta_m=%a\\n",\n         dsir_c2_diag_z_literal,tau,pppaw->k,dsir_c2_diag_delta_m_raw,dsir_c2_diag_theta_m_raw);\n  fflush(stdout);\n  dsir_c2_diag_armed = _FALSE_;\n  return _SUCCESS_;\n}\n''',
    "perturbations include/diagnostic state",
)

p = replace_once(
    p,
    '''    if ((ppt->has_source_delta_m == _TRUE_) || (ppt->has_source_theta_m == _TRUE_))\n      ppw->theta_m = rho_plus_p_theta_m/rho_plus_p_m;\n\n    /* could include Lambda contribution to rho_tot (not done to match CMBFAST/CAMB definition) */''',
    '''    if ((ppt->has_source_delta_m == _TRUE_) || (ppt->has_source_theta_m == _TRUE_))\n      ppw->theta_m = rho_plus_p_theta_m/rho_plus_p_m;\n\n    /* DSIR C2: capture only the native current-gauge totals, before the\n       downstream gauge-invariant delta_m transformation in perturb_einstein. */\n    if (dsir_c2_diag_armed == _TRUE_) {\n      dsir_c2_diag_delta_m_raw = ppw->delta_m;\n      dsir_c2_diag_theta_m_raw = ppw->theta_m;\n      dsir_c2_diag_captured = _TRUE_;\n    }\n\n    /* could include Lambda contribution to rho_tot (not done to match CMBFAST/CAMB definition) */''',
    "pre-transform raw matter capture",
)

p = replace_once(
    p,
    '''  /* conformal time */\n  double tau,tau_lower,tau_upper,tau_mid;''',
    '''  /* conformal time */\n  double tau,tau_lower,tau_upper,tau_mid;\n  double dsir_tau_end;''',
    "diagnostic tau local",
)

p = replace_once(
    p,
    '''  tau = tau_mid;\n\n  /** - find the number of intervals over which approximation scheme is constant */''',
    '''  tau = tau_mid;\n\n  /* Ordinary path uses the unchanged final source-sampling time. In opt-in\n     C2 diagnostic mode only the one native k_output_values mode terminates\n     at the literal-z background_tau_of_z endpoint. */\n  dsir_tau_end = ppt->tau_sampling[tau_actual_size-1];\n  class_call(dsir_c2_diag_prepare(pba,ppt,index_md,index_k,k,&dsir_tau_end,ppt->error_message),\n             ppt->error_message,ppt->error_message);\n  class_test(dsir_tau_end <= tau,ppt->error_message,"DSIR C2 exact endpoint is not later than perturbation initial time");\n\n  /** - find the number of intervals over which approximation scheme is constant */''',
    "literal-z endpoint prepare",
)

old_end = 'ppt->tau_sampling[tau_actual_size-1]'
if p.count(old_end) < 3:
    raise RuntimeError(f"unexpected tau-end anchor count after insertion: {p.count(old_end)}")
pos = p.index('class_call(perturb_find_approximation_number')
head, tail = p[:pos], p[pos:]
tail = tail.replace(old_end, 'dsir_tau_end', 2)
p = head + tail

e = replace_once(
    e,
    '#include "evolver_ndf15.h"\n',
    '''#include "evolver_ndf15.h"\n\n/* Exp073HB diagnostic hook implemented in perturbations.c. */\nextern int dsir_c2_diag_enabled(void);\nextern int dsir_c2_diag_arm_terminal(double, void *, ErrorMsg);\nextern int dsir_c2_diag_commit_terminal(double, void *, ErrorMsg);\n''',
    "evolver extern hook declarations",
)

e = replace_once(
    e,
    '''    /** Output **/\n    while ((next<tres)&&(tdir * (tnew - t_vec[next]) >= 0.0)){''',
    '''    /* Exp073HB: only after a successful accepted terminal NDF15 step,\n       arm the raw current-gauge matter capture and re-evaluate derivatives\n       on the accepted ynew at tnew=tfinal. This bypasses interp_from_dif. */\n    if ((done==_TRUE_) && (dsir_c2_diag_enabled()!=0)) {\n      class_call(dsir_c2_diag_arm_terminal(tnew,parameters_and_workspace_for_derivs,error_message),\n                 error_message,error_message);\n      class_call((*derivs)(tnew,ynew+1,f0+1,parameters_and_workspace_for_derivs,error_message),\n                 error_message,error_message);\n      class_call(dsir_c2_diag_commit_terminal(tnew,parameters_and_workspace_for_derivs,error_message),\n                 error_message,error_message);\n    }\n\n    /** Output **/\n    while ((next<tres)&&(tdir * (tnew - t_vec[next]) >= 0.0)){''',
    "accepted terminal ynew hook",
)

P.write_text(p)
E.write_text(e)
print(f"patched_perturbations_sha256={sha256(P)}")
print(f"patched_evolver_ndf15_sha256={sha256(E)}")
print("EXP073HB_PATCH_APPLIED")
