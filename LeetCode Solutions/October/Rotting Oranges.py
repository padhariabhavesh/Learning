"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        fresh = set()
        rotten = set()

        # store coordinates (x,y) for fresh and rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.add((i, j))

        minutes = 0

        # all reachable directions (up, down, left, right) by a rotten orange that can be infected
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        # loop through until we have fresh oranges
        while len(fresh) > 0:

            # stores infected oranges during the bfs
            infected = set()

            for rot in rotten:
                # remeber each rot is a tuple like (x,y)
                i, j = rot
                for d in directions:
                    next_i, next_j = d
                    next_i += i
                    next_j += j

                    if (next_i, next_j) in fresh:
                        fresh.remove((next_i, next_j))
                        infected.add((next_i, next_j))

            if len(infected) == 0:
                return -1

            minutes += 1
            rotten = infected

        return minutes