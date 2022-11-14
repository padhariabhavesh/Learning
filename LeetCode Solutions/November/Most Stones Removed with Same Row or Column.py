"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
"""


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = defaultdict(list)
        for stone in stones:
            r = stone[0]
            c = stone[1]
            graph[('r', r)].append(stone)
            graph[('c', c)].append(stone)
        visited = set()

        def dfs(stone):
            r, c = stone[0], stone[1]
            visited.add(tuple(stone))
            # call for the neightbors
            for stone in graph[('r', r)]:
                if tuple(stone) not in visited:
                    dfs(stone)
            for stone in graph[('c', c)]:
                if tuple(stone) not in visited:
                    dfs(stone)

        count = 0
        for stone in stones:
            if tuple(stone) not in visited:
                dfs(stone)
                count += 1
        return len(stones) - count
