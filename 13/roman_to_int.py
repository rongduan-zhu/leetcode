class Solution(object):
    numeral_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        for i in xrange(len(s)):
            next_i_value = Solution.numeral_map[s[i + 1] if i + 1 < len(s) else s[i]]
            i_value = Solution.numeral_map[s[i]]

            if i_value < next_i_value:
                total -= i_value
            else:
                total += i_value

        return total
