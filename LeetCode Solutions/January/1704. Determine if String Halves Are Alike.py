'''
1704. Determine if String Halves Are Alike

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Check: https://leetcode.com/problems/determine-if-string-halves-are-alike/solutions/4549220/1704-determine-if-string-halves-are-alike-python
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        c1 = c2 = 0
        for c in s[:n]:
            if c in 'aeiouAEIOU':
                c1 += 1
        for c in s[n:]:
            if c in 'aeiouAEIOU':
                c2 += 1
        return c1 == c2


        