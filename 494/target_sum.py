class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if (total + S) % 2 != 0 or total < S:
            return 0

        target = (total + S) / 2

        sum_count = [0 for i in range(target + 1)]
        sum_count[0] = 1

        for num in nums:
            for i in range(target, num - 1, -1):
                sum_count[i] += sum_count[i - num]

        return sum_count[target]
