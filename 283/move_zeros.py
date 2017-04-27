class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first_zero = 0

        for i in xrange(len(nums)):
            if (nums[i] != 0 and i != first_zero):
                nums[i] = nums[i] ^ nums[first_zero]
                nums[first_zero] = nums[i] ^ nums[first_zero]
                nums[i] = nums[i] ^ nums[first_zero]
                first_zero += 1
            if (nums[first_zero] != 0):
                first_zero += 1
