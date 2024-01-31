'''
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

https://leetcode.com/problems/daily-temperatures/solutions/4651814/739-daily-temperatures-python
'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for today_day, today_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < today_temp:
                past_day = stack.pop()
                answer[past_day] = today_day - past_day
            stack.append(today_day)
        return answer
