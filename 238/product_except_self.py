class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningProduct = 1
        output = []

        for i in xrange(len(nums)):
            output.append(runningProduct)
            runningProduct *= nums[i]

        runningProduct = 1
        for i in xrange(len(nums) - 1, -1, -1):
            output[i] *= runningProduct
            runningProduct *= nums[i]

        return output
