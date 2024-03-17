'''
933. Number of Recent Calls

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

    RecentCounter() Initializes the counter with zero recent requests.
    int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

https://leetcode.com/problems/number-of-recent-calls/solutions/4887052/933-number-of-recent-calls-python
'''

class RecentCounter:

    def __init__(self):
        self.data = deque()
        self.k = 3000
        self.calls = 0

    def ping(self, t: int) -> int:
        self.calls += 1
        if not self.data or self.data[-1][0] < t:
            self.data.append([t, 1])
        else:
            self.data[-1][0] += 1
        
        while self.data[0][0] < t - self.k:
            self.calls -= self.data.popleft()[1]
        
        return self.calls

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)