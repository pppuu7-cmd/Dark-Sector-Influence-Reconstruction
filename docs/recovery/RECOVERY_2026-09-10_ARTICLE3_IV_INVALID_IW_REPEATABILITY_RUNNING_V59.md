# DSIR recovery V59 — Exp073IV invalid; Exp073IW exact-repeatability diagnostic running

Scope: DSIR only.

Exp073IV run/job 34435415273 / 102739350045 completed FAILURE because its prospectively frozen exact-parent-max requirement was not met. The rerun itself remained NUMERICALLY_UNRESOLVED_EXP073IR with 0 invalid rows, f_B=0, retained 107 and intact covariance firewall. Rerun convergence maximum was 0.9998247463807128 versus parent 0.9998247463807295, so Exp073IV is SUPPORT_INVALID_PLUS_0_PLUS_0 and must not be rescued by tolerance. Artifact 10136032028, GitHub ZIP digest sha256:a32fb7e8bc357f1818e5ac7eeb0ff5d90c4685b3907e064fcd73ba68d7210ade.

Exp073IV nevertheless localized the two observed maxima without creating authority: alpha-left at z=0.7000000000000001, k=0.002502504647141259 Mpc^-1, production=15.004842008323749, dense=0.0026296528687907994, relative=0.9998247463807128; beta-symmetric at z=0.9351, k=0.01860440444314368 Mpc^-1, production=12.060403106488593, dense=0.0038719963413313963, relative=0.9996789496746383.

To distinguish deterministic arithmetic from run-to-run binary64 drift without weakening any gate, Exp073IW exact-repeatability diagnostic v0.1 was prospectively frozen at commit 577e41714b813142113a0cacfbed93272b30c0a4. Workflow commit a173451f5a3836bcf27cb53e33360497bdd86fc3. Trigger/head 70cf145eae559c57cbc2c8105c9d4c05ce097fb1. Authoritative run 34439055218 is queued at registration; GitHub-hosted ubuntu-24.04, home/self-hosted ownership none, checkpoint N/A.

Exp073IW executes the unchanged repaired Exp073IR twice sequentially in one pinned environment with independent scratch paths and compares complete JSON bytes plus exact binary64 convergence maxima. Valid outcomes REPEATABLE_EXACT_PLUS_0_PLUS_0 or NONREPEATABLE_EXACT_PLUS_0_PLUS_0 are both support-only; INVALID_INFRA_PLUS_0_PLUS_0 denotes execution/lineage failure. No outcome changes REL_TOL=1e-3, h=1e-4, domains, interpolation, atomization, Layer-B authority or covariance authorization.

Exact next action: terminal-consume run 34439055218, inspect raw log and artifact/digest, classify exact A/B repeatability. If repeatable, the cross-run parent/IV mismatch is environment/build-level and the next prospective diagnostic must isolate environment fingerprint differences. If nonrepeatable within one job, localize the first solver/output field exhibiting exact drift before any numerical-resolution experiment. If invalid infrastructure, repair only the first causal defect.

All frozen DSIR scientific boundaries and earlier admitted authorities remain unchanged.