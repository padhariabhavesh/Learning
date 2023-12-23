'''
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}

        for direction in path:
            x += 1 if direction == 'E' else (-1 if direction == 'W' else 0)
            y += 1 if direction == 'N' else (-1 if direction == 'S' else 0)

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False