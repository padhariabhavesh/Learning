"""
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
"""

class Solution:
  def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    n = len(jobDifficulty)
    if d > n:
      return -1

    # dp[i][k] := min difficulty to schedule the first i jobs in k days
    dp = [[math.inf] * (d + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
      for k in range(1, d + 1):
        maxDifficulty = 0  # Max(job[j + 1..i])
        for j in range(i - 1, k - 2, -1):  # 1-based
          # 0-based
          maxDifficulty = max(maxDifficulty, jobDifficulty[j])
          dp[i][k] = min(dp[i][k], dp[j][k - 1] + maxDifficulty)

    return dp[n][d]
