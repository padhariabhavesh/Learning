"""
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
"""


class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:

        M, N = range(len(grid)), range(len(grid[0]))

        zeros = sum(row.count(0) for row in grid)  # count the zeros to ensure all cells visited
        start = tuple((r, c) for r in M for c in N  # find start in grid
                      if grid[r][c] == 1)[0]
        self.ans = 0

        def dfs(row, col, zeros):
            grid[row][col] = 3  # change 0 to 3 to avoid returning

            for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):  # explore the grid recursively
                R, C = row + dr, col + dc
                if R in M and C in N:
                    if grid[R][C] == 0: dfs(R, C, zeros - 1)
                    if grid[R][C] == 2 and zeros == 0: self.ans += 1

            grid[row][col] = 0  # change back
            return

        dfs(*start, zeros)
        return self.ans