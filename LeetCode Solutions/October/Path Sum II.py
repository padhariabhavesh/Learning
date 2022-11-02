# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        return self._pathSum(root, sum, [], [])

    def _pathSum(self, root, sum, path, result):
        if root is None:
            return result

        if sum == root.val and root.left is None and root.right is None:
            return result + [path + [root.val]]
        else:
            return self._pathSum(root.left, sum - root.val, path + [root.val], result) + self._pathSum(root.right, sum - root.val,
                                                                                                       path + [root.val], result)


