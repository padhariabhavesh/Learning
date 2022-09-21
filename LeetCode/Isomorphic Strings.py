"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        iso_map = {}
        for s1, t1 in zip(s,t):
            if s1 not in iso_map:
                iso_map[s1] = t1
            elif iso_map[s1] != t1:
                return False
        return len(set(iso_map.values())) == len(iso_map.values())

s = "egg", t = "add"