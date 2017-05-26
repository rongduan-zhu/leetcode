class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        current_sell = 0
        prev_sell = 0
        current_buy = -prices[0]

        for price in prices[1:]:
            prev_buy = current_buy
            current_buy = max(prev_sell - price, current_buy)
            prev_sell = current_sell
            current_sell = max(prev_buy + price, current_sell)

        return current_sell
