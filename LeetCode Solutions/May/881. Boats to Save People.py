'''

881. Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
https://leetcode.com/problems/boats-to-save-people/solutions/5111549/881-boats-to-save-people-python

'''

class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        x=0
        l, r=0, len(p)-1
        while l<=r:
            x+=1
            if p[l]+p[r]<=limit:
                l+=1
            r-=1
        return x
        