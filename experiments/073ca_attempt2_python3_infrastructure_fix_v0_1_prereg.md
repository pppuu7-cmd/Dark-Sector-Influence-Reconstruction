# Exp073CA attempt 2 — infrastructure-only Python 3 binding fix v0.1

**Project:** DSIR only.  
**Frozen prospectively:** 2026-09-01, after Exp073CA attempt 1 stopped before any PCL, coupling matrix, compact band, checkpoint, finalizer or scientific comparator input was produced.  
**Classification of attempt 1:** `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`; `+0 Verified / +0 Draft-data`.

## Observed attempt-1 failure

Run `33446586747`, self-hosted job `99666949361` on runner `DSIR-HOME-PC` completed checkout successfully and then failed in the prospective binding-verification shell at the command `python - <<'PY'` with exit 127: `python: command not found`.

All subsequent scientific/execution steps were skipped. In particular the run did **not** create a Wm_S2 PCL, compile or call the streaming helper, run the mandatory exact preflight, restore/create a scientific checkpoint, compute a compact band, produce two comparator inputs, or execute a finalizer.

Therefore no scientific result exists from attempt 1 and no acceptance criterion has been observed against scientific data.

## Sole permitted change for attempt 2

Change only the pre-environment binding-verification interpreter invocation from:

```text
python - <<'PY'
```

to:

```text
python3 - <<'PY'
```

The self-hosted runner has `/usr/bin/python3` available as part of the Linux base environment used for shell infrastructure checks. The proven cached NaMaster environment bootstrap remains unchanged and all scientific Python execution continues through the explicitly bound `${NMT_PY}` interpreter after that bootstrap.

## Immutable scientific contract

Everything in `experiments/073ca_article3_wm_s2_checkpoint_streaming_track_a_v0_1_prereg.md` remains unchanged, including:

- task `Wm_S2` and Wm signature `(0,2,0,2)`;
- real DES Y1 authorities, `NSIDE=4096`, ell `0..12287`, 39 frozen bands;
- exact BW helper arithmetic and compiler flags;
- complete-band-only checkpoint boundaries and maximum 4-band chunks;
- 8-thread independent-band scheduling only;
- two independent replicas A/B;
- exact compact `numpy.array_equal` plus canonical `<f8` SHA comparator;
- unchanged Exp073AZ Wm finalizer path;
- exact final comparator;
- no tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue;
- Exp073BD remains forbidden;
- G8 remains forbidden.

No scientific code, input, edge, thread count, comparator, threshold, finalizer or authority label may change under this infrastructure fix.

Attempt 2 requires a newly frozen workflow commit, an updated immutable binding receipt referencing this preregistration and that workflow commit, and a new trigger commit. The first attempt remains permanently recorded as infrastructure incomplete.
