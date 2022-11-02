"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.


"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        def valid(gene1, gene2):
            diff = 0
            for char1, char2 in zip(gene1, gene2):
                if char1 != char2: diff += 1
            return diff == 1

        def backtrack(current, mutations, path):
            if current in path:
                return sys.maxsize

            if current == end:
                return mutations

            path.add(current)

            res = sys.maxsize
            for gene in bank:
                if valid(current, gene):
                    res = min(
                        backtrack(gene, mutations + 1, path),
                        res
                    )

            path.remove(current)

            return res

        res = backtrack(start, 0, set())

        return res if res != sys.maxsize else -1