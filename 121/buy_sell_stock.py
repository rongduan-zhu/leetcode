class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_so_far = best_to_now = 0

        for i in xrange(1, len(prices)):
            best_to_now = max(prices[i] - prices[i - 1] + best_to_now, 0)
            best_so_far = max(best_to_now, best_so_far)

        return best_so_far
