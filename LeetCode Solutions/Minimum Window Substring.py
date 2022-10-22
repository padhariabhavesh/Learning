"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = collections.Counter(t)
        letters_missing = len(needed)
        min_substring = s + s

        l = 0
        for r in range(len(s)):
            if s[r] in needed:
                needed[s[r]] -= 1
                if needed[s[r]] == 0:
                    letters_missing -= 1
            if letters_missing > 0:
                continue
            while l < r and (s[l] not in needed or needed[s[l]] < 0):
                if s[l] in needed:
                    needed[s[l]] += 1
                l += 1
            if r - l + 1 < len(min_substring):
                min_substring = s[l:r + 1]

        return min_substring if len(min_substring) <= len(s) else

