'''
992. Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

    For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

A subarray is a contiguous part of an array.

'''
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt=[0]*(len(nums)+1)
        ans=0
        l=0
        m=0
        for num in nums:
            cnt[num]+=1
            if cnt[num]==1:
                k-=1
                if k<0:
                    cnt[nums[m]]=0
                    m+=1
                    l=m
            if k<=0:
                while cnt[nums[m]]>1:
                    cnt[nums[m]]-=1
                    m+=1
                ans+=m-l+1
        return ans                        