class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ways = [[0] * n for _ in xrange(m)]
        ways[m - 1][n - 1] = 1

        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                if j + 1 < n:
                    ways[i][j] += ways[i][j + 1]
                if i + 1 < m:
                    ways[i][j] += ways[i + 1][j]

        return ways[0][0]
