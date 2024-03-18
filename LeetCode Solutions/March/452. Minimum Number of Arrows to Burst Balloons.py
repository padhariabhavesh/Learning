'''

452. Minimum Number of Arrows to Burst Balloons


There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/solutions/4893147/452-minimum-number-of-arrows-to-burst-balloons-python
'''


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res, curEnd = 1, points[0][1]
        for start,end in points:
            if start>curEnd:
                curEnd = end
                res += 1
        return res