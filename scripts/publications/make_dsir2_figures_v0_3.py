#!/usr/bin/env python3
"""Generate visually refined DSIR-2 Figures 1--4 from the frozen manifest.

v0.3 is presentation-only. Scientific values, thresholds and classifications are
unchanged. Changes follow the render-first v0.2 visual audit:
- Fig.1 removes the crowded support annotation and moves the legend away from
  categorical block labels.
- Fig.2 moves Exp071M/N explanatory text outside the plotting field.
- Fig.3 uses exact terminal semantics for BOSS/Exp073A/KiDS-Exp073L.
- Fig.4 retains the accepted fail-closed hierarchy layout.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save(fig, outdir: Path, stem: str):
    outdir.mkdir(parents=True, exist_ok=True)
    fig.savefig(outdir / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(outdir / f"{stem}.svg", bbox_inches="tight")
    plt.close(fig)


def figure1(m, outdir):
    f=m['figure1']
    labels=['matter','Weyl+slip','matter+Weyl+slip','temporal K2+ ray','raw t_tot K2+ ray','projected t_tot K2+ ray','K2 line from K2+','fresh K2−']
    cs2=[f['K2_static']['matter_only']['cs2_deg'],f['K2_static']['weyl_slip']['cs2_deg'],f['K2_static']['matter_weyl_slip']['cs2_deg'],f['K2_positive_ray']['temporal']['cs2_deg'],f['K2_positive_ray']['raw_ttot']['cs2_deg'],f['K2_positive_ray']['projected_ttot_shape']['cs2_deg'],f['K2_line']['predicted_from_positive_shape']['cs2_deg'],f['K2_line']['fresh_negative']['cs2_deg']]
    cv2=[f['K2_static']['matter_only']['cv2_deg'],f['K2_static']['weyl_slip']['cv2_deg'],f['K2_static']['matter_weyl_slip']['cv2_deg'],f['K2_positive_ray']['temporal']['cv2_deg'],f['K2_positive_ray']['raw_ttot']['cv2_deg'],f['K2_positive_ray']['projected_ttot_shape']['cv2_deg'],f['K2_line']['predicted_from_positive_shape']['cv2_deg'],f['K2_line']['fresh_negative']['cv2_deg']]
    x=np.arange(len(labels),dtype=float); dx=0.11
    fig,ax=plt.subplots(figsize=(12.2,6.1))
    ax.scatter(x-dx,cs2,marker='o',s=55,label='K2 vs GDM cs2')
    ax.scatter(x+dx,cv2,marker='s',s=55,label='K2 vs GDM cv2')
    ax.axhline(m['frozen_separator_deg'],linestyle='--',label='frozen 45° separator')
    ax.axvline(2.5,linestyle=':'); ax.axvline(5.5,linestyle=':')
    ax.text(1.0,176,'static response',ha='center',va='top')
    ax.text(4.0,176,'selected positive ray',ha='center',va='top')
    ax.text(6.5,176,'two-sided line geometry',ha='center',va='top')
    ax.set_ylabel('Angular separation [deg]')
    ax.set_xticks(x); ax.set_xticklabels(labels,rotation=27,ha='right')
    ax.set_ylim(0,180)
    ax.set_title('K2 specificity is conditional on representation and nuisance geometry',pad=14)
    ax.legend(loc='center right',bbox_to_anchor=(0.985,0.55))
    fig.text(0.5,0.015,f"Exp071K robustness: all {f['support_robustness']['primary_angle_count']} positive-ray support deletions remain above 45°; minimum {f['support_robustness']['global_min_primary_angle_deg']:.2f}°.",ha='center',fontsize=9)
    fig.subplots_adjust(bottom=0.22)
    save(fig,outdir,'dsir2_figure1_k2_specificity_hierarchy_v0_3')


def figure2(m,outdir):
    n=m['figure2']['Exp071N']; vals=[n['K1_line_cs2_deg'],n['K1_line_cv2_deg']]
    fig,ax=plt.subplots(figsize=(8.8,5.9)); x=np.arange(2)
    fig.subplots_adjust(top=0.73,bottom=0.16)
    bars=ax.bar(x,vals,width=0.58)
    ax.axhline(m['frozen_separator_deg'],linestyle='--')
    ax.text(1.48,45.7,'frozen 45° separator',ha='right',va='bottom',fontsize=9)
    ax.set_xticks(x); ax.set_xticklabels(['K1 line vs GDM cs2','K1 line vs GDM cv2'])
    ax.set_ylabel('Physical nuisance-line angle [deg]'); ax.set_ylim(0,55)
    ax.set_title('K1: representation kernel followed by resolved two-sided overlap')
    for b,v in zip(bars,vals): ax.text(b.get_x()+b.get_width()/2,v+0.8,f'{v:.2f}°',ha='center',va='bottom')
    fig.text(0.5,0.90,'Exp071M: transfer-only Δln|t_tot| = 0 for both K1 signs → normalized angle undefined; INVALID_FOR_SCIENCE',ha='center',fontsize=9.5)
    fig.text(0.5,0.855,f"Exp071N: Δln P_R + 2Δln|t_tot| resolves K1; retained shape norm = {n['retained_shape_norm_fraction']['K1']:.3f}",ha='center',fontsize=9.5)
    save(fig,outdir,'dsir2_figure2_k1_representation_kernel_v0_3')


def box(ax,x,y,text):
    ax.text(x,y,text,ha='center',va='center',transform=ax.transAxes,bbox={'boxstyle':'round,pad=0.45','fill':False},wrap=True)

def arrow(ax,x1,y1,x2,y2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),xycoords=ax.transAxes,arrowprops={'arrowstyle':'->'})


def figure3(m,outdir):
    f=m['figure3']; fig,ax=plt.subplots(figsize=(11.2,7.1)); ax.set_axis_off()
    ax.set_title('Provider completeness is not finite-observation admissibility',pad=12)
    box(ax,.50,.89,f"Certified common provider support\n{f['provider_cells_retained']}/{f['provider_cells_total']} cells")
    box(ax,.50,.73,f"ACT×unWISE first route\n0 retained coordinates at {100*f['act_unwise_leakage_threshold_fraction']:.0f}% leakage")
    box(ax,.50,.57,f"Planning frontier only\nz_min ≈ {f['joint_frontier_z_min']:.10f}, k_max ≈ {f['joint_frontier_k_max_Mpc_inv']:.4f} Mpc⁻¹")
    box(ax,.50,.41,'Exp073A linear/no-CLEFT eligibility\n0/26 retained even through Δ² ≤ 2')
    box(ax,.27,.20,f"BOSS finite-matrix component\n{f['boss_nonempty_rows']}/{f['boss_total_rows']} rows retained — non-classifying")
    box(ax,.73,.20,'KiDS finite-theta absolute positive-support\nnon-normalizable under Exp073L')
    arrow(ax,.50,.85,.50,.77); arrow(ax,.50,.69,.50,.61); arrow(ax,.50,.53,.50,.45)
    arrow(ax,.47,.36,.30,.25); arrow(ax,.53,.36,.70,.25)
    ax.text(.5,.055,'Support/operator statements only — not covariance-whitened likelihood or survey-significance results.',transform=ax.transAxes,ha='center',fontsize=9.5)
    save(fig,outdir,'dsir2_figure3_support_admissibility_v0_3')


def figure4(m,outdir):
    stages=m['figure4']['hierarchy']; stop=m['figure4']['article2_stops_before']; stop_i=stages.index(stop)
    fig,ax=plt.subplots(figsize=(10.4,7.4)); ax.set_axis_off(); ax.set_title('DSIR fail-closed hierarchy for response-space specificity')
    y=np.linspace(.91,.09,len(stages))
    for i,(yy,text) in enumerate(zip(y,stages)):
        prefix='Article 2' if i<stop_i else 'Downstream'; box(ax,.5,yy,f'{prefix}: {text}')
        if i<len(stages)-1: arrow(ax,.5,yy-.035,.5,y[i+1]+.035)
    boundary=(y[stop_i-1]+y[stop_i])/2; ax.axhline(boundary,linestyle='--'); ax.text(.72,boundary+.012,'DSIR-2 boundary',transform=ax.transAxes,va='bottom')
    save(fig,outdir,'dsir2_figure4_fail_closed_hierarchy_v0_3')


def main():
    p=argparse.ArgumentParser(); p.add_argument('--manifest',type=Path,default=Path('docs/publications/DSIR2_FIGURE_NUMERIC_MANIFEST_V0_1.json')); p.add_argument('--outdir',type=Path,default=Path('artifacts/publications/article2/figures')); a=p.parse_args()
    m=load_manifest(a.manifest); figure1(m,a.outdir); figure2(m,a.outdir); figure3(m,a.outdir); figure4(m,a.outdir)
    print(f'Wrote DSIR-2 publication Figures 1-4 v0.3 to {a.outdir}')

if __name__=='__main__': main()
