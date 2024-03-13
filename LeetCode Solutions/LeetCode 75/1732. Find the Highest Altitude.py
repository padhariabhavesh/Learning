'''

1732. Find the Highest Altitude

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

https://leetcode.com/problems/find-the-highest-altitude/solutions/4866696/1732-find-the-highest-altitude-python
'''

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxVal=0
        alt=0
        for i in gain:
            alt+=i
            maxVal=max(alt,maxVal)
        return maxVal