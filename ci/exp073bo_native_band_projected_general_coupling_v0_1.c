#include <stdlib.h>
#include <stdint.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

typedef int (*drc3jj_fn)(int,int,int,int,int*,int*,double*,int);

/*
 * Native low-memory projection of NaMaster-v2.7 general-coupling rows.
 * The Wigner kernel itself is NOT reimplemented: the caller supplies the
 * exact runtime address of NaMaster's drc3jj symbol.
 *
 * out is row-major [nband, lmax+1] and must be pre-zeroed.
 */
int exp073bo_project_wm(int lmax,
                        const double *pcl,
                        const int32_t *edges,
                        int nband,
                        void *drc_addr,
                        double *out) {
  if(lmax < 2 || pcl == NULL || edges == NULL || drc_addr == NULL || out == NULL)
    return 10;

  const int L=lmax+1;
  const int s1=0, s2=2, n1=0, n2=2;
  const int lstart=(s1>s2) ? s1 : s2;
  const int same_sn=(s1==s2) && (n1==n2);
  drc3jj_fn drc=(drc3jj_fn)drc_addr;

  double *wl_mask=(double *)malloc((size_t)L*sizeof(double));
  double *wigner_sn1=(double *)malloc((size_t)(2*L)*sizeof(double));
  double *wigner_sn2=same_sn ? wigner_sn1 : (double *)malloc((size_t)(2*L)*sizeof(double));
  if(wl_mask==NULL || wigner_sn1==NULL || wigner_sn2==NULL) {
    free(wl_mask); free(wigner_sn1); if(!same_sn) free(wigner_sn2);
    return 11;
  }

  for(int ell=0;ell<L;ell++)
    wl_mask[ell]=pcl[ell]*(2*ell+1)/(4*M_PI);

  for(int ib=0;ib<nband;ib++) {
    const int lo=(int)edges[ib];
    const int hi=(int)edges[ib+1];
    if(lo<0 || hi<=lo || hi>L) {
      free(wl_mask); free(wigner_sn1); if(!same_sn) free(wigner_sn2);
      return 12;
    }
    double *acc=out+(size_t)ib*L;

    for(int ll2=lo;ll2<hi;ll2++) {
      if(ll2<lstart)
        continue;

      for(int ll3=lstart;ll3<=lmax;ll3++) {
        int lmin_here=abs(ll2-ll3);
        int lmax_here=ll2+ll3;
        int lmin_sn1=0,lmax_sn1=2*L+1;
        int lmin_sn2=0,lmax_sn2=2*L+1;

        int rc=drc(ll2,ll3,n1,-s1,&lmin_sn1,&lmax_sn1,wigner_sn1,2*L);
        if(rc!=0) {
          free(wl_mask); free(wigner_sn1); if(!same_sn) free(wigner_sn2);
          return 20+rc;
        }
        if(same_sn) {
          wigner_sn2=wigner_sn1;
          lmin_sn2=lmin_sn1;
          lmax_sn2=lmax_sn1;
        }
        else {
          rc=drc(ll2,ll3,n2,-s2,&lmin_sn2,&lmax_sn2,wigner_sn2,2*L);
          if(rc!=0) {
            free(wl_mask); free(wigner_sn1); free(wigner_sn2);
            return 40+rc;
          }
        }

        double cell=0.0;
        for(int l1=lmin_here;l1<=lmax_here;l1++) {
          if(l1<=lmax) {
            int jsn1=l1-lmin_sn1;
            int jsn2=l1-lmin_sn2;
            double wsn1=(jsn1<0) ? 0.0 : wigner_sn1[jsn1];
            double wsn2=(jsn2<0) ? 0.0 : wigner_sn2[jsn2];
            cell += wl_mask[l1]*wsn1*wsn2;
          }
        }
        cell *= (2*ll3+1.0);
        acc[ll3] += cell;
      }
    }

    const double width=(double)(hi-lo);
    for(int ll3=0;ll3<L;ll3++)
      acc[ll3] /= width;
  }

  free(wl_mask);
  free(wigner_sn1);
  if(!same_sn)
    free(wigner_sn2);
  return 0;
}
