"""
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
"""

class Solution:
  def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
    if S == T:
      return 0

    graph = defaultdict(list)
    usedBuses = set()

    for i in range(len(routes)):
      for route in routes[i]:
        graph[route].append(i)

    ans = 0
    q = deque([S])

    while q:
      ans += 1
      for _ in range(len(q)):
        for bus in graph[q.popleft()]:
          if bus in usedBuses:
            continue
          usedBuses.add(bus)
          for nextRoute in routes[bus]:
            if nextRoute == T:
              return ans
            else:
              q.append(nextRoute)

    return -1
