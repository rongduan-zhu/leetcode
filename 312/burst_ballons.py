class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        length = len(nums)
        largest = [[0] * length for _ in xrange(length)]

        return self.best_burst(nums, largest, 0, length - 1)

    @staticmethod
    def best_burst(nums, largest, left, right):
        # no ballons to pop
        if (left + 1 == right):
            return 0

        # return the result if we've already seen this case
        if largest[left][right] != 0:
            return largest[left][right]

        local_best = 0
        for i in xrange(left + 1, right):
            local_best = max(
                local_best,
                nums[left] * nums[i] * nums[right] + Solution.best_burst(nums, largest, left, i) + Solution.best_burst(nums, largest, i, right)
            )

        largest[left][right] = local_best

        return local_best
