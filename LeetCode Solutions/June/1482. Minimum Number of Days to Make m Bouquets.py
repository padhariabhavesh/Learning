'''

1482. Minimum Number of Days to Make m Bouquets

You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Youtube : https://youtu.be/4Zv-BHYyzDY
'''

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 1, 1000000000
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            consecutive_length, bouquets = 0, 0
            for bloom in bloomDay:
                if bloom <= mid:
                    consecutive_length += 1
                    if consecutive_length >= k:
                        consecutive_length = 0
                        bouquets += 1
                else:
                    consecutive_length = 0
            if bouquets >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans