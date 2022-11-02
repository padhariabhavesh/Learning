"""
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution:
	def calculate(self, s: str) -> int:
		s_len = len(s)
		stack_nums = list()
		stack_ops = list()
		curr_num = 0

		for i in range(s_len):
			if s[i] == ' ':
				continue
			elif s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
				stack_nums.append(curr_num)
				stack_ops.append(s[i])
				curr_num = 0
			else:
				curr_num = curr_num*10 + int(s[i])

		stack_nums.append(curr_num)
		# print(stack_nums)
		# print(stack_ops)

		i = 0
		while i<len(stack_ops):
			if stack_ops[i] == '*':
				first = stack_nums.pop(i)
				second = stack_nums.pop(i)
				res = first*second
				stack_nums.insert(i, res)
				stack_ops.pop(i)
			elif stack_ops[i] == '/':
				first = stack_nums.pop(i)
				second = stack_nums.pop(i)
				res = first//second
				stack_nums.insert(i, res)
				stack_ops.pop(i)
			else:
				i += 1
				continue
		# print(stack_nums)
		# print(stack_ops)
		res = stack_nums[0]
		num_items = len(stack_nums)
		num_ops = len(stack_ops)
		for i in range(num_ops):
			if stack_ops[i] == '+':
				res += stack_nums[i+1]
			elif stack_ops[i] == '-':
				res -= stack_nums[i+1]
		return res