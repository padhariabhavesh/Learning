'''
1347. Minimum Number of Steps to Make Two Strings Anagram

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Check Here: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/solutions/4556797/1347-minimum-number-of-steps-to-make-two-strings-anagram-python
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = defaultdict(int)
        for i in s:
            freq[i] += 1
        for i in t:
            if freq[i]:
                freq[i] -= 1
        return sum(freq.values())
        
