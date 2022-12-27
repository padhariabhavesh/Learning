"""
You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.
"""

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        diff = [capacity[i] - rocks[i] for i in range(n)]
        diff.sort()
        i = 0
        while additionalRocks > 0 and i < n:
            additionalRocks -= diff[i]
            i += 1
        if additionalRocks < 0:
            return i - 1
        return i