"""Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""


class Solution:
    def calculate(self, s: str) -> int:
        res, cur, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in "+-":
                res += (cur * sign)
                cur = 0
                if c == "-":
                    sign = -1
                else:
                    sign = 1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += (cur * sign)
                res *= stack.pop()
                res += stack.pop()
                cur = 0
        return res + (cur * sign)
