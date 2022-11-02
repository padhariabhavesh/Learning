"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
            if len(nums)<3: return False
            size = len(nums)
            dp = [1]*size
            pre_max = nums[0]
            for i in range(1,size):
                pre_max = nums[i-1] if nums[i-1]>pre_max else pre_max
                for j in range(i-1,-1,-1):
                    if nums[i]>nums[j]:
                        if nums[j]==pre_max:
                            dp[i]=max(dp[i],dp[j]+1)
                            break
                        dp[i]=max(dp[i],dp[j]+1)
            return True if max(dp)>=3 else False