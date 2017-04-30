class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        hold = False
        hold_date = 0
        profit = 0

        for i, price in enumerate(prices[:-1]):
            if prices[i + 1] > price and not hold:
                hold = True
                hold_date = i

            if (prices[i + 1] <= price) and hold:
                hold = False
                profit += price - prices[hold_date]

        if hold:
            profit += prices[-1] - prices[hold_date]

        return profit
