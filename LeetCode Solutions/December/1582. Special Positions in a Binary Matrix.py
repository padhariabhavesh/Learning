'''
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
'''

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    continue
                good = True
                for r in range(m):
                    if r != row and mat[r][col] == 1:
                        good = False
                        break
                for c in range(n):
                    if c != col and mat[row][c] == 1:
                        good = False
                        break
                if good:
                    ans += 1
        return ans