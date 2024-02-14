'''
2149. Rearrange Array Elements by Sign
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        v1, v2, ans = [], [], []
        
        for num in nums:
            if num > 0:
                v1.append(num)
            else:
                v2.append(num)
        
        ind1, ind2 = 0, 0
        
        while ind2 < len(nums) // 2:
            ans.append(v1[ind1])
            ind1 += 1
            ans.append(v2[ind2])
            ind2 += 1
        
        return ans


