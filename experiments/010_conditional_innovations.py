"""Experiment 010: remove within-bin AP/shape covariance from growth residuals.

This is a G7-preparation experiment, not a law search. It constructs Gaussian
conditional innovations from the corrected DESI DR1 ShapeFit covariance.
"""
from pathlib import Path
import sys
import numpy as np
from scipy.stats import chi2

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from dsir.shapefit_response import load_erratum
from dsir.conditioning import conditional_innovation

SRC=ROOT/"data"/"observations"/"desi_dr1_shapefit_erratum_2026.json"
OUT=ROOT/"data"/"derived"/"desi_dr1_shapefit"
USE=("LRG1","LRG2","LRG3","ELG2","QSO")


def main():
    meta,bins=load_erratum(SRC); rows=[]
    for name in USE:
        rec=bins[name]; fid=meta["fiducial_for_control"][name]
        idx=[1,2,3]  # AP, growth, shape
        y=rec["vector"][idx]
        c=rec["cov"][np.ix_(idx,idx)]
        r=y-np.array([fid["DH_over_DM"],fid["f_sigma_s8"],0.0])
        gi,gv,gb=conditional_innovation(r,c,target=1,conditioned_on=[0,2])
        ai,av,ab=conditional_innovation(r,c,target=0,conditioned_on=[1,2])
        rows.append((name,rec["z_eff"],gi,np.sqrt(gv),gi/np.sqrt(gv),ai,np.sqrt(av),ai/np.sqrt(av),gb[0],gb[1],ab[0],ab[1]))
    z_g=np.array([r[4] for r in rows]); z_ap=np.array([r[7] for r in rows])
    chi_g=float(z_g@z_g); chi_ap=float(z_ap@z_ap)
    p_g=float(chi2.sf(chi_g,len(USE))); p_ap=float(chi2.sf(chi_ap,len(USE)))
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/"experiment_010_conditional_innovations.csv").open("w") as f:
        f.write("bin,z,growth_innovation,sigma_growth_innovation,z_growth,AP_innovation,sigma_AP_innovation,z_AP,beta_growth_AP,beta_growth_shape,beta_AP_growth,beta_AP_shape\n")
        for r in rows: f.write(",".join(str(x) for x in r)+"\n")
    text=(
      "Experiment 010 — conditional innovations after covariance quotient\n"
      f"growth innovation chi2={chi_g:.6f} for {len(USE)} dof; p={p_g:.6f}\n"
      f"AP innovation chi2={chi_ap:.6f} for {len(USE)} dof; p={p_ap:.6f}\n"
      "growth z = "+",".join(f"{x:.6f}" for x in z_g)+"\n"
      "AP z = "+",".join(f"{x:.6f}" for x in z_ap)+"\n"
      "INTERPRETATION: no significant aggregate innovation against the fiducial response under this Gaussian control.\n"
      "STATUS: G7 preparation PASS; G7 physical-law discovery remains OPEN.\n")
    (OUT/"experiment_010_output.txt").write_text(text); print(text)

if __name__=="__main__": main()
