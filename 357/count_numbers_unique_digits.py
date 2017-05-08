class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        if n >= 11:
            return 0

        count = 10
        product = 9
        choice = 9

        for i in range(2, n + 1):
            product *= choice
            count += product
            choice -= 1

        return count
