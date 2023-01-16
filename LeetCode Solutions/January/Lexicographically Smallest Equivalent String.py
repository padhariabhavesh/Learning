"""
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.


"""


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        UF = {}

        def find(x):
            UF.setdefault(x, x)
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            # The main issue we need to take care of in this problem is
            # that we want the root of a group to be
            # the smallest element in the group
            # So every time we add an element in a group, we check if it is the smallest one,
            # If it is, we set it as the root.
            if rootX > rootY:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX

        # Union the two equivalent characters
        # at the same position from s1 and s2 into the same group.
        for i in range(len(s1)):
            union(s1[i], s2[i])

        # Simply find the root of the group a character belongs to
        # Note that if c is not in any group,
        # we have UF.setdefault(x,x) in def find(x) to take care of it
        res = []
        for c in baseStr:
            res.append(find(c))

        return ''.join(res)
