"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s =set()
        c = Counter(arr)
        res = sum(c.values()) - sum(set(c.values()))
        return False if res > 0 else True

################################ Second solution
        s = set()
        c =Counter(arr)
        for i in c:
            if c[i] in s:
                return False
            s.add(c[i])
        return True