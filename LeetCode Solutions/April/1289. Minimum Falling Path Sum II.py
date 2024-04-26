'''

1289. Minimum Falling Path Sum II

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

https://leetcode.com/problems/minimum-falling-path-sum-ii/solutions/5073432/1289-minimum-falling-path-sum-ii-python
'''

class Solution:
  def minFallingPathSum(self, grid: List[List[int]]) -> int:
    n = len(grid)

    for i in range(1, n):
      (firstMinNum, firstMinIndex), (secondMinNum, _) = sorted(
          {(a, i) for i, a in enumerate(grid[i - 1])})[:2]
      for j in range(n):
        if j == firstMinIndex:
          grid[i][j] += secondMinNum
        else:
          grid[i][j] += firstMinNum

    return min(grid[-1])