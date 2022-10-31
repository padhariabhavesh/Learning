"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
"""


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        # r, c, pathLength, remaining_k
        q.append((0, 0, 0, k))
        seen = set()

        while q:
            r, c, pathLength, kRemain = q.popleft()
            if (r, c, kRemain) in seen or kRemain < 0:
                continue

            if r == (rows - 1) and c == (cols - 1):
                return pathLength

            seen.add((r, c, kRemain))
            if grid[r][c] == 1:
                kRemain -= 1

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols):
                    q.append((nr, nc, pathLength + 1, kRemain))

        return -1