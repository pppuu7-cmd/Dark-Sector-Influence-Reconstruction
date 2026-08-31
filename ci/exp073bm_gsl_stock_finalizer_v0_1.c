#include <stdio.h>
#include <stdlib.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_blas.h>

#define NB 39
#define L 12288

static void read_exact(const char *path, double *x, size_t n) {
  FILE *f=fopen(path,"rb"); if(!f){perror(path);exit(2);} size_t got=fread(x,sizeof(double),n,f); if(got!=n){fprintf(stderr,"short read %s %zu/%zu\n",path,got,n);exit(3);} int c=fgetc(f); if(c!=EOF){fprintf(stderr,"extra bytes %s\n",path);exit(4);} fclose(f);
}
static void write_exact(const char *path, const double *x, size_t n) {
  FILE *f=fopen(path,"wb"); if(!f){perror(path);exit(5);} size_t got=fwrite(x,sizeof(double),n,f); if(got!=n){fprintf(stderr,"short write\n");exit(6);} fclose(f);
}
int main(int argc,char **argv) {
  if(argc!=4){fprintf(stderr,"usage: %s K.bin A.bin W.bin\n",argv[0]);return 1;}
  double *k=malloc(NB*NB*sizeof(double));
  double *a=malloc((size_t)NB*L*sizeof(double));
  double *w=calloc((size_t)NB*L,sizeof(double));
  if(!k||!a||!w){fprintf(stderr,"alloc\n");return 7;}
  read_exact(argv[1],k,NB*NB); read_exact(argv[2],a,(size_t)NB*L);
  gsl_matrix_view km=gsl_matrix_view_array(k,NB,NB);
  gsl_matrix_view am=gsl_matrix_view_array(a,NB,L);
  gsl_matrix_view wm=gsl_matrix_view_array(w,NB,L);
  gsl_matrix *inv=gsl_matrix_alloc(NB,NB);
  gsl_permutation *p=gsl_permutation_alloc(NB);
  int sig=0;
  int s=gsl_linalg_LU_decomp(&km.matrix,p,&sig); if(s){fprintf(stderr,"LU decomp %d\n",s);return 8;}
  s=gsl_linalg_LU_invert(&km.matrix,p,inv); if(s){fprintf(stderr,"LU invert %d\n",s);return 9;}
  s=gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,1.0,inv,&am.matrix,0.0,&wm.matrix); if(s){fprintf(stderr,"dgemm %d\n",s);return 10;}
  write_exact(argv[3],w,(size_t)NB*L);
  gsl_permutation_free(p); gsl_matrix_free(inv); free(k); free(a); free(w); return 0;
}
