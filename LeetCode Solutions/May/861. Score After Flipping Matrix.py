'''

861. Score After Flipping Matrix


A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).



'''

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = (1 << (m - 1)) * n

        for j in range(1, m):
            val = 1 << (m - 1 - j)
            set_count = 0

            for i in range(n):
                if grid[i][j] == grid[i][0]:
                    set_count += 1

            res += max(set_count, n - set_count) * val

        return res