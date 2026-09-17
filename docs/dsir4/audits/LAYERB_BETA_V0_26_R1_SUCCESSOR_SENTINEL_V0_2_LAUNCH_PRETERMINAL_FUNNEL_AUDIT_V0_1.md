# DSIR Funnel Auditor — V0.26 R1 successor sentinel v0.2 launch/preterminal funnel audit

Date: 2026-09-17. Scope: DSIR only. GitHub repository/Actions are the durable scientific source of truth; chat is not authority.

Reviewed current main at start of review: `1fd68a9814ac987300710c4e67d080c7455efa34` (`Merge PR #202: launch exactly one V0.26 R1 successor sentinel v0.2`).

Reviewed active science workflow: run `35181812498`, workflow `360201395`, exact head `1fd68a9814ac987300710c4e67d080c7455efa34`, run #1 / attempt #1, event `push`.

At the last Actions recheck in this audit the target run is `in_progress/nonterminal`. No lane scientific values, lane failure/success pattern, decision values, partial artifacts or partial classification are used in this review. Completed response-blind authorization/provenance controls may be reviewed without consuming the nonterminal scientific result.

## Recovered gate chain

Repository recovery documents were stale relative to the actual repository. The authoritative chain on GitHub has advanced beyond the prior v0.3/v0.4 notes:

1. v0.5 explicit post-run failure-funnel chain completed and was durably consumed. Target run `35148542110` and terminal auditor run `35148573508` were each run #1 / attempt #1; chronology was target-terminal before terminal audit; exact dispatch histories were one-and-one; the independent post-runtime Critic classified governance/provenance `PASS_SCOPED` while the historical scientific result remained `NOT_EVALUATED`.
2. A first new successor sentinel v0.1 was prospectively authorized under a new identity. Run `35174721773`, run #1 / attempt #1, is terminal failure and is permanently consumed; it must not be rerun.
3. Response-blind diagnostic run `35177449482`, run #1 / attempt #1, localized that successor failure to GRID896 binary materialization dependence on NumPy CPU dispatch. Native NumPy 1.26.4 produced the exact frozen GRID896 bytes while the forced profile produced a different binary node payload; geometry and ratio were unchanged. CLASS was not invoked and no scientific response/covariance was read.
4. Independent diagnostic Critic verdict `PASS_SCOPED` authorized only a prospective design primitive: materialize the exact frozen GRID896 bytes under native dispatch, then consume those exact bytes inside the otherwise unchanged forced science runtime. It did not authorize science by itself.
5. PR #201 merge `d7ed277617cd91b74d4f734edafc1e8fff0ec57b` froze the repaired v0.2 executor, target workflow, terminal-history workflow, terminal launch authority and independent design Critic without a launch marker.
6. PR #202 merge `1fd68a9814ac987300710c4e67d080c7455efa34` added only the one-shot v0.2 launch marker and triggered the current exact target run.

## Authorization and prospective chronology

The predecessor v0.5 independent Critic explicitly required a new experiment identity, new nonce, new workflow identity and separate prospective authority before any successor science. The GRID896 diagnostic independent Critic later narrowed the supported repair primitive to native materialization of the already-frozen GRID896 bytes followed by exact-byte consumption inside the unchanged forced science runtime.

The v0.2 launch authority is `docs/dsir4/authority/LAYERB_BETA_V0_26_R1_SUCCESSOR_SENTINEL_SCIENCE_AUTHORIZATION_V0_2.json`, blob `f5932ce87acc392220ca2fa71abbade8c5899723`, status `TERMINAL_LAUNCH_AUTHORITY`, classification `AUTHORIZED_SCOPED`. It authorizes exactly one new experiment `LAYERB_BETA_V0_26_R1_SUCCESSOR_SENTINEL_SCIENCE_V0_2` with nonce `DSIR-V026R1-SUCCESSOR-20260917-B1-4C92E7A1`, requires run #1 / attempt #1, forbids historical reruns and same-nonce retries, and keeps full 107-row/full replay closed.

The independent v0.2 design Critic was frozen before launch and has verdict `PASS_SCOPED`. It binds executor blob `1f727056491a6f4997298bb63dba26589fd3ddec`, target-workflow blob `00bb68196c995079cad50da70be555d737d28ecb`, terminal-history-workflow blob `9dc4962288471fbcd0803d22cabe1182bfac8ed3`, and the parent diagnostic critic/consumption identities. It explicitly records numerical validity, exact-target validity and scientific criterion as `NOT_EVALUATED`.

