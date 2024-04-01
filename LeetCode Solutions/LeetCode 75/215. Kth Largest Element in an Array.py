'''

215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/4954364/215-kth-largest-element-in-an-array-python
'''
class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k-1]