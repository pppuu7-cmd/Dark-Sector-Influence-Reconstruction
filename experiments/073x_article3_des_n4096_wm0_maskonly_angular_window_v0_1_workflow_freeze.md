# Exp073X workflow freeze

Frozen 2026-08-30 before the Exp073X trigger commit and before any exact nside=4096 angular-window output.

workflow_last_modifying_commit: `6e383a076a0184dbe3a2c47938d176fd2142b500`

implementation_last_modifying_commit: `dd645f0060731e75737a569ad9ea50c9cdb9e15f`

preregistration_last_modifying_commit: `bb1755205f0944a0be5fcf714be705e8e76d356e`

The trigger commit must modify only `ci/exp073x_des_n4096_wm0_maskonly_angular_window_v0_1.trigger`.

Scientific rule: this is a real-data angular-operator execution pilot only. It must not evaluate redshift/physical-k support, retained coordinates, covariance, nuisance geometry, relation/null statistics or G8. Infrastructure failure is incomplete, not a support FAIL.
