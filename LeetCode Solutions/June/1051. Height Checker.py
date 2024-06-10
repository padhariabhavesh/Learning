'''

1051. Height Checker

Solution Explained: https://www.youtube.com/watch?v=FRhQOlwIiLA
'''

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)

        return sum(h1 != h2 for h1, h2 in zip(heights, sorted_heights))
        
