# Exp073HP — C2 HO first-request failure diagnostic v0.1

Status: **PROSPECTIVELY FROZEN BEFORE DIAGNOSTIC EXECUTION**. Scope: DSIR only; infrastructure/runtime diagnosis only.

Parent failure: Exp073HO run `34229170304`, job `102070681656`, failed in the frozen 28-request execution step after binding verification and exact post-HM build succeeded. The workflow redirected the first solver request's stdout/stderr to ephemeral files and exited before upload, so the first causal solver message is not present in the terminal Actions log.

This diagnostic reruns **only the same first frozen request** `z=0.295`, physical `k=0.00067 Mpc^-1`, model point `(alpha_idm_iv,beta_idm_iv)=(0,0)`, using the same pinned parent, post-HM patch stack, baseline SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`, p8 SHA256 `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`, exact `DSIR_C2_EXACT_Z=0.295`, and appended `k_output_values = 0.00067`.

No coordinate/config/tolerance/arithmetic change is permitted. The diagnostic must capture the solver exit code and, only on nonzero exit, expose its diagnostic stdout/stderr with any `DSIR_C2_EXACT_ENDPOINT` record line removed. It must not serialize or upload a packet and cannot create raw/scientific authority.

PASS means only that the first causal runtime failure message was made observable. Classification is always `INFRASTRUCTURE_DIAGNOSTIC_PLUS_0_PLUS_0`; `raw_record_set_admitted=false`; `decoded=false`; `scientific_model_authority_created=false`.
