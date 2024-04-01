'''
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

 https://leetcode.com/problems/length-of-last-word/solutions/4954348/58-length-of-last-word-python
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        if not words:
            return 0
        
        return len(words[-1])