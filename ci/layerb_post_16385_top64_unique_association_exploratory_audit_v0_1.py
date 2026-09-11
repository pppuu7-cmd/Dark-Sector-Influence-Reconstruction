#!/usr/bin/env python3
import argparse
import json
import math
from pathlib import Path


def average_ranks(values):
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i + 1
        while j < len(order) and values[order[j]] == values[order[i]]:
            j += 1
        rank = (i + 1 + j) / 2.0
        for k in range(i, j):
            ranks[order[k]] = rank
        i = j
    return ranks


def pearson(x, y):
    mx = sum(x) / len(x)
    my = sum(y) / len(y)
    dx = [v - mx for v in x]
    dy = [v - my for v in y]
    num = sum(a * b for a, b in zip(dx, dy))
    den = math.sqrt(sum(a * a for a in dx) * sum(b * b for b in dy))
    return num / den


def spearman(x, y):
    return pearson(average_ranks(x), average_ranks(y))


def fisher_greater(a, b, c, d):
    n = a + b + c + d
    row1 = a + b
    col1 = a + c
    lo = max(0, row1 - (n - col1))
    hi = min(row1, col1)
    denom = math.comb(n, row1)
    return sum(math.comb(col1, x) * math.comb(n - col1, row1 - x) / denom for x in range(max(a, lo), hi + 1))


def odds_ratio(a, b, c, d):
    return (a * d) / (b * c)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--census', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    src = json.load(open(args.census))
    assert src['classification'] == 'POST_16385_TOP64_ROLE_CANCELLATION_CENSUS_PASS_PLUS_0_PLUS_0'
    assert src['atom_count'] == 64
    assert src['max_primary_reproduction_relative_error'] == 0.0

    unique = {}
    for atom in src['atoms']:
        s = atom['source_atom']
        key = (s['block'], s['z_binary64_hex'], s['target_k_binary64_hex'], s['component'])
        pair = (atom['primary_min_cancellation_scale'], atom['primary_response_cross_grid_relative_difference'])
        if key in unique:
            assert unique[key] == pair
        else:
            unique[key] = pair

    pairs = list(unique.values())
    assert len(pairs) == 58
    scales = [p[0] for p in pairs]
    discrepancies = [p[1] for p in pairs]
    high = [d >= 1e-3 for d in discrepancies]
    assert sum(high) == 19

    rho = spearman(scales, discrepancies)

    order = sorted(range(len(pairs)), key=lambda i: scales[i])
    q1 = set(order[:15])
    q1_high = sum(high[i] for i in q1)
    q1_low = len(q1) - q1_high
    rest_high = sum(high[i] for i in range(len(pairs)) if i not in q1)
    rest_low = (len(pairs) - len(q1)) - rest_high
    q1_p = fisher_greater(q1_high, q1_low, rest_high, rest_low)
    q1_or = odds_ratio(q1_high, q1_low, rest_high, rest_low)

    lower_half = set(order[:29])
    lh_high = sum(high[i] for i in lower_half)
    lh_low = len(lower_half) - lh_high
    uh_high = sum(high[i] for i in range(len(pairs)) if i not in lower_half)
    uh_low = (len(pairs) - len(lower_half)) - uh_high
    half_p = fisher_greater(lh_high, lh_low, uh_high, uh_low)
    half_or = odds_ratio(lh_high, lh_low, uh_high, uh_low)

    high_scales = sorted(scales[i] for i in range(len(scales)) if high[i])
    low_scales = sorted(scales[i] for i in range(len(scales)) if not high[i])
    med_high = high_scales[len(high_scales)//2]
    med_low = low_scales[len(low_scales)//2]

    result = {
        'schema': 'LAYERB_POST_16385_TOP64_UNIQUE_ASSOCIATION_EXPLORATORY_AUDIT_V0_1',
        'classification': 'POST_16385_TOP64_UNIQUE_ASSOCIATION_EXPLORATORY_PASS_PLUS_0_PLUS_0',
        'effect': '+0/+0',
        'exploratory_post_hoc': True,
        'source_atom_count': 64,
        'unique_physical_atom_count': 58,
        'unique_count_ge_1e_3': 19,
        'unique_spearman': rho,
        'lowest_scale_quartile_vs_rest': {
            'table_high_low': [[q1_high, q1_low], [rest_high, rest_low]],
            'odds_ratio': q1_or,
            'fisher_exact_one_sided_p': q1_p
        },
        'lower_half_vs_upper_half': {
            'table_high_low': [[lh_high, lh_low], [uh_high, uh_low]],
            'odds_ratio': half_or,
            'fisher_exact_one_sided_p': half_p
        },
        'median_cancellation_scale_ge_1e_3': med_high,
        'median_cancellation_scale_lt_1e_3': med_low,
        'median_scale_ratio_high_to_low': med_high / med_low,
        'class_solver_invoked': False,
        'scientific_classification_created': False,
        'scientific_authority_created': False,
        'next_rung_authorized': False,
        'covariance_restriction_authorized': False,
        'Wm_S3_opened': False,
        'interpretation': 'Exploratory/post-hoc support only. After collapsing exact physical duplicates, strict-threshold exceedances remain strongly enriched among the smallest cancellation scales. The p-values are descriptive stress-test evidence, not preregistered confirmatory inference and do not change the frozen scientific gate.'
    }

    assert abs(rho - (-0.5163800793626381)) < 1e-15
    assert result['lowest_scale_quartile_vs_rest']['table_high_low'] == [[12, 3], [7, 36]]
    assert q1_or > 20 and q1_p < 2e-5
    assert result['lower_half_vs_upper_half']['table_high_low'] == [[17, 12], [2, 27]]
    assert half_or > 19 and half_p < 3e-5
    assert result['median_scale_ratio_high_to_low'] < 0.13

    Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')


if __name__ == '__main__':
    main()
