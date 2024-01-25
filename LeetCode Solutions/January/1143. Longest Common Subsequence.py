'''
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            return self.LCS(text1, text2)
        return self.LCS(text2, text1)

    def LCS(self, s1: str, s2: str) -> int:
        M = [[0] * (len(s1) + 1) for _ in range(2)]

        for i in range(1, len(s2) + 1):
            M[i % 2][0] = 0
            for j in range(1, len(s1) + 1):
                if s1[j - 1] == s2[i - 1]:
                    M[i % 2][j] = M[(i - 1) % 2][j - 1] + 1
                else:
                    M[i % 2][j] = max(M[(i - 1) % 2][j - 1],
                                      max(M[(i - 1) % 2][j], M[i % 2][j - 1]))
        return M[len(s2) % 2][len(s1)]

