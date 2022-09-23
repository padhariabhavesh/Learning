"""
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.
"""

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res, M = 0, 10 ** 9 + 7
        for x in range(n):
            res = (res * (1 << (len(bin(x + 1)) - 2)) + x + 1) % M
        return res