'''
875. Koko Eating Bananas


Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

https://leetcode.com/problems/koko-eating-bananas/submissions/1225722020?envType=study-plan-v2&envId=leetcode-75
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) >> 1
            total_hours = 0
            
            # Calculate total hours required to eat all bananas at current speed 'mid'
            for p in piles:
                total_hours += math.ceil(p / mid)
            
            # Determine if current eating speed 'mid' is valid
            if total_hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res