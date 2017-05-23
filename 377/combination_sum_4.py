class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        counts = [-1] * (target + 1)

        ans = 0
        for num in nums:
            ans += Solution.comb_recursive(counts, nums, target - num)

        return ans

    @staticmethod
    def comb_recursive(counts, nums, target):
        if target <= 0:
            return 1 if target == 0 else 0

        if counts[target] != -1:
            return counts[target]

        ans = 0
        for num in nums:
            ans += Solution.comb_recursive(counts, nums, target - num)

        counts[target] = ans

        return ans

