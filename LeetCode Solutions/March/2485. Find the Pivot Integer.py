'''
2485. Find the Pivot Integer

Given a positive integer n, find the pivot integer x such that:

    The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.


https://leetcode.com/problems/find-the-pivot-integer/solutions/4866686/2485-find-the-pivot-integer-python


'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) / 2)

        if x % 1 != 0:
            return -1
        else:
            return int(x)