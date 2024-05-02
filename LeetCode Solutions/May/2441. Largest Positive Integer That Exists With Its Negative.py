'''

2441. Largest Positive Integer That Exists With Its Negative


Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/solutions/5098772/2441-largest-positive-integer-that-exists-with-its-negative-python
'''

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] > 0 and -nums[i] in nums:
                return nums[i]
        return -1  # If no such pair found