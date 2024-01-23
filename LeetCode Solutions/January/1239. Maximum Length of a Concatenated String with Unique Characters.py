'''
1239. Maximum Length of a Concatenated String with Unique Characters


You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Check Here: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solutions/4611456/1239-maximum-length-of-a-concatenated-string-with-unique-characters-python
'''

from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxLength = [0]
        self.backTrack(arr, "", 0, maxLength)
        return maxLength[0]

    def backTrack(self, arr, current, start, maxLength):
        if maxLength[0] < len(current):
            maxLength[0] = len(current)

        for i in range(start, len(arr)):
            if not self.isValid(current, arr[i]):
                continue

            self.backTrack(arr, current + arr[i], i + 1, maxLength)

    def isValid(self, currentString, newString):
        charSet = set()

        for ch in newString:
            if ch in charSet:
                return False

            charSet.add(ch)

            if ch in currentString:
                return False

        return True




