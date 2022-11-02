"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if (root == None):
            return False

        stack = []
        stack.append(root)
        curr_list = []
        sum_vals = 0
        while (len(stack) != 0):
            curr_root = stack.pop()
            sum_vals += curr_root.val
            curr_list.append(curr_root)
            if (curr_root.left == None and curr_root.right == None):
                if (sum_vals == targetSum):
                    return True
                while (len(curr_list) > 0):
                    node = curr_list.pop()
                    if (node.left == None and node.right == None):
                        sum_vals -= node.val
                        child_node = node
                    elif (node.left == child_node and (node.right == None or not (node.right in stack))):
                        sum_vals -= node.val
                        child_node = node
                    elif (node.right == child_node and (node.left == None or not (node.left in stack))):
                        sum_vals -= node.val
                        child_node = node
                    else:
                        curr_list.append(node)
                        break
            else:
                if (curr_root.left != None):
                    stack.append(curr_root.left)
                if (curr_root.right != None):
                    stack.append(curr_root.right)
        return False