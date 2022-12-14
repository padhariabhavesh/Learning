"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

Intuition
Approach
Complexity
Time
complexity:
Space
complexity:
Code


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.msum = float('-inf')
        self.get_sum(root)
        return self.msum

    def get_sum(self, node):
        if not node:
            return 0

        ls, rs = self.get_sum(node.left), self.get_sum(node.right)
        max_single_path = max(node.val + max(ls, rs), node.val)
        self.msum = max(self.msum, max_single_path, node.val + ls + rs)
        return max_single_path

