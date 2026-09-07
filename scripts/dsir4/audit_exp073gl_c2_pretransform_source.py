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

# Static source-binding checks. Whitespace/comments/guard layout may differ;
# symbol and arithmetic identity may not.
def match(pattern, label, haystack=text, flags=re.S):
    m = re.search(pattern, haystack, flags)
    if not m:
        raise SystemExit(f"FAIL missing {label}")
    return m

# Isolate the helper that constructs current-gauge matter sums. The caller later
# applies the gauge-invariant correction after this helper returns.
helper = match(
    r"int\s+perturb_total_stress_energy\s*\([^)]*\)\s*\{(?P<body>.*?)(?=\nint\s+[A-Za-z_][A-Za-z0-9_]*\s*\()",
    "perturb_total_stress_energy function",
).group("body")

# Pinned class_iv source places IDE matter contributions behind source/gauge
# guards. Freeze the exact arithmetic identities while remaining insensitive to
# comments and brace/guard formatting.
match(
    r"delta_rho_m\s*\+=\s*ppw->pvecback\s*\[\s*pba->index_bg_rho_idm_iv\s*\]\s*\*\s*y\s*\[\s*ppw->pv->index_pt_delta_idm_iv\s*\]\s*;",
    "idm_iv density contribution",
    text,
)
match(
    r"rho_m\s*\+=\s*ppw->pvecback\s*\[\s*pba->index_bg_rho_idm_iv\s*\]\s*;",
    "idm_iv matter-density normalization contribution",
    text,
)
match(
    r"rho_plus_p_theta_m\s*\+=\s*ppw->pvecback\s*\[\s*pba->index_bg_rho_idm_iv\s*\]\s*\*\s*y\s*\[\s*ppw->pv->index_pt_theta_idm_iv\s*\]\s*;",
    "idm_iv momentum contribution",
    text,
)
match(
    r"if\s*\(\s*ppt->gauge\s*!=\s*synchronous\s*\).*?rho_plus_p_theta_m\s*\+=\s*ppw->pvecback\s*\[\s*pba->index_bg_rho_idm_iv\s*\]\s*\*\s*y\s*\[\s*ppw->pv->index_pt_theta_idm_iv\s*\]",
    "idm_iv momentum synchronous-gauge guard",
    text,
)

p_delta = match(
    r"ppw->delta_m\s*=\s*delta_rho_m\s*/\s*rho_m\s*;",
    "pre-transform delta_m assignment",
    helper,
).start()
p_theta = match(
    r"ppw->theta_m\s*=\s*rho_plus_p_theta_m\s*/\s*rho_plus_p_m\s*;",
    "pre-transform theta_m assignment",
    helper,
).start()
if not p_delta < p_theta:
    raise SystemExit("FAIL unexpected helper assignment ordering")

# In the caller, require the helper call to occur before the exact native CLASS
# gauge-invariant density correction. This establishes runtime ordering without
# falsely assuming the helper definition must appear lexically before its caller.
einstein = match(
    r"int\s+perturb_einstein\s*\([^)]*\)\s*\{(?P<body>.*?)(?=\nint\s+perturb_total_stress_energy\s*\()",
    "perturb_einstein function",
).group("body")
p_call = match(
    r"perturb_total_stress_energy\s*\(\s*ppr\s*,\s*pba\s*,\s*pth\s*,\s*ppt\s*,\s*index_md\s*,\s*k\s*,\s*y\s*,\s*ppw\s*\)",
    "total stress-energy helper call",
    einstein,
).start()
p_corr = match(
    r"ppw->delta_m\s*\+=\s*3\s*\.\s*\*\s*ppw->pvecback\s*\[\s*pba->index_bg_a\s*\]\s*\*\s*ppw->pvecback\s*\[\s*pba->index_bg_H\s*\]\s*\*\s*ppw->theta_m\s*/\s*k2\s*;",
    "gauge-invariant density correction",
    einstein,
).start()
if not p_call < p_corr:
    raise SystemExit("FAIL total-matter helper is not called before density correction")

match(r"index_bg_a", "native scale factor in correction", einstein)
match(r"index_bg_H", "native H in correction", einstein)
match(r"index_tp_delta_m", "delta_m export symbol")
match(
    r"transform\s*\(delta_m,\s*theta_m\)\s*of\s*the\s*current\s*gauge\s*into\s*gauge-independent\s*variables",
    "native current-gauge to gauge-independent transformation comment",
    einstein,
    flags=re.S | re.I,
)

print("classification=SUPPORT_PLUS_0_PLUS_0")
print("self_hosted_science_started=false")
print("prediction_ready=false")
print("scientific_model_authority_created=false")
print("G_DOMAIN_MAPPING=NOT_YET_TESTABLE")
print(PASS)
