"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxx = 0;

        def levels(root):
            if not root: return 0;
            left, right = levels(root.left), levels(root.right)
            self.maxx = max(self.maxx, left + right)
            return 1 + max(left, right)
            # return 0;

        levels(root)
        return self.maxx