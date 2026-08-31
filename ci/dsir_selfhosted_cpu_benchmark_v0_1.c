#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <math.h>

#define COMPUTE_N 262144
#define COMPUTE_INNER 128
#define MEM_N (8u * 1024u * 1024u)

static double run_compute(int threads, double target_s, double *checksum, long long *steps_out) {
    double t0 = omp_get_wtime();
    double elapsed = 0.0;
    long long chunks = 0;
    double total = 0.0;
    do {
        double sum = 0.0;
        #pragma omp parallel for num_threads(threads) schedule(static) reduction(+:sum)
        for (int i = 0; i < COMPUTE_N; ++i) {
            double x = 0.5 + (double)(i & 1023) * 0.000001;
            for (int k = 0; k < COMPUTE_INNER; ++k) {
                x = x * 1.00000011920928955078125 + 0.00000095367431640625;
                x = x - 0.00000001 * x * x;
            }
            sum += x;
        }
        total += sum;
        ++chunks;
        elapsed = omp_get_wtime() - t0;
    } while (elapsed < target_s);
    long long steps = chunks * (long long)COMPUTE_N * (long long)COMPUTE_INNER;
    *checksum = total;
    *steps_out = steps;
    return (double)steps / elapsed / 1.0e6;
}

static double run_memory_triad(int threads, double target_s, double *a, double *b, double *c) {
    const double scale = 1.00000011920928955078125;
    #pragma omp parallel for num_threads(threads) schedule(static)
    for (size_t i = 0; i < MEM_N; ++i) a[i] = b[i] + scale * c[i];

    long long reps = 0;
    double t0 = omp_get_wtime();
    double elapsed = 0.0;
    do {
        #pragma omp parallel for num_threads(threads) schedule(static)
        for (size_t i = 0; i < MEM_N; ++i) a[i] = b[i] + scale * c[i];
        ++reps;
        elapsed = omp_get_wtime() - t0;
    } while (elapsed < target_s);

    volatile double guard = a[(size_t)(threads * 131u) % MEM_N];
    (void)guard;
    const double bytes = (double)reps * (double)MEM_N * 3.0 * sizeof(double);
    return bytes / elapsed / 1.0e9;
}

int main(int argc, char **argv) {
    const char *out_path = argc > 1 ? argv[1] : "benchmark.json";
    omp_set_dynamic(0);
    int logical = omp_get_num_procs();
    if (logical < 1) logical = 1;

    int levels[32];
    int nlevels = 0;
    int t = 1;
    while (t < logical && nlevels < 31) {
        levels[nlevels++] = t;
        if (t > logical / 2) break;
        t *= 2;
    }
    if (nlevels == 0 || levels[nlevels - 1] != logical) levels[nlevels++] = logical;

    double *a = NULL, *b = NULL, *c = NULL;
    if (posix_memalign((void **)&a, 64, MEM_N * sizeof(double)) ||
        posix_memalign((void **)&b, 64, MEM_N * sizeof(double)) ||
        posix_memalign((void **)&c, 64, MEM_N * sizeof(double))) {
        fprintf(stderr, "memory allocation failed\n");
        return 2;
    }

    #pragma omp parallel for schedule(static)
    for (size_t i = 0; i < MEM_N; ++i) {
        b[i] = 1.0 + (double)(i & 255) * 1e-6;
        c[i] = 2.0 - (double)(i & 127) * 1e-6;
        a[i] = 0.0;
    }

    double compute[32], memory_bw[32], checksum[32];
    long long steps[32];
    for (int i = 0; i < nlevels; ++i) {
        compute[i] = run_compute(levels[i], 1.20, &checksum[i], &steps[i]);
        memory_bw[i] = run_memory_triad(levels[i], 0.60, a, b, c);
        fprintf(stderr, "threads=%d compute_Msteps_s=%.3f memory_GB_s=%.3f\n",
                levels[i], compute[i], memory_bw[i]);
    }

    FILE *f = fopen(out_path, "w");
    if (!f) return 3;
    fprintf(f, "{\n");
    fprintf(f, "  \"benchmark\": \"DSIR_SELFHOSTED_CPU_BENCHMARK_V0_1\",\n");
    fprintf(f, "  \"logical_cpus_visible\": %d,\n", logical);
    fprintf(f, "  \"sysconf_online_cpus\": %ld,\n", sysconf(_SC_NPROCESSORS_ONLN));
    fprintf(f, "  \"compute_kernel\": {\"unit\": \"million_recurrence_steps_per_second\", \"inner_iterations\": %d, \"outer_size\": %d},\n", COMPUTE_INNER, COMPUTE_N);
    fprintf(f, "  \"memory_kernel\": {\"unit\": \"GB_per_second\", \"working_set_bytes\": %zu},\n", (size_t)MEM_N * sizeof(double) * 3u);
    fprintf(f, "  \"results\": [\n");
    for (int i = 0; i < nlevels; ++i) {
        double speedup = compute[i] / compute[0];
        double efficiency = speedup / (double)levels[i];
        fprintf(f,
                "    {\"threads\": %d, \"compute_msteps_s\": %.9f, \"compute_speedup\": %.9f, \"parallel_efficiency\": %.9f, \"memory_gb_s\": %.9f, \"steps\": %lld, \"checksum\": %.17g}%s\n",
                levels[i], compute[i], speedup, efficiency, memory_bw[i], steps[i], checksum[i],
                (i + 1 == nlevels) ? "" : ",");
    }
    fprintf(f, "  ]\n}\n");
    fclose(f);

    free(a); free(b); free(c);
    return 0;
}
