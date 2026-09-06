#!/usr/bin/env python3
from pathlib import Path

EN=Path('ci/exp073en_home_filebacked_fullres_v0_1.sh').read_text()
EO=Path('ci/exp073eo_ww_s0_s0_provenance_admission_v0_1.py').read_text()
CONSUMER=Path('ci/exp073eo_consume_real_en_artifact_v0_1.sh').read_text()
PREREG=Path('experiments/073eo_ww_s0_s0_filebacked_checkpoint_provenance_admission_v0_1_prereg.md').read_text()

required_en=[
    "for p in root.rglob('*.json')",
    "'selected_ee.bin'",
    "'A_driver.log'",
    "'B_driver.log'",
    "'ab_compare_stdout.txt'",
    "'resource_telemetry.log'",
    "'tiny.stderr'",
    "local_exp073em_activation",
    "terminal_science_candidate_receipt.json",
    "exp073en_prune_receipt.json",
    "bytes=19327352832 rows=49152",
    "PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1",
]
required_eo=[
    "terminal_science_candidate_receipt.json",
    "component_blobs.json",
    "local_exp073em_activation'/'local_activation_receipt.json",
    "local_exp073em_activation'/'build_identity.json",
    "ab_compare.json",
    "replica_receipt.json",
    "exp073en_prune_receipt.json",
    "selected_ee.bin",
    "f'{rep}_driver.log'",
    "tiny.stderr",
    "MCM_BYTES=19327352832",
    "MCM_ROWS=49152",
    "np.array_equal",
    "BLOCKED_EXP073EO_PROVENANCE_ADMISSION_V0_1",
    "PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1",
]
required_consumer=[
    "actions/runs/$EN_RUN_ID",
    "actions/artifacts/$EN_ARTIFACT_ID",
    "actions/artifacts/$EN_ARTIFACT_ID/zip",
    "sha256sum \"$ZIP\"",
    "unzip -q \"$ZIP\"",
    "exp073eo_ww_s0_s0_provenance_admission_v0_1.py",
    "PASS_EXP073EO_ZIP_DIGEST",
    "PASS_EXP073EO_GITHUB_METADATA_BINDING",
]
required_prereg=[
    "complete ordered six-stage chain",
    "fresh_s0_mask_complete",
    "fresh_workspace_mcm_complete",
    "mcm_fits_verified",
    "full_window_complete",
    "selected_ee_complete",
    "replica_receipt_complete",
    "19327352832",
    "49152",
    "PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1",
]

def missing(text, needles): return [x for x in needles if x not in text]
miss={'en_collector':missing(EN,required_en),'eo_auditor':missing(EO,required_eo),'consumer':missing(CONSUMER,required_consumer),'prereg':missing(PREREG,required_prereg)}
if any(miss.values()):
    print('FAIL_EXP073ES_EN_EO_ARTIFACT_INTERFACE_STATIC_V0_1')
    print(miss)
    raise SystemExit(3)
print('PASS_EXP073ES_EN_EO_ARTIFACT_INTERFACE_STATIC_V0_1')
print({'classification':'STATIC_ARTIFACT_INTERFACE_COMPLETE','accounting':'+0/+0','science_gate_scored':False,'ww_authority_created':False,'missing':miss})
