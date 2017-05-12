class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        matched_pos = 0

        for c in t:
            if c == s[matched_pos]:
                matched_pos += 1
            if matched_pos == len(s):
                break

        return matched_pos == len(s)
