"""
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.


"""


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0

        # for each column index
        for j in range(len(strs[0])):

            # for each row index start from 1, since we need to compare with the previous one.
            for i in range(1, len(strs)):

                # this column is not sorted, don't look farther.
                if strs[i][j] < strs[i - 1][j]:
                    res += 1
                    break
        return res