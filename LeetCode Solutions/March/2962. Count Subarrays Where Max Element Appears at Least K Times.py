'''

2962. Count Subarrays Where Max Element Appears at Least K Times

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/solutions/4939914/2962-count-subarrays-where-max-element-appears-at-least-k-times-python
'''

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ans = 0
        l = 0
        r = 0
        n = len(nums)
        
        while r < n:
            k -= nums[r] == mx
            r += 1
            while k == 0:
                k += nums[l] == mx
                l += 1
            ans += l
            
        return ans
