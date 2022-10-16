"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def helper(self, coins, amount, cache):
        if amount == 0:
            return 0
        elif amount in cache:
            return cache[amount]
        cache[amount] = float('inf')
        for c in coins:
            if amount - c >= 0:
                cache[amount] = min(cache[amount], self.helper(coins, amount - c, cache) + 1)
        return cache[amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        elif min(coins) > amount:
            return -1
        else:
            coins.sort(reverse=True)
            answer = self.helper(coins, amount, {})
            return answer if answer != float('inf') else -1