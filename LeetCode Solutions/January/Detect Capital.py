"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
"""

class Solution:
    def detectCapitalUse(self, w: str) -> bool:
        up = low = 0
        for c in w:
            if c.isupper():
                up += 1
            else:
                low += 1
        return up==len(w) or low==len(w) or (up==1 and w[0].isupper())