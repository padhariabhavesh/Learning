'''
2108. Find First Palindromic String in the Array


Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
'''

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((s for s in words if all(s[i]==s[-(i+1)] for i in range(len(s)//2))), "")