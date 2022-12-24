"""
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
"""

class Solution:
    def numTilings(self, N):
        def numTilingsD(N):
            if N in cacheD: return cacheD[N]
            if N <= 2: return N if N > 0 else 1
            cacheD[N] = (numTilingsD(N - 2) + numTilingsD(N - 1) + (2 * numTilingsT(N - 1))) % ((10**9) + 7)
            return cacheD[N]

        def numTilingsT(N):
            if N in cacheT: return cacheT[N]
            if N <= 2: return 0 if N == 1 else 1
            cacheT[N] = (numTilingsD(N - 2) + numTilingsT(N - 1)) % ((10**9) + 7)
            return cacheT[N]
        cacheD, cacheT = {}, {}
        return numTilingsD(N)