# BuyanovGPT table — DSIR influence atlas

**Date:** 2026-08-25  
**Status:** live research atlas / hypothesis organizer  
**Important:** this is not a fundamental theory, not a no-hair theorem, and not evidence that the dark sector has exactly three parameters.

The nickname **BuyanovGPT table** refers to the DSIR classification of dark-sector models by observable influence channels rather than by microscopic model labels.

## 1. Hard lesson already established

The same microscopic direction can be null, degenerate, or strongly separated depending on the observation/response operator. Therefore model identity belongs to a **multi-channel influence trajectory**, not to one scalar response.

Current hard discriminator graph minimum hitting set for the frozen evidence graph:

`{metric slip, small-scale transfer, time/sign evolution}`.

This is a property of the current evidence graph only, not a proof of three fundamental parameters.

## 2. Candidate influence labels from the chat

The following labels are retained as provisional bookkeeping:

- `G` — growth/global structure-amplitude information;
- `T` — scale/transfer dependence;
- `tau` — time evolution;
- `I` — **scale-time nonseparability**, the irreducible `k x z` interaction left after additive `G+T+tau` projection;
- `S` — metric slip / anisotropic-stress / gravitational-potential information;
- `M` — small-scale/free-streaming/domain-localized information;
- `N` — interaction / exchange / non-conservation information;
- `B` — background/geometry information when independently relevant.

These are **response types**, not guaranteed independent parameters.

## 3. Core + Activation hypothesis: first falsification

The chat proposed

`Core ?= (G,T,tau)`

with mechanism-sensitive additional channels such as

`Activation ?= (S,M,N)`.

Experiment 045A made the core hypothesis operational by decomposing each common-grid response as

`R(z,k)=mu + T(k) + tau(z) + I(z,k)`.

### Hard result

Run `32883280742`, artifact `9576600500`, SHA256 `59839a2717646e50501a949cf5b310cb6c0e55f85dd6839fce2832c704ec28dd`.

Status:

`FAIL_COMPACT_G_T_TAU_CORE_LOW_K_V0_1`.

Therefore the **simple additive three-type core is falsified** on the common C1/C2/C3/C5 low-k theory block.

Key nonseparable fractions:

| Direction | `||I||/||R||` | interaction power | core power capture |
|---|---:|---:|---:|
| C1 smooth-w | 3.29% | 0.108% | 99.892% |
| C2 IDE negative-alpha | 0.000397% | ~`1.6e-9%` | ~100% |
| C2 IDE beta | 0.000741% | ~`5.5e-9%` | ~100% |
| C3 GDM cs2 | **21.29%** | **4.53%** | 95.47% |
| C3 GDM cv2 | **20.89%** | **4.36%** | 95.64% |
| C5 designer f(R) | **54.76%** | **29.99%** | **70.01%** |

This means that `T(k)` and `tau(z)` cannot in general be treated as independent additive summaries. **How scale dependence evolves in time is itself informative.**

Dropping `I` reduces GDM/f(R) acute angles from about `25.2-25.5 deg` to about `14.8-14.9 deg`. The largest pairwise distortion is IDE negative-alpha/f(R): **14.31 deg**.

### Revised working architecture

Do **not** replace the failed hypothesis by an untested four-parameter claim. The current evidence supports only the weaker organizer

`Structure fingerprint = (G, T, tau, I) + other channels`,

where `I` is now a **hard-required representation component for C5 on the tested block**, not yet a universal fundamental "hair".

## 4. Current family map

The table below distinguishes **validated facts** from **candidate labels**.

| Family | Validated influence facts | Current table interpretation |
|---|---|---|
| C0 LambdaCDM/GR | common response origin | origin / zero point |
| C1 smooth non-phantom DE | nonzero background/AP and structure response; additive core captures 99.89% structure power | background + largely separable growth/time response on current low-k block |
| C2 IDE | alpha/beta nonzero AP and structure responses; channel migration; additive core captures essentially all low-k structure power | exchange mechanism candidate `N`; tested structure is extremely close to additive `G+T+tau` |
| C3 GDM (`w=0`) | exact background/AP null; cs2/cv2 almost collinear in density/time; slip separates; ~4.4-4.5% structure power is nonseparable | perturbation-only direction; demonstrated `S` discriminator and non-negligible `I` |
| C4 thermal WDM | frozen low-k nearly blind, high-k transfer strongly nonzero | domain-localized/free-streaming candidate `M`; cannot be inserted into common low-k core matrix as zero; `I` status unknown until high-k/time extension |
| C5 designer f(R) | exact background/AP null; nonzero structure; scale-only close to GDM but time/full structure separate; density-velocity compression defect; ~30% structure power nonseparable | strongest current example that scale and time must be treated jointly; large `I` |

## 5. Representation dimension versus discrimination dimension

Keep two quantities conceptually separate:

- `N_repr`: minimum coordinates needed to reconstruct/approximate the response atlas;
- `N_disc`: minimum independent channels needed to distinguish different physical mechanisms.

A small `N_repr` does not imply a small `N_disc`. The hard GDM `cs2/cv2` example demonstrates why: their density/time fingerprints are nearly collinear while metric slip carries mechanism information.

Experiment 045A adds a second warning: even if separate `G`, `T`, and `tau` summaries appear intuitive, their additive combination can have insufficient `N_repr` because the joint `k x z` interaction carries information.

## 6. Dark-sector no-hair hypothesis

The black-hole analogy is retained only as a falsifiable organizing idea:

> many microscopic dark-sector models might project onto a much smaller stable observable influence space.

DSIR does **not** claim an analogue of the black-hole no-hair theorem. The first simple three-core candidate has already failed. Any revised low-dimensional basis must survive:

1. family expansion including C4's proper high-k domain;
2. gauge and cross-solver bridges;
3. observation/window/covariance projection;
4. family-prior and sampling changes;
5. channel removal;
6. withheld-family prediction.

## 7. Current research program

1. Continue the main model-comparison atlas and search for new hard cross-family regularities.
2. Preserve exact nulls, failed compressions, channel reversals, scale-time interaction and numerical/gauge limitations.
3. Test candidate low-dimensional coordinates without forcing the answer to three, four, or any preselected number.
4. Extend C4 WDM with its physically relevant high-k domain before any family-complete core claim.
5. Investigate whether `I(k,z)` has stable mechanism-specific patterns across GDM, f(R), IDE and future families.
6. Build a universal model only when `docs/UNIVERSAL_MODEL_READINESS.md` criteria are satisfied.
