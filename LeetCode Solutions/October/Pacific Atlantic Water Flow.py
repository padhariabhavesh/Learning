"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""

class Solution:
    def pacificAtlantic(self, M: List[List[int]]) -> List[List[int]]:
        if not M: return M
        x, y = len(M[0]), len(M)
        ans, dp = [], [0] * (x * y)
        def dfs(i: int, j: int, w: int, h: int):
            ij = i * x + j
            if dp[ij] & w or M[i][j] < h: return
            dp[ij] += w
            h = M[i][j]
            if dp[ij] == 3: ans.append([i,j])
            if i + 1 < y: dfs(i+1, j, w, h)
            if i > 0: dfs(i-1, j, w, h)
            if j + 1 < x: dfs(i, j+1, w, h)
            if j > 0: dfs(i, j-1, w, h)
        for i in range(y):
            dfs(i, 0, 1, M[i][0])
            dfs(i, x-1, 2, M[i][x-1])
        for j in range(x):
            dfs(0, j, 1, M[0][j])
            dfs(y-1, j, 2, M[y-1][j])
        return ans
