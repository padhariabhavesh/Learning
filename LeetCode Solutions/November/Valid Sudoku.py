"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules."""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        #{0: ()}
        cols = collections.defaultdict(set)
        blocks = collections.defaultdict(set) # keys = (r//3, c//3) = 0,1

        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    continue

                value = board[row][column]

                if value in rows[row] or value in cols[column] or value in blocks[(row//3, column//3)]:
                    return False

                rows[row].add(value)
                cols[column].add(value)
                blocks[(row//3, column//3)].add(value)

        return True