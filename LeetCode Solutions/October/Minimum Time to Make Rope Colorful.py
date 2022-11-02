"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.


"""


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Initalize two pointers i, j.
        total_time = 0
        i, j = 0, 0

        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0

            # Find all the balloons having the same color as the
            # balloon indexed at i, record the total removal time
            # and the maximum removal time.
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1

            # Once we reach the end of the current group, add the cost of
            # this group to total_time, and reset two pointers.
            total_time += curr_total - curr_max
            i = j

        return total_time