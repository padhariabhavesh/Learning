'''

2597. The Number of Beautiful Subsets

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

'''

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # nums = [2,4,6]
        # k = 2
        # [], [2], [4], [6], [2, 4], [2, 6], [4, 6], [2, 4, 6]
        # [2], [4], [6], [2, 6] -> 4 ans
        # SOLUTION
        # num - k or n + k

        count = 0
        lenNums = len(nums)

        def explore(index):
            nonlocal count
            if lenNums == index:
                count += 1
                return

            num = nums[index]

            if num - k not in visited and num + k not in visited:
                visited[num] += 1
                explore(index + 1)
                visited[num] -= 1
                if visited[num] == 0:
                    del visited[num]

            explore(index + 1)

        visited = defaultdict(int)
        explore(0)
        return count - 1
