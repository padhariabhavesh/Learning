'''
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

URL: https://leetcode.com/problems/squares-of-a-sorted-array/solutions/4807877/977-squares-of-a-sorted-array-python
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [num * num for num in nums]
        squares.sort()
        return squares