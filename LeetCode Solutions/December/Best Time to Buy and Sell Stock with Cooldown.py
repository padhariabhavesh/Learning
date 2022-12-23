class Solution:
    def maxProfit(self, prices):

        """
        # We must rest for a single term before buying.
        # Thus maximum obtainable from buying today is the max of:
        #   1. Buying (Max obtainable from selling 2 periods ago - stock price at i)
        #   2. Not Buying (max from previous)
        #
        # Therefore:
        #   buy[i] = max(sell[i-2]-price, buy[i-1])
        #
        #
        # Selling is straight forward. We either sell or not
        # Thus maximum from selling is the max of:
        #   1. Selling (Max obtainable from buying a day ago + stock price at i)
        #   2. Not Selling (max from previous)
        #
        # Therefore:
        #   sell[i] = max(buy[i-1]+price, sell[i-1])

        """

        if len(prices) < 2: return 0
        prev_sell, sell, buy = 0, 0, -prices[0]  # buy initialized to buying a stock at i=0
        for i in range(1, len(prices)):
            prev_sell, sell, buy = sell, max(buy + prices[i], sell), max(prev_sell - prices[i], buy)
        return max(sell, buy)