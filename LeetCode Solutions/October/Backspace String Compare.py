1"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 """

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        for c in S:
            if c == '#':
                if s: s.pop()
            else: s.append(c)

        t = []
        for c in T:
            if c == '#':
                if t: t.pop()
            else: t.append(c)

        return ''.join(s) == ''.join(t)