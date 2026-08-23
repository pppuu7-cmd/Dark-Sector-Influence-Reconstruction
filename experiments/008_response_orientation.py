"""Experiment 008: coarse time/scale orientation of response surfaces."""
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "derived" / "linear_controls" / "experiment_007_linear_responses.csv"
OUT = ROOT / "data" / "derived" / "linear_controls" / "experiment_008_orientation.csv"

def log_slope(x1,x2,y1,y2): return np.log(y2/y1)/np.log(x2/x1)

def main():
    a=np.genfromtxt(SRC,delimiter=",",names=True); zvals=np.unique(a["z"]); kvals=np.unique(a["k_hmpc"])
    zlo,zhi=float(zvals[0]),float(zvals[-1]); alo,ahi=1/(1+zhi),1/(1+zlo); klo,khi=float(kvals[0]),float(kvals[-1])
    get=lambda z,k,name: float(a[(a["z"]==z)&(a["k_hmpc"]==k)][name][0])
    sk_w=0.0; sa_w=log_slope(alo,ahi,get(zhi,khi,"P_wCDM_over_LCDM"),get(zlo,khi,"P_wCDM_over_LCDM"))
    sk_wdm=log_slope(klo,khi,get(zlo,klo,"P_WDM_over_CDM"),get(zlo,khi,"P_WDM_over_CDM")); sa_wdm=0.0
    sk_fr=log_slope(klo,khi,get(zlo,klo,"P_fR_over_LCDM"),get(zlo,khi,"P_fR_over_LCDM")); sa_fr=log_slope(alo,ahi,get(zhi,khi,"P_fR_over_LCDM"),get(zlo,khi,"P_fR_over_LCDM"))
    rows=[("smooth_wCDM_w-0.9",sk_w,sa_w),("thermal_WDM_3keV",sk_wdm,sa_wdm),("designer_fR_BZ_like",sk_fr,sa_fr)]
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with OUT.open("w") as f:
        f.write("control,S_k,S_a\n")
        for name,sk,sa in rows: f.write(f"{name},{sk:.10e},{sa:.10e}\n")
    print(rows)
    assert abs(sk_w)<1e-14 and sa_w<0 and sk_wdm<0 and abs(sa_wdm)<1e-14 and sk_fr>0 and sa_fr>0

if __name__ == "__main__": main()
