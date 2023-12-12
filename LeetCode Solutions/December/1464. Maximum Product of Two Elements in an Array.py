'''
1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1). 
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max, second_max = 0, 0
        for num in nums:
            if num > first_max:
                second_max, first_max = first_max, num
            else:
                second_max = max(second_max, num)

        return (first_max - 1) * (second_max - 1)