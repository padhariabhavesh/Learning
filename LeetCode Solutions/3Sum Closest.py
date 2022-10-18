"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.


"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        ls = len(nums)
        if(ls < 3):
            return []

        nums = sorted(nums)

        resus = sum(nums[0:3])

        for i in range(ls - 2):
            j = i + 1
            m = ls - 1

            while(j < m):
                tem = nums[i] + nums[j] + nums[m]
                v = tem - target

                if(abs(v) < abs(resus - target)):
                    resus = tem

                if(v == 0):
                    return target
                elif(v > 0):
                    m -= 1
                else:
                    j += 1

        return resus