"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            tmp = max_prod
            max_prod = max(max_prod * nums[i], min_prod * nums[i], nums[i])
            min_prod = min(tmp * nums[i], min_prod * nums[i], nums[i])
            ans = max(ans, max_prod)
        return ans