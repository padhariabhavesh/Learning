'''

2997. Minimum Number of Operations to Make Array XOR Equal to K

You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:

    Choose any element of the array and flip a bit in its binary representation. Flipping a bit means changing a 0 to 1 or vice versa.

Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k.

Note that you can flip leading zero bits in the binary representation of elements. For example, for the number (101)2 you can flip the fourth bit and obtain (1101)2.

https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/solutions/5085817/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k-python
'''

class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    return functools.reduce(operator.xor, nums, k).bit_count()