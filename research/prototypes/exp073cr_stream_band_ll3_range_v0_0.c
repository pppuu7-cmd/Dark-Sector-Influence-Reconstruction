#define _GNU_SOURCE
#include <dlfcn.h>
#include <math.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>

#ifndef M_PI
#define M_PI 3.141592653589793238462643383279502884
#endif

typedef int (*drc3jj_fn)(int,int,int,int,int *,int *,double *,int);

static drc3jj_fn load_drc3jj(const char *nmtlib_path, void **handle_out)
{
  void *h=dlopen(nmtlib_path,RTLD_NOW|RTLD_LOCAL);
  if(h==NULL)
    return NULL;
  void *sym=dlsym(h,"drc3jj");
  if(sym==NULL) {
    dlclose(h);
    return NULL;
  }
  *handle_out=h;
  return (drc3jj_fn)sym;
}

static int max_int(int a,int b)
{
  return a>b ? a:b;
}

/*
 * NON-AUTHORITATIVE RESEARCH PROTOTYPE v0.0.
 *
 * Prospective exact-order ll3-shard helper for a possible post-Exp073CQ
 * resource successor.  This file is not preregistered, not authorized, and
 * must not be used for scientific production or for reinterpreting CQ.
 *
 * Arithmetic-preservation rule:
 *   - one frozen complete band ib is selected;
 *   - the original ll2 loop remains outer and strictly ascending;
 *   - only the original inner ll3 loop is restricted to [ll3_lo,ll3_hi);
 *   - for every retained output ll3, the drc3jj inputs, ascending l1 loop,
 *     acc += xi sequence, and final division by the FULL band width are the
 *     same as ci/exp073ca_stream_general_coupling_range_v0_1.c;
 *   - different ll3 shards have disjoint outputs and require placement /
 *     concatenation only, never a floating-point reduction.
 *
 * nthreads is deliberately required to equal 1. Parallelism is intended to
 * exist only across outer process-level complete shards.
 */
int exp073cr_stream_compress_band_ll3_range(const char *nmtlib_path,
                                            const double *pcl_mask,
                                            int lmax,int s1,int s2,int n1,int n2,
                                            const int *edges,int nb,
                                            int ib,int ll3_lo,int ll3_hi,
                                            int nthreads,double *out)
{
  int nls=lmax+1;
  int lstart=max_int(s1,s2);
  void *handle=NULL;
  drc3jj_fn drc3jj=load_drc3jj(nmtlib_path,&handle);
  if(drc3jj==NULL)
    return 90;
  if((nthreads!=1)||(nb<1)||(ib<0)||(ib>=nb)||
     (ll3_lo<lstart)||(ll3_hi<=ll3_lo)||(ll3_hi>nls)) {
    dlclose(handle);
    return 91;
  }
  if((edges[0]!=0)||(edges[nb]!=nls)) {
    dlclose(handle);
    return 94;
  }
  for(int jb=0;jb<nb;jb++) {
    if((edges[jb]<0)||(edges[jb]>=edges[jb+1])||(edges[jb+1]>nls)) {
      dlclose(handle);
      return 95;
    }
  }

  int nout=ll3_hi-ll3_lo;
  memset(out,0,(size_t)nout*sizeof(double));

  int same_sn=(s1==s2) && (n1==n2);
  double *wl_mask=(double *)malloc((size_t)(lmax+1)*sizeof(double));
  double *wigner_sn1=(double *)malloc((size_t)2*(size_t)(lmax+1)*sizeof(double));
  double *wigner_sn2=NULL;
  if(same_sn)
    wigner_sn2=wigner_sn1;
  else
    wigner_sn2=(double *)malloc((size_t)2*(size_t)(lmax+1)*sizeof(double));

  if((wl_mask==NULL)||(wigner_sn1==NULL)||((!same_sn)&&(wigner_sn2==NULL))) {
    free(wl_mask);
    free(wigner_sn1);
    if(!same_sn)
      free(wigner_sn2);
    dlclose(handle);
    return 92;
  }

  for(int ll=0;ll<=lmax;ll++)
    wl_mask[ll]=pcl_mask[ll]*(2*ll+1)/(4*M_PI);

  int error_code=0;
  int lo=edges[ib];
  int hi=edges[ib+1];

  /* Keep the frozen ll2-outer / ll3-inner nesting exactly. */
  for(int ll2=lo;ll2<hi;ll2++) {
    if(ll2<lstart)
      continue;
    for(int ll3=ll3_lo;ll3<ll3_hi;ll3++) {
      double *acc=out+(size_t)(ll3-ll3_lo);
      int lmin_here=abs(ll2-ll3);
      int lmax_here=ll2+ll3;
      int lmin_sn1=0,lmax_sn1=2*(lmax+1)+1;
      int lmin_sn2=0,lmax_sn2=2*(lmax+1)+1;
      double xi=0.0;
      int rc1=drc3jj(ll2,ll3,n1,-s1,&lmin_sn1,&lmax_sn1,
                     wigner_sn1,2*(lmax+1));
      int rc2=0;
      if(same_sn) {
        wigner_sn2=wigner_sn1;
        lmin_sn2=lmin_sn1;
        lmax_sn2=lmax_sn1;
      }
      else
        rc2=drc3jj(ll2,ll3,n2,-s2,&lmin_sn2,&lmax_sn2,
                   wigner_sn2,2*(lmax+1));
      if((rc1!=0)||(rc2!=0)) {
        error_code=93;
        continue;
      }
      for(int l1=lmin_here;l1<=lmax_here;l1++) {
        if(l1<=lmax) {
          int jsn1=l1-lmin_sn1;
          int jsn2=l1-lmin_sn2;
          double wsn1=0,wsn2=0;
          wsn1=jsn1<0 ? 0 : wigner_sn1[jsn1];
          wsn2=jsn2<0 ? 0 : wigner_sn2[jsn2];
          xi += wl_mask[l1]*wsn1*wsn2;
        }
      }
      xi *= (2*ll3+1.0);
      *acc += xi;
    }
  }

  {
    double width=(double)(hi-lo);
    for(int ll3=ll3_lo;ll3<ll3_hi;ll3++)
      out[ll3-ll3_lo] /= width;
  }

  free(wl_mask);
  free(wigner_sn1);
  if(!same_sn)
    free(wigner_sn2);
  dlclose(handle);
  return error_code;
}
