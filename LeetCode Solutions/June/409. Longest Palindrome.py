'''

409. Longest Palindrome


Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        val = 0
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        for count in mp.values():
            if count % 2 != 0:
                res += count - 1
                val = 1
            else:
                res += count
        return res + val            
        