'''
576. Out of Boundary Paths


There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 1000000007
        @cache
        def recur(r, c, moves):
            if r < 0 or c < 0 or r >= m or c >= n: return 1
            if moves == 0: return 0
            return recur(r+1,c, moves-1) + recur(r-1,c,moves-1) + recur(r,c-1, moves-1) + recur(r,c+1, moves-1)
        
        return recur(startRow, startColumn, maxMove) % MODx``