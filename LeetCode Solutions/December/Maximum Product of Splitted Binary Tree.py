"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def natural_nums():
            num = 0
            while True:
                yield num
                num += 1

        def dfs_sum(node):
            if not node: return 0
            nodenum = next(numgen)
            cache[nodenum] = node.val + dfs_sum(node.left) + dfs_sum(node.right)
            return cache[nodenum]

        def dfs(node):
            if not node: return 1
            nodenum = next(numgen)
            return max(cache[nodenum] * (cache[0] - cache[nodenum]), dfs(node.left), dfs(node.right))

        cache = defaultdict(int)
        numgen = natural_nums()
        dfs_sum(root)
        numgen = natural_nums()
        return dfs(root) % (10 ** 9 + 7)