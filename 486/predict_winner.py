class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        value = [[-1 for i in range(0, len(nums))] for j in range(0, len(nums))]
        highest = self.find_best(nums, value, 0, len(nums) - 1)
        return highest * 2 >= sum(nums)

    def find_best(self, nums, value, start, end):
        if start > end:
            return 0

        if value[start][end] != -1:
            return value[start][end]

        pick_head = nums[start] + min(
            self.find_best(nums, value, start + 1, end - 1),
            self.find_best(nums, value, start + 2, end)
        )
        pick_tail = nums[end] + min(
            self.find_best(nums, value, start + 1, end - 1),
            self.find_best(nums, value, start, end - 2)
        )

        value[start][end] = max(pick_head, pick_tail)

        return value[start][end]
