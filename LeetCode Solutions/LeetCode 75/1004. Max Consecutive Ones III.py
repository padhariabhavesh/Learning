'''

1004. Max Consecutive Ones III


Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

https://leetcode.com/problems/max-consecutive-ones-iii/solutions/4856501/1004-max-consecutive-ones-iii-python

'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return r-l+1