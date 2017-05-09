class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = [0] * (n + 1)
        product[1] = 1

        for i in range(2, n + 1):
            product[i] = max([max(product[j], j) * max(product[i - j], i - j) for j in range(1, i)])

        return product[-1]
