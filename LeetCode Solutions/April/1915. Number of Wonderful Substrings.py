'''

1915. Number of Wonderful Substrings

A wonderful string is a string where at most one letter appears an odd number of times.

    For example, "ccjjc" and "abab" are wonderful, but "ab" is not.

Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

https://leetcode.com/problems/number-of-wonderful-substrings/solutions/5092298/1915-number-of-wonderful-substrings-python
'''

class Solution(object):
    def wonderfulSubstrings(self, word):
        count = [0] * 1024  # 2^10 to store XOR values
        result = 0
        prefix_xor = 0
        count[prefix_xor] = 1
        
        for char in word:
            char_index = ord(char) - ord('a')
            prefix_xor ^= 1 << char_index
            result += count[prefix_xor]
            for i in range(10):
                result += count[prefix_xor ^ (1 << i)]
            count[prefix_xor] += 1
        
        return result