# DSIR research log — FS admission and FU self-healing

Date: 2026-09-07.

Exp073FS run `34067352681` attempt 2 was terminal-consumed. Artifact `10005532345` independently matched ZIP SHA256 `f878a49241dde97eb0ef1d24561719cf896a77d111c3a3b91725d4989b894d23`. Candidate A/B canonical SHA256 was exactly `77f3e314d76f85cb95ed8edade672575bfa0e40c3b10a831f380a6c6d5f977fd`, with `<f8 [39,12288] EE<-EE`, exact equality, all finite, ordered S1->S2, distinct fields, complete pre-prune chains and exact file-backed MCM proof. Exp073FT job `101632852284` independently admitted `WW_S1_S2` with `PASS_EXP073FT_WW_S1_S2_FILEBACKED_PROVENANCE_ADMISSION_V0_1`.

The automatically dispatched Exp073FU then exposed three sequential pre-science implementation/configuration defects, each recorded as `+0/+0` and never as scientific FAIL: run `34087011068` self-matched the inherited forbidden-token scanner; run `34089005639` exposed nested transform-of-transform shell corruption; run `34089259696` exposed missing frozen FA-base storage helper identities. No science/checkpoint artifact was created by those failures.

Repairs were minimal and prospective: scanner repair `07de7028dd2cb8baf1927ddcdbceef812bda45f3`; direct frozen FA-base wrapper repair `fa01c7d7a2d20cd222c1d208ac4e359ad1313710`; exact storage helper binding `614c5bca01280792b5ea0affe93729fbea174d40`, wrapper blob `4e6d24fc26760c7e7d31545837239148269d81d5`. Frozen science/arithmetic/domain/tolerances were unchanged.

Exp073FU run `34089383137`, head `11b62ebd73fe8bed03f31c559593756149c7fbc0`, hosted launch job `101639612389`, progressed successfully into home job `101639652148` and the frozen `WW_S1_S3 A/B gate`. No partial numerical output was inspected. Canonical workflow trigger was restored to dispatch-only after launch in commit `80f9f8f23f391edc3906218badb4a1dc4e535e6f`.

Exact next action is terminal consumption of run `34089383137`. Candidate PASS must be independently provenance-verified and admitted only by Exp073FV before any FW successor authority is allowed.
