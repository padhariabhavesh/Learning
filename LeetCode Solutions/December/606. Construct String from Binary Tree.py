'''
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root):
        # Step 1: Base case - if the root is None, return an empty string
        if root is None:
            return ""

        # Step 2: Start with the value of the current node as the result string
        result = str(root.val)

        # Step 3: Recursively process the left and right subtrees
        left_subtree = self.tree2str(root.left)
        right_subtree = self.tree2str(root.right)

        # Step 4: Check conditions to determine the final result
        if not left_subtree and not right_subtree:
            # Both left and right subtrees are empty, return the current result
            return result
        if not left_subtree:
            # Left subtree is empty, include empty parentheses for it and the right subtree
            return result + "()" + "(" + right_subtree + ")"
        if not right_subtree:
            # Right subtree is empty, include the left subtree
            return result + "(" + left_subtree + ")"

        # Both left and right subtrees are non-empty, include both in the result
        return result + "(" + left_subtree + ")" + "(" + right_subtree + ")"