"""Tools for finding minimal observable-channel sets that break known degeneracies."""
from __future__ import annotations

from itertools import combinations
from collections.abc import Mapping, Sequence


def minimal_separating_channel_sets(
    pair_to_channels: Mapping[str, Sequence[str]],
) -> list[tuple[str, ...]]:
    """Return all minimum-cardinality channel sets that hit every degeneracy edge.

    `pair_to_channels[pair]` contains channels with *established* separating power for
    that pair under the frozen model-instance/domain assumptions. Unknown or merely
    possible discriminants should not be inserted as if established.
    """
    if not pair_to_channels:
        return [tuple()]
    for pair, channels in pair_to_channels.items():
        if not channels:
            raise ValueError(f"No established discriminant for pair {pair!r}")
    universe = sorted({c for cs in pair_to_channels.values() for c in cs})
    edges = [set(cs) for cs in pair_to_channels.values()]
    for r in range(1, len(universe) + 1):
        hits = []
        for combo in combinations(universe, r):
            s = set(combo)
            if all(s & edge for edge in edges):
                hits.append(combo)
        if hits:
            return hits
    raise RuntimeError("Unreachable: finite nonempty edges must admit a hitting set")
