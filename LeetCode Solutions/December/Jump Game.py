"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) <= 1:
            return True
        j = len(nums) - 2
        i = len(nums) - 1
        while j > -1:
            if j + nums[j] >= i:
                i = j
                j -= 1

            else:
                j -= 1
        # print('i', i, 'j', j)
        if i <= 0:
            return True
        else:
            return False