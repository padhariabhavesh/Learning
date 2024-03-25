'''

236. Lowest Common Ancestor of a Binary Tree


Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solutions/4924706/236-lowest-common-ancestor-of-a-binary-tree-python
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_lca(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node: return None
            if node in [p, q]: return node
            l, r = get_lca(node.left), get_lca(node.right)
            if l and r: return node
            return l or r

        return get_lca(root)