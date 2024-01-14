'''
1657. Determine if Two Strings Are Close


Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Check Here: https://leetcode.com/problems/determine-if-two-strings-are-close/solutions/4561609/1657-determine-if-two-strings-are-close-python
'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        n1 = Counter([v for v in c1.values()])
        n2 = Counter([v for v in c2.values()])

        return c1 == c2 or (n1 == n2 and set(word1) == set(word2))

                     