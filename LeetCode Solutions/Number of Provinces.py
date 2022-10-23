"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

class UnionFind:
  def __init__(self, n: int):
    self.count = n
    self.id = list(range(n))

  def union(self, u: int, v: int) -> None:
    i = self.find(u)
    j = self.find(v)
    if i == j:
      return
    self.id[i] = j
    self.count -= 1

  def find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self.find(self.id[u])
    return self.id[u]


class Solution:
  def findCircleNum(self, M: List[List[int]]) -> int:
    n = len(M)
    uf = UnionFind(n)

    for i in range(n):
      for j in range(i, n):
        if M[i][j] == 1:
          uf.union(i, j)

    return uf.count
