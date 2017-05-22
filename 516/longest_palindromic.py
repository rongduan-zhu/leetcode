class Solution(object):
    def longestPalindromeSubseq(self, s):
        s_length = len(s)
        longest = [[0] * s_length for _ in xrange(s_length)]

        for i in xrange(s_length - 1, -1, -1):
            longest[i][i] = 1
            for j in xrange(i + 1, s_length):
                if s[i] == s[j]:
                    longest[i][j] = longest[i + 1][j - 1] + 2
                else:
                    longest[i][j] = max(longest[i + 1][j], longest[i][j - 1])

        return longest[0][s_length - 1]
