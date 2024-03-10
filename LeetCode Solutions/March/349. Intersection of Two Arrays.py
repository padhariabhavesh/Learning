'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        for num in nums1:
            mp[num] = mp.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if num in mp:
                result.append(num)
                del mp[num]
        
        return result


