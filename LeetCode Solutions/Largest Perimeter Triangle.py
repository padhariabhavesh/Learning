"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.


"""

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        """
        sort and scanning from right
        """
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return sum(A[i:i+3])
        else:
            return 0