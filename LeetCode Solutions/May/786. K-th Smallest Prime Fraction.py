'''

786. K-th Smallest Prime Fraction


You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

https://leetcode.com/problems/k-th-smallest-prime-fraction/solutions/5140196/786-k-th-smallest-prime-fraction-python

'''

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0, 1
        res = []

        while left <= right:
            mid = left + (right - left) / 2
            j, total, num, den = 1, 0, 0, 0
            maxFrac = 0
            for i in range(n):
                while j < n and arr[i] >= arr[j] * mid:
                    j += 1
                
                total += n - j

                if j < n and maxFrac < arr[i] * 1.0 / arr[j]:
                    maxFrac = arr[i] * 1.0 / arr[j]
                    num, den = i, j

            if total == k:
                res = [arr[num], arr[den]]
                break

            if total > k:
                right = mid
            else:
                left = mid

        return res
