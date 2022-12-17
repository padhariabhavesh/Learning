"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operations = {
            "*": lambda x,y: x*y,
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "/": lambda x,y: float(x)/y
        }

        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                result = operations[token](left, right)
                stack.append(int(result))
        return stack.pop()