


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mask = 1 << len(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                mask |= (1 << i)
        i = len(nums)-1
        while i > -1:
            if mask & (1 << i):
                del nums[i]
            i -= 1