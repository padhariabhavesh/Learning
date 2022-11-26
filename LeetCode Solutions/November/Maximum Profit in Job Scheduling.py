"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.


"""


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # sort jobs by start time
        jobs = sorted(zip(startTime, endTime, profit))

        @cache
        def dfs(idx: int) -> int:
            # If we reach the end of jobs, return
            if idx >= len(jobs):
                return 0
            # Binary search the next job index based on end time of current job
            nextPos = bisect_left(jobs, jobs[idx][1], key=lambda job: job[0])
            # Take -> Consider the current job and start the recursion from the binary-searched nextPos
            # Leave -> Do not consider the current job and start a recursive call from the next job
            # Consider the maximum of take and leave to maximise profit
            return max(dfs(idx + 1), jobs[idx][2] + dfs(nextPos))

        # Start the dfs
        return dfs(0)