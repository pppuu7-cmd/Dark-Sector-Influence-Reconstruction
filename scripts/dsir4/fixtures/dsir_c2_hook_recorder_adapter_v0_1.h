#ifndef DSIR_C2_HOOK_RECORDER_ADAPTER_V0_1_H
#define DSIR_C2_HOOK_RECORDER_ADAPTER_V0_1_H

#include <stdio.h>
#include "dsir_c2_recorder_v0_1.h"

static inline int dsir_c2_pretransform_observe_to_file_v0_1(
    FILE *fp,
    const double tau,
    const double k,
    const double a,
    const double H,
    const double delta_m,
    const double theta_m,
    const double rho_idm_iv,
    const double rho_iv) {
  const dsir_c2_record_v0_1 r = {
      tau, k, a, H, delta_m, theta_m, rho_idm_iv, rho_iv};
  return dsir_c2_record_write_v0_1(fp, &r);
}

#endif
