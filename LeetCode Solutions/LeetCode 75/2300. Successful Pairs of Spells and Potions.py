'''
2300. Successful Pairs of Spells and Potions


You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

https://leetcode.com/problems/successful-pairs-of-spells-and-potions/solutions/4969857/2300-successful-pairs-of-spells-and-potions-python
'''

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def BinarySearch(nums,x):
            l=0
            r=len(nums)-1
            while l<=r:
                m=(l+r)//2
                if nums[m]>=x:
                    r=m-1
                elif nums[m]<x:
                    l=m+1
            return r+1
        ans=[]
        res=0
        potions.sort()
        n=len(potions )
        for i in range (0,len(spells)):
            res=0
            index=BinarySearch(potions,success/spells[i])
            print(index)
            if index<=n:
                res=n-index
            ans.append(res)
        return ans
