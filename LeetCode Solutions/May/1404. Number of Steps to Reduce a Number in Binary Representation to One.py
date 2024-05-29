'''

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

    If the current number is even, you have to divide it by 2.

    If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.



'''

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        n = len(s) - 1
        for i in range(n, 0, -1):
            if int(s[i]) + carry == 1:
                carry = 1
                steps += 2
            else:
                steps += 1
        return steps + carry

        