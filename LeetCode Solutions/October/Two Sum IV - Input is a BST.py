"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self.dfs(root,k,{})

    def dfs(self,root,k,hashmap):
        if not root:
            return False
        if root.val in hashmap:
            return True
        hashmap[k-root.val] = 1
        return self.dfs(root.left,k,hashmap) or self.dfs(root.right,k,hashmap)