The launch marker was added only after the authority and design Critic were on the prelaunch main. Comparing prelaunch main `d7ed277617cd91b74d4f734edafc1e8fff0ec57b` with launch head `1fd68a9814ac987300710c4e67d080c7455efa34` shows only one added path: `docs/dsir4/launch/LAYERB_BETA_V0_26_R1_SUCCESSOR_SENTINEL_LAUNCH_V0_2.json`. Therefore no executor, workflow, authority, threshold, data or decision object was changed in the launch step.

The launch marker binds exact authority, design-Critic, executor, target-workflow and terminal-history-workflow blobs and repeats the one-run/attempt/no-rerun/no-full-107 ceiling.

## Frozen scientific identity

V0.26 R1 remains bound to preregistration blob `545e5be589e0f8029d23db2edb4e2faad116c3a0` and contract blob `b510d8e97baf1c0b7b216c0605d83cdd029254e9`.

The v0.2 authority preserves:
- 107 retained rows = DES 53 + BOSS 54;
- retained-id SHA256 `44b57c6c910bc3612310ce415d773c8c180497528bfc5fc2927ce61da6ad40d7`;
- full-order SHA256 `bfaf582518cdbfd34b1e8392da83dac6b0885948bc31f2c29d4e48247c23af75`;
- response-blind plan artifact `10298655751`, ZIP SHA256 `9b8bdcf03cb05bc979e8c72135acac92232864a74dc1d510b579d8efb5cbb2a7`, inner SHA256 `c12bdb2a407de3f9e2c0c410719ae604d9b3516dabb76c9b1598340418ee8064`;
- CLASS commit `ac627d54e9ce196a08878d1ba33999819925d19c`;
- Python 3.12.3, NumPy 1.26.4, SciPy 1.17.1;
- 32 sentinel lanes, 14 CLASS constructions per eligible lane, mixed batches M076/M298/M300 with direct comparators D50/D00/D58;
- minimum 6 eligible lanes with >=3 native AVX512-active and >=3 native AVX512-inactive;
- `h=1e-4`, native `k_per_decade_for_pk=20`, `perturb_sampling_stepsize=0.00035`;
- alpha `3e-10`, beta `1e-12`;
- scientific strict `<1e-3`, technical strict `<1e-5`, requested-node binding `<=1e-12`.

No outcome-dependent threshold, precision or row selection change is authorized.

## GRID896 repair identity

The terminal diagnostic consumption and independent Critic support one narrow causal statement only: GRID896 binary materialization depends on NumPy CPU dispatch, while the tested geometry and ratio remain the same. Frozen/native payload SHA256 is `8499eb0f240b85581e0dcb804b841ba911c4b3a58e8fe15702aea134e40bd65d`; forced-profile reconstruction produced a different payload `1ad5c76772b193086b1f10bc8e150cc7095504c4e4c80fd50da6821a30750097`, with 247 differing nodes in the diagnostic.

The v0.2 executor implements exactly the supported repair primitive. It first materializes GRID896 under clean/native NumPy dispatch and refuses to proceed unless the raw 897 x binary64 bytes hash to the frozen `8499...` payload. It then launches the unchanged forced child with the exact byte file path in `DSIR_V026_R1_FROZEN_GRID896_BIN`; the inherited v0.1 reconstruction is monkey-patched only for `guarded_lattice(896)` to consume those bytes and still validates byte length, SHA256, finite/increasing geometry and the frozen contract. The forced NumPy mask remains required before the scientific child imports and solves CLASS.

This review found no source-level evidence that the v0.2 repair changes alpha/beta, CLASS inputs, target rows, scientific thresholds or requested-node criterion. It is a materialization repair, not a new scientific hypothesis.

## Hosted static/design controls

Response-blind GRID896 repair static run `35181631286`, workflow `360200575`, head `e25324612756c38c2435f6db1a22d74e701ed4ec`, is terminal `completed/success`, run #1 / attempt #1. Its only job `105074835330` completed success, including executor compilation and response-blind repair-boundary checks. This static run qualifies the repair primitive only; it is not a scientific result.

The later independent design Critic binds the final executor, target workflow and terminal-history workflow identities and keeps numerical/scientific validity `NOT_EVALUATED`.

## Current run provenance controls

Exact-head Actions enumeration for launch head `1fd68a9814ac987300710c4e67d080c7455efa34` returns exactly one workflow run: target run `35181812498`, workflow `360201395`, run #1 / attempt #1, event `push`.

