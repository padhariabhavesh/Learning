'''
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

URL: https://leetcode.com/problems/merge-strings-alternately/solutions/4797569/1768-merge-strings-alternately-python
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        ind = 0
        while ind < len(word1) or ind < len(word2):
            char1 = word1[ind] if ind < len(word1) else ""
            char2 = word2[ind] if ind < len(word2) else ""
            new_str += char1 + char2
            ind += 1
        return new_str
