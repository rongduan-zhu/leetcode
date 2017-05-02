class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        majority = len(nums) / 2

        for key in counter:
            if counter[key] > majority:
                return key

        raise ValueError('No majority number found')
