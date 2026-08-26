# Gate update — Exp054C / F27 — 2026-08-26

## Exp054C prospective C7 common-slope test

**Result: HARD FAIL for candidate v0.1.**

The Exp054A relation

`C = Delta ln(k_R_geo) / Delta ln(k_source)`

used a raw full-response `R^2` scale centroid and was calibrated only on C3 GDM + C5 designer-f(R). Before any C7 response, the acceptance interval was frozen as

`[0.0022992620786061375, 0.09951219222831723]`.

The first science-evaluable C7 IDM-DR run `32920776596` returned

`C={-1.3855941363,-0.6685100505,-0.2190645818,-0.07156512047}`.

All four adjacent steps have the opposite sign and are outside the frozen interval.

Therefore:

- **G7: OPEN.** The proposed common quantitative relation v0.1 is falsified, not established.
- **G8: OPEN.** The withheld C7 mechanism rejected the relation; no withheld-survival pass exists for this candidate.
- **G9: OPEN.** No action/dynamics reconstruction follows.

The broad characteristic-scale/epoch organizing hypothesis remains supported by earlier mechanism-native results, but it is not upgraded to a law.

## Method consequence

Do not recalibrate Exp054A after C7. A new relation must receive a new version and a new withheld mechanism. C7 may be used for retrospective diagnosis and future within-C7 stability tests, but not as unseen G8 evidence for a relation designed after Exp054C.

## Post-gate clue

C7 has `chi_I~1e-8..1e-10` on the frozen low-k grid and the failed `R^2` centroid accumulates `69.2% -> 99.4%` of its weight at the `k=0.1 h/Mpc` endpoint. This identifies endpoint-amplitude domination as a concrete failure mode for the common centroid.

A separate endpoint-normalized half-transition coordinate is promising but currently retrospective only.
