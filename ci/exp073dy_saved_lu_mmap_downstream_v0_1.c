#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_permutation.h>

#ifndef DSIR_WORKERS
#define DSIR_WORKERS 2
#endif

static void die(const char *m){fprintf(stderr,"%s\n",m);exit(2);}

int main(int argc,char **argv){
  if(argc!=3) die("usage: saved_lu_downstream input.bin output.bin");
  omp_set_dynamic(0);
  omp_set_num_threads(DSIR_WORKERS);
  int team=0;
  #pragma omp parallel num_threads(DSIR_WORKERS)
  {
    #pragma omp single
    team=omp_get_num_threads();
  }
  if(team!=DSIR_WORKERS) die("OpenMP team size mismatch");
  fprintf(stderr,"DSIR_OMP_TEAM=%d\n",team);

  int fd=open(argv[1],O_RDONLY); if(fd<0) die("open input");
  struct stat st; if(fstat(fd,&st)!=0) die("fstat");
  if(st.st_size<12) die("short input");
  unsigned char *base=mmap(NULL,(size_t)st.st_size,PROT_READ,MAP_PRIVATE,fd,0);
  if(base==MAP_FAILED) die("mmap");

  int32_t ncls=0,nb=0,L=0;
  __builtin_memcpy(&ncls,base,4); __builtin_memcpy(&nb,base+4,4); __builtin_memcpy(&L,base+8,4);
  if(ncls<=0||ncls>8||nb<=0||nb>4096||L<=0||L>1000000) die("dims");
  size_t edges_bytes=(size_t)(nb+1)*sizeof(int32_t);
  size_t hdr=12+edges_bytes;
  size_t nr=(size_t)ncls*(size_t)L;
  size_t nm=nr*nr;
  size_t nbr=(size_t)ncls*(size_t)nb;
  size_t nlu=nbr*nbr;
  size_t need=hdr;
  if(nm>SIZE_MAX/sizeof(double) || nlu>SIZE_MAX/sizeof(double)) die("overflow");
  if(need>SIZE_MAX-nm*sizeof(double)) die("overflow"); need+=nm*sizeof(double);
  if(need>SIZE_MAX-nlu*sizeof(double)) die("overflow"); need+=nlu*sizeof(double);
  if(need>SIZE_MAX-nbr*sizeof(int32_t)) die("overflow"); need+=nbr*sizeof(int32_t);
  if((size_t)st.st_size!=need) die("size");

  const int32_t *edges=(const int32_t *)(base+12);
  if(edges[0]<0||edges[nb]!=L) die("edges boundary");
  for(int b=0;b<nb;b++) if(edges[b+1]<=edges[b]) die("edges monotonic");
  const double *m=(const double *)(base+hdr);
  const double *lu_src=m+nm;
  const int32_t *perm_src=(const int32_t *)(lu_src+nlu);

  /* Import the exact LU-decomposed binned MCM and exact permutation written
     by NaMaster. Do not re-bin and do not call gsl_linalg_LU_decomp here. */
  gsl_matrix *lu=gsl_matrix_alloc(nbr,nbr); if(!lu) die("lu alloc");
  for(size_t i=0;i<nbr;i++) for(size_t j=0;j<nbr;j++)
    gsl_matrix_set(lu,i,j,lu_src[i*nbr+j]);
  gsl_permutation *perm=gsl_permutation_alloc(nbr); if(!perm) die("perm alloc");
  for(size_t i=0;i<nbr;i++){
    if(perm_src[i]<0 || (size_t)perm_src[i]>=nbr) die("perm bounds");
    perm->data[i]=(size_t)perm_src[i];
  }
  /* Validate that the imported permutation is a true permutation. */
  unsigned char *seen=calloc(nbr,1); if(!seen) die("seen alloc");
  for(size_t i=0;i<nbr;i++){
    size_t p=perm->data[i]; if(seen[p]) die("perm duplicate"); seen[p]=1;
  }
  free(seen);

  gsl_matrix *mat=gsl_matrix_calloc(nbr,nr); if(!mat) die("mat alloc");

  /* Match NaMaster nmt_compute_bandpower_windows accumulation order for
     mat_coupled_bin. Parallelism is only across independent output rows. */
  #pragma omp parallel for collapse(2) schedule(static) num_threads(DSIR_WORKERS)
  for(int icl1=0;icl1<ncls;icl1++) for(int ib1=0;ib1<nb;ib1++){
    size_t index_b1=(size_t)ncls*(size_t)ib1+(size_t)icl1;
    double wf=1.0/(double)(edges[ib1+1]-edges[ib1]);
    for(int l1=edges[ib1];l1<edges[ib1+1];l1++){
      size_t index_1=(size_t)ncls*(size_t)l1+(size_t)icl1;
      const double *matrix_row=m+index_1*nr;
      for(int icl2=0;icl2<ncls;icl2++) for(int l2=0;l2<L;l2++){
        size_t index_2=(size_t)ncls*(size_t)l2+(size_t)icl2;
        double m0=gsl_matrix_get(mat,index_b1,index_2);
        gsl_matrix_set(mat,index_b1,index_2,m0+matrix_row[index_2]*wf);
      }
    }
  }

  gsl_matrix *inv=gsl_matrix_alloc(nbr,nbr); if(!inv) die("inv alloc");
  gsl_matrix *bpw=gsl_matrix_calloc(nbr,nr); if(!bpw) die("bpw alloc");
  if(gsl_linalg_LU_invert(lu,perm,inv)!=0) die("LU invert");
  if(gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,1.0,inv,mat,0.0,bpw)!=0) die("dgemm");

  FILE *fo=fopen(argv[2],"wb"); if(!fo) die("open output");
  for(int icl1=0;icl1<ncls;icl1++) for(int ib1=0;ib1<nb;ib1++){
    size_t index_1=(size_t)ncls*(size_t)ib1+(size_t)icl1;
    for(int icl2=0;icl2<ncls;icl2++) for(int l2=0;l2<L;l2++){
      size_t index_2=(size_t)ncls*(size_t)l2+(size_t)icl2;
      double v=gsl_matrix_get(bpw,index_1,index_2);
      if(fwrite(&v,sizeof(double),1,fo)!=1) die("write");
    }
  }
  fclose(fo);
  gsl_matrix_free(bpw); gsl_matrix_free(inv); gsl_matrix_free(mat);
  gsl_permutation_free(perm); gsl_matrix_free(lu);
  munmap(base,(size_t)st.st_size); close(fd);
  return 0;
}
