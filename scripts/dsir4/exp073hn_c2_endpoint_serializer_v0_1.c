#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fixtures/dsir_c2_recorder_v0_1.h"

static int parse_hex(const char *s,double *v){char *e=NULL; *v=strtod(s,&e); return e && *e=='\0';}
int main(int argc,char **argv){
  if(argc!=3){fprintf(stderr,"usage: %s OUT.bin 'DSIR_C2_EXACT_ENDPOINT ...'\n",argv[0]); return 2;}
  const char *p=argv[2]; char z[32],tau[64],k[64],a[64],H[64],dm[64],tm[64],ri[64],rv[64];
  int n=sscanf(p,"DSIR_C2_EXACT_ENDPOINT z=%31s tau=%63s k=%63s a=%63s H=%63s delta_m=%63s theta_m=%63s rho_idm_iv=%63s rho_iv=%63s",z,tau,k,a,H,dm,tm,ri,rv);
  if(n!=9){fprintf(stderr,"malformed endpoint line\n"); return 3;}
  dsir_c2_record_v0_1 r;
  if(!parse_hex(tau,&r.tau)||!parse_hex(k,&r.k)||!parse_hex(a,&r.a)||!parse_hex(H,&r.H)||!parse_hex(dm,&r.delta_m)||!parse_hex(tm,&r.theta_m)||!parse_hex(ri,&r.rho_idm_iv)||!parse_hex(rv,&r.rho_iv)) return 4;
  FILE *f=fopen(argv[1],"wb"); if(!f) return 5; int ok=dsir_c2_record_write_v0_1(f,&r); if(fclose(f)!=0) ok=0; if(!ok) return 6;
  FILE *g=fopen(argv[1],"rb"); if(!g) return 7; if(fseek(g,0,SEEK_END)!=0){fclose(g);return 8;} long sz=ftell(g); fclose(g); if(sz!=64) return 9;
  fprintf(stderr,"DSIR_C2_SYNTHETIC_SERIALIZER_OK z=%s bytes=64\n",z); return 0;
}
