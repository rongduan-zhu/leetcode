class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = {}

        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        for c in t:
            if c in counter:
                counter[c] -= 1
            else:
                return False

        for v in counter.values():
            if v != 0:
                return False

        return True
