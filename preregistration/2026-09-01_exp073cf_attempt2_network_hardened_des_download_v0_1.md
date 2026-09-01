# Exp073CF attempt2 — network-hardened DES download v0.1

Date: 2026-09-01
Experiment: Exp073CF / Wm_S2
Classification: prospective infrastructure-only retry

## Predecessor terminal state

Exp073CF attempt1 run `33546929256` is terminal `completed/cancelled`.

- replica A job `99986640839` failed before spill preflight/PCL/heavy computation while downloading the exact DES Y1 lens mask;
- log terminated with `curl: (92) HTTP/2 stream 1 was not closed cleanly: INTERNAL_ERROR (err 2)` after only about 15.95 MiB of the 99.75 MiB response had arrived;
- replica B job `99986641160` was manually cancelled on the same DES-download step before any PCL/scientific computation;
- no complete comparator input, compact matrix, finalizer output, or scientific authority was produced;
- predecessor classification is `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CF_ATTEMPT1`, readiness delta `+0/+0`.

## Frozen scientific contract

Attempt2 MUST NOT alter any scientific input, arithmetic, support, acceptance rule, exact comparator, finalizer, thread contract, banding, or checkpoint arithmetic from the activated Exp073CF attempt1 contract.

Frozen items include:

- Wm_S2, `NSIDE=4096`, true ell `0..12287`, 39 bands, `TE <- TE`;
- exact DES Y1 lens mask bytes `104595840` and SHA-256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- source R1 run `33270843577` and artifact digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- memory-stable PCL helper last-modifying commit `5423976c09d5ee338d1a7894ce143faf1bb88225`;
- production/finalizer helper `d77b7ba88801f6788f3d386e72b445c7859c7153`;
- corrected independent A/B authority-tail commit `80c273d89f20cd91065b18236b50060328d33ae8`;
- range helper `fa971eb4ef8c47e81eb0bb4e13eeb76f7cf42e22`;
- stream driver `583c34420d5f02a1ac8e77efb9625bbc3ab73de8`;
- BW helper `9fb0ecb79986cf5f542760377533a685745b31e2`;
- checkpoint utility `0b0324afb69acb16cbea97bb924b9be48f303dde` and checkpoint sync `96886916b41dce7f0a40807622928c841ef5fc58`;
- `OMP_NUM_THREADS=8`, BLAS-style pools=1, `OMP_DYNAMIC=FALSE`, matrix `max-parallel=1`;
- local spill floor `2684354560` bytes;
- exact compact A/B comparator and independent A/B finalizers; no tolerance/ULP/rounding/averaging/smoothing/majority/preferred-replica rescue.

## Sole authorized infrastructure change

Only the transport mechanics of the DES mask download may change:

1. force curl HTTP/1.1 instead of HTTP/2;
2. enable retries for transport errors with `--retry-all-errors`;
3. use a persistent partial file under runner temp and `--continue-at -` so a retry/run can resume instead of restarting from byte zero;
4. keep fail-closed final validation of exact byte count and SHA-256 before the file is admitted as a scientific input.

No cached/partial file may bypass the final exact size/SHA checks. A server that does not honor range requests may cause curl to restart; this is infrastructure behavior only.

## Classification rules

- failure before complete valid A/B comparator inputs => infrastructure incomplete, `+0/+0`;
- exact A/B mismatch after valid comparator inputs => scientific repeatability FAIL;
- exact terminal PASS may become authority only after immutable run/artifact/digest capture and separate readiness-ledger inspection;
- attempt2 never changes Article-3 readiness merely by executing successfully as infrastructure.

## Home environment observation

User-reported WSL environment before attempt2: `nproc=8`, total memory about `5.8 GiB`, swap `16 GiB`, root filesystem free about `949 GiB`. This is infrastructure context, not a scientific criterion.
