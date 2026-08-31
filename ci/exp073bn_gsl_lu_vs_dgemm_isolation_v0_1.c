#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_blas.h>

#define NB 39
#define L 12288

static void read_exact(const char *path, double *x, size_t n) {
  FILE *f=fopen(path,"rb"); if(!f){perror(path);exit(2);} size_t got=fread(x,sizeof(double),n,f); if(got!=n){fprintf(stderr,"short read %s %zu/%zu\n",path,got,n);exit(3);} int c=fgetc(f); if(c!=EOF){fprintf(stderr,"extra bytes %s\n",path);exit(4);} fclose(f);
}
static void write_exact(const char *path,const double *x,size_t n) {
  FILE *f=fopen(path,"wb"); if(!f){perror(path);exit(5);} size_t got=fwrite(x,sizeof(double),n,f); if(got!=n){fprintf(stderr,"short write %s\n",path);exit(6);} fclose(f);
}
static void fixed_matmul(const double *inv,const double *a,double *w) {
  for(int i=0;i<NB;i++) {
    for(int c=0;c<L;c++) {
      double s=0.0;
      for(int j=0;j<NB;j++) {
        double prod=inv[(size_t)i*NB+j]*a[(size_t)j*L+c];
        s=s+prod;
      }
      w[(size_t)i*L+c]=s;
    }
  }
}
int main(int argc,char **argv) {
  if(argc!=6){fprintf(stderr,"usage: %s K.bin A.bin invK.bin W_dgemm.bin W_scalar.bin\n",argv[0]);return 1;}
  double *k=malloc((size_t)NB*NB*sizeof(double));
  double *a=malloc((size_t)NB*L*sizeof(double));
  double *invraw=malloc((size_t)NB*NB*sizeof(double));
  double *wdg=calloc((size_t)NB*L,sizeof(double));
  double *wsc=malloc((size_t)NB*L*sizeof(double));
  if(!k||!a||!invraw||!wdg||!wsc){fprintf(stderr,"alloc\n");return 7;}
  read_exact(argv[1],k,(size_t)NB*NB); read_exact(argv[2],a,(size_t)NB*L);
  gsl_matrix_view km=gsl_matrix_view_array(k,NB,NB);
  gsl_matrix_view am=gsl_matrix_view_array(a,NB,L);
  gsl_matrix_view wm=gsl_matrix_view_array(wdg,NB,L);
  gsl_matrix_view im=gsl_matrix_view_array(invraw,NB,NB);
  gsl_permutation *p=gsl_permutation_alloc(NB); if(!p){fprintf(stderr,"perm\n");return 8;}
  int sig=0;
  int s=gsl_linalg_LU_decomp(&km.matrix,p,&sig); if(s){fprintf(stderr,"LU decomp %d\n",s);return 9;}
  s=gsl_linalg_LU_invert(&km.matrix,p,&im.matrix); if(s){fprintf(stderr,"LU invert %d\n",s);return 10;}
  write_exact(argv[3],invraw,(size_t)NB*NB);
  s=gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,1.0,&im.matrix,&am.matrix,0.0,&wm.matrix); if(s){fprintf(stderr,"dgemm %d\n",s);return 11;}
  write_exact(argv[4],wdg,(size_t)NB*L);
  fixed_matmul(invraw,a,wsc);
  write_exact(argv[5],wsc,(size_t)NB*L);
  gsl_permutation_free(p); free(k); free(a); free(invraw); free(wdg); free(wsc); return 0;
}
