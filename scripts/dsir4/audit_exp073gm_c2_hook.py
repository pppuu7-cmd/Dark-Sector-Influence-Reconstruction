#!/usr/bin/env python3
from pathlib import Path
import hashlib, re, subprocess, sys, tempfile

EXPECTED_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
PASS = "PASS_EXP073GM_C2_IDE_OBSERVATION_ONLY_HOOK_STATIC_AUDIT_V0_1"

if len(sys.argv) != 4:
    raise SystemExit("usage: audit_exp073gm_c2_hook.py <class_iv_checkout> <reported_commit> <transformer>")
root = Path(sys.argv[1]); reported = sys.argv[2].strip(); transformer = Path(sys.argv[3])
if reported != EXPECTED_COMMIT:
    raise SystemExit(f"FAIL commit identity {reported} != {EXPECTED_COMMIT}")
src = root / "source" / "perturbations.c"
raw = src.read_text(encoding="utf-8")

with tempfile.TemporaryDirectory() as td:
    out = Path(td) / "perturbations.c"
    subprocess.run([sys.executable, str(transformer), str(src), str(out)], check=True)
    patched = out.read_text(encoding="utf-8")

include_block = '#ifdef DSIR_C2_PRETRANSFORM_HOOK\n#include "dsir_c2_pretransform_hook.h"\n#endif\n'
call_block = (
    '#ifdef DSIR_C2_PRETRANSFORM_HOOK\n'
    '  dsir_c2_pretransform_observe(\n'
    '      tau,\n'
    '      k,\n'
    '      a,\n'
    '      ppw->pvecback[pba->index_bg_H],\n'
    '      ppw->delta_m,\n'
    '      ppw->theta_m,\n'
    '      ppw->pvecback[pba->index_bg_rho_idm_iv],\n'
    '      ppw->pvecback[pba->index_bg_rho_iv]);\n'
    '#endif\n'
)
if patched.count(include_block) != 1 or patched.count(call_block) != 1:
    raise SystemExit("FAIL diagnostic block multiplicity")
restored = patched.replace(include_block, "", 1).replace('\n' + call_block, "", 1)
if restored != raw:
    raise SystemExit("FAIL source not byte-equivalent modulo exact diagnostic regions")

m = re.search(r"int\s+perturb_einstein\s*\([^)]*\)\s*\{(?P<body>.*?)(?=\nint\s+perturb_total_stress_energy\s*\()", patched, re.S)
if not m:
    raise SystemExit("FAIL perturb_einstein isolation")
e = m.group("body")
helper = re.search(r"class_call\(\s*perturb_total_stress_energy\s*\(.*?\)\s*,.*?\);", e, re.S)
if not helper:
    raise SystemExit("FAIL helper class_call missing")
hook_pos = e.find("dsir_c2_pretransform_observe(")
if hook_pos < 0 or hook_pos <= helper.end():
    raise SystemExit("FAIL hook is not after helper return")
corr = re.search(r"ppw->delta_m\s*\+=\s*3\s*\.\s*\*\s*ppw->pvecback\s*\[\s*pba->index_bg_a\s*\]\s*\*\s*ppw->pvecback\s*\[\s*pba->index_bg_H\s*\]\s*\*\s*ppw->theta_m\s*/\s*k2\s*;", e)
if not corr or hook_pos >= corr.start():
    raise SystemExit("FAIL hook is not before native gauge correction")

# Exact call_block equality above freezes the complete ordered argument list.
# Only scan that exact block for mutation/forbidden downstream operations.
for forbidden in ['++','--','+=','-=','*=','/=','index_tp_delta_m','background_at_tau','thermodynamics_at_z','memcpy','memset','malloc(','realloc(','free(']:
    if forbidden in call_block:
        raise SystemExit(f"FAIL forbidden hook token {forbidden}")

# Reconfirm pinned helper's pretransform assignments themselves were not changed.
for token in ['ppw->delta_m = delta_rho_m/rho_m;', 'ppw->theta_m = rho_plus_p_theta_m/rho_plus_p_m;']:
    if raw.count(token) != 1 or patched.count(token) != 1:
        raise SystemExit(f"FAIL current-gauge assignment identity {token}")

print("classification=SUPPORT_PLUS_0_PLUS_0")
print("source_commit=" + reported)
print("original_perturbations_sha256=" + hashlib.sha256(raw.encode()).hexdigest())
print("patched_perturbations_sha256=" + hashlib.sha256(patched.encode()).hexdigest())
print("source_equation_equivalent_modulo_diagnostics=true")
print("self_hosted_science_started=false")
print("prediction_ready=false")
print("scientific_model_authority_created=false")
print("G_DOMAIN_MAPPING=NOT_YET_TESTABLE")
print(PASS)
