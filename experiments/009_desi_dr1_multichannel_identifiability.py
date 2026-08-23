"""Experiment 009: first real multi-channel DSIR response/identifiability gate.

Uses the *corrected 2026 erratum* Gaussian ShapeFit response vectors. It does not
fit a new cosmology and does not claim a dark-sector law. The main purpose is to
measure observational covariance directions that must be quotiented before law
searches.
"""
from pathlib import Path
import sys
import numpy as np
from scipy.stats import chi2

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from dsir.shapefit_response import load_erratum, validate_covariance, ap_growth_correlation, fiducial_chi2_three_channel

SRC = ROOT / "data" / "observations" / "desi_dr1_shapefit_erratum_2026.json"
OUT = ROOT / "data" / "derived" / "desi_dr1_shapefit"
USE = ("LRG1", "LRG2", "LRG3", "ELG2", "QSO")


def main():
    meta, bins = load_erratum(SRC)
    OUT.mkdir(parents=True, exist_ok=True)
    rows=[]; chi_total=0.0
    for name, rec in bins.items():
        assert validate_covariance(rec["cov"]), name
        rho = ap_growth_correlation(rec["cov"])
        sig = np.sqrt(np.diag(rec["cov"]))
        if name in USE:
            fid = meta["fiducial_for_control"][name]
            c2 = fiducial_chi2_three_channel(rec["vector"], rec["cov"], fid["DH_over_DM"], fid["f_sigma_s8"])
            chi_total += c2
            ap_ratio = rec["vector"][1] / fid["DH_over_DM"]
            g_ratio = rec["vector"][2] / fid["f_sigma_s8"]
        else:
            c2=ap_ratio=g_ratio=np.nan
        rows.append((name,rec["z_eff"],rec["vector"][0],rec["vector"][1],rec["vector"][2],rec["vector"][3],sig[1],sig[2],rho,ap_ratio,g_ratio,c2))

    arr = np.array([[r[1],r[8]] for r in rows if r[0] in USE])
    rhos = arr[:,1]
    dof = 3*len(USE)
    p = float(chi2.sf(chi_total,dof))
    header="bin,z,DV_over_rd,DH_over_DM,f_sigma_s8,m_plus_n,sigma_AP,sigma_growth,rho_AP_growth,AP_over_fid,growth_over_fid,chi2_AP_growth_shape"
    with (OUT / "experiment_009_multichannel.csv").open("w") as f:
        f.write(header+"\n")
        for r in rows:
            f.write(",".join(str(x) for x in r)+"\n")
    text=(
        "Experiment 009 — corrected DESI DR1 ShapeFit multi-channel identifiability\n"
        f"informative bins = {','.join(USE)}\n"
        f"rho(AP,growth) = {','.join(f'{x:.6f}' for x in rhos)}\n"
        f"mean rho(AP,growth) = {np.mean(rhos):.6f}\n"
        f"sample std rho(AP,growth) = {np.std(rhos,ddof=1):.6f}\n"
        f"fiducial 3-channel chi2 = {chi_total:.6f} for {dof} dof; p={p:.6f}\n"
        "BGS excluded from rho-constancy/control sum because AP is strongly prior-dominated.\n"
        "INTERPRETATION: stable negative AP-growth covariance is an observational identifiability direction, not a dark-sector law.\n"
        "STATUS: G6B real multi-channel response ingest PASS; physical-law gate G7 remains OPEN.\n"
    )
    (OUT / "experiment_009_output.txt").write_text(text)
    print(text)

if __name__ == "__main__": main()
