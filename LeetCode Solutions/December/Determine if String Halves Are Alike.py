"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""

class Solution(object):
    def halvesAreAlike(self,s):
        half = int(len(s)/2)
        length = int(len(s))
        a = s[0 :half ]
        b = s[half:  length]
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowelCount = 0
        vowelsInA = [vowel in vowels for vowel in a]
        vowelsInB = [vowel in vowels for vowel in b]
        count_A = vowelsInA.count(True)
        count_B = vowelsInB.count(True)
        if(count_A == count_B):
            return True
        else:
            return False