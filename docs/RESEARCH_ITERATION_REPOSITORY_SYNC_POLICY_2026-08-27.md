# DSIR research-iteration repository synchronization policy — 2026-08-27

**Status:** persistent project operating rule requested by the project owner.

After every completed DSIR research iteration, the repository must be brought up to date before the next scientific iteration is treated as current.

At minimum, each iteration must leave a repository record containing whichever of the following apply:

- the preregistration that existed before any new scientific output;
- implementation/workflow changes actually used;
- immutable run/job/artifact provenance for executed computations;
- machine-readable key metrics or result artifact bindings;
- the exact scientific classification under the frozen criteria;
- preservation of permanent negative results and infrastructure-only failures;
- the current G7/G8/G9 state;
- a recovery/checkpoint note sufficient to continue from another chat/session;
- the next admissible step and its scientific boundary.

No result may be described as merged, executed, PASS, FAIL, or gate-closing unless that state has actually been verified from the repository/Actions record.

A scientific threshold or PASS/FAIL criterion may not be edited after the corresponding numerical output is observed. Any causal corrective experiment must receive a new prospective preregistration and experiment identifier.

This rule is methodological/project-state bookkeeping only; it does not itself alter any scientific gate or historical classification.
