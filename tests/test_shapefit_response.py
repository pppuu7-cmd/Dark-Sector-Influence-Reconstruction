from pathlib import Path
import numpy as np
from dsir.shapefit_response import load_erratum, validate_covariance, ap_growth_correlation

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"data"/"observations"/"desi_dr1_shapefit_erratum_2026.json"

def test_corrected_shapefit_covariances_are_spd():
    _, bins=load_erratum(SRC)
    assert all(validate_covariance(r["cov"]) for r in bins.values())

def test_corrected_lrg1_growth_value_guards_against_old_appendix():
    _, bins=load_erratum(SRC)
    assert bins["LRG1"]["vector"][2] == 0.513635
    assert bins["LRG1"]["vector"][2] != 0.318967

def test_ap_growth_covariance_is_negative_in_informative_bins():
    _, bins=load_erratum(SRC)
    for name in ("LRG1","LRG2","LRG3","ELG2","QSO"):
        assert ap_growth_correlation(bins[name]["cov"]) < -0.5
