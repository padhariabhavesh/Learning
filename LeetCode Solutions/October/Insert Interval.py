"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        retIntervals = []
        newIntAdded = False

        # iterate over every interval in list of intervals
        for interval in intervals:
            # four cases

            # no overlap
            if (interval[1] < newInterval[0] or interval[0] > newInterval[1]):
                if (not newIntAdded and interval[0] > newInterval[1]):
                    retIntervals.append(newInterval)
                    newIntAdded = True
                retIntervals.append(interval)
                continue

            # new interval starts inside
            if (newInterval[0] >= interval[0] and newInterval[0] <= interval[1]):
                newInterval[0] = interval[0]

            # new interval ends inside
            if (newInterval[1] >= interval[0] and newInterval[1] <= interval[1] and not newIntAdded):
                newInterval[1] = interval[1]
                retIntervals.append(newInterval)
                newIntAdded = True

            # new interval surrounds
            # do nothing

        # if new interval never got added, add it
        if (not newIntAdded):
            retIntervals.append(newInterval)

        return retIntervals