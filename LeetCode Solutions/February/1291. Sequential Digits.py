'''
1291. Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 https://leetcode.com/problems/sequential-digits/solutions/4662896/1291-sequential-digits-python

'''


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for num in range(1,9):
            while num <= high and num % 10 !=0:
                if num >= low:
                    res.append(num)
                num = (num * 10) + (num % 10) + 1
        return sorted(res)
        

        