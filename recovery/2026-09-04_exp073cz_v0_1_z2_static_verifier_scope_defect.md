# DSIR immutable recovery — Exp073CZ v0.1 raw Z2 from static-verifier scope defect

Date: 2026-09-04. Scope: DSIR only.

Authoritative hosted process: run/job/head `33871139536 / 101017142157 / 95a8154fa68f7c58a9c0762c3dff88a68344d7b9`; artifact `9935924269`; GitHub artifact ZIP digest and independently downloaded ZIP SHA256 both `0d7d03973fe1ec1144548881c2ff80106f9ac29e173bc65c50a7a79fe6780734`; raw receipt SHA256 `650b85c39aa97a7d920ed2ea75291d1c494fa23a8c7633d571fe160ae72036ad`.

Frozen raw classification: `Z2_IMPLEMENTATION_CONTRACT_FAIL`, accounting `+0/+0`; no DES-scale numerics, Wm_S3 authority, or Exp073BU activation occurred.

All source/provenance bindings, exact edges, checkpoint order, isolated A/B namespaces, one lens/source reconstruction site, exactly two NmtField constructors, same-field PCL/workspace handoff, stock write_to, forbidden get_coupling_matrix check, adapter composition, TE semantics, exact SHA plus numpy.array_equal comparator, no tolerance rescue, 8-worker declaration, nested-thread pins, source-head/fingerprint binding and historical/cross-replica exclusions passed. The only false field was `resume_final_before_expensive`.

First causal defect is in the frozen static verifier, not the production driver: it computed source positions using `src.index(...)` over the whole module, so the earlier function definition `fresh_or_restore_masks(...)` was encountered before `run_replica`. Inside `run_replica`, the intended order is already final-receipt restore -> fresh-workspace manifest restore -> fresh mask reconstruction only when workspace is absent. Historical Z2 remains immutable. The permitted prospective repair is verifier v0.2 scoped to the AST/source of `run_replica` only; production arithmetic and driver blob remain unchanged.