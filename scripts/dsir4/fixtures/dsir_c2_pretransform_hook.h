#ifndef DSIR_C2_PRETRANSFORM_HOOK_H
#define DSIR_C2_PRETRANSFORM_HOOK_H

static inline void dsir_c2_pretransform_observe(
    const double tau,
    const double k,
    const double a,
    const double H,
    const double delta_m,
    const double theta_m,
    const double rho_idm_iv,
    const double rho_iv) {
  (void)tau;
  (void)k;
  (void)a;
  (void)H;
  (void)delta_m;
  (void)theta_m;
  (void)rho_idm_iv;
  (void)rho_iv;
}

#endif
