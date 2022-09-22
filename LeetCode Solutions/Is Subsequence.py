"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s == t):
            return True
        else:
            temp=''
            cou=0
            for i in range(len(t)):
                if(cou < len(s)):
                    if(s != "" and s[cou] == t[i]):
                        temp+=t[i]
                        cou+=1
            if(temp == s):
                return True
            else:
                return False

s = "abc", t = "ahbgdc"