"""
You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

Return an integer array answer where answer[i] is the answer to the ith query.
"""


class Solution:
  def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    ans = []
    summ = sum(a for a in A if a % 2 == 0)

    for q in queries:
      if A[q[1]] % 2 == 0:
        summ -= A[q[1]]
      A[q[1]] += q[0]
      if A[q[1]] % 2 == 0:
        summ += A[q[1]]
      ans.append(summ)

    return ans
nums = [1], queries = [[4,0]]