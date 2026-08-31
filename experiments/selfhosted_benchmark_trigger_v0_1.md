# DSIR self-hosted benchmark trigger v0.1

Purpose: benchmark the connected WSL self-hosted runner before assigning heavy DSIR workloads. This is infrastructure/performance QA only and changes no scientific readiness.

Benchmark source commit: `6e109f22e442e6ebf19020b9ae3690068eba9f8c`.
Workflow creation commit: `6d31ffa3535ea3314d882e33a949771099b06a75`.

Measure CPU inventory, memory inventory, OpenMP compute scaling from 1 thread to all WSL-visible logical CPUs, and memory-triad bandwidth. Use the result to choose a safe high-utilization thread count for later DSIR self-hosted computation.

Retriggered after workflow registration to dispatch the benchmark to the already-listening WSL runner.
