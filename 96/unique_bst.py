class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        count = [0] * (n + 1)
        count[0] = count[1] = 1

        for i in xrange(2, n + 1):
            for j in xrange(0, i):
                count[i] += count[j] * count[i - 1 - j]

        return count[n]
