#!/usr/bin/env python3
"""Exp073HJ deterministic post-HB complete native record observation extension.

Apply only after the admitted Exp073HI build-compat transform and the frozen
Exp073HB v0.2 exact-endpoint producer patch. This extension changes diagnostic
observation only: it reads four already-refreshed native background workspace
fields at the accepted terminal endpoint and extends the exact hexadecimal
observation line to the frozen eight-field recorder ABI. It does not serialize
records and does not alter solver evolution.
"""
from pathlib import Path
import hashlib
import sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
P = ROOT / "source/perturbations.c"

HB_SHA256 = "da7c427e383f1e9b83d7ff75ef82784c2fe89d91f9681e21e7805b7f354e7e79"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exact anchor count 1, got {count}")
    return text.replace(old, new, 1)


if sha256(P) != HB_SHA256:
    raise RuntimeError(
        f"source/perturbations.c must be exact HB-patched source {HB_SHA256}, got {sha256(P)}"
    )

p = P.read_text()

old = '''int dsir_c2_diag_commit_terminal(double tau, void *parameters_and_workspace, ErrorMsg error_message) {
  struct perturb_parameters_and_workspace *pppaw = (struct perturb_parameters_and_workspace *)parameters_and_workspace;
  if (dsir_c2_diag_enabled_flag == _FALSE_) return _SUCCESS_;
  class_test(dsir_c2_diag_armed == _FALSE_ || dsir_c2_diag_captured == _FALSE_,error_message,"DSIR C2 exact endpoint raw matter state was not captured");
  class_test(tau != dsir_c2_diag_tau_target || pppaw->k != dsir_c2_diag_k_target,error_message,"DSIR C2 committed endpoint identity mismatch");
  /* %a is exact hexadecimal IEEE-754 text; external frozen recorder owns serialization. */
  printf("DSIR_C2_EXACT_ENDPOINT z=%s tau=%a k=%a delta_m=%a theta_m=%a\\n",
         dsir_c2_diag_z_literal,tau,pppaw->k,dsir_c2_diag_delta_m_raw,dsir_c2_diag_theta_m_raw);
  fflush(stdout);
  dsir_c2_diag_armed = _FALSE_;
  return _SUCCESS_;
}
'''

new = '''int dsir_c2_diag_commit_terminal(double tau, void *parameters_and_workspace, ErrorMsg error_message) {
  struct perturb_parameters_and_workspace *pppaw = (struct perturb_parameters_and_workspace *)parameters_and_workspace;
  struct background *pba = pppaw->pba;
  struct perturb_workspace *ppw = pppaw->ppw;
  if (dsir_c2_diag_enabled_flag == _FALSE_) return _SUCCESS_;
  class_test(dsir_c2_diag_armed == _FALSE_ || dsir_c2_diag_captured == _FALSE_,error_message,"DSIR C2 exact endpoint raw matter state was not captured");
  class_test(tau != dsir_c2_diag_tau_target || pppaw->k != dsir_c2_diag_k_target,error_message,"DSIR C2 committed endpoint identity mismatch");
  /* The accepted-terminal derivative has already refreshed ppw->pvecback at
     this exact tau. Observe those native values directly; do not perform a
     second background lookup or interpolation. %a is exact IEEE-754 text. */
  printf("DSIR_C2_EXACT_ENDPOINT z=%s tau=%a k=%a a=%a H=%a delta_m=%a theta_m=%a rho_idm_iv=%a rho_iv=%a\\n",
         dsir_c2_diag_z_literal,
         tau,
         pppaw->k,
         ppw->pvecback[pba->index_bg_a],
         ppw->pvecback[pba->index_bg_H],
         dsir_c2_diag_delta_m_raw,
         dsir_c2_diag_theta_m_raw,
         ppw->pvecback[pba->index_bg_rho_idm_iv],
         ppw->pvecback[pba->index_bg_rho_iv]);
  fflush(stdout);
  dsir_c2_diag_armed = _FALSE_;
  return _SUCCESS_;
}
'''

p = replace_once(p, old, new, "complete native record diagnostic commit")
P.write_text(p)
print(f"exp073hj_patched_perturbations_sha256={sha256(P)}")
print("EXP073HJ_COMPLETE_NATIVE_RECORD_OBSERVATION_PATCH_APPLIED")
