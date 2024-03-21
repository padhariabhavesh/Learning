'''

1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

https://leetcode.com/problems/count-good-nodes-in-binary-tree/solutions/4904068/1448-count-good-nodes-in-binary-tree-python
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, currMax):
            if not node:
                return 0
            if node.val >= currMax:
                cnt = 1
            else:
                cnt = 0
            currMax = max(currMax, node.val)
            cnt += helper(node.left, currMax)
            cnt += helper(node.right, currMax)
            return cnt
        return helper(root, root.val)