"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)

        for i in range(1, N):
            nums[i] += nums[i - 1]
        return nums


nums = [1,2,3,4]