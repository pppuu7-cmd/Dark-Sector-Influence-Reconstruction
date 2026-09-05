# Exp073EA — WW cross-field serialization-state exactness diagnostic v0.1

Status: preregistered support-only diagnostic. Accounting `+0/+0`; no science authority and no production authorization.

## Motivation

Exp073DY showed a strict but last-bit distinction between an in-memory PyMaster 2.7 `WW_S0_S1` workspace and the same workspace after `write_to()` / `read_from()`. The saved-LU DSIR route also differed from the original in-memory reference. Exp073EA determines whether the serialized workspace defines its own exact deterministic numerical state and whether the saved-LU route reproduces that official PyMaster reload state bit-for-bit.

## Frozen scientific geometry

- PyMaster/NaMaster 2.7;
- deterministic distinct spin-2 masks S0 and S1 exactly as Exp073DU/DV/DY;
- `NSIDE=16`, `nl=48`, `ncls=4`;
- edges `[0,6,12,18,24,30,36,42,48]`;
- ordered `W01 = workspace(S0,S1)`;
- full shape `[4,8,4,48]`;
- selected semantics `wins[0,:,0,:] = EE<-EE`;
- no tolerance, rounding, smoothing, averaging, or approximate-equality rescue.

## Required chronology

Within one process:

1. construct `W01`;
2. serialize `W01` to `pre.fits` **before any call** to `get_bandpower_windows()`;
3. call in-memory `get_bandpower_windows()` twice (`direct_1`, `direct_2`);
4. serialize the same workspace to `post.fits` after those calls;
5. reload `pre.fits` into a new `NmtWorkspace` and call windows twice (`reload_pre_1`, `reload_pre_2`);
6. reload `post.fits` into another workspace and call windows once (`reload_post`);
7. extract `WSP_PRIMARY`, `MCM_BINNED`, and `MCM_PERM` from `pre.fits` and `post.fits` and compare them exactly;
8. run the frozen Exp073DY saved-LU downstream from the `pre.fits` numerical extensions;
9. compare saved-LU output to `reload_pre_1` exactly, in addition to comparisons against the original in-memory reference.

## Required exact checks

The receipt must record exact `numpy.array_equal`, SHA256, maximum absolute difference, nonzero-difference counts, finiteness, and selected-EE comparisons for all relevant pairs.

The diagnostic must answer separately:

- **in-memory repeatability:** `direct_1 == direct_2` bit-for-bit;
- **reload repeatability:** `reload_pre_1 == reload_pre_2` bit-for-bit;
- **serialization numerical-state mutation:** whether `WSP_PRIMARY`, `MCM_BINNED`, or `MCM_PERM` differ between pre/post writes;
- **pre/post reload equality:** whether `reload_pre_1 == reload_post` bit-for-bit;
- **saved-LU reload equivalence:** whether saved-LU output equals official `reload_pre_1` bit-for-bit, full array and selected EE.

## Diagnostic tokens

- `PASS_EXP073EA_SAVED_LU_EXACT_OFFICIAL_RELOAD_STATE_V0_1` only if in-memory and reload calls are each internally repeatable, pre/post serialized numerical extensions are identical, pre/post reload windows are identical, and saved-LU full + selected EE are bit-for-bit equal to official PyMaster reload-from-FITS output.
- `DIAG_EXP073EA_RELOAD_STATE_EXACT_BUT_SAVED_LU_MISMATCH_V0_1` if the official reload state is deterministic but saved-LU does not exactly reproduce it.
- `DIAG_EXP073EA_SERIALIZATION_NUMERICAL_STATE_MUTATES_V0_1` if pre/post serialized numerical extensions differ.
- `DIAG_EXP073EA_INPROCESS_NONREPEATABILITY_V0_1` if repeated calls on the same workspace are not exact.
- otherwise fail closed as `DIAG_EXP073EA_UNRESOLVED_V0_1`.

A PASS here is **support-only**. It would establish an exact checkpoint-state equivalence route, not equivalence to the original pre-serialization in-memory window and not Article-3 science authority.

## Execution firewall

GitHub-hosted only. It must not dispatch, cancel, rerun, or modify the active self-hosted Exp073DT science job.
