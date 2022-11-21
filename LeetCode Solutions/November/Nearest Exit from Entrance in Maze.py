"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
"""

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        Q = [entrance]
        Q_next = []
        maze[entrance[0]][entrance[1]] = '+'
        near = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        row, col = len(maze) - 1, len(maze[0]) - 1
        step = 0
        while len(Q) > 0:
            curr = Q.pop(0)
            for n in near:
                next = [curr[0] + n[0], curr[1] + n[1]]
                if (next[0] >= 0) and (next[1] >= 0) and (next[0] <= row) and (next[1] <= col):
                    if maze[next[0]][next[1]] == '.':
                        if (next[0] == 0) or (next[1] == 0) or (next[0] == row) or (next[1] == col):
                            return step + 1
                        Q_next.append(next)
                        maze[next[0]][next[1]] = '+'
            if len(Q) == 0:
                Q, Q_next = Q_next, Q
                step += 1
        return -1