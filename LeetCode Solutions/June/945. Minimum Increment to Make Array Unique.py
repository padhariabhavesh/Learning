'''

945. Minimum Increment to Make Array Unique


Explain: https://youtu.be/4OPgtXUsJeI?si=femKiDF4e7eW2u0Q  
'''

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # Step 1 sort the array
        nums.sort()
        n = len(nums)
        ans = 0

        # Step 2 Iterate through the array and increment as necessary
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                #calculate the difference needed to make the nums[i] unique
                diff = nums[i-1] + 1 - nums[i]
                ans += diff
                nums[i] = nums[i-1] +1
        # return the total number of moves
        return ans 

        
