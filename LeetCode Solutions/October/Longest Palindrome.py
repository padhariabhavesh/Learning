"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaired_chars = set()

        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)

        return pairs * 2 + 1 if unpaired_chars else pairs * 2