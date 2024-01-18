'''
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev1 = 1
        prev2 = 2
        current = 0
        for i in range(2,n):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return current