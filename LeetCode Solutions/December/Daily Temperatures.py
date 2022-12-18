"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        arr = [-1 for _ in range(71)]
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            t = temperatures[i]
            j = [x for x in arr[t-30+1:] if x > -1]
            res[i] = 0 if len(j) == 0 else min(j)-i
            arr[t-30] = i

        return res