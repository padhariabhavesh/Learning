'''
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

    For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.

Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.
'''

class Solution:

    def maxProductDifference(self, nums: List[int]) -> int:

        first_big = second_big = 0

        first_small = second_small = float("inf")



        for n in nums:

            if n < first_small:

                second_small, first_small = first_small, n                

            elif n < second_small:                

                second_small = n                



            if n > first_big:

                second_big, first_big = first_big, n

            elif n > second_big:

                second_big = n        



        return first_big * second_big - first_small * second_small