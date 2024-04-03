'''

2542. Maximum Subsequence Score


You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

    The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
    It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).

Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

https://leetcode.com/problems/maximum-subsequence-score/solutions/4965180/2542-maximum-subsequence-score-python
'''

import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        lst=list(zip(nums2,nums1))
        lst.sort(key=lambda x:(-x[0],-x[1]))
        flst=[]
        heapq.heapify(flst)
        i=0
        sm=0
        ef=float("infinity")
        prd=float("-infinity")
        while i<k:
            x=lst.pop(0)
            heapq.heappush(flst,x[1])
            ef=min(ef,x[0])
            sm+=x[1]
            i+=1
        prd=max(prd,sm*ef)
        while lst:
            x=heapq.heappop(flst)
            sm-=x
            y=lst.pop(0)
            heapq.heappush(flst,y[1])
            ef=min(ef,y[0])
            sm+=y[1]
            prd=max(prd,sm*ef)
        return prd