The completed `authorize` job independently passed the exact live checks before any scientific lane result is admissible. Its logs show:
- checkout of exact head `1fd68a...`;
- `CURRENT_RUN_NUMBER=1`, `CURRENT_RUN_ATTEMPT=1`, event `push`;
- exact R1 contract, promotion authority, v0.2 executor, target workflow, terminal-history workflow, parent diagnostic Critic and diagnostic consumption blob bindings;
- exact experiment id and nonce;
- launch marker absent at the event-before SHA and added exactly once at the launch head;
- fresh target workflow history containing exactly the current run #1 / attempt #1.

The response-blind plan-materialization job also completed success. These completed controls may be audited while the target remains nonterminal. No lane result or decision output is used here.

## Terminal-history requirement

The v0.2 authority requires a separate terminal-history closure before any science promotion. Frozen terminal-history workflow blob `9dc4962288471fbcd0803d22cabe1182bfac8ed3` is triggered on completion of the v0.2 target workflow. It independently requires target run #1 / attempt #1, auditor run #1 / attempt #1, a fresh exact target-workflow history containing exactly one target run, and a unique decision artifact whose ZIP and inner JSON digests are recorded in a terminal receipt.

Because target run `35181812498` is still nonterminal, no terminal-history receipt is expected or admissible yet. A target result, even if eventually green, cannot be promoted until that separate terminal-history gate itself becomes terminal and is independently reviewed.

## Alternative explanations and counterexample search

The principal prior alternative explanation for the first successor failure — a scientific response failure — is not supported by the response-blind diagnostic. The supported cause is GRID896 binary identity under NumPy CPU dispatch. The v0.2 design addresses that exact cause without changing frozen science values.

Potential overclaim routes remain explicitly closed: a working GRID896 materialization does not prove numerical reproducibility of CLASS responses; a successful sentinel would not prove covariance/nuisance identifiability; a green CI run would not establish statistical/model validity or physical dark-sector evidence; and no sentinel outcome by itself authorizes the full 107-row traversal.

No deterministic source-level counterexample was found in the exact launch/authorization chain during this preterminal review. In particular, the previous dispatch-history issue is addressed for the current v0.2 target by an explicit `run_number==1`, `run_attempt==1`, fresh unique-run history check before science and a separate post-run terminal-history closure.

## Review result

Verdict: **CONFIRMED_SCOPED**.

Confirmed scope only: the exact PR #201/PR #202 prospective authorization and one-shot launch chain is consistent with prior terminal authorities and the independently localized GRID896 repair primitive; the launch step changed only the launch marker; exact live authorization/history controls passed before science; and the target run is the unique run #1 / attempt #1 for the v0.2 workflow.

Not confirmed: any lane numerical result, sentinel classification, interpolation/resolution/tolerance stability, scientific reproducibility, covariance/nuisance/statistical/model validity, dark-sector inference, or permission for the full 107-row replay. The current target workflow remains nonterminal and must not be rerun or selectively interpreted.

## Funnel position after review

`V0.25 TERMINAL -> V0.26 R1 FROZEN -> ORIGINAL SENTINEL CONSUMED PRE-SCIENCE -> V0.5 FAILURE-FUNNEL GOVERNANCE CLOSED -> SUCCESSOR V0.1 CONSUMED/TERMINAL FAILURE -> GRID896 RESPONSE-BLIND DIAGNOSTIC TERMINAL -> DIAGNOSTIC CRITIC PASS_SCOPED -> SUCCESSOR V0.2 PROSPECTIVELY FROZEN -> INDEPENDENT DESIGN CRITIC PASS_SCOPED -> EXACT ONE-SHOT V0.2 LAUNCH CONFIRMED_SCOPED -> TARGET RUN 35181812498 IN_PROGRESS/NONTERMINAL -> TERMINAL-HISTORY GATE PENDING -> FULL 107 ROW CLOSED`.

Effect remains `+0/+0`. Scientific frontier/readiness are not increased by this launch audit.

Next admissible gate: allow the already-running exact run `35181812498` to terminate without rerun. Do not consume partial lane/decision values. After target termination, require the frozen terminal-history workflow to become terminal, independently verify unique target/auditor histories, exact target head/run/attempt, decision artifact id/ZIP digest/inner digest and terminal receipt digest, then review the terminal sentinel classification against the frozen contract. Only a separate later terminal authority may decide whether any next Layer-B stage is admissible. Full 107 rows, covariance, whitening, nuisance marginalization, relation-null, `Wm_S3`, global 65537 and downstream statistical/physical inference remain closed.