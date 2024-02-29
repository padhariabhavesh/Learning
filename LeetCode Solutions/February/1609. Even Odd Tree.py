'''
1609. Even Odd Tree python solution

A binary tree is named Even-Odd if it meets the following conditions:

    The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
    For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
    For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

URL https://leetcode.com/problems/even-odd-tree/solutions/4797377/1609-even-odd-tree-python

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            # An empty tree is considered an Even-Odd tree.
            return True

        # Use a deque for efficient queue operations.
        queue = deque([root])
        level = 0

        while queue:
            prev_val = None  # Previous value at the current level.

            # Process all nodes at the current level.
            for _ in range(len(queue)):
                node = queue.popleft()

                # Check if the values follow the Even-Odd conditions.
                if (level % 2 == 0 and (node.val % 2 == 0 or (prev_val is not None and node.val <= prev_val))) or \
                   (level % 2 == 1 and (node.val % 2 == 1 or (prev_val is not None and node.val >= prev_val))):
                    return False

                prev_val = node.val

                # Add children to the deque.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        # All levels satisfy the conditions.
        return True
