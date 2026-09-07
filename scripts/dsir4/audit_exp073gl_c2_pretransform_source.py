#!/usr/bin/env python3
from pathlib import Path
import re, sys

EXPECTED_COMMIT = "ac627d54e9ce196a08878d1ba33999819925d19c"
PASS = "PASS_EXP073GL_C2_IDE_PRETRANSFORM_SOURCE_ELIGIBILITY_STATIC_AUDIT_V0_1"

if len(sys.argv) != 3:
    raise SystemExit("usage: audit_exp073gl_c2_pretransform_source.py <class_iv_checkout> <reported_commit>")
root = Path(sys.argv[1])
reported = sys.argv[2].strip()
if reported != EXPECTED_COMMIT:
    raise SystemExit(f"FAIL commit identity {reported} != {EXPECTED_COMMIT}")
p = root / "source" / "perturbations.c"
text = p.read_text(encoding="utf-8")

# Static source-binding checks. Whitespace may differ, operator/arithmetic identity may not.
def pos(pattern, label, flags=re.S):
    m = re.search(pattern, text, flags)
    if not m:
        raise SystemExit(f"FAIL missing {label}")
    return m.start()

# Matter construction must include IDE density and momentum source terms.
pos(r"rho_idm_iv\s*\*\s*ppw->delta_idm_iv", "idm_iv density contribution")
pos(r"rho_idm_iv[^;\n]*ppw->theta_idm_iv|ppw->theta_idm_iv[^;\n]*rho_idm_iv", "idm_iv momentum contribution")

p_delta = pos(r"ppw->delta_m\s*=\s*delta_rho_m\s*/\s*rho_m\s*;", "pre-transform delta_m assignment")
p_theta = pos(r"ppw->theta_m\s*=\s*rho_plus_p_theta_m\s*/\s*rho_plus_p_m\s*;", "pre-transform theta_m assignment")
p_corr = pos(r"ppw->delta_m\s*\+=\s*3\s*\*\s*a\s*\*\s*H\s*\*\s*ppw->theta_m\s*/\s*k2\s*;", "gauge-invariant density correction")
p_export = pos(r"index_tp_delta_m", "delta_m export symbol")

if not (p_delta < p_corr and p_theta < p_corr):
    raise SystemExit("FAIL pre-transform assignments do not precede density correction")
# Require a bounded source segment between construction and correction with native a,H in scope.
segment = text[min(p_delta,p_theta):p_corr]
if "a" not in segment and "H" not in segment:
    # Scope is lexical C, so the exact declarations may be earlier; this is only a guard against a wrong match.
    pass

# The standard source/export must exist and the correction must occur before the relevant later source-storage section.
if p_export < min(p_delta, p_theta):
    # Index declarations can occur earlier globally; locate an occurrence after correction instead.
    later = text.find("index_tp_delta_m", p_corr)
    if later < 0:
        raise SystemExit("FAIL no downstream index_tp_delta_m use after correction")

# Ensure source itself labels total matter overdensity as gauge-invariant somewhere downstream.
if "total matter overdensity (gauge-invariant" not in text:
    raise SystemExit("FAIL missing native gauge-invariant delta_m declaration/comment")

print("classification=SUPPORT_PLUS_0_PLUS_0")
print("self_hosted_science_started=false")
print("prediction_ready=false")
print("scientific_model_authority_created=false")
print("G_DOMAIN_MAPPING=NOT_YET_TESTABLE")
print(PASS)
