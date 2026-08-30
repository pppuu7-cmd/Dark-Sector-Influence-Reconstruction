# Exp073X2 workflow freeze v0.1

This record freezes the prospective implementation chain before the hosted trigger.

- prereg_last_modifying_commit: `efe8a4e17638dfd9568fa710e24f56cd10526c6a`
- replica_code_last_modifying_commit: `df2eecd73ed0d8de080348ba155a2f1a3e84d7e1`
- aggregator_code_last_modifying_commit: `8ec6f94ea9ddf3cc0a4c98e5af696d28d995b2b3`
- workflow_last_modifying_commit: `a14047090d46e024965d1bd76b60830ef21616e9`

Frozen interpretation:

1. Exp073X remains `INCOMPLETE_INFRASTRUCTURE_RESOURCE_CANCELLED_NO_AUTHORITY_REUSE`.
2. X2 is an infrastructure/repeatability repair only. It preserves the exact real-DES `NSIDE=4096`, NaMaster 2.7, 39-band, `TE <- TE` angular operator contract.
3. Replica A and replica B are independent hosted computations and must each persist one exact workspace before any cross-replica comparison.
4. Only the downstream aggregator may issue the X2 repeatability PASS token, and only after exact metadata, canonical SHA-256, and `numpy.array_equal` agreement.
5. No X2 result closes G7/G8/G9, performs Layer A, reads covariance/G8, or increases Article 3 scientific readiness above 52%.
6. A cancellation or missing replica artifact is INCOMPLETE; it is never re-labelled scientific FAIL or PASS.

The next commit touching the trigger file is execution-only and must not modify preregistration, implementation, aggregator, or workflow semantics.
