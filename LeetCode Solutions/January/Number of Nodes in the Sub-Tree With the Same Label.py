"""
You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.
"""


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # Construct the tree using the edges.
        # Since the tree is undricted, we need to add both directions in the tree.
        tree = defaultdict(list)
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)

        # The result of length n will be returned at the end.
        # It is being modified in the dfs.
        res = [0] * n

        # node is the current node we are examing.
        # par is the node's direct parent node.
        def dfs(node, par):
            nonlocal res
            # Using count to store the count of each letters in the sub-tree rooted at the current node.
            # The size of this hashmap (count) will be at most 26,
            # Since there are at most 26 lowercase English letters
            count = Counter()
            for nei in tree[node]:
                # Make sure we are not going backward to its parent node.
                if nei != par:
                    # Update count with the letters' frequency in the children nodes
                    # This is the same as going through a to z and increase the frequency of each letter.
                    count += dfs(nei, node)

            # Adding 1 to count with the current label
            count[labels[node]] += 1
            # Update the result.
            res[node] = count[labels[node]]

            return count

        # Starting from node 0, and assign fake parent -1 for it.
        dfs(0, -1)
        return res