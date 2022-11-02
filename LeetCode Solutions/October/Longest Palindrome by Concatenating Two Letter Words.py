"""
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
"""


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # First attempt, time O(N), space O(N)
        ans = 0
        seen = collections.defaultdict(int)
        for word in words:
            if seen[word] > 0:
                ans += 4
                seen[word] -= 1
            else:
                seen[word[::-1]] += 1
        for word in seen:
            if seen[word] > 0 and word[0] == word[1]:
                ans += 2
                break
        return ans

