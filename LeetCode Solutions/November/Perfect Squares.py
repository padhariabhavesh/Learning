"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        squares= [i**2 for i in range(floor(n**0.5),0,-1)]
        visited = set()
        q = deque([(n,0)])
        while q:
            x,s = q.popleft()
            for i in squares:
                if not x-i: return s+1
                if x-i >= 0:
                    if x-i not in visited:
                        q.append((x-i,s+1))
                        visited.add(x-i)
