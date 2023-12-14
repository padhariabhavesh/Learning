'''
2482. Difference Between Ones and Zeros in Row and Column

You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

    Let the number of ones in the ith row be onesRowi.
    Let the number of ones in the jth column be onesColj.
    Let the number of zeros in the ith row be zerosRowi.
    Let the number of zeros in the jth column be zerosColj.
    diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj

Return the difference matrix diff.
'''

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        def summation(nums) : 
            return 2 * sum(nums) - len(nums)
        m, n = len(grid), len(grid[0])
            
        rows = list(map(summation, grid))
        cols = list(map(summation, zip(*grid)))
        
        for i,j in product(range(m), range(n)):
            grid[i][j] = rows[i] + cols[j]
        return grid