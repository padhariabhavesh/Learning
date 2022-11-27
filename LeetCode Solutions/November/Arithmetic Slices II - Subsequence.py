"""
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.


"""

from collections import deque, Counter, defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        ctr = Counter(nums)
        for el in ctr:
            res += 1 << ctr[el]
            res -= ctr[el] + 1
            res -= ctr[el] * (ctr[el] - 1) // 2
        pos = defaultdict(list)
        q = deque()
        for i in range(n):
            pos[nums[i]].append(i)
            for j in range(i + 1, n):
                if nums[j] != nums[i]:
                    q.appendleft((nums[j] - nums[i], j, 2))
        while len(q) > 0:
            d, i, l = q.pop()
            if l >= 3:
                res += 1
            for j in pos[nums[i] + d]:
                if j > i:
                    q.appendleft((d, j, l + 1))
        return res