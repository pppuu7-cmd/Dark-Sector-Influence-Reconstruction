# DSIR Article III recovery V140 — home runner profiled, 32769 excluded

Date: 2026-09-12. Scope: DSIR only.

## Scientific frontier unchanged
Canonical 8193->16385 remains independently verified NOT_CONVERGED with max relative component difference `0.012484060640679777` versus frozen strict `<1e-3`. No 16385->32769 scientific execution is authorized or has occurred. Covariance restriction remains unauthorized and Wm_S3 remains closed.

## New V140 operational evidence
The user started the existing WSL self-hosted runner `DSIR-HOME-PC` (runner 2.337.0). A superseded generic self-hosted job was picked up, but terminated before heavy compute because `gfortran` was absent. The repeated attempt likewise terminated before heavy compute. This creates no scientific or resource authority.

A dedicated environment probe run `34663628847`, job `103471030533`, artifact `10288042655`, ZIP SHA256 `dcc543bd160857ec62985c57f07f0280201c14c01bb79351dd49821fab037b71`, measured:
- WSL2 `MemTotal=6067840 kB` (~5.79 GiB);
- `MemAvailable=5382384 kB` at probe;
- `SwapTotal=16777216 kB` (16 GiB), fully free at probe;
- 8 visible logical CPUs, Intel i5-1235U;
- Python/GCC/G++/make/pkg-config/cmake/git present;
- `gfortran` absent;
- GSL pkg-config absent;
- non-interactive sudo unavailable.

A host-memory probe run `34663666364`, job `103471138939`, artifact `10288262607`, ZIP SHA256 `ec01e9d561bed83397ffda320c4fef4b42b0ab505239e57a38bf619827bfc88d`, used WSL interop and measured Windows total physical memory `8245334016` bytes (~7.68 GiB). The existing `.wslconfig` is:

```
[wsl2]
memory=6GB
processors=8
swap=16GB
vmIdleTimeout=86400000
localhostForwarding=true
```

Therefore the physical host itself cannot satisfy the V139 clean-RAM control envelope (`MemTotal >= 62914560 kB`, `SwapTotal==0`). This is not merely a WSL configuration cap; Windows physical RAM is also far below the required control envelope.

Durable authority: `docs/dsir4/authority/DSIR_HOME_PC_RESOURCE_PROFILE_V0_1.json`.

## Runner policy after V140
- `DSIR-HOME-PC` MAY be used for scientifically admissible independent DSIR tasks whose measured/expected memory footprint fits the ~6 GiB WSL RAM envelope, after required build dependencies are available.
- It MUST NOT run the V139 clean-RAM 32769 reference control.
- It MUST NOT run the V0.3 32769 four-role resource lifecycle.
- It MUST NOT run the canonical 16385->32769 production science.
- The V139 clean-RAM route remains blocked on a separate high-physical-RAM runner.

The old superseded generic run `34550495778` is now terminal failure rather than queued. Its latest attempt job `103470879253` failed at native prerequisites before heavy compute, so the previous queued ownership hazard is closed.

## Readiness
`ARTICLE3_REPOSITORY_READINESS: 68%`.

Funnel-freeze/scientific frontier: `67%`.

`WORKING_PLAN_COMPLETION: 90%`.

The +1 operational increment closes the ambiguity about whether the user's available home runner could satisfy the clean 32769 resource gate and closes the stale queued-run ownership hazard. It does not advance scientific convergence.

## Exact next high-value actions
1. Keep `DSIR-HOME-PC` available for lower-memory DSIR diagnostics/compute after installing the missing build dependencies when such tasks are scientifically useful.
2. For the 32769 convergence path, provision a separate isolated nominal-64-GiB-class physical-RAM runner with swap disabled and frozen `dsir-32769-highmem` registration provenance.
3. Run exactly one V139 clean-RAM `reference` control there; consume and classify its artifact before any four-role lifecycle.
4. Production science remains forbidden until the real resource chain and live authorization pass.
