#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_permutation.h>

static void die(const char *m){fprintf(stderr,"%s\n",m);exit(2);}

int main(int argc,char **argv){
  if(argc!=3) die("usage: emulator input.bin output.bin");
  int fd=open(argv[1],O_RDONLY); if(fd<0) die("open input");
  struct stat st; if(fstat(fd,&st)!=0) die("fstat");
  if(st.st_size<12) die("short input");
  unsigned char *base=mmap(NULL,(size_t)st.st_size,PROT_READ,MAP_PRIVATE,fd,0);
  if(base==MAP_FAILED) die("mmap");
  int32_t ncls=0,nb=0,L=0;
  __builtin_memcpy(&ncls,base,4); __builtin_memcpy(&nb,base+4,4); __builtin_memcpy(&L,base+8,4);
  if(ncls<=0||ncls>8||nb<=0||nb>4096||L<=0||L>1000000) die("dims");
  size_t hdr=12+(size_t)(nb+1)*4;
  size_t nr=(size_t)ncls*(size_t)L, nm=nr*nr;
  if(hdr>SIZE_MAX-nm*sizeof(double) || (size_t)st.st_size!=hdr+nm*sizeof(double)) die("size");
  const int32_t *edges=(const int32_t *)(base+12);
  const double *m=(const double *)(base+hdr);
  if(edges[0]<0||edges[nb]!=L) die("edges boundary");
  for(int b=0;b<nb;b++) if(edges[b+1]<=edges[b]) die("edges monotonic");

  size_t nbr=(size_t)ncls*(size_t)nb;
  gsl_matrix *kb=gsl_matrix_alloc(nbr,nbr); if(!kb) die("kb alloc");
  for(int icla=0;icla<ncls;icla++) for(int iclb=0;iclb<ncls;iclb++) for(int ib2=0;ib2<nb;ib2++) for(int ib3=0;ib3<nb;ib3++){
    double coupling_b=0.0; double w2=1.0/(double)(edges[ib2+1]-edges[ib2]);
    for(int l2=edges[ib2];l2<edges[ib2+1];l2++){
      size_t row=(size_t)ncls*(size_t)l2+(size_t)icla;
      for(int l3=edges[ib3];l3<edges[ib3+1];l3++){
        size_t col=(size_t)ncls*(size_t)l3+(size_t)iclb;
        coupling_b += m[row*nr+col]*w2;
      }
    }
    gsl_matrix_set(kb,(size_t)ncls*ib2+icla,(size_t)ncls*ib3+iclb,coupling_b);
  }
  gsl_permutation *perm=gsl_permutation_alloc(nbr); if(!perm) die("perm alloc");
  int sig=0; if(gsl_linalg_LU_decomp(kb,perm,&sig)!=0) die("LU decomp");
  gsl_matrix *mat=gsl_matrix_calloc(nbr,nr); if(!mat) die("mat alloc");
  for(int icl1=0;icl1<ncls;icl1++) for(int ib1=0;ib1<nb;ib1++){
    size_t index_b1=(size_t)ncls*ib1+icl1; double wf=1.0/(double)(edges[ib1+1]-edges[ib1]);
    for(int l1=edges[ib1];l1<edges[ib1+1];l1++){
      size_t index_1=(size_t)ncls*l1+icl1;
      for(int icl2=0;icl2<ncls;icl2++) for(int l2=0;l2<L;l2++){
        size_t index_2=(size_t)ncls*l2+icl2;
        double m0=gsl_matrix_get(mat,index_b1,index_2);
        gsl_matrix_set(mat,index_b1,index_2,m0+m[index_1*nr+index_2]*wf);
      }
    }
  }
  gsl_matrix *inv=gsl_matrix_alloc(nbr,nbr); if(!inv) die("inv alloc");
  gsl_matrix *bpw=gsl_matrix_calloc(nbr,nr); if(!bpw) die("bpw alloc");
  if(gsl_linalg_LU_invert(kb,perm,inv)!=0) die("LU invert");
  if(gsl_blas_dgemm(CblasNoTrans,CblasNoTrans,1.0,inv,mat,0.0,bpw)!=0) die("dgemm");
  FILE *fo=fopen(argv[2],"wb"); if(!fo) die("open output");
  for(int icl1=0;icl1<ncls;icl1++) for(int ib1=0;ib1<nb;ib1++){
    size_t index_1=(size_t)ncls*ib1+icl1;
    for(int icl2=0;icl2<ncls;icl2++) for(int l2=0;l2<L;l2++){
      size_t index_2=(size_t)ncls*l2+icl2; double v=gsl_matrix_get(bpw,index_1,index_2);
      if(fwrite(&v,sizeof(double),1,fo)!=1) die("write");
    }
  }
  fclose(fo); gsl_matrix_free(bpw); gsl_matrix_free(inv); gsl_matrix_free(mat); gsl_permutation_free(perm); gsl_matrix_free(kb);
  munmap(base,(size_t)st.st_size); close(fd); return 0;
}
