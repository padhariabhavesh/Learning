"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        self.traverse(root, root.val, root.val, result)
        return result[0]

    def traverse(self, root, low, high, result):
        if not root:
            return
        result[0] = max(result[0], abs(root.val - low), abs(root.val - high))
        if root.val < low:
            low = root.val
        if root.val > high:
            high = root.val
        self.traverse(root.left, low, high, result)
        self.traverse(root.right, low, high, result)