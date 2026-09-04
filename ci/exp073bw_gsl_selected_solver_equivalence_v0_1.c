#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_permutation.h>
#include <gsl/gsl_vector.h>

static void die(const char *m) { fprintf(stderr,"%s\n",m); exit(2); }

int main(int argc, char **argv) {
  if(argc!=3) die("usage: solver input.bin output.bin");
  FILE *fi=fopen(argv[1],"rb"); if(!fi) die("open input");
  int32_t nb=0,l=0;
  if(fread(&nb,sizeof(nb),1,fi)!=1 || fread(&l,sizeof(l),1,fi)!=1) die("header");
  if(nb<=0 || l<=0 || nb>4096 || l>1000000) die("dimensions");
  size_t nk=(size_t)nb*(size_t)nb, na=(size_t)nb*(size_t)l;
  double *k=malloc(nk*sizeof(double)); double *a=malloc(na*sizeof(double)); double *xout=malloc(na*sizeof(double));
  if(!k||!a||!xout) die("alloc");
  if(fread(k,sizeof(double),nk,fi)!=nk || fread(a,sizeof(double),na,fi)!=na) die("payload");
  if(fgetc(fi)!=EOF) die("trailing bytes"); fclose(fi);

  gsl_matrix *km=gsl_matrix_alloc(nb,nb); gsl_permutation *p=gsl_permutation_alloc(nb);
  gsl_vector *b=gsl_vector_alloc(nb); gsl_vector *x=gsl_vector_alloc(nb);
  if(!km||!p||!b||!x) die("gsl alloc");
  for(int i=0;i<nb;i++) for(int j=0;j<nb;j++) gsl_matrix_set(km,i,j,k[(size_t)i*nb+j]);
  int signum=0; if(gsl_linalg_LU_decomp(km,p,&signum)!=0) die("LU decomp");
  for(int ell=0;ell<l;ell++) {
    for(int i=0;i<nb;i++) gsl_vector_set(b,i,a[(size_t)i*l+ell]);
    if(gsl_linalg_LU_solve(km,p,b,x)!=0) die("LU solve");
    for(int i=0;i<nb;i++) xout[(size_t)i*l+ell]=gsl_vector_get(x,i);
  }
  FILE *fo=fopen(argv[2],"wb"); if(!fo) die("open output");
  if(fwrite(xout,sizeof(double),na,fo)!=na) die("write"); fclose(fo);
  gsl_vector_free(x); gsl_vector_free(b); gsl_permutation_free(p); gsl_matrix_free(km);
  free(xout); free(a); free(k); return 0;
}
