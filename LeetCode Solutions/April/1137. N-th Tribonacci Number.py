'''

1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

https://leetcode.com/problems/n-th-tribonacci-number/solutions/5064756/1137-n-th-tribonacci-number-python
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        def fib(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1
            elif dp[n]!=-1:
                return dp[n]
            dp[n]=fib(n-1)+fib(n-2)+fib(n-3)
            return dp[n]
            
            



        dp=[-1]*(n+1)
        a=fib(n)
        return(a)
        