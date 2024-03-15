'''

2352. Equal Row and Column Pairs


Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

https://leetcode.com/problems/equal-row-and-column-pairs/solutions/4876944/2352-equal-row-and-column-pairs-python
'''

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = {}
        result = 0
        
        for i in range(len(grid)):
            if tuple(grid[i]) not in count:
                count[tuple(grid[i])] = 1
            elif tuple(grid[i]) in count:
                count[tuple(grid[i])] += 1
        
        for n in range(len(grid)):
            col = [i[n] for i in grid]
            if col in grid:
                result += count[tuple(col)]
        return result
        