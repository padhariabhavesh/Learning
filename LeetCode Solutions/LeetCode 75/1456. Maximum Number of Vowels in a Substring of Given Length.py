'''
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/solutions/4851028/1456-maximum-number-of-vowels-in-a-substring-of-given-length-python
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        maxi = 0
        kVowels = 'aeiou'

        for i, c in enumerate(s):
            if c in kVowels:
                maxi += 1
            if i >= k and s[i - k] in kVowels:
                maxi -= 1
            ans = max(ans, maxi)

        return ans