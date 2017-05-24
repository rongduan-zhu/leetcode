class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while (True):
            if start == end:
                return nums[start]

            mid = ((end - start) / 2) + start

            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    start = mid + 2
                else:
                    end = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if mid % 2 == 0:
                    end = mid - 2
                else:
                    start = mid + 1
            else:
                return nums[mid]
