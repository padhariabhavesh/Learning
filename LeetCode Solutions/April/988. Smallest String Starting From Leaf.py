'''
988. Smallest String Starting From Leaf

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

    For example, "ab" is lexicographically smaller than "aba".

A leaf of a node is a node that has no children.

https://leetcode.com/problems/smallest-string-starting-from-leaf/solutions/5037695/988-smallest-string-starting-from-leaf-python
'''

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Helper function to perform DFS
        def dfs(node, path, smallest):
            if not node:
                return
            
            # Append current node's character to the path
            path.append(chr(node.val + ord('a')))
            
            # If it's a leaf node, reverse the path and compare
            if not node.left and not node.right:
                current_string = ''.join(path[::-1])  # reverse path to get string
                smallest[0] = min(smallest[0], current_string)
            
            # Recursively traverse left and right subtrees
            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)
            
            # Backtrack: remove the current node's character from the path
            path.pop()
        
        # Initialize smallest string as a large value
        smallest = [chr(ord('z') + 1)]  # Store smallest string found
        
        # Start DFS from the root with an empty path
        dfs(root, [], smallest)
        
        return smallest[0]