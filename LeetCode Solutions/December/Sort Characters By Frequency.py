"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
"""

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s).most_common()
        return ''.join([letter * stats for letter, stats in cnt])