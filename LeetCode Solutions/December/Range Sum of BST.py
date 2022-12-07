"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


"""


def rangeSumBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """

    def traverse(root, L, R):
        if root is None: return 0
        if root.val >= L and root.val <= R:
            return root.val + traverse(root.left, L, R) + traverse(root.right, L, R)
        if root.val < L:
            return traverse(root.right, L, R)
        if root.val > R:
            return traverse(root.left, L, R)

    sum = traverse(root, L, R)

    return sum