#ifndef DSIR_C2_RECORDER_V0_1_H
#define DSIR_C2_RECORDER_V0_1_H

#include <math.h>
#include <stddef.h>
#include <stdio.h>

typedef struct dsir_c2_record_v0_1 {
  double tau;
  double k;
  double a;
  double H;
  double delta_m;
  double theta_m;
  double rho_idm_iv;
  double rho_iv;
} dsir_c2_record_v0_1;

static inline int dsir_c2_record_is_finite_v0_1(const dsir_c2_record_v0_1 *r) {
  return r != NULL &&
         isfinite(r->tau) && isfinite(r->k) && isfinite(r->a) && isfinite(r->H) &&
         isfinite(r->delta_m) && isfinite(r->theta_m) &&
         isfinite(r->rho_idm_iv) && isfinite(r->rho_iv);
}

static inline int dsir_c2_record_write_v0_1(FILE *fp, const dsir_c2_record_v0_1 *r) {
  if (fp == NULL || !dsir_c2_record_is_finite_v0_1(r)) return 0;
  const double payload[8] = {
      r->tau, r->k, r->a, r->H,
      r->delta_m, r->theta_m, r->rho_idm_iv, r->rho_iv};
  return fwrite(payload, sizeof(double), 8, fp) == 8;
}

#endif
