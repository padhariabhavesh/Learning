'''

1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/solutions/4930526/1466-reorder-routes-to-make-all-paths-lead-to-the-city-zero-python

'''
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        T = Hashable
        Direction = bool
        Graph = Mapping[T, Iterable[tuple[T, Direction]]]

        def min_flips(graph: Graph, u: T, parent: T | None = None) -> int:
            return sum(min_flips(graph, v, u) + d for v, d in graph[u] if v != parent)

        g = defaultdict(list)
        for u, v in connections: g[u].append((v, True)); g[v].append((u, False))
        return min_flips(g, 0)

