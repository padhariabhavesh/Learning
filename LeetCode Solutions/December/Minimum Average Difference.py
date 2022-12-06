"""
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.
"""


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        summ = 0
        count = 0
        result = []
        for i in range(len(nums)):
            summ += nums[i]
            count += 1
            try:
                avg = summ // count
            except:
                avg = 0
            try:
                avg2 = (total - summ) // (len(nums) - count)
            except:
                avg2 = 0

            result.append((i, abs(avg - avg2)))

        result.sort(key=lambda x: x[1])
        return result[0][0]

