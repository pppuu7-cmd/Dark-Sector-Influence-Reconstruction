# Exp073R1 rerun-semantics correction

Date: 2026-08-28
Run: https://github.com/pppuu7-cmd/Dark-Sector-Influence-Reconstruction/actions/runs/33135622749

A rerun request was issued against the completed shard-0 job with the intent of obtaining a single transport probe. GitHub Actions materialized a new matrix attempt rather than an isolated visible shard-0-only attempt: new job IDs appeared for all eight matrix members. Seven of those jobs rapidly returned failure again while shard 0 entered `in_progress` at the time of this checkpoint.

This is an execution-topology observation only. It does not alter any scientific acceptance criterion, and it does not convert the transport failures into scientific FAILs.

No further rerun is authorized from this checkpoint while the current shard-0 attempt remains active. If shard 0 repeats the zero-byte DES range timeout, the next permitted repair is transport/checkpoint architecture only (or an immutable equivalent public-input delivery path with explicit checksum/byte binding), not another blind matrix rerun and not any change to Exp073P criteria.

G7 remains locked at Exp073R1 reproduction PASS before Exp073P support classification and all downstream stages.
