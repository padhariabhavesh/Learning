'''
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/solutions/4925803/1161-maximum-level-sum-of-a-binary-tree-python
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> List[float]:
        level_sum = defaultdict(int)

        for lvl, val in self.inorder(root):
            level_sum[lvl + 1] += val

        return max(level_sum, key=lambda x: (level_sum[x], -x))

    @classmethod
    def inorder(cls, tree: TreeNode | None, level: int = 0):
        if tree is not None:
            yield from cls.inorder(tree.left, level + 1)
            yield level, tree.val
            yield from cls.inorder(tree.right, level + 1)
