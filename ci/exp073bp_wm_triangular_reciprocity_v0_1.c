#include <stdlib.h>
#include <stdint.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

typedef int (*drc3jj_fn)(int,int,int,int,int*,int*,double*,int);

/*
 * Wm triangular-reciprocity projected kernel.
 * Wigner values come from the exact runtime NaMaster drc3jj symbol.
 * out is row-major [nband,L] and must be pre-zeroed.
 */
int exp073bp_project_wm_triangular(int lmax,
                                   const double *pcl,
                                   const int32_t *edges,
                                   int nband,
                                   void *drc_addr,
                                   double *out) {
  if(lmax < 2 || pcl == NULL || edges == NULL || drc_addr == NULL || out == NULL)
    return 10;
  const int L=lmax+1;
  const int lstart=2;
  drc3jj_fn drc=(drc3jj_fn)drc_addr;

  double *wl_mask=(double *)malloc((size_t)L*sizeof(double));
  double *wigner_00=(double *)malloc((size_t)(2*L)*sizeof(double));
  double *wigner_02=(double *)malloc((size_t)(2*L)*sizeof(double));
  int *band_of=(int *)malloc((size_t)L*sizeof(int));
  if(wl_mask==NULL || wigner_00==NULL || wigner_02==NULL || band_of==NULL) {
    free(wl_mask); free(wigner_00); free(wigner_02); free(band_of);
    return 11;
  }

  for(int ell=0;ell<L;ell++) {
    wl_mask[ell]=pcl[ell]*(2*ell+1)/(4*M_PI);
    band_of[ell]=-1;
  }
  for(int ib=0;ib<nband;ib++) {
    int lo=(int)edges[ib], hi=(int)edges[ib+1];
    if(lo<0 || hi<=lo || hi>L) {
      free(wl_mask); free(wigner_00); free(wigner_02); free(band_of);
      return 12;
    }
    for(int ell=lo;ell<hi;ell++) band_of[ell]=ib;
  }
  for(int ell=0;ell<L;ell++) {
    if(band_of[ell]<0) {
      free(wl_mask); free(wigner_00); free(wigner_02); free(band_of);
      return 13;
    }
  }

  for(int l2=lstart;l2<=lmax;l2++) {
    for(int l3=l2;l3<=lmax;l3++) {
      int lmin_here=abs(l2-l3);
      int lmax_here=l2+l3;
      int lmin_00=0,lmax_00=2*L+1;
      int lmin_02=0,lmax_02=2*L+1;

      int rc=drc(l2,l3,0,0,&lmin_00,&lmax_00,wigner_00,2*L);
      if(rc!=0) {
        free(wl_mask); free(wigner_00); free(wigner_02); free(band_of);
        return 20+rc;
      }
      rc=drc(l2,l3,2,-2,&lmin_02,&lmax_02,wigner_02,2*L);
      if(rc!=0) {
        free(wl_mask); free(wigner_00); free(wigner_02); free(band_of);
        return 40+rc;
      }

      double core=0.0;
      for(int l1=lmin_here;l1<=lmax_here;l1++) {
        if(l1<=lmax) {
          int j00=l1-lmin_00;
          int j02=l1-lmin_02;
          double w00=(j00<0) ? 0.0 : wigner_00[j00];
          double w02=(j02<0) ? 0.0 : wigner_02[j02];
          core += wl_mask[l1]*w00*w02;
        }
      }

      int b2=band_of[l2];
      out[(size_t)b2*L+l3] += core*(2*l3+1.0);
      if(l3!=l2) {
        int b3=band_of[l3];
        out[(size_t)b3*L+l2] += core*(2*l2+1.0);
      }
    }
  }

  for(int ib=0;ib<nband;ib++) {
    double width=(double)((int)edges[ib+1]-(int)edges[ib]);
    double *row=out+(size_t)ib*L;
    for(int j=0;j<L;j++) row[j] /= width;
  }

  free(wl_mask); free(wigner_00); free(wigner_02); free(band_of);
  return 0;
}
