'''

450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.

    https://leetcode.com/problems/delete-node-in-a-bst/solutions/4939920/450-delete-node-in-a-bst-python
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestDescendant(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        else:
            # Checks for Lesser value
            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            # Checks for Greater value
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            # Checks if we have reached the node we want to delete
            else:
                # First we check if only 1 child node is present
                if not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                # If both the children are present then we find the
                # smallest child in the right child and assign it's
                # value to node and recursively delete that child 
                # until we have reach node with 1 child or leaf node
                    temp = self.smallestDescendant(root.right)
                    root.val = temp.val
                    root.right = self.deleteNode(root.right, temp.val)
            return root


